[![Release status](https://github.com/ken-morel/comberload/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ken-morel/comberload/releases)
[![PyPI package](https://badge.fury.io/py/comberload.svg)](https://pypi.org/project/comberload)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/comberload)](https://pypi.org/project/comberload)
[![Test](https://github.com/ken-morel/comberload/actions/workflows/test.yml/badge.svg)](https://github.com/ken-morel/comberload/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/ken-morel/comberload/badge.svg?branch=main&cache=3000)](https://coveralls.io/github/ken-morel/comberload?branch=main)
[![Pypi downloads](https://img.shields.io/pypi/dd/comberload)](https://pypi.org/project/comberload)
[![Pypi downloads](https://img.shields.io/pypi/dw/comberload)](https://pypi.org/project/comberload)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# comberload

I have recently built some little command line utility. It simply
receives a command, parses the command and evaluates it with syntax coloring
and autocompletion from [prompt_toolkit](https://pypi.org/project/prompt_toolkit).
But there was an issue, prompt_toolkit loaded **extremely**, I was wasting alot
time to load a package which was not indispensable to my app.

Comberloads, since comberload 1.0.2, were added two more methods to comberloader,
`failback` and `fail`

comberload permits you to register modules for queued loading and callbacks
if they are not loaded yet, howaworks?

a simple example for a function which uses prompt_toolkit.prompt but can
fallback to simple input

## fallback

```python
import comberload

@comberload("prompt_toolkit")
def get_input():
    import prompt_toolkit

    return prompt_toolkit.prompt()

@get_input.fallback
def fallback_get_input():
    return input()

get_input()  # immediately uses fallback

get_input()  # abit later, uses prompt_toolkit
```

comberload uses a worker function running on a seperate thread to load the
modules as listed in the queue. Each time you call on `comberload("module1", "module2")`
the modules are queued and loaded.

## multiple fallbacks

You can easily queue fallbacks as:

```python
import comberload


comberload("mod1", "mod2")
def first():
    pass

@first.fallback
@comberload("mod3")
def second():
    pass

@second.fallback
def third():
    pass
```

## fail

Use this handler in case the module fails to import

```python
import comberload


comberload("mod1", "mod2")
def first():
    pass

@first.fail
def second():
    print(first.error)
```

## failback

This is what I advice to use, it uses the default handler in case the module is
not loaded due to error or any else.

```python
import comberload


comberload("mod1", "mod2")
def first():
    pass

@first.failback
def second():
    pass
```
# callbacks

comberload also permits you to register callbacks when some modules finish loading
as

```python
import comberload

@comberload("mod", "mod2").fallback
def mod_and_mod2_loaded():
    pass
```

## best practice

### Only what necessary

I will advice to load only what is necessary taking such an approach

## Loading in beginning

What I will advice is to queue all the required import at the begining of each
of your modules to permit all of them load without having to fallback.

```python
... # imports
import comberload

comberload("all", "my", "modules")

... # rest of code
```



Well, you're all set. Listening for issues at https://github.com/ken-morel/comberload ,
till then, good coding!
