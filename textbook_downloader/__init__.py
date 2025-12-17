"""
Textbook Downloader - An open-source tool for downloading electronic textbooks and academic ebooks.
"""

__version__ = "0.1.0"
__author__ = "Textbook Downloader Team"

from .downloader import TextbookDownloader
from .sources import BaseSource

__all__ = ["TextbookDownloader", "BaseSource"]
