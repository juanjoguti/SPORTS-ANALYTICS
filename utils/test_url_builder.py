import pytest
import requests
from utils.url_builder import UrlBuilder


@pytest.fixture
def google_dns():

    return 'google'

@pytest.mark.parametrize(
    'scheme, expected_scheme', [
        (None, 'https'),
        ('http', 'http')
    ]
)
def test_scheme_setter(google_dns, scheme, expected_scheme):

    assert UrlBuilder(google_dns, scheme=scheme).scheme == expected_scheme

@pytest.mark.parametrize('domain_name', [None, 'google'])
def test_domain_name_setter(domain_name):

    assert UrlBuilder(domain_name).domain_name == domain_name

@pytest.mark.parametrize(
    'top_level_domain, expected_tld', [
        (None, 'com'),
        ('es', 'es')
    ]
)
def test_top_level_domain_setter(google_dns, top_level_domain, expected_tld):

    url_builder = UrlBuilder(google_dns, top_level_domain=top_level_domain)
    assert url_builder.top_level_domain == expected_tld

@pytest.mark.parametrize(
    'dns, expected_url', [
        ('google', 'https://google.com'),
        ('fbref', 'https://fbref.com')
    ]
)
def test_domain(dns, expected_url):

    url = UrlBuilder(dns).domain_url
    assert url == expected_url
    assert requests.get(url).ok

@pytest.mark.parametrize(
    'dns, path, expected_url', [
        ('fbref', '', 'https://fbref.com/'),
        ('fbref', 'en/comps/', 'https://fbref.com/en/comps/')
    ]
)
def test_get_url_to_path(dns, path, expected_url):

    url = UrlBuilder(dns).get_url_to_path(path)
    assert url == expected_url
    assert requests.get(url).ok
