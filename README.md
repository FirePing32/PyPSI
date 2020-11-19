# PyPSI
CLI 🖥 + API for Google PageSpeed Insights

<center><img src="PyPSI.png" width="75%"></center>

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
