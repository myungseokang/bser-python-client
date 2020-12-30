# BSER Python API Client

> [블랙서바이벌: 영원회귀 openapi](https://developer.eternalreturn.io/) 를 위한 Python API Client 입니다.
>
> A Python API Client for [Black Survival: Eternal Return openapi](https://developer.eternalreturn.io/).

## Requirements

- Python 3.6 or higher
- [requests](https://github.com/psf/requests)

## Installation

```
$ pip install bser-python-client
```

If you use pipenv,

```
$ pipenv install bser-python-client
```

## Example

Before run examples,

```
$ python setup.py develop
```

And then,

```python
from bser_client import BserAPIClient

api_client = BserAPIClient(api_key='your_token', version='v1')

characters = api_client.fetch_meta_data(meta_type='Character')

for character in characters:
    print(character.get('name'))
```

[More examples](/examples)
