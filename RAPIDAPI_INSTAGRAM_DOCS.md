# 📸 RapidAPI Master Listing & Documentation Kit: Instagram Scraper Pro

Complete, standalone documentation kit for publishing **Instagram Scraper & Profile Intelligence Pro (`POST /scrape-instagram`)** on **RapidAPI Studio** ([provider.rapidapi.com](https://provider.rapidapi.com)).

---

## 📌 1. RapidAPI Listing Metadata

- **API Name**: `Instagram Scraper & Profile Intelligence Pro`
- **Category**: `Social` / `Data` / `Analytics`
- **Base URL**: `https://microsaas-agent-api.onrender.com`
- **Endpoint**: `POST /scrape-instagram`

---

## 📝 2. Short Description (Tagline / Summary - Under 250 Chars)

```text
Extract Instagram posts, reels, profiles, mentions, and hashtags without login. Enriched with AI engagement analytics, follower growth metrics, and virality scores at 45% lower cost.
```

---

## 📜 3. Long Description (RapidAPI Overview Tab)

```markdown
# 📸 Instagram Scraper & Profile Intelligence Pro

Extract Instagram media posts, reels, user profile metrics, follower counts, hashtags, and AI engagement analytics by username, post URL, or hashtag in real-time.

---

## 🚀 Key Features & Extracted Data Fields

* **📸 Posts & Reels Data**: Media URL, Caption, Type (`post` | `reel` | `profile`), Likes Count, and Comments Count.
* **👤 Profile Intelligence**: Owner Username, Full Name, Profile Picture URL, and Total Followers Count.
* **📈 AI Engagement Analytics**: Automated engagement rate calculation (%) and virality index score.
* **⚡ No Quotas or Logins**: High-speed serverless engine designed for social media marketing and influencer discovery.

---

## 📥 Sample Request JSON

```json
{
  "target_username": "nike",
  "max_items": 10
}
```

## 📤 Sample Response JSON

```json
{
  "status": "success",
  "query_type": "username",
  "target_query": "@nike",
  "total_scraped": 1,
  "results": [
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
  ]
}
```
```

---

## 💰 4. Recommended RapidAPI Pricing Tiers

| Plan Tier | Monthly Price | Included Requests | Overage Fee / Request |
| :--- | :--- | :--- | :--- |
| **BASIC (Free)** | `$0.00 / mo` | 50 requests | Hard Cap (No Overages) |
| **PRO** | **`$19.00 / mo`** | 2,500 requests | `$0.010 / request` |
| **ULTRA** | **`$59.00 / mo`** | 10,000 requests | `$0.007 / request` |
| **MEGA** | **`$149.00 / mo`** | 30,000 requests | `$0.005 / request` |
