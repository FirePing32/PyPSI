import click

from PythonPSI.utils.data import HTTPS_OR_HTTP, RAW
from PythonPSI.utils.version import current_version, latest_version

version_info = (
    "---  Current version: "
    + current_version()
    + "  ---  "
    + "Latest version: "
    + latest_version()
    + "  ---"
)


@click.command(help=version_info)
@click.option(
    "--api_key",
    default="",
    help="Required to use the API in an "
    + "automated way and make multiple requests per second",
)
@click.option(
    "--category",
    default="performance",
    help="A Lighthouse category to run; if none are given, "
    + "only Performance category will be run",
)
@click.option(
    "--metrics",
    default="",
    help="Returns metrics of a particular field in response object",
)
@click.option(
    "--locale", default="en", help="The locale used to localize formatted results"
)
@click.option(
    "--strategy",
    default="desktop",
    help="The analysis strategy (desktop or mobile) to use, and desktop is the default",
)
@click.option(
    "--threshold",
    default="",
    help="Threshold score to pass the PageSpeed test. "
    + "Useful for setting a performance budget.",
)
@click.option(
    "--links",
    default="",
    help="If passed adds links with more info about opportunities. "
    + "Useful for checking documentation about opportunities.",
)
@click.option("--utm_campaign", default="", help="Campaign name for analytics.")
@click.option("--utm_source", default="", help="Campaign source for analytics.")
@click.option(
    "--captcha_token",
    default="",
    help="The captcha token passed when filling out a captcha.",
)
@click.argument("url")
def psi(
    api_key,
    category,
    metrics,
    locale,
    strategy,
    threshold,
    links,
    utm_campaign,
    utm_source,
    captcha_token,
    url,
):
    if "https" in url or "http" in url:
        response = HTTPS_OR_HTTP(
            api_key=api_key,
            category=category,
            locale=locale,
            strategy=strategy,
            threshold=threshold,
            links=links,
            utm_campaign=utm_campaign,
            utm_source=utm_source,
            captcha_token=captcha_token,
            url=url,
        )
        try:
            click.echo(response[metrics])
        except Exception:
            click.echo(response)
    else:
        response = RAW(
            api_key=api_key,
            category=category,
            locale=locale,
            strategy=strategy,
            threshold=threshold,
            links=links,
            utm_campaign=utm_campaign,
            utm_source=utm_source,
            captcha_token=captcha_token,
            url=url,
        )
        try:
            click.echo(response[metrics])
        except Exception:
            click.echo(response)
