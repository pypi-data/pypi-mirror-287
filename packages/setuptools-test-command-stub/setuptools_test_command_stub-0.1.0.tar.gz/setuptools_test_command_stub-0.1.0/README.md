# Stub for setuptools.command.test

So, you are facing with project installation issue after setuptools upgrading?
You are in the right place.

## Usage

Add that dependency first in the list of the dependencies in you pyproject.toml
```console
setuptools-test-command-stub = '0.1.0'
```
And than lock your dependencies with `poetry lock`. Whats all!


## How it works? 

It's just patches `setuptools.command.test` with `unittest.mock.MagicMock`. 
