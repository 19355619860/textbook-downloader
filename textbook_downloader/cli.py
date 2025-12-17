"""
Command-line interface for Textbook Downloader.
"""

import argparse
import sys
import os
from .downloader import TextbookDownloader


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Textbook Downloader - Download electronic textbooks and academic ebooks"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search for textbooks")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument(
        "-s", "--source",
        help="Specific source to search (searches all if not specified)"
    )
    
    # Download command
    download_parser = subparsers.add_parser("download", help="Download a textbook")
    download_parser.add_argument("url", help="URL of the textbook")
    download_parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output file path"
    )
    download_parser.add_argument(
        "-s", "--source",
        help="Source name (auto-detects if not specified)"
    )
    
    # List sources command
    subparsers.add_parser("sources", help="List available sources")
    
    # Info command
    subparsers.add_parser("info", help="Show detailed information about sources")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    downloader = TextbookDownloader()
    
    if args.command == "search":
        print(f"Searching for: {args.query}")
        if args.source:
            print(f"Source: {args.source}")
        print()
        
        results = downloader.search(args.query, args.source)
        
        if not results:
            print("No results found.")
            return 0
        
        print(f"Found {len(results)} result(s):\n")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result.get('title', 'Unknown Title')}")
            print(f"   Author: {result.get('author', 'Unknown')}")
            print(f"   Source: {result.get('source', 'Unknown')}")
            print(f"   Format: {result.get('format', 'Unknown')}")
            print(f"   URL: {result.get('url', 'N/A')}")
            print()
    
    elif args.command == "download":
        print(f"Downloading from: {args.url}")
        print(f"Output: {args.output}")
        if args.source:
            print(f"Source: {args.source}")
        print()
        
        success = downloader.download(args.url, args.output, args.source)
        
        if success:
            print(f"✓ Successfully downloaded to: {args.output}")
            return 0
        else:
            print("✗ Download failed")
            return 1
    
    elif args.command == "sources":
        sources = downloader.list_sources()
        print("Available sources:")
        for source in sources:
            print(f"  • {source}")
    
    elif args.command == "info":
        info = downloader.get_source_info()
        print("Source Information:\n")
        for source_name, source_info in info.items():
            print(f"• {source_name}")
            print(f"  Base URL: {source_info['base_url']}")
            print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
