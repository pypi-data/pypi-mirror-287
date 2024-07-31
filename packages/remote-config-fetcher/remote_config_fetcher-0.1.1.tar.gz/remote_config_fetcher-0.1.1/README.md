# Remote Config Fetcher

A package to fetch Firebase RemoteConfig values.

## Installation

```bash
pip install remote_config_fetcher
```

## Usage

```python
from remote_config_fetcher import RemoteConfigFetcher

config_fetcher = RemoteConfigFetcher('path/to/your/serviceAccountKey.json')
values = config_fetcher.get_remote_config_values()
print(values)
```
