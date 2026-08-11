<div align="center">

# Amazon Product Api

Amazon Product API - Real-time product, pricing, and review data via REST API

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?logo=opensourceinitiative&logoColor=white)
![Stars](https://img.shields.io/github/stars/data-scrape/amazon-product-api?style=social)
![API](https://img.shields.io/badge/CoreClaw-API-9966FF?style=social)

</div>

<div align="center">

## 🚀 Powered by CoreClaw

[![CoreClaw](https://img.shields.io/badge/CoreClaw-Web_Data_API-9966FF?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDMgN3YxMGw5IDUgOS01VjdsLTktNXoiLz48L3N2Zz4=&logoColor=white)](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

**Web Data Infrastructure for AI Agents & Automation**

E-commerce Data API — Production-ready REST API for structured web data extraction.

📍 Google Maps · 👤 LinkedIn · 📱 Social Media · 🛒 E-commerce · 🔍 Search

✅ No browser automation · ✅ No proxy management · ✅ AI-ready data · ✅ Free credits

⬇️ [Start Building with CoreClaw Free](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

</div>

---

## 📖 Overview

**amazon-product-api** showcases the E-commerce Data API from CoreClaw — a production-ready web data API platform designed for developers, AI agent builders, and SaaS companies who need structured data without maintaining scraping infrastructure.

### Why E-commerce Data API?

- **API-First Design** — Structured JSON responses, no HTML parsing required
- **Production-Ready** — Built-in rate limiting, retry logic, and proxy rotation
- **AI Agent Compatible** — MCP-compatible data tools for agentic workflows
- **Enterprise Scale** — Handle millions of requests with consistent performance
- **Developer-Friendly** — Simple REST API with comprehensive documentation
- **Cost-Effective** — Pay only for successful requests, free credits for new users

---

## 🔧 API Quick Start

### Python Example

```python
import requests

# CoreClaw API endpoint
API_URL = "https://api.coreclaw.com/v1/amazon"
HEADERS = {"Authorization": "Bearer YOUR_API_KEY"}

response = requests.get(API_URL, params={
    "query": "search term",
    "limit": 100,
    "format": "json"
}, headers=HEADERS, timeout=30)

data = response.json()
print(f"Got {len(data['results'])} records")
```

### cURL Example

```bash
curl -X GET "https://api.coreclaw.com/v1/amazon" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"query": "search term", "limit": 100}'
```

---

## 📊 Data Schema

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique record identifier |
| name | string | Business/entity name |
| address | string | Full street address |
| phone | string | Contact phone number |
| website | string | Business website URL |
| rating | float | Rating score (0-5) |
| reviews_count | int | Number of reviews |
| categories | array | Business categories |
| latitude | float | GPS latitude |
| longitude | float | GPS longitude |
| hours | object | Operating hours |
| scraped_at | string | ISO timestamp |

---

## 🎯 Target Users

| User Type | Use Case |
|-----------|----------|
| AI Developer | Feed real-time data to AI agents via MCP tools |
| SaaS Founder | Build data products without scraping infrastructure |
| Lead Gen Agency | Bulk business data extraction for sales pipelines |
| Local SEO Agency | Google Maps business data for local SEO campaigns |
| Data Engineer | Stable API replacing self-built scrapers |
| Marketing Team | Competitor and market intelligence data |

---

## 💡 Use Cases

1. **Lead Generation** — Extract business contacts, phone numbers, and emails
2. **AI Agent Data** — Connect AI agents to real-time web data via MCP
3. **CRM Enrichment** — Auto-fill missing company data in your CRM
4. **Market Intelligence** — Monitor competitor pricing and reviews
5. **Local SEO** — Track Google Maps rankings and business data changes
6. **Automation** — Trigger workflows based on data changes

---

## 📋 CoreClaw Product Suite

| Product | Description | API Endpoint |
|---------|-------------|-------------|
| Google Maps Scraper API | Local business data extraction | `/v1/google-maps` |
| LinkedIn Data API | B2B contact and company data | `/v1/linkedin` |
| Social Media Data API | Instagram, TikTok, YouTube, Reddit | `/v1/social` |
| E-commerce Data API | Amazon, Walmart, eBay product data | `/v1/ecommerce` |
| Search Data API | Google SERP and search results | `/v1/search` |

---

<!-- CROSS_LINKS_START -->

## Related Scrapers

Explore more data extraction tools:

### Awesome Lists

- [awesome-lead-generation](https://github.com/data-scrape/awesome-lead-generation) — Awesome Lead Generation - Curated B2B lead gen tools, APIs, and data sources

### Competitor Alternatives

- [brightdata-alternative](https://github.com/data-scrape/brightdata-alternative) — Best Bright Data Alternative - Web data platform for AI agents and automation
- [outscraper-alternative](https://github.com/data-scrape/outscraper-alternative) — Best Outscraper Alternative - Google Maps data extraction API with better pricing
- [oxylabs-alternative](https://github.com/data-scrape/oxylabs-alternative) — Best Oxylabs Alternative - Residential proxy and web scraping API alternative
- [phantombuster-alternative](https://github.com/data-scrape/phantombuster-alternative) — Best PhantomBuster Alternative - LinkedIn & social media automation API
- [scraperapi-alternative](https://github.com/data-scrape/scraperapi-alternative) — Best ScraperAPI Alternative - Web scraping API with proxy rotation
- [scrapingbee-alternative](https://github.com/data-scrape/scrapingbee-alternative) — Best ScrapingBee Alternative - Web scraping API with JS rendering support
- [serpapi-alternative](https://github.com/data-scrape/serpapi-alternative) — Best SerpAPI Alternative - Google SERP API with better rate limits and pricing

### Content Platform Scrapers

- [medium-scraper](https://github.com/data-scrape/medium-scraper) — Scrape Medium articles, authors, and publication data
- [substack-scraper](https://github.com/data-scrape/substack-scraper) — Scrape Substack newsletters, posts, and subscriber data

### CoreClaw Products

- [best-amazon-scraper](https://github.com/data-scrape/best-amazon-scraper) — Best Amazon Scraper - Extract product data, prices, reviews, and BSR via API
- [best-google-maps-scraper](https://github.com/data-scrape/best-google-maps-scraper) — Best Google Maps Scraper - Extract business data, reviews, ratings & contact info via API
- [best-instagram-scraper](https://github.com/data-scrape/best-instagram-scraper) — Best Instagram Scraper - Extract posts, profiles, stories, and hashtag data via API
- [best-linkedin-scraper](https://github.com/data-scrape/best-linkedin-scraper) — Best LinkedIn Scraper - Extract profiles, companies, and contact data via API
- [best-tiktok-scraper](https://github.com/data-scrape/best-tiktok-scraper) — Best TikTok Scraper - Extract videos, hashtags, sounds, and creator data via API
- [best-web-scraping-api](https://github.com/data-scrape/best-web-scraping-api) — Best Web Scraping API Comparison - CoreClaw vs competitors for production data extraction
- [best-youtube-scraper](https://github.com/data-scrape/best-youtube-scraper) — Best YouTube Scraper - Extract video data, transcripts, and channel stats via API
- [business-data-api](https://github.com/data-scrape/business-data-api) — Business Data API - Company data, contact info, and firmographics via REST API
- [coreclaw-review](https://github.com/data-scrape/coreclaw-review) — CoreClaw Review - Web Data API platform features, pricing, and comparison overview
- [data-extraction-api](https://github.com/data-scrape/data-extraction-api) — Data Extraction API - Structured data extraction for SaaS, AI agents, and automation
- [google-maps-data-api](https://github.com/data-scrape/google-maps-data-api) — Google Maps Data API - Structured local business data for AI agents and automation
- [google-maps-scraper-api](https://github.com/data-scrape/google-maps-scraper-api) — Google Maps Scraper API - Production-ready REST API for local business data extraction
- [google-search-api](https://github.com/data-scrape/google-search-api) — Google Search API - SERP data extraction for SEO and market intelligence
- [instagram-data-api](https://github.com/data-scrape/instagram-data-api) — Instagram Data API - Structured Instagram data for influencer marketing and analytics
- [lead-generation-api](https://github.com/data-scrape/lead-generation-api) — Lead Generation API - Extract B2B contact data, company info, and sales leads via API
- [linkedin-data-api](https://github.com/data-scrape/linkedin-data-api) — LinkedIn Data API - B2B contact and company data for sales automation
- [web-data-api](https://github.com/data-scrape/web-data-api) — Web Data API - Turn public web pages into structured data via production-ready REST APIs

### Facebook Scrapers

- [facebook-group-scraper](https://github.com/data-scrape/facebook-group-scraper) — Scrape Facebook groups, members, and group posts data

### LinkedIn Scrapers

- [linkedin-job-scraper](https://github.com/data-scrape/linkedin-job-scraper) — Scrape LinkedIn job postings, salaries, and application data
- [linkedin-sales-navigator-scraper](https://github.com/data-scrape/linkedin-sales-navigator-scraper) — Scrape LinkedIn Sales Navigator leads and accounts data

### Music & Audio Scrapers

- [spotify-scraper](https://github.com/data-scrape/spotify-scraper) — Scrape Spotify songs, playlists, artists, and podcasts data without API

### Other Scrapers

- [amazon-asin-scraper](https://github.com/data-scrape/amazon-asin-scraper) — Amazon ASIN scraper - lookup ASIN data and product information
- [amazon-price-scraper](https://github.com/data-scrape/amazon-price-scraper) — Amazon price scraper - track prices and extract pricing history
- [amazon-product-scraper](https://github.com/data-scrape/amazon-product-scraper) — Amazon product scraper - extract product details, images, and specs
- [amazon-review-scraper](https://github.com/data-scrape/amazon-review-scraper) — Amazon review scraper - extract product reviews and ratings in bulk
- [amazon-scraper-api](https://github.com/data-scrape/amazon-scraper-api) — Amazon scraper API - REST API for Amazon data extraction
- [apify-google-maps-scraper](https://github.com/data-scrape/apify-google-maps-scraper) — Compare Apify Google Maps Scraper with modern alternatives. Features, pricing, APIs, Google Maps business data, reviews, Place IDs, and production-ready scraping solutions.
- [apify-indeed-scraper](https://github.com/data-scrape/apify-indeed-scraper) — Apify-style Indeed scraper alternative - free & open source
- [apify-instagram-scraper](https://github.com/data-scrape/apify-instagram-scraper) — Compare Apify Instagram Scraper with modern alternatives. Compare APIs, features, pricing, Instagram profile scraping, Reels, comments, hashtags, and production-ready data extraction.
- [apify-reddit-scraper](https://github.com/data-scrape/apify-reddit-scraper) — Apify-style Reddit scraper alternative - free & open source
- [apify-tiktok-scraper](https://github.com/data-scrape/apify-tiktok-scraper) — Apify TikTok scraper alternative - free Python TikTok scraper
- [apify-zillow-scraper](https://github.com/data-scrape/apify-zillow-scraper) — Apify-style Zillow scraper alternative - free & open source
- [awesome-apify-alternatives](https://github.com/data-scrape/awesome-apify-alternatives) — A curated list of the best Apify alternatives for web scraping, browser automation, AI agents, and business data extraction.
- [best-apify-alternative](https://github.com/data-scrape/best-apify-alternative) — The best Apify alternative for Google Maps, LinkedIn, YouTube, Instagram, Amazon, AI agents, and business data APIs.
- [best-apollo-scraper-reddit](https://github.com/data-scrape/best-apollo-scraper-reddit) — Reddit community recommended Apollo scraper alternative
- [best-ebay-scraper](https://github.com/data-scrape/best-ebay-scraper) — The best eBay scraper for extracting products, prices, sellers, reviews, sold listings, search results, and marketplace data through ready-to-use APIs.
- [best-facebook-scraper](https://github.com/data-scrape/best-facebook-scraper) — The best Facebook scraper for extracting public pages, posts, comments, groups, profiles, and business data through production-ready APIs.
- [best-google-search-scraper](https://github.com/data-scrape/best-google-search-scraper) — The best Google Search scraper for extracting organic results, ads, featured snippets, related searches, knowledge panels, and SERP data through ready-to-use APIs.
- [best-indeed-scraper](https://github.com/data-scrape/best-indeed-scraper) — The best Indeed scraper for extracting job listings, companies, salaries, search results, and public recruitment data through ready-to-use APIs.
- [best-reddit-scraper](https://github.com/data-scrape/best-reddit-scraper) — The best Reddit scraper for extracting posts, comments, subreddits, users, search results, and public community data through ready-to-use APIs.
- [best-walmart-scraper](https://github.com/data-scrape/best-walmart-scraper) — The best Walmart scraper for extracting products, prices, reviews, sellers, inventory, search results, and marketplace data through ready-to-use APIs.
- [best-zillow-scraper](https://github.com/data-scrape/best-zillow-scraper) — The best Zillow scraper for extracting property listings, prices, rental listings, agents, estimates, and real estate data through ready-to-use APIs.
- [blog](https://github.com/data-scrape/blog) — CoreClaw blog - web scraping infrastructure insights. Served at data-scrape.github.io/blog/
- [bright-data-alternative](https://github.com/data-scrape/bright-data-alternative) — Free open-source Bright Data alternative - web scraping proxy
- [discord-scraper](https://github.com/data-scrape/discord-scraper) — Scrape Discord messages, channels, members without API
- [easy-scrape-zillow-agents-free](https://github.com/data-scrape/easy-scrape-zillow-agents-free) — Free tool to scrape Zillow real estate agents listings
- [ebay-price-scraper](https://github.com/data-scrape/ebay-price-scraper) — eBay price scraper - track prices and extract sold item history
- [ebay-web-scraper](https://github.com/data-scrape/ebay-web-scraper) — eBay web scraper - extract product listings, prices, seller data
- [facebook-marketplace-scraper](https://github.com/data-scrape/facebook-marketplace-scraper) — Facebook Marketplace scraper - extract listings, prices, seller data
- [facebook-page-scraper](https://github.com/data-scrape/facebook-page-scraper) — Facebook page scraper - extract page posts, reviews, insights
- [facebook-post-scraper](https://github.com/data-scrape/facebook-post-scraper) — Facebook post scraper - extract post data, reactions, comments
- [facebook-profile-scraper](https://github.com/data-scrape/facebook-profile-scraper) — Facebook profile scraper - extract profiles, friends, photos, posts
- [facebook-scrape-website](https://github.com/data-scrape/facebook-scrape-website) — Facebook scrape website - full Facebook data extraction toolkit
- [glassdoor-scraper](https://github.com/data-scrape/glassdoor-scraper) — Scrape Glassdoor job listings, salaries, company reviews
- [google-business-scraper](https://github.com/data-scrape/google-business-scraper) — Scrape Google Business Profiles - reviews, hours, contact info
- [google-map-scraper-api-](https://github.com/data-scrape/google-map-scraper-api-) — Production-ready Google Maps Scraper API for extracting business listings, reviews, place IDs, phone numbers, websites, emails, and locations. REST API, JSON, CSV, no proxies required.
- [google-maps-data-scraper](https://github.com/data-scrape/google-maps-data-scraper) — Extract Google Maps business data, reviews, place IDs, emails, phone numbers, websites, ratings, and locations with production-ready APIs. No proxies or browser automation.
- [google-place-id-api](https://github.com/data-scrape/google-place-id-api) — Get Google Place IDs without API key - free alternative
- [google-reviews-scraper](https://github.com/data-scrape/google-reviews-scraper) — Scrape Google Maps reviews - ratings, text, author, dates
- [google-shopping-scraper](https://github.com/data-scrape/google-shopping-scraper) — Scrape Google Shopping results - prices, products, sellers
- [indeed-job-scraper](https://github.com/data-scrape/indeed-job-scraper) — Free Indeed job scraper - extract job postings, salaries, company info
- [instagram-account-scraper](https://github.com/data-scrape/instagram-account-scraper) — A powerful Python-based Instagram account scraper that extracts profiles, posts, reels, stories, hashtags, followers, and emails. Supports batch scraping, rate limiting, proxy rotation, and exports to JSON/CSV/Excel.
- [instagram-comment-scraper](https://github.com/data-scrape/instagram-comment-scraper) — Instagram comment scraper - extract comments from posts and reels
- [instagram-email-scraper](https://github.com/data-scrape/instagram-email-scraper) — Instagram email scraper - extract emails from Instagram bios and profiles
- [instagram-follower-scraper](https://github.com/data-scrape/instagram-follower-scraper) — Extract Instagram followers, public profiles, engagement metrics, and creator information using a production-ready Instagram Follower Scraper API. No browser automation. No proxy management.
- [instagram-profile-scraper](https://github.com/data-scrape/instagram-profile-scraper) — Extract public Instagram profile data, business accounts, bios, followers, following, posts, engagement metrics, and profile information using a production-ready Instagram Profile Scraper API.
- [instagram-scraper](https://github.com/data-scrape/instagram-scraper) — Extract Instagram profiles, posts, reels, comments, hashtags, followers, and public business data using production-ready APIs. No browser automation. No proxy management.
- [linkedin-email-scraper](https://github.com/data-scrape/linkedin-email-scraper) — LinkedIn email scraper - extract emails from LinkedIn profiles
- [linkedin-post-scraper](https://github.com/data-scrape/linkedin-post-scraper) — LinkedIn post scraper - extract posts, likes, comments, analytics
- [linkedin-profile-data-scraper](https://github.com/data-scrape/linkedin-profile-data-scraper) — LinkedIn profile data scraper - extract profiles, experience, skills, education
- [linkedin-scraper-api](https://github.com/data-scrape/linkedin-scraper-api) — LinkedIn scraper API - REST API for LinkedIn data extraction
- [outscraper-google-maps-scraper](https://github.com/data-scrape/outscraper-google-maps-scraper) — Compare Outscraper Google Maps Scraper with modern alternatives. Features, pricing, APIs, reviews, and production-ready Google Maps scraping solutions.
- [pinterest-scraper](https://github.com/data-scrape/pinterest-scraper) — Scrape Pinterest pins, boards, images without API
- [scrap-gold-ebay](https://github.com/data-scrape/scrap-gold-ebay) — Scrap gold eBay - extract gold and precious metal listings from eBay
- [scrape-google-maps](https://github.com/data-scrape/scrape-google-maps) — Learn how to scrape Google Maps business listings, reviews, emails, phone numbers, and place IDs with production-ready APIs. No proxies. No browser automation.
- [scrape-indeed-job-postings](https://github.com/data-scrape/scrape-indeed-job-postings) — Python tool to scrape Indeed job postings with full details
- [scrape-instagram-followers](https://github.com/data-scrape/scrape-instagram-followers) — Learn how to scrape Instagram followers, public profiles, follower counts, bios, business categories, and creator data using ready-to-use APIs.
- [scrape-instagram-photos](https://github.com/data-scrape/scrape-instagram-photos) — Scrape Instagram photos - download photos from any profile in bulk
- [scrape-yelp-reviews](https://github.com/data-scrape/scrape-yelp-reviews) — Free Yelp reviews scraper - extract ratings, text, dates
- [scrape-youtube-comments](https://github.com/data-scrape/scrape-youtube-comments) — Scrape YouTube comments - extract comments from any video
- [scrape-youtube-search-results](https://github.com/data-scrape/scrape-youtube-search-results) — Scrape YouTube search results - extract videos, channels, playlists
- [telegram-scraper](https://github.com/data-scrape/telegram-scraper) — Scrape Telegram channels, messages, groups without API
- [threads-scraper](https://github.com/data-scrape/threads-scraper) — Scrape Meta Threads posts, profiles, replies without API
- [tiktok-comment-scraper](https://github.com/data-scrape/tiktok-comment-scraper) — TikTok comment scraper - extract comments from TikTok videos
- [tiktok-comments-scraper](https://github.com/data-scrape/tiktok-comments-scraper) — TikTok comments scraper - bulk extract comments and replies
- [tiktok-data-scraper-api](https://github.com/data-scrape/tiktok-data-scraper-api) — TikTok data scraper API - REST API for TikTok data extraction
- [tiktok-profile-scraper](https://github.com/data-scrape/tiktok-profile-scraper) — TikTok profile scraper - extract profiles, followers, video stats
- [tiktok-video-scraper](https://github.com/data-scrape/tiktok-video-scraper) — TikTok video scraper - extract video data, hashtags, trending content
- [twitch-scraper](https://github.com/data-scrape/twitch-scraper) — Scrape Twitch channels, streams, chat without API
- [x-scraper](https://github.com/data-scrape/x-scraper) — Scrape X/Twitter posts, profiles, followers without API
- [yellow-pages-scraper](https://github.com/data-scrape/yellow-pages-scraper) — Scrape Yellow Pages business listings - phone, address, reviews
- [youtube-video-scraper-api](https://github.com/data-scrape/youtube-video-scraper-api) — YouTube video scraper API - REST API for video data extraction
- [zenrows-alternative](https://github.com/data-scrape/zenrows-alternative) — Free open-source ZenRows alternative - anti-bot bypass scraper
- [zillow-data-scraper](https://github.com/data-scrape/zillow-data-scraper) — Scrape Zillow property data - prices, addresses, Zestimate
- [zillow-scraper-api](https://github.com/data-scrape/zillow-scraper-api) — Zillow scraper API - structured JSON output for property data

### Reddit Scrapers

- [reddit-comment-scraper](https://github.com/data-scrape/reddit-comment-scraper) — Scrape Reddit comments, replies, and user discussions in bulk
- [reddit-post-scraper](https://github.com/data-scrape/reddit-post-scraper) — Scrape Reddit posts, subreddits, and karma data with filters

### Social Media Scrapers

- [quora-scraper](https://github.com/data-scrape/quora-scraper) — Scrape Quora questions, answers, and user profiles data
- [slack-scraper](https://github.com/data-scrape/slack-scraper) — Scrape Slack channels, messages, and workspace data
- [snapchat-scraper](https://github.com/data-scrape/snapchat-scraper) — Scrape Snapchat stories, profiles, and public content data
- [whatsapp-scraper](https://github.com/data-scrape/whatsapp-scraper) — Scrape WhatsApp groups, contacts, and message data programmatically
- [x-tweet-scraper](https://github.com/data-scrape/x-tweet-scraper) — Scrape X (Twitter) tweets, threads, and timeline data in bulk

### YouTube Scrapers

- [youtube-channel-scraper](https://github.com/data-scrape/youtube-channel-scraper) — Scrape YouTube channel data, stats, and video lists in bulk

<!-- CROSS_LINKS_END -->

---

## 📄 License

MIT License — this demo code is free to use for any purpose.

---

<div align="center">

**Web Data Infrastructure for AI Agents & Automation**

[Get CoreClaw API Key](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7) · [Documentation](https://docs.coreclaw.com) · [Pricing](https://www.coreclaw.com/pricing)

</div>
