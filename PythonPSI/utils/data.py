import requests
import json

QUERY_URL = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='

def HTTPS_OR_HTTP(url, 
                api_key="", 
                stratergy="desktop", 
                locale="en", 
                category="performance", 
                threshold="", 
                utm_campaign="", 
                utm_source="", 
                captcha_token=""):

    raw_data = requests.get(QUERY_URL 
                            + url 
                            + '&key=' + api_key 
                            + '&stratergy=' + stratergy 
                            + '&locale=' + locale 
                            + '&category=' + category 
                            + '&threshold=' + threshold 
                            + '&links=' + links 
                            + '&utm_campaign=' + utm_campaign 
                            + '&utm_source=' + utm_source 
                            + '&captchaToken=' + captcha_token)
    data = raw_data.json()

    return(data)

def RAW(url, 
        api_key="", 
        stratergy="desktop", 
        locale="en", 
        category="performance", 
        threshold="", 
        utm_campaign="", 
        utm_source="", 
        captcha_token=""):

    site_url = "http://" + url
    raw_data = requests.get(QUERY_URL
                            + site_url 
                            + '&key=' + api_key 
                            + '&stratergy=' + stratergy 
                            + '&locale=' + locale 
                            + '&category=' + category 
                            + '&threshold=' + threshold 
                            + '&utm_campaign=' + utm_campaign 
                            + '&utm_source=' + utm_source 
                            + '&captchaToken=' + captcha_token)
    data = raw_data.json()

    return(data)