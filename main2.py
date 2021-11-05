import urllib3
from bs4 import BeautifulSoup
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36' # Kako bi uvjerili stranicu da nismo bot već dolazimo sa browsera
}
login_data = {
    'Input.Email' : 'davor.begovic@scan.hr',
    'Input.Password' : 'a123456A',
    '__RequestVerificationToken': ''
}

    
    