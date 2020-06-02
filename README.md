# Demo app

Python demo app using Click and Mocking AWS for pytest

Medium blog: https://medium.com/@tomarv2/mock-aws-pytest-click-51a2a7b41123

To install: `pip install demo-python-aws-click`

To use:

```
demo
Usage: demo [OPTIONS] COMMAND [ARGS]...
Options:
  --help  Show this message and exit.
Commands:
  get  get secrets
```

To test:

```
pytest -s -v 
```