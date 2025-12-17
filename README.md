# Textbook Downloader

An open-source tool designed to help users download electronic textbooks and academic ebooks easily and efficiently. It supports multiple sources and provides a simple workflow for accessing educational resources.

## Features

- 🔍 **Multi-source Search**: Search across multiple textbook sources simultaneously
- 📚 **Multiple Format Support**: Download textbooks in various formats (PDF, EPUB, etc.)
- 🚀 **Simple CLI Interface**: Easy-to-use command-line interface
- 🔌 **Extensible Architecture**: Add custom sources with ease
- 📖 **Support for Popular Sources**: 
  - Library Genesis
  - Open Library
  - Project Gutenberg

## Installation

### From Source

```bash
git clone https://github.com/19355619860/textbook-downloader.git
cd textbook-downloader
pip install -r requirements.txt
pip install -e .
```

### Using pip (once published)

```bash
pip install textbook-downloader
```

## Usage

### Command Line Interface

#### Search for textbooks

Search across all sources:
```bash
textbook-downloader search "introduction to algorithms"
```

Search in a specific source:
```bash
textbook-downloader search "python programming" --source "Open Library"
```

#### Download a textbook

```bash
textbook-downloader download <url> --output /path/to/save/textbook.pdf
```

With specific source:
```bash
textbook-downloader download <url> --output textbook.pdf --source "Library Genesis"
```

#### List available sources

```bash
textbook-downloader sources
```

#### Get detailed source information

```bash
textbook-downloader info
```

### Python API

You can also use Textbook Downloader in your Python code:

```python
from textbook_downloader import TextbookDownloader

# Create downloader instance
downloader = TextbookDownloader()

# Search for textbooks
results = downloader.search("machine learning")
for result in results:
    print(f"{result['title']} by {result['author']}")

# Download a textbook
downloader.download(
    url="https://example.com/textbook.pdf",
    output_path="./downloads/textbook.pdf"
)

# List available sources
sources = downloader.list_sources()
print(f"Available sources: {', '.join(sources)}")
```

## Supported Sources

| Source | Website | Formats |
|--------|---------|---------|
| Library Genesis | https://libgen.is | PDF, EPUB, DJVU |
| Open Library | https://openlibrary.org | EPUB, PDF |
| Project Gutenberg | https://www.gutenberg.org | EPUB, HTML, Plain Text |

## Contributing

Contributions are welcome! Feel free to:
- Add new sources
- Improve existing functionality
- Fix bugs
- Enhance documentation

## Requirements

- Python 3.7 or higher
- requests >= 2.31.0
- beautifulsoup4 >= 4.12.0
- lxml >= 4.9.0

## License

This project is open-source and available under the MIT License.

## Disclaimer

This tool is intended for downloading legally available educational resources. Users are responsible for ensuring they have the right to download and use any materials. Always respect copyright laws and the terms of service of the sources you access.

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/19355619860/textbook-downloader).
