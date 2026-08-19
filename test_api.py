#!/usr/bin/env python3
"""
Automated Test Suite for Instagram Scraper & Profile Intelligence API
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "api"))

from index import app, read_root, scrape_instagram, InstagramScrapeRequest

def test_suite():
    print("==================================================")
    print(" 📸 TESTING INSTAGRAM SCRAPER & PROFILE INTELLIGENCE API")
    print("==================================================")

    # Test 1: Root Health Check
    print("\n[Test 1] Health Check Endpoint (GET /)...")
    res_root = read_root()
    assert res_root.get("status") == "online"
    print("✓ Health Check Passed!")

    # Test 2: Scrape Profile Username
    print("\n[Test 2] Scrape Profile Username (POST /scrape-instagram)...")
    res_user = scrape_instagram(InstagramScrapeRequest(
        target_username="nike",
        max_items=5
    ))
    print("Query Type:", res_user.query_type)
    print("Target Query:", res_user.target_query)
    print("Total Scraped Items:", res_user.total_scraped)
    print("Sample Item Caption:", res_user.results[0].caption if res_user.results else "None")
    assert res_user.total_scraped > 0
    assert "instagram.com" in res_user.results[0].url
    print("✓ Username Scrape Passed!")

    # Test 3: Scrape Hashtag
    print("\n[Test 3] Scrape Hashtag (POST /scrape-instagram)...")
    res_tag = scrape_instagram(InstagramScrapeRequest(
        hashtag="fitness",
        max_items=3
    ))
    assert res_tag.total_scraped > 0
    print("✓ Hashtag Scrape Passed!")

    print("\n==================================================")
    print(" 🎉 ALL INSTAGRAM SCRAPER TESTS PASSED 100%!")
    print("==================================================")

if __name__ == "__main__":
    test_suite()
