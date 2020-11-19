from setuptools import setup

long_description = """
# PyPSI
CLI 🖥 + API for Google PageSpeed Insights

![PythonPSI](https://raw.githubusercontent.com/prakhargurunani/PyPSI/main/PyPSI.png)

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

### Arguments
- `URL` - Required
- `--category` - Optional, default: **performance**, description: _A Lighthouse category to run; if none are given, only Performance category will be run_
- `--locale` - Optional, default: **en**, description: _The locale used to localize formatted results_
- `--stratergy` - Optional, default: **desktop**, description: _The analysis strategy (desktop or mobile) to use, and desktop is the default_
- `--utm_campaign` - Optional, default: **None**, description: _Campaign name for analytics._
- `--utm_source` - Optional, default: **None**, description: _Campaign source for analytics._
- `--captcha_token` - Optional, default: **None**, description: _The captcha token passed when filling out a captcha._

## API Usage

```python
from PythonPSI.api import PSI

PSI('google.com', category='seo', locale='en', stratergy='desktop')
# Returns JSON output
```
- `PSI` - Required arguments: 1, Optional arguments: 6

"""

setup(
    name="PythonPSI",
    version='1.3.2',
    description='CLI + API for Google PageSpeed Insights',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/prakhargurunani/PyPSI',
    author='Prakhar Gurunani',
    author_email='prakhargurunani@gmail.com',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='cli, google, python, seo, page-speed-insights, performance, google-apis',
    python_requires='>=3.5, <4',
    py_modules=['psi'],
    install_requires=[
        'click',
        'urllib3'
    ],
    entry_points='''
        [console_scripts]
        psi=main:psi
    ''',
)