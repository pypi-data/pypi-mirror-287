# frii.site Python API
The official API for contacting frii.site through it's API

## Installation
You can install this package using pip
`pip install frii_site`

## Usage
This package is very easy to use. First initialize the API.
```python
from frii_site.api import API

api = API("your-api-key")

api.modify(domain="super-awesome-domain",content="1.2.3.4",type_="A") # True
api.modify(domain="domain-i-dont-own",content="1.2.3.4",type_="A") # InvalidPerms exception
```

## Creating an API key
There are two methods to creating an API key. The recommended one is explained [here](https://github.com/ctih1/frii.site-frontend/wiki/API#getting-started)
The second method (not recommended) is to create the API using this library.
```python
from frii_site.perms import permissions as p
api_key = api.create(auth_token="",domains=["super-awesome-domain","another-domain"],perms=[p.MODIFY_CONTENT,...])
```