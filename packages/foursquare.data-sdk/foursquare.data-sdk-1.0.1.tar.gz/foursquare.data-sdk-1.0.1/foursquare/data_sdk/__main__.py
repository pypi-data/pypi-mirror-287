"""Stub file to allow CLI use as an entry point

E.g.

```
python -m foursquare.data_sdk
```

instead of

```
fsq-data-sdk
```

This can be useful to ensure that the CLI is using the same Python environment as the
active one. Otherwise in some circumstances, the PATH could be set up so that the
`fsq-data-sdk` CLI and `python` are two different environments.
"""
from foursquare.data_sdk.cli import main

if __name__ == "__main__":
    main()
