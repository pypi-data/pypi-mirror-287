# GUGiK API

A Python client for the GUGiK API [link](https://uldk.gugik.gov.pl/opis.html#)

## Installation

```sh
pip install gugik_api
```


# Usage

```python
from gugik_api.gugik_api import GUGiKAPI

api = GUGiKAPI()

# Pobierz działkę przez identyfikator
parcel_info = api.get_object_by_id(request_type='GetParcelById', identifier='141201_1.0001.6509')
print(parcel_info)

# Pobierz budynek przez identyfikator
building_info = api.get_object_by_id(request_type='GetBuildingById', identifier='141301_1.0010.713/2.5_BUD')
print(building_info)
```

# Local install 
```sh
pip install -e .
```

# Package
## Install dependencies
```sh
pip install twine setuptools wheel
```

## Build package
```sh
python setup.py sdist bdist_wheel
```

# Tests
```sh
tox
```