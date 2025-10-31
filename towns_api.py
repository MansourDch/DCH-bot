#!/usr/bin/env python3
"""
Towns Protocol API module.
Handles all interactions with the Towns Protocol API.
"""

import logging
from typing import Dict, List, Optional
import requests
from datetime import datetime

logger = logging.getLogger(__name__)


class TownsAPI:
    """
    Client for interacting with the Towns Protocol API.
    """
    
    def __init__(self, base_url: str = "https://api.towns.com"):
        """
        Initialize the Towns API client.
        
        Args:
            base_url: The base URL of the Towns API
        """
        self.base_url = base_url
        self.session = requests.Session()
        logger.info(f"Initialized TownsAPI with base URL: {base_url}")
    
    def get_prices(self, town_id: str = None) -> Optional[List[Dict]]:
        """
        Get prices for towns.
        
        Args:
            town_id: Optional specific town ID to fetch prices for
        
        Returns:
            List of price dictionaries or None if request fails
        """
        try:
            endpoint = f"{self.base_url}/prices"
            if town_id:
                endpoint += f"?town_id={town_id}"
            
            response = self.session.get(endpoint)
            response.raise_for_status()
            
            prices = response.json()
            logger.info(f"Successfully fetched prices: {len(prices)} records")
            return prices
        
        except requests.RequestException as e:
            logger.error(f"Error fetching prices: {e}")
            return None
    
    def get_town_data(self, town_id: str) -> Optional[Dict]:
        """
        Get data for a specific town.
        
        Args:
            town_id: The town ID to fetch data for
        
        Returns:
            Town data dictionary or None if request fails
        """
        try:
            endpoint = f"{self.base_url}/towns/{town_id}"
            response = self.session.get(endpoint)
            response.raise_for_status()
            
            town_data = response.json()
            logger.info(f"Successfully fetched data for town: {town_id}")
            return town_data
        
        except requests.RequestException as e:
            logger.error(f"Error fetching town data for {town_id}: {e}")
            return None
    
    def post_data(self, endpoint: str, data: Dict) -> Optional[Dict]:
        """
        Post data to the API.
        
        Args:
            endpoint: The API endpoint to post to
            data: The data to post
        
        Returns:
            Response dictionary or None if request fails
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.post(url, json=data)
            response.raise_for_status()
            
            logger.info(f"Successfully posted data to {endpoint}")
            return response.json()
        
        except requests.RequestException as e:
            logger.error(f"Error posting data to {endpoint}: {e}")
            return None
    
    def close(self) -> None:
        """
        Close the API session.
        """
        self.session.close()
        logger.info("TownsAPI session closed")
