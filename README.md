<p align="center">
    <a href="https://www.apache.org/licenses/LICENSE-2.0" alt="license">
        <img src="https://img.shields.io/github/license/tomarv2/demo-python-aws-click" /></a>
    <a href="https://github.com/tomarv2/demo-python-aws-click/tags" alt="GitHub tag">
        <img src="https://img.shields.io/github/v/tag/tomarv2/demo-python-aws-click" /></a>
    <a href="https://stackoverflow.com/users/6679867/tomarv2" alt="Stack Exchange reputation">
        <img src="https://img.shields.io/stackexchange/stackoverflow/r/6679867"></a>
    <a href="https://discord.gg/XH975bzN" alt="chat on Discord">
        <img src="https://img.shields.io/discord/813961944443912223?logo=discord"></a>
    <a href="https://twitter.com/intent/follow?screen_name=varuntomar2019" alt="follow on Twitter">
        <img src="https://img.shields.io/twitter/follow/varuntomar2019?style=social&logo=twitter"></a>
</p>

# Demo app

Python demo app using Click and Mocking AWS for pytest

**Medium blog:** https://medium.com/@tomarv2/mock-aws-pytest-click-51a2a7b41123

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