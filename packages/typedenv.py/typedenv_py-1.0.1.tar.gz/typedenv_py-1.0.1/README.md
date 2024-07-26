[![Python 3.10](https://github.com/ShajeshJ/typedenv.py/actions/workflows/python-3.10.yml/badge.svg?branch=main)](https://github.com/ShajeshJ/typedenv.py/actions/workflows/python-3.10.yml)
[![Python 3.11](https://github.com/ShajeshJ/typedenv.py/actions/workflows/python-3.11.yml/badge.svg?branch=main)](https://github.com/ShajeshJ/typedenv.py/actions/workflows/python-3.11.yml)
[![Python 3.12](https://github.com/ShajeshJ/typedenv.py/actions/workflows/python-3.12.yml/badge.svg?branch=main)](https://github.com/ShajeshJ/typedenv.py/actions/workflows/python-3.12.yml)

# typedenv.py
Load environment variables with class type hints

## 🚀 Quickstart
The library supports type hints for `str`, `int`, `float`, and `bool` out of the box.

```python
import typedenv

# Assuming the given environment variables
# $ export LOG_LEVEL=INFO
# $ export POOL_SIZE=100
# $ export DEBUG=1
# $ export SCALING=1.5

class EnvConfig(typedenv.EnvLoader):
    LOG_LEVEL: str
    POOL_SIZE: int
    DEBUG: bool
    SCALING: float

env = EnvConfig()
assert env.LOG_LEVEL == "INFO"
assert env.POOL_SIZE == 100
assert env.DEBUG == True
assert env.SCALING == 1.5
```

## 📚 Documentation
Environment variables will be loaded into the instance of your class
on initialization. The name of the class attributes will be used
to look up the corresponding environment variables. Only attributes
that are capitalized and are type-hinted will be loaded.

### Optional Keys
By default, a ValueError is raised if an environment key matching
your class attribute is not found. To make keys optional, you can either
give them default values, use `typing.Optional`, or union your type with `None`.

```python
class EnvConfig(typedenv.EnvLoader):
    DEBUG: bool = True
    API_KEY: str | None
    MAX_SIZE: typing.Optional[int]
```

### Supporting Additional Types
Additional support for types can be added by providing a converting function
through `typedenv.Converter`. These can either passed in as a class option or
through `typing.Annotated` for a specific key.

```python
def str_list(value: str) -> list[str]:
    return value.split(",")

def to_path(value: str) -> Path:
    return Path(value)

class EnvConfig(typedenv.EnvLoader, converters=[typedenv.Converter(str_list)]):
    CLUSTERS: list[str]
    CONFIG_FILE: typing.Annotated[Path, typedenv.Converter(to_path)]
```

### Validation and Transformation
In addition to supporting new types, `typedenv.Converter` can also be used to
validate and transform already supported types.

```python
def validate_str(value: str) -> str:
    if not value.isalnum():
        raise ValueError("only letters/numbers allowed")
    return value.upper()

class EnvConfig(typedenv.EnvLoader, converters=[typedenv.Converter(validate_str)]):
    API_KEY: str
```

### Mutability
By default, attributes loaded with an environment variable will be immutable.
This can be disabled through the `frozen` option.

```python
class EnvConfig(typedenv.EnvLoader, frozen=False):
    TIMEOUT: int

config = EnvConfig()
config.TIMEOUT = 30
```

### One-time Loading
By default, environment variables will be loaded into the class every time
a new instance is created. You can use the `singleton` option to convert
your class into a Singleton and ensure it will only load from environment
variables on the first initialization.

```python
class EnvConfig(typedenv.EnvLoader, singleton=True):
    LOG_LEVEL: str

assert EnvConfig() is EnvConfig()
```

### Subclass Overriding
Your `EnvLoader` class can be further subclassed, which can be useful for
type narrowing keys required by certain modules in your application, or for
adding default values.

```python
class EnvConfig(typedenv.EnvLoader):
    LOG_LEVEL: str
    GOOGLE_API_KEY: str | None

class GoogleRequiredConfig(EnvConfig):
    GOOGLE_API_KEY: str

class TestConfig(EnvConfig):
    GOOGLE_API_KEY = "fake-google-key"
```
