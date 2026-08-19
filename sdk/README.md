# 📸 Instagram Scraper & Profile Intelligence Pro Python SDK

Official Python SDK for `instagram-scraper-api`. Extract Instagram posts, reels, profiles, hashtags, and AI engagement analytics in 1 line of Python code.

## 🚀 Installation
```bash
pip install instagram-scraper-api
```

## 💻 Quick Usage
```python
from instagram_scraper import InstagramScraperClient

client = InstagramScraperClient(api_key="YOUR_RAPIDAPI_KEY")
res = client.scrape_instagram(target_username="nike", max_items=10)

for item in res["results"]:
    print(f"Post URL: {item['url']} | Likes: {item['likes_count']} | Virality: {item['ai_engagement_analysis']}")
```
