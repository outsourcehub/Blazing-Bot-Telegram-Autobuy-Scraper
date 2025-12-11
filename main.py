#!/usr/bin/env python3
"""
Main entry point for Ultra-Fast Trading Bot (Telethon)
"""
import asyncio
import sys
import logging

if __name__ == "__main__":
    from first_run_setup import check_and_run_setup
    check_and_run_setup()

    # Disable all logging
    logging.disable(logging.CRITICAL)

    from bot import main as bot_main
    try:
        asyncio.run(bot_main())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)