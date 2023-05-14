import pyfiglet
import urllib.request
import io
import colorama
from colorama import Fore
colorama.init() 

ascii_banner = pyfiglet.figlet_format("Crawk")
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
    return data.read(), path + 'robots.txt'
    print(get_robots_txt('url'))

# Find sitemap.xml in robots.txt and save to file.
def save_sitemap_links(url):
    robots_txt, robots_url = get_robots_txt(url)
    print(Fore.GREEN + 'Robots.txt content: ' + robots_url)
    print(robots_txt)
    sitemap_links = [line.split(': ')[1] for line in robots_txt.split('\n') if 'sitemap:' in line.lower()]
    if sitemap_links:
        with open('sitemap_links.txt', 'w') as f:
            f.write('\n'.join(sitemap_links))
        print(Fore.YELLOW + 'Sitemap links saved to sitemap_links.txt')
    else:
        print(Fore.RED + 'No sitemap links found in robots.txt')

save_sitemap_links(url)
