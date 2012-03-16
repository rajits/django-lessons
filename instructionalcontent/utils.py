from BeautifulSoup import BeautifulSoup

def truncate(string, limit):
    return string[:limit] + (string[limit:] and '...')

def ul_as_list(html):
    soup = BeautifulSoup(html)
    return [li.contents[0] for li in soup('li')]
