import json
import requests

def PSI(url, api_key="", metrics="", category="performance", locale="en", stratergy="desktop", threshold="", links="", utm_campaign="", utm_source="", captcha_token=""):
    if "https" in url:
        raw_data = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url + '&key=' + api_key + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&threshold=' + threshold + '&links=' + links + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token)
        data = raw_data.json()
        try:
            return(data[metrics])
        except:
            return(data)
    if "http" in url:
        raw_data = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url + '&key=' + api_key + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&threshold=' + threshold + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token)
        data = raw_data.json()
        try:
            return(data[metrics])
        except:
            return(data)
    else:
        site_url = "http://" + url
        raw_data = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + site_url + '&key=' + api_key + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&threshold=' + threshold + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token)
        data = raw_data.json()
        try:
            return(data[metrics])
        except:
            return(data)