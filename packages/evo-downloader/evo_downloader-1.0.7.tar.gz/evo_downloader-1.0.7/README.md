# Evo Downloader

[![codecov](https://codecov.io/gh/maycuatroi/evo_downloader/branch/main/graph/badge.svg?token=evo_downloader_token_here)](https://codecov.io/gh/maycuatroi/evo_downloader)
[![CI](https://github.com/maycuatroi/evo_downloader/actions/workflows/main.yml/badge.svg)](https://github.com/maycuatroi/evo_downloader/actions/workflows/main.yml)

This module contains the main functionality for downloading files, including support for multi-threaded downloads and handling servers that do not support range requests.

## Install it from PyPI

```bash
pip install evo-downloader
```

## Usage

### As a Library

You can use `evo-download` to download files programmatically.

```python
from evo_downloader.downloader import Downloader

downloader = Downloader(num_threads=10)

# Example file URLs
file_urls = [
    # url only
    "http://images.cocodataset.org/annotations/image_info_test2014.zip",
    # Tuple with file name
    ('evo_downloader.zip', 'https://github.com/maycuatroi/evo_downloader/archive/refs/heads/main.zip')
]

downloaded_files = downloader.download_files(file_urls, "example_folder")

for file_path in downloaded_files:
    print(f"Downloaded: {file_path}")
```

### CLI Usage

You can also use `edownload` from the command line.

```bash
$ python -m edownload download http://images.cocodataset.org/annotations/image_info_test2014.zip --folder example_folder --num-threads 10

# or if installed as a script
$ edownload download http://images.cocodataset.org/annotations/image_info_test2014.zip --folder example_folder --num-threads 10
```

### Example Commands

```bash
# Download a file with range support
$ evo_downloader download http://images.cocodataset.org/annotations/image_info_test2014.zip --folder example_folder --num-threads 10

# Download a file without range support
$ evo_downloader download https://github.com/maycuatroi/evo_downloader/archive/refs/heads/main.zip --folder example_folder --num-threads 10
```

### download_example.py

This example demonstrates how to use the `Downloader` class to download files programmatically.



_Evo Downloader developed with ❤️ by maycuatroi_
