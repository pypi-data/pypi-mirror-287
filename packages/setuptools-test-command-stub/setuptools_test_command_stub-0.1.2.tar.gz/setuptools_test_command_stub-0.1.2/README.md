# Stub for setuptools.command.test

This package provides a stub for the setuptools.command.test command, which can be used to work around issues with setuptools upgrades that break the test command.

### Installation

Install the package using your preferred package manager:

```
pip install setuptools-test-command-stub
```

Or poetry:

```
[tool.poetry.dependencies]
setuptools-test-command-stub = "*"
```

Add that dependency first in the list of the dependencies in you pyproject.toml. Then, run poetry lock to lock your dependencies.


## How it works? 

It's just patches `setuptools.command.test` with `unittest.mock.MagicMock`. 

Remember to remove this package and fix the underlying setuptools issue once possible.
