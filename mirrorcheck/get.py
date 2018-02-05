import htmllistparse
import requests
import bs4

def check_xenial_security_date(mirror):
    cwd, listing = htmllistparse.fetch_listing(mirror + "/dists/xenial-security/main/binary-amd64/")
    latest = max(listing, key=lambda x: x.modified)
    print(mirror, latest.modified)


def get_http_mirrors():
    response = requests.get("https://launchpad.net/ubuntu/+archivemirrors")
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.content, 'html5lib')
    return [a['href'] for a in soup.find_all('a', text='http')]

mirrors = get_http_mirrors()
for mirror in mirrors:
    try:
        check_xenial_security_date(mirror)
    except:
        pass
