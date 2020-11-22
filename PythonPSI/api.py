import json
import requests
from PythonPSI.utils.data import HTTPS_OR_HTTP, RAW

def PSI(url, 
        api_key="", 
        metrics="", 
        category="performance", 
        locale="en", 
        stratergy="desktop", 
        threshold="", 
        links="", 
        utm_campaign="", 
        utm_source="", 
        captcha_token=""):
        
    if "https" in url:
        response = HTTPS_OR_HTTP(url, api_key, stratergy, locale, category, threshold, utm_campaign, utm_source, captcha_token)
        try:
            return(response[metrics])
        except:
            return(response)
    if "http" in url:
        response= HTTPS_OR_HTTP(url, api_key, stratergy, locale, category, threshold, utm_campaign, utm_source, captcha_token)
        try:
            return(response[metrics])
        except:
            return(response)
    else:
        response = RAW(url, api_key, stratergy, locale, category, threshold, utm_campaign, utm_source, captcha_token)
        try:
            return(response[metrics])
        except:
            return(response)