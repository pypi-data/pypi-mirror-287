# loggext-py
logging extensions for pythons logging library

<!-- TOC -->
* [loggext-py](#loggext-py)
  * [Installation](#installation)
  * [Usage](#usage)
<!-- TOC -->

## Installation

```shell
pip install loggext
```

## Usage

```python
import logging
from loggext.decorators import add_logging

logging.basicConfig(level=logging.NOTSET)

@add_logging()
def myfn(arg):
    ...  # stuff

myfn("value")
# DEBUG:root:<function myfn at 0x7f06a6cc3400> was called with ('value')
# DEBUG:root:<function myfn at 0x7f06a6cc3400> returned None after 65μs+614ns
```
