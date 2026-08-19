# 📸 Instagram Scraper & Profile Intelligence Pro

Extract Instagram posts, reels, profiles, hashtags, and comments without login. Get captions, timestamps, likes, comments, owner profile stats, hashtags, and AI engagement analytics. Just $1.49/1k results—45% cheaper than legacy scrapers!

## 🚀 Usage & Input Parameters

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `target_username` | string | Instagram handle | `nike` |
| `target_url` | string | Post/Reel URL | `https://www.instagram.com/p/C98x01A/` |
| `hashtag` | string | Hashtag keyword | `fitness` |
| `max_items` | integer | Max items to extract | `20` |

## 📤 Output Format

```json
{
  "item_id": "C98x01A",
  "url": "https://www.instagram.com/p/C98x01A/",
  "type": "post",
  "caption": "Check out the new high-performance collection for nike! 🚀 #viral #nike",
  "likes_count": 148500,
  "comments_count": 3240,
  "owner_username": "nike",
  "owner_full_name": "Nike Official",
  "followers_count": 12500000,
  "display_url": "https://images.instagram.com/p/C98x01A/sample.jpg",
  "hashtags": ["viral", "nike", "trending"],
  "timestamp": "2026-08-19 12:00:00",
  "ai_engagement_analysis": "High Virality Index (1.21% engagement)."
}
```
