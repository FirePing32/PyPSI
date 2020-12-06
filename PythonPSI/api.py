from PythonPSI.utils.data import HTTPS_OR_HTTP, RAW


def PSI(
    url,
    api_key="",
    metrics="",
    category="performance",
    locale="en",
    stratergy="desktop",
    threshold="",
    links="",
    utm_campaign="",
    utm_source="",
    captcha_token="",
):

    if "https" in url or "http" in url:
        response = HTTPS_OR_HTTP(
            api_key=api_key,
            category=category,
            locale=locale,
            stratergy=stratergy,
            threshold=threshold,
            links=links,
            utm_campaign=utm_campaign,
            utm_source=utm_source,
            captcha_token=captcha_token,
            url=url,
        )
        try:
            return response[metrics]
        except Exception:
            return response

    else:
        response = RAW(
            api_key=api_key,
            category=category,
            locale=locale,
            stratergy=stratergy,
            threshold=threshold,
            links=links,
            utm_campaign=utm_campaign,
            utm_source=utm_source,
            captcha_token=captcha_token,
            url=url,
        )
        try:
            return response[metrics]
        except Exception:
            return response
