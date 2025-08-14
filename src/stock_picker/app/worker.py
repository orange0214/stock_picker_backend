from __future__ import annotations

import logging

from .core.logging import setup_logging


setup_logging()
logger = logging.getLogger(__name__)


def run_worker() -> None:
    logger.info("Background worker started")
    # Implement periodic tasks or message queue consumers here


if __name__ == "__main__":
    run_worker()
