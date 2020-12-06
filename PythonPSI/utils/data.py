import requests

QUERY_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="


def HTTPS_OR_HTTP(
    url,
    api_key="",
    stratergy="desktop",
    locale="en",
    category="performance",
    threshold="",
    links="false",
    utm_campaign="",
    utm_source="",
    captcha_token="",
):
    API_KEY = "&key=" + api_key
    apikey = f"{'' if api_key == '' else API_KEY}"
    raw_data = requests.get(
        QUERY_URL
        + url
        + "&stratergy="
        + stratergy
        + "&locale="
        + locale
        + "&category="
        + category
        + "&threshold="
        + threshold
        + "&links="
        + links
        + "&utm_campaign="
        + utm_campaign
        + "&utm_source="
        + utm_source
        + "&captchaToken="
        + captcha_token
        + apikey
    )
    data = raw_data.json()

    return data


def RAW(
    url,
    api_key="",
    stratergy="desktop",
    locale="en",
    category="performance",
    threshold="",
    links="false",
    utm_campaign="",
    utm_source="",
    captcha_token="",
):

    API_KEY = "&key=" + api_key
    apikey = f"{'' if api_key == '' else API_KEY}"
    site_url = "http://" + url
    raw_data = requests.get(
        QUERY_URL
        + site_url
        + "&stratergy="
        + stratergy
        + "&locale="
        + locale
        + "&category="
        + category
        + "&threshold="
        + threshold
        + "&links="
        + links
        + "&utm_campaign="
        + utm_campaign
        + "&utm_source="
        + utm_source
        + "&captchaToken="
        + captcha_token
        + apikey
    )
    data = raw_data.json()

    return data
