# URL-CRAWLER V1.0.0
URL-CRAWLER is a Python script that extracts all third-party links from a given domain. It uses the BeautifulSoup library to parse the HTML and filter out links that belong to the same domain as the original domain.


## Requirements
To run this script, you need to have Python 3 installed on your computer, as well as the following Python libraries:

- argparse  
- requests  
- bs4 (BeautifulSoup)  

### You can install the required libraries using pip:  

```
pip install argparse requests bs4
```
## Usage  
To use extract_links.py, run the script from the command line and provide the domain you want to extract links from as a command line argument. You can also specify additional options, such as whether to show link status codes or save the links to a file.

Here are some examples:

```python
# Extract links from a single domain and display them in the console
python urlcrawler.py -d example.com

# Extract links from a single domain and save them to a file
python urlcrawler.py -d example.com -o links.txt

# Extract links from multiple domains and save them to a file
python urlcrawler.py -t -o links.txt

# Extract links from a single domain and display their status codes in the console
python urlcrawler.py -d example.com -s

#For more detailed usage instructions, run the script with the -h or --help option.
```

# Author
This script was created by BLACK-SCORP10. 
You can contact me on Telegram at https://t.me/BLACK_SCORP10 or on Instagram at @hacke_1o1.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
