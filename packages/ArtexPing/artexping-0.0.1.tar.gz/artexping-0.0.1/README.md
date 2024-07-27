# Internet active checkking Project

This project leverages `requests` module to check internet connectivity. It's designed for simplicity and ease of use, allowing you to check internet connection active status.

## Features

- **Check internet**: Check if your device have a proper working internet connection or not.

## Prerequisites

- `requests`

## Setup

1. **Install dependencies**:
    ```sh
    pip install requests
    ```

## Usage

To use the functionality, import the `checkConnection` function from `ArtexPing`.

```python

from ArtexPing import InternetStatus

a = InternetStatus(output_file_path="output.txt")
a.checkConnection()

```

## Continuous Usage

If you want to check internet connection active status continuously, it is recommended to use threading. This will prevent the function from blocking the execution of further code until it is stopped.

Example with Threading
```python
import threading
import time
from ArtexPing import InternetStatus

a = InternetStatus(output_file_path="output.txt", continous=True)
ping_thread = threading.thread(target=a.checkStatus())

ping_thread.start()
time.sleep(10)
a.quit()
thread.join()
```

**This project is managed by Artex AI. Soon an improved and stable version will roll out**