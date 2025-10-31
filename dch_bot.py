#!/usr/bin/env python3
"""
Main DCH Bot module.
This is the entry point for the DCH bot application.
"""

import logging
from fetch_prices import fetch_prices
from schedule_jobs import setup_scheduler
from towns_api import TownsAPI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """
    Main function to initialize and run the DCH bot.
    """
    logger.info("Starting DCH Bot...")
    
    try:
        # Initialize APIs
        towns_api = TownsAPI()
        
        # Setup scheduler for periodic jobs
        scheduler = setup_scheduler()
        
        # Fetch initial prices
        prices = fetch_prices()
        logger.info(f"Fetched {len(prices) if prices else 0} prices")
        
        # Keep the scheduler running
        scheduler.start()
        
    except Exception as e:
        logger.error(f"Error in main: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
