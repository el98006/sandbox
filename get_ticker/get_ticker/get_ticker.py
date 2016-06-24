import requests
from datetime import datetime,timedelta
from requests.exceptions import HTTPError
import os
import re 

def get_urls_by_dates(start, end):
    
    base = 'http://data.pystock.com/2016/'
    
    ind = start
    while ind <= end:
        t = datetime.strftime(ind, '%Y%m%d')
        url = base + t  + '.tar.gz'
        ind += timedelta(1)
        yield url
def extract_filename(url):
    parts= url.split('/')
    fname = parts[-1:]
    return fname[0]

def request_by_urls(urls):
    for url in urls:
        print(url)
        fname = extract_filename(url)
        print(fname)
        try:
            r= requests.get(url)
            print(r.headers['Content-Length'])
            yield (r, fname)
        except HTTPError:
            print ('failed get the csv file, error code{}'.format(r.status_code))
            exit(0)
def save_to_files(responds):
    for r, fname in responds:
        filen = os.path.join('/tmp',fname)
        with open(filen,'wb') as f:
            f.write(r.content)
                

if __name__ == '__main__':
    end = datetime.today() - timedelta(days=1)
    ten_days = timedelta(days=10)
    start = end - ten_days
    urls = get_urls_by_dates(start, end)
    resp_fname = request_by_urls(urls)
    save_to_files(resp_fname)


    