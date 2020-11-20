import click
import urllib3

http = urllib3.PoolManager()

@click.command()
@click.option('--api_key', default='', help='Required to use the API in an automated way and make multiple requests per second')
@click.option('--category', default='performance', help='A Lighthouse category to run; if none are given, only Performance category will be run')
@click.option('--locale', default='en', help='The locale used to localize formatted results')
@click.option('--stratergy', default='desktop', help='The analysis strategy (desktop or mobile) to use, and desktop is the default')
@click.option('--utm_campaign', default='', help='Campaign name for analytics.')
@click.option('--utm_source', default='', help='Campaign source for analytics.')
@click.option('--captcha_token', default='', help='The captcha token passed when filling out a captcha.')
@click.argument('url')
def psi(api_key, category, locale, stratergy, utm_campaign, utm_source, captcha_token, url):
    if "https" in url:
        click.echo(http.request('GET', 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url + '&key=' + api_key + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token).data)
    if "http" in url:
        click.echo(http.request('GET', 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + url + '&key=' + api_key + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token).data)
    else:
        site_url = "http://" + url
        click.echo(http.request('GET', 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=' + site_url + '&key=' + api_key + '&stratergy=' + stratergy + '&locale=' + locale + '&category=' + category + '&utm_campaign=' + utm_campaign + '&utm_source=' + utm_source + '&captchaToken=' + captcha_token).data)