"""
alertmanagermeshtastic.processor
~~~~~~~~~~~~~~~~~~~~~

Connect HTTP server and MESHTASTIC interface.

:Copyright: 2007-2022 Jochen Kupperschmidt
:Copyright: 2023 Alexander Volz
:License: MIT, see LICENSE for details.
"""

from __future__ import annotations
import logging
from queue import SimpleQueue, Empty
from datetime import datetime, timedelta
import json

from typing import Any, Optional

from .config import Config
from .http import start_receive_server
from .meshtastic import create_announcer
from .signals import message_received, queue_size_updated, clear_queue_issued


logger = logging.getLogger(__name__)


class Processor:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.announcer = create_announcer(config.meshtastic, config.general)
        self.enabled_channel_names: set[str] = set()
        self.message_queue: SimpleQueue = SimpleQueue()
        self.qn = 0

        # Up to this point, no signals must have been sent.
        self.connect_to_signals()
        # Signals are allowed be sent from here on.

    def connect_to_signals(self) -> None:
        message_received.connect(self.handle_message)
        clear_queue_issued.connect(self.handle_clear_queue)

    def handle_clear_queue(self, sender):
        logger.debug('\t clearing queue.... ')
        queue_entries = []

        while not self.message_queue.empty():
            try:
                entry = self.message_queue.get_nowait()
                queue_entries.append(entry)
            except Empty:
                break

        with open('/tmp/queueclear', 'w') as f:
            json.dump(queue_entries, f)

        mock_alert = {
            "status": "quecleared",
            "fingerprint": "quecleared",
            "labels": {"alertname": "quecleared", "severity": "info"},
            "annotations": {
                "summary": "This is a alert for clearing the queue."
            },
        }
        self.handle_message(alert=mock_alert, sender=None)
        queue_size_updated.send(self.message_queue.qsize())

        logger.debug('\t clearing queue finished. ')

    def handle_message(
        self,
        sender: Optional[Any],
        *,
        alert: str,
    ) -> None:
        """Log and announce an incoming message."""
        self.qn = self.qn + 1
        alert["qn"] = self.qn
        alert["inputtime"] = (
            datetime.now() + timedelta(hours=self.config.general.inputtimeshift)
        ).strftime('%Y-%m-%d %H:%M:%S')
        logger.debug(
            '\t [%s][%s][%d][%d] put in queue',
            alert["fingerprint"],
            alert["inputtime"],
            self.config.general.inputtimeshift,
            alert["qn"],
        )
        self.message_queue.put((alert))
        queue_size_updated.send(self.message_queue.qsize())

    def announce_message(self, alert: str) -> None:
        """Announce message on MESHTASTIC."""
        self.announcer.announce(alert)

    def process_queue(self, timeout_seconds: Optional[int] = None) -> None:
        logger.debug('\t Messages in queue: %d', self.message_queue.qsize())
        """Process a message from the queue."""
        alert = self.message_queue.get(timeout=timeout_seconds)
        logger.debug(
            '\t [%s][%d] processing message ', alert["fingerprint"], alert["qn"]
        )
        self.announce_message(alert)
        queue_size_updated.send(self.message_queue.qsize())

    def run(self) -> None:
        """Run the main loop."""
        self.announcer.start()
        start_receive_server(self.config.http)

        logger.info('\t Starting to process queue ...')
        try:
            while True:
                self.process_queue()
        except KeyboardInterrupt:
            pass

        logger.info('\t Shutting down ...')
        self.announcer.shutdown()


def start(config: Config) -> None:
    """Start the MESHTASTIC interface and the HTTP listen server."""
    processor = Processor(config)
    processor.run()
