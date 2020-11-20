import click
import requests

@click.command()
@click.option('--api_key', default='', help='Required to use the API in an automated way and make multiple requests per second')
@click.option('--category', default='performance', help='A Lighthouse category to run; if none are given, only Performance category will be run')
@click.option('--metrics', default='', help='Returns metrics of a particular field in response object')
@click.option('--locale', default='en', help='The locale used to localize formatted results')
@click.option('--stratergy', default='desktop', help='The analysis strategy (desktop or mobile) to use, and desktop is the default')
@click.option('--threshold', default='', help='Threshold score to pass the PageSpeed test. Useful for setting a performance budget.')
@click.option('--links', default='', help='If passed adds links with more info about opportunities. Useful for checking documentation about opportunities.')
@click.option('--utm_campaign', default='', help='Campaign name for analytics.')
@click.option('--utm_source', default='', help='Campaign source for analytics.')
@click.option('--captcha_token', default='', help='The captcha token passed when filling out a captcha.')
@click.argument('url')
def psi(api_key, category, metrics, locale, stratergy, threshold, links, utm_campaign, utm_source, captcha_token, url):
    if "https" in url:
        raw_data = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url + '&key=' + api_key + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&threshold=' + threshold + '&links=' + links + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token)
        data = raw_data.json()
        try:
            click.echo(data[metrics])
        except:
            click.echo(data)
    if "http" in url:
        raw_data = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url + '&key=' + api_key + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&threshold=' + threshold + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token)
        data = raw_data.json()
        try:
            click.echo(data[metrics])
        except:
            click.echo(data)
    else:
        site_url = "http://" + url
        raw_data = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + site_url + '&key=' + api_key + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&threshold=' + threshold + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token)
        data = raw_data.json()
        try:
            click.echo(data[metrics])
        except:
            click.echo(data)