import pyfiglet
import urllib.request
import io
import colorama
from colorama import Fore
colorama.init() 

ascii_banner = pyfiglet.figlet_format("crawl")
print(Fore.CYAN + ascii_banner)

url = input(str("Please enter target URL:"))

# Uses URL Library to obtain information on URL's with a robots.txt page.
# Uses IO to format output from request.
def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

# Find all links to sitemap.xml in robots.txt and save to file.
def save_sitemap_links(url):
    robots_txt = get_robots_txt(url)
    sitemap_links = [line.split(': ')[1] for line in robots_txt.split('\n') if 'sitemap:' in line.lower()]
    if sitemap_links:
        with open('sitemap_links.txt', 'w') as f:
            f.write('\n'.join(sitemap_links))
        print(Fore.GREEN + 'Sitemap links saved to sitemap_links.txt')
    else:
        print(Fore.YELLOW + 'No sitemap links found in robots.txt')

save_sitemap_links(url)
