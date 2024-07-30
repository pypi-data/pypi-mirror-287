# logging-extenson
Extension of built-in python module `logging`


## Instalation
```
pip install logging-extension
```


## Extensions
### JSONFormatter
Formats logs in JSON format
<details>
<summary>
Configuration example
</summary>



```python
import logging
from logging_extension import JSONFormatter


json_formatter = JSONFormatter(fmt_keys=dict(
    logger='name',
    level='levelno',
))

logging.basicConfig(level='DEBUG', force=True)
logging.getLogger().handlers[0].setFormatter(json_formatter)

logging.getLogger().info('info_message', extra={'extra': ['value']})
```

    {"logger": "root", "level": 20, "created": "2024-07-29T12:35:21.505616+00:00", "message": "info_message", "extra": ["value"]}



</details>

<details>
<summary>
Dictionary-based configuration example
</summary>



```python
import logging.config


config = {
    "version": 1,
    "disable_existing_handlers": False,
    "formatters": {
        "json_formatter": {
            "()": "logging_extension.JSONFormatter",
            "fmt_keys": {
                "name": "name",
                "level": "levelno",
            }
        }
    },
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
            "formatter": "json_formatter"
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "stream_handler"
        ]
    }
}

logging.config.dictConfig(config)
logging.debug('debug_msg', extra={'extra': ['value']})
```

    {"name": "root", "level": 10, "created": "2024-07-29T12:35:21.513188+00:00", "message": "debug_msg", "extra": ["value"]}


</details>

### LevelFilter
Logging level filter. Allows specifying a comparison function from the built-in `operator` module or providing your own.
<details>
<summary>
Configuration example
</summary>


```python
import logging 
from logging_extension import LevelFilter

# `compare` argument also can be any function that compares levels
# e.g. compare(record_level: int, filter_level: int) -> bool: ...
only_error_filter = LevelFilter(level='ERROR', compare='eq', name='only_error_filter')

logging.basicConfig(level='DEBUG', force=True)
logging.getLogger().addFilter(only_error_filter)

logging.critical('skip critical')
logging.error('show error')
```

    ERROR:root:show error



</details>


<details>
<summary>
Dictionary-based configuration example
</summary>


```python
import logging.config

config = {
    "version": 1,
    "disable_existing_handlers": False,
    "filters": {
        "only_error_filter": {
            "()": "logging_extension.LevelFilter",
            "level": "ERROR",
            "compare": "eq",
        }
        
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "filters": [
                "only_error_filter",
            ]
        }
    }
}
logging.config.dictConfig(config)

logging.critical('skip critical', extra={'extra': 'value'})
logging.error('show error', extra={'extra': 'value'})

logging.getLogger().filters.clear()
```

    ERROR:root:show error




</details>

### ThreadedHandler
Container for handlers that perform non-blocking logging in a separate thread.
Essentially, a wrapper around `QueueHandler` with automatic start of `QueueListener` using the provided handlers.
<details>
<summary>
Configuration example
</summary>










```python
import logging
from logging_extension import ThreadedHandler


threaded_handler = ThreadedHandler(
    handler_0=logging.StreamHandler(),
    handler_2=logging.StreamHandler(),
)

logging.basicConfig(force=True, level='DEBUG')
logging.getLogger().handlers = [threaded_handler]

logging.getLogger().warning('debug msg')
print('in main thread')
```
    in main thread
    debug msg
    debug msg

</details>



<details>
<summary>
Dictionary-based configuration example
</summary>



```python
import logging.config


config = {
    "version": 1,
    "disable_existing_handlers": False,
    "handlers": {
        "stream_handler_0": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "stream_handler_1": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "threaded_handler": {
            "()": "logging_extension.ThreadedHandler",
            "handler_0": "cfg://handlers.stream_handler_0",
            "handler_1": "cfg://handlers.stream_handler_1",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "threaded_handler"
        ]
    }
}

logging.config.dictConfig(config)

logging.getLogger().warning('debug msg')
print('in main thread')
```
    debug msg
    in main thread
    debug msg

</details>

