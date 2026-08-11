#!/usr/bin/env python3
"""
amazon-product-api - CoreClaw Amazon API Demo

This script demonstrates how to use CoreClaw's Web Data API for Amazon data extraction.

Sponsored by CoreClaw - https://www.coreclaw.com
"""

import argparse
import json
import sys
import time
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any

try:
    import requests
except ImportError:
    print("Installing requests...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests


@dataclass
class CoreClawResult:
    """Data model for CoreClaw API response."""
    id: str = ""
    name: str = ""
    address: str = ""
    phone: str = ""
    website: str = ""
    rating: float = 0.0
    reviews_count: int = 0
    categories: list = None
    latitude: float = 0.0
    longitude: float = 0.0
    metadata: Dict[str, Any] = None
    scraped_at: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


class AmazonProductApi:
    """CoreClaw Amazon API client demo."""

    BASE_URL = "https://api.coreclaw.com/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "CoreClaw-Demo/1.0",
        })
        self.results: List[CoreClawResult] = []

    def search(self, query: str, limit: int = 100) -> List[CoreClawResult]:
        """Search Amazon data via CoreClaw API."""
        url = f"{self.BASE_URL}/ecommerce/amazon"
        params = {"query": query, "limit": limit, "format": "json"}
        print(f"Calling CoreClaw API: {url}")
        resp = self.session.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        for item in data.get("results", []):
            self.results.append(CoreClawResult(
                id=item.get("id", ""),
                name=item.get("name", ""),
                address=item.get("address", ""),
                phone=item.get("phone", ""),
                website=item.get("website", ""),
                rating=item.get("rating", 0.0),
                reviews_count=item.get("reviews_count", 0),
                categories=item.get("categories", []),
                latitude=item.get("latitude", 0.0),
                longitude=item.get("longitude", 0.0),
                metadata=item,
                scraped_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            ))
        return self.results

    def export(self, filepath: str, fmt: str = "json") -> None:
        """Export results to JSON or CSV."""
        data = [r.to_dict() for r in self.results]
        if fmt == "csv":
            import csv
            if not data:
                print("No data to export.")
                return
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        else:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Exported {len(data)} records to {filepath}")


def main():
    parser = argparse.ArgumentParser(description="amazon-product-api - CoreClaw Amazon API Demo")
    parser.add_argument("--api-key", required=True, help="CoreClaw API key")
    parser.add_argument("--query", "-q", required=True, help="Search query")
    parser.add_argument("--output", "-o", default="output.json", help="Output file")
    parser.add_argument("--format", "-f", choices=["json", "csv"], default="json")
    parser.add_argument("--limit", "-m", type=int, default=50, help="Max results")
    args = parser.parse_args()

    client = AmazonProductApi(api_key=args.api_key)
    client.search(args.query, args.limit)
    client.export(args.output, args.format)
    print(f"Done! Got {len(client.results)} records from CoreClaw Amazon API.")
    print(f"Get your API key: https://www.coreclaw.com")


if __name__ == "__main__":
    main()
