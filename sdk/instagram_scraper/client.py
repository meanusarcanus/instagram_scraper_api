"""
Official Python SDK Client for Instagram Scraper & Profile Intelligence Pro
"""

import requests
from typing import Optional, Dict, Any

class InstagramScraperClient:
    """
    Python SDK Client for Instagram Scraper API.
    """
    def __init__(self, api_key: str, base_url: str = "https://microsaas-agent-api.onrender.com"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def scrape_instagram(self, target_username: Optional[str] = None, target_url: Optional[str] = None, hashtag: Optional[str] = None, max_items: int = 10) -> dict:
        """
        Scrape Instagram posts, reels, profiles, and hashtags without login.
        """
        url = f"{self.base_url}/scrape-instagram"
        payload = {
            "target_username": target_username,
            "target_url": target_url,
            "hashtag": hashtag,
            "max_items": max_items
        }
        response = requests.post(url, json=payload, headers=self.headers, timeout=30)
        response.raise_for_status()
        return response.json()
