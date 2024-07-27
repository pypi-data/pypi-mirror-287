[![PyPI Version](https://shields.mitmproxy.org/pypi/v/logni.svg)](https://pypi.org/project/logni/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/441b9bb67c0f4956b5d4bcfbe76e00c6)](https://www.codacy.com/manual/erikni/logni.py?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=erikni/logni.py&amp;utm_campaign=Badge_Grade)
[![Github Releases](https://img.shields.io/github/downloads/atom/atom/latest/total.svg)](https://github.com/erikni/logni.py/releases)
[![Build Status](https://api.travis-ci.org/erikni/logni.py.svg?branch=develop)](http://travis-ci.org/erikni/logni.py)
[![Maintainability](https://api.codeclimate.com/v1/badges/27cb403386b704028bb5/maintainability)](https://codeclimate.com/github/erikni/logni.py/maintainability)
[![Known Vulnerabilities](https://snyk.io//test/github/erikni/logni.py/badge.svg?targetFile=requirements.txt)](https://snyk.io//test/github/erikni/logni.py?targetFile=requirements.txt)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENCE)

# logni.py
logni is a python library for event logging and application states

## How to install?
- git (github) #1
- wget (github) #2
- pip (python packages) #3


Install from Github #1
```
$ git clone https://github.com/erikni/logni.py.git
$ cd logni.py
$ sudo pip3 install -r requirements.txt
$ python3 test/example/basic_example.py
```

Install from Github #2
```
$ sudo wget -O - https://raw.githubusercontent.com/erikni/logni.py/master/setup.sh | bash
```

Install with PIP (Python Package Installer) #3
```
$ pip3 install logni
$ python3 /usr/local/lib/python3/dist-packages/logni/logni.py
```

## Example

```
$ python3

>>> from logni import log

>>> log.mask('ALL')
>>> log.console(1)

>>> log.critical('critical message')
2016/04/01 22:08:18 [15489] F4: critical message [7e995d1a] {logni.py:fatal():161}

>>> log.error('error message #%s', time.time(), priority=4)
2016/04/01 22:08:18 [15489] E4: error message #1459541298.29 [58138001] {logni.py:error():164}

>>> log.warn('warning message #%s', time.time(), priority=3)
2016/04/01 22:08:18 [15489] W3: warning message #1459541298.29 [91b483ab] {logni.py:warn():167}

>>> log.info('info message #%s', time.time(), priority=2)
2016/04/01 22:08:18 [15489] I2: info message #1459541298.29 [eaf58c15] {logni.py:info():170}

>>> log.debug('debug message #%s', time.time(), priority=1)
2016/04/01 22:08:18 [15489] D1: debug message #1459541298.29 [37e911b8] {logni.py:debug():173}
```

## Support

Logni support python >= 3.6

## Roadmap

Current roadmap:

* new integration (rollbar, logentries, sentry, ... )
* performance improvement.

## Test

[test/unit](https://github.com/erikni/logni.py/tree/develop/test/unit)

## Contribution

[Pull Requests](https://github.com/erikni/logni.py/pulls) are very welcome.

# Licence

[GNU General Public License v3.0](LICENSE)
