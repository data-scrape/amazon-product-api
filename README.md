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
<!-- CROSS_LINKS_END -->

---

## 📄 License

MIT License — this demo code is free to use for any purpose.

---

<div align="center">

**Web Data Infrastructure for AI Agents & Automation**

[Get CoreClaw API Key](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7) · [Documentation](https://docs.coreclaw.com) · [Pricing](https://www.coreclaw.com/pricing)

</div>
