# PyPSI
CLI 🖥 + API for Google PageSpeed Insights

[![PythonPSI](https://img.shields.io/pypi/v/PythonPSI)](https://pypi.org/project/PythonPSI/) ![PyPI - Downloads](https://img.shields.io/pypi/dm/PythonPSI)

![PyPSI](https://raw.githubusercontent.com/prakhargurunani/PyPSI/main/PyPSI.png)

## Installation
```bash
pip install PythonPSI
```

## Usage
```bash
psi <SITE_URL> <OPTION1> <OPTION2> ...
```

Example:
```bash
psi google.com --category seo --stratergy desktop --locale en
```

## CLI
```bash
$ psi --help

    Usage: psi [OPTIONS] URL

    Options:
    --api_key TEXT        Required to use the API in an automated way and make
                            multiple requests per second

    --category TEXT       A Lighthouse category to run; if none are given, only
                            Performance category will be run

    --metrics TEXT        Returns metrics of a particular field in response
                            object

    --locale TEXT         The locale used to localize formatted results
    --stratergy TEXT      The analysis strategy (desktop or mobile) to use, and
                            desktop is the default

    --threshold TEXT      Threshold score to pass the PageSpeed test. Useful for
                            setting a performance budget.

    --links TEXT          If passed adds links with more info about
                            opportunities. Useful for checking documentation about
                            opportunities.

    --utm_campaign TEXT   Campaign name for analytics.
    --utm_source TEXT     Campaign source for analytics.
    --captcha_token TEXT  The captcha token passed when filling out a captcha.
    --help                Show this message and exit.
```

## API Usage

```python
from PythonPSI.api import PSI

PSI('google.com', category='seo', locale='en', stratergy='desktop')
# Returns JSON output
```
- `PSI` - _Required arguments_: 1, _Optional arguments_: 9

    - `URL`: 
        - Required
        - _Default_: **_None_**
    - `api_key`: 
        - Optional
        - _Default_: **_None_**
    - `category`: 
        - Optional
        - _Default_: **performance**
        - Options: `accessibility`, `best_practices`, `performance`, `pwa`, `seo`
    - `metrics`:
        - Optional
        - _Default_: **None**
        - Options: `kind`, `captchaResult`, `id`, `loadingExperience`, `originLoadingExperience`, `analysisUTCTimestamp`, `lighthouseResult`, `version`
    - `locale`: 
        - Optional
        - _Default_: **en**
    - `stratergy`: 
        - Optional
        - _Default_: **desktop**
        - Options: `desktop`, `mobile`
    - `threshold`:
        - Optional
        - _Default_: **_None_**
        - Options: `INT` 0-100
    - `links`:
        - Optional
        - _Default_: **false**
        - Options: `true`, `false`
    - `utm_campaign`: 
        - optional
        - _Default_: **_None_**
    - `utm_source`: 
        - Optional
        - _Default_: **_None_**
    - `captcha_token`: 
        - Optional
        - _Default_: **_None_**
