# easysemver

This package provides utilities for comparing [SemVer](https://semver.org/) versions,
with special attention on the correct treatment of prerelease parts.

## Installation

`easysemver` can be installed from PyPI:

```sh
pip install easysemver
```

## Usage

Before versions can be compared, they must be converted into `Version` objects. If the version
is not valid SemVer, a `TypeError` will be raised.

```python
from easysemver import Version

# Not a valid SemVer version, so raises TypeError
version = Version("20230809-1")
# Create a SemVer version
version = Version("1.2.3")
# Prerelease and build parts are supported
version = Version("1.2.3-alpha.0+abcdefg")

# Comparing versions respects prerelease parts
#   The following all resolve to True
Version("1.2.3") < Version("1.2.4")
Version("1.2.3") < Version("2.0.0")
Version("1.2.3") < Version("1.2.4-alpha.0")
Version("1.2.3-alpha.0") < Version("1.2.3")
#   Prerelease parts that are all digits are compared as numbers
Version("1.2.3-alpha.0") < Version("1.2.3-alpha.100")
#   Prerelease parts that are strings are compared as strings
Version("1.2.3-alpha.0") < Version("1.2.3-beta.0")
#   Note that build parts don't affect comparison
Version("1.2.3") == Version("1.2.3+abcdefg")
```

Versions can also be compared to a SemVer range, which consists of a number of constraints
separated by commas. Similar to `Version`, a `TypeError` will be raised if the constraints
are not valid.

The supported constraints are SemVer versions with an operator, where the supported operators
are `==`, `!=`, `>=`, `>`, `<=` and `<`.

```python
from easysemver import Range, Version

# Resolves to True
Version("1.2.3") in Range(">=1.0.0,<2.0.0")
# Resolves to False
Version("1.2.3") in Range(">=2.0.0")
# Prerelease versions are only considered part of a range if the lower bound includes a prerelease part
#   Resolves to False
Version("1.2.3-alpha.0") in Range(">=1.0.0")
#   Resolves to True
Version("1.2.3-alpha.0") in Range(">=1.0.0-0")
# Specific versions can be exclulded
#   Resolves to False
Version("1.2.3") in Range(">=1.0.0,<2.0.0,!=1.2.3")
#   Resolves to True
Version("1.2.4") in Range(">=1.0.0,<2.0.0,!=1.2.3")
```
