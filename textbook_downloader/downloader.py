"""
Main downloader class for managing textbook downloads.
"""

import os
from typing import List, Dict, Optional
from urllib.parse import urlparse
from .sources import BaseSource, LibraryGenesisSource, OpenLibrarySource, ProjectGutenbergSource


class TextbookDownloader:
    """Main class for downloading textbooks from multiple sources."""

    def __init__(self):
        """Initialize the downloader with available sources."""
        self.sources = [
            LibraryGenesisSource(),
            OpenLibrarySource(),
            ProjectGutenbergSource()
        ]

    def add_source(self, source: BaseSource):
        """
        Add a custom source to the downloader.
        
        Args:
            source: A BaseSource implementation
        """
        self.sources.append(source)

    def list_sources(self) -> List[str]:
        """
        Get list of available sources.
        
        Returns:
            List of source names
        """
        return [source.name for source in self.sources]

    def search(self, query: str, source_name: Optional[str] = None) -> List[Dict]:
        """
        Search for textbooks across sources.
        
        Args:
            query: Search query string
            source_name: Optional specific source to search (searches all if None)
            
        Returns:
            List of search results
        """
        results = []
        
        if source_name:
            # Search specific source
            for source in self.sources:
                if source.name == source_name:
                    results.extend(source.search(query))
                    break
        else:
            # Search all sources
            for source in self.sources:
                try:
                    results.extend(source.search(query))
                except Exception as e:
                    print(f"Error searching {source.name}: {e}")
        
        return results

    def download(self, url: str, output_path: str, source_name: Optional[str] = None) -> bool:
        """
        Download a textbook.
        
        Args:
            url: URL of the textbook
            output_path: Path to save the downloaded file
            source_name: Optional source name (auto-detects if None)
            
        Returns:
            True if download successful, False otherwise
        """
        # Ensure output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        if source_name:
            # Use specific source
            for source in self.sources:
                if source.name == source_name:
                    return source.download(url, output_path)
            print(f"Source '{source_name}' not found")
            return False
        else:
            # Try to auto-detect source from URL
            parsed_url = urlparse(url)
            hostname = parsed_url.hostname or ""
            
            for source in self.sources:
                source_hostname = urlparse(source.base_url).hostname or ""
                if hostname == source_hostname:
                    return source.download(url, output_path)
            
            # If no source detected, require explicit source specification
            print(f"Error: Could not detect source from URL: {url}")
            print("Please specify the source using --source parameter")
            return False

    def get_source_info(self) -> Dict[str, Dict]:
        """
        Get information about all available sources.
        
        Returns:
            Dictionary with source information
        """
        info = {}
        for source in self.sources:
            info[source.name] = {
                "base_url": source.base_url,
                "name": source.name
            }
        return info
