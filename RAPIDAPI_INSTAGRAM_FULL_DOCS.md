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

## 🛠️ Example Use Cases

1. **Influencer Discovery & Tracking**: Identify top-performing content creators by niche and follower metrics.
2. **Social Media Competitor Analysis**: Benchmark competitor post frequency, reel engagement, and hashtag performance.
3. **Trend & Hashtag Monitoring**: Track viral posts and reels across specific hashtags in real-time.

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

## 🌐 4. Endpoint & Integration Details

- **HTTP Method**: `POST`
- **Endpoint Path**: `/scrape-instagram`
- **Headers**:
  - `Content-Type`: `application/json`
  - `X-RapidAPI-Key`: `{YOUR_RAPIDAPI_KEY}`

---

## 📥 Request Body Schema (JSON)

| Parameter | Type | Required | Default | Description | Example |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `target_username` | `string` | Optional* | — | Instagram profile handle | `"nike"` |
| `target_url` | `string` | Optional* | — | Post or reel URL | `"https://instagram.com/p/C98x01A/"` |
| `hashtag` | `string` | Optional* | — | Hashtag keyword | `"fitness"` |
| `max_items` | `integer` | No | `10` | Max items to scrape (1–100) | `10` |

*\*Note: Provide at least one of `target_username`, `target_url`, or `hashtag`.*

---

## 💻 5. Integration Code Snippets

### cURL:
```bash
curl -X POST "https://microsaas-agent-api.onrender.com/scrape-instagram" \
  -H "Content-Type: application/json" \
  -H "X-RapidAPI-Key: YOUR_RAPIDAPI_KEY" \
  -d '{
    "target_username": "nike",
    "max_items": 10
  }'
```

### Python (SDK):
```python
from instagram_scraper import InstagramScraperClient

client = InstagramScraperClient(api_key="YOUR_RAPIDAPI_KEY")

res = client.scrape_instagram(
    target_username="nike",
    max_items=10
)

for item in res["results"]:
    print(f"Post URL: {item['url']} | Likes: {item['likes_count']} | Virality: {item['ai_engagement_analysis']}")
```

### JavaScript / Node.js (fetch):
```javascript
const response = await fetch("https://microsaas-agent-api.onrender.com/scrape-instagram", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY"
  },
  body: JSON.stringify({
    target_username: "nike",
    max_items: 10
  })
});

const data = await response.json();
console.log(data);
```

---

## 💰 6. Recommended RapidAPI Pricing Tiers

| Plan Tier | Monthly Price | Included Requests | Overage Fee / Request |
| :--- | :--- | :--- | :--- |
| **BASIC (Free)** | `$0.00 / mo` | 50 requests | Hard Cap (No Overages) |
| **PRO** | **`$19.00 / mo`** | 2,500 requests | `$0.010 / request` |
| **ULTRA** | **`$59.00 / mo`** | 10,000 requests | `$0.007 / request` |
| **MEGA** | **`$149.00 / mo`** | 30,000 requests | `$0.005 / request` |

---

## ⚠️ HTTP Status Codes

| Code | Status | Meaning |
| :--- | :--- | :--- |
| `200` | **OK** | Instagram media and profile metrics successfully extracted. |
| `400` | **Bad Request** | Missing username, post URL, or hashtag. |
| `429` | **Too Many Requests** | Monthly subscription quota exceeded. Upgrade plan on RapidAPI. |
| `500` | **Internal Server Error** | Temporary scraping timeout. Retried automatically. |
