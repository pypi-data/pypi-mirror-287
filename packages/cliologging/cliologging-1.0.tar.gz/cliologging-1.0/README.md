# Cliologging

![version](https://img.shields.io/badge/version-1.0-blue)

The cliologging library is an add-on to the official Python logging library.
Clio is one of the nine Muses, and is the muse of history and annals. This name suggests an ability to record and archive events so that you can keep a log of your projects.

![log-exemple.png](https://i.postimg.cc/nVG2vt3p/log-exemple.png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install cliologging
```

## Usage

```python
from cliologging import logger

log = logger.create('mylogger', "./log/debug.log")

log.debug("This is a debug log level message.")
log.info("This is a information log level message.")
log.warning("This is a warning log level message.")
log.error("This is a error log level message.")
log.critical("This is a critical log level message.")
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
