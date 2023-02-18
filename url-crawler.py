import argparse
import requests
from bs4 import BeautifulSoup
import colorama

def extract_links(domain):
  # Add "https://" to the beginning of the domain if it does not start with "http" or "https"
  if not domain.startswith('http://') and not domain.startswith('https://'):
    domain = 'https://' + domain
  
  # Make a GET request to the domain
  response = requests.get(domain)
  html = response.text
  
  # Use BeautifulSoup to parse the HTML and extract all links
  soup = BeautifulSoup(html, 'html.parser')
  links = soup.find_all('a')
  
  # Filter the links to only include third-party domains
  third_party_links = []
  for link in links:
    href = link.get('href')
    if href and domain not in href and (href.startswith('http://') or href.startswith('https://')):
      third_party_links.append(href)
  
  # Remove duplicate links
  third_party_links = list(set(third_party_links))
  
  return third_party_links

def main():
  # Initialize colorama
  colorama.init()
  
  # Set up the command line argument parser
  parser = argparse.ArgumentParser(description=colorama.Fore.CYAN + 'Extract third party links from a domain', epilog=colorama.Fore.YELLOW + "Examples: \n1. python url-crawler.py -d example.com, \n2. python url-crawler.py -d example.com -o links.txt, \n3. python url-crawler.py -t -o links.txt", formatter_class=argparse.RawTextHelpFormatter)
  print(colorama.Fore.BLUE + "Made by BLACK-SCORP10")
  print(colorama.Fore.BLUE + "t.me/BLACK_SCORP10")
  print(colorama.Fore.BLUE + "Instagram: @hacke_1o1")
  parser.add_argument('-o', '--output', help='Output file name')
  parser.add_argument('-d', '--domain', help='Domain name', required=True)
  parser.add_argument('-t', '--multiple', help='Extract links from multiple domains', action='store_true')
  parser.add_argument('-s', '--status', help='Show link status code', action='store_true')
  args = parser.parse_args()
  
  # Print the banner
  #print(colorama.Fore.BLUE + "Made by BLACK-SCORP10")
  #print(colorama.Fore.BLUE + "Instagram: @hacke_1o1")
  print("\n")
  
  # Extract the links from the domain
  if args.multiple:
    # TODO: Extract links from multiple domains
    pass
  else:
    links = extract_links(args.domain)
    
    # Print the links or save them to a file
    if args.output:
      with open(args.output, 'w') as f:
        for link in links:
          if args.status:
            # Make an HTTP HEAD request to the link and get the status code
            try:
              response = requests.head(link)
              status_code = response.status_code
              f.write(f'[{status_code}] : {link}\n')
            except:
              f.write(colorama.Fore.RED + f'[err] : {link}\n')
          else:
            f.write(link + '\n')
    else:
      for link in links:
        if args.status:
          # Make an HTTP HEAD request to the link and get the status code
          try:
            response = requests.head(link)
            status_code = response.status_code
            print(colorama.Fore.GREEN + f'[{status_code}] : {link}')
          except:
            print(colorama.Fore.RED + f'[err] : {link}')
        else:
          print(link)
          
  # Reset the colorama settings
  colorama.deinit()

if __name__ == '__main__':
  main()

# This code is made and owned by BLACK-SCORP10.
# Feel free to contact me at https://t.me/BLACK_SCORP10
