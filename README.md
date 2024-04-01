# canada-recalls-api

This package is under development and currently used to interact with the canadian governments automotive database. 

Currently supports the use of simple querying on the API and retrieving counts.

# How to install

```Python
pip install canada_recalls
```

# Example

```Python
from canada_recalls import *

c = CanadaRecalls()

c.list()
```