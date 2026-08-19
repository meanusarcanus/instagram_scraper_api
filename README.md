# 📸 Instagram Scraper & Profile Intelligence Pro API

High-performance API engine and Apify Actor designed to scrape Instagram posts, reels, user profiles, followers counts, hashtags, and AI engagement analytics by username, post URL, or hashtag query.

---

## 🚀 Quick Start

### 1. Run Locally
```bash
pip install -r requirements.txt
uvicorn api.index:app --reload
```

### 2. Run Tests
```bash
python3 test_api.py
```

### 3. API Endpoint (`POST /scrape-instagram`)
```json
{
  "target_username": "nike",
  "max_items": 10
}
```
