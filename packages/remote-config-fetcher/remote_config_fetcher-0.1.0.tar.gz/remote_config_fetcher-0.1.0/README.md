# Firebase RemoteConfig

An small python package to retrieve Firebase Remote Config Values.

## Install

```bash
pip install remote_config_fetcher
```

## Usage

```python
from firebase_remote_config import FirebaseRemoteConfig

# Init the remote config credentials path
config = FirebaseRemoteConfig('ruta/a/tu/archivo/serviceAccountKey.json')

# get remote config values
values = config.get_remote_config_values()
print(values)
```
