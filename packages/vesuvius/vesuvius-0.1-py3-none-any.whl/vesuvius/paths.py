import os
import requests
import site
from lxml import html
from urllib.parse import urljoin

# Function to recursively create directory structure
def create_structure(session, url, local_path):
    response = session.get(url)
    response.raise_for_status()
        
    tree = html.fromstring(response.content)
    links = tree.xpath('//a/@href')
        
    for href in links:
        if href and not href.startswith('?') and not href.startswith('/'):
            full_url = urljoin(url, href)
            local_file_path = os.path.join(local_path, href)
                
            if href.endswith('/'):
                # It's a directory, create it and recurse into it
                if not os.path.exists(local_file_path):
                    os.makedirs(local_file_path)
                create_structure(session, full_url, local_file_path)

def create_local_directory_structure(remote_directory):
    install_path = site.getsitepackages()[-1]
    local_path = os.path.join(install_path, 'vesuvius', 'downloads')

    url = 'https://registeredusers:only@dl.ash2txt.org/'
    url = urljoin(url, remote_directory)
    # Create a session to manage cookies and headers
    session = requests.Session()

    response = session.get(url)
    response.raise_for_status()
        
    tree = html.fromstring(response.content)
    links = tree.xpath('//a/@href')
        
    for href in links:
        if href and not href.startswith('?') and not href.startswith('/'):
            full_url = urljoin(url, href)
            local_file_path = os.path.join(local_path, href)
                
            if href.endswith('/'):
                # It's a directory, create it and recurse into it
                if not os.path.exists(local_file_path):
                    os.makedirs(local_file_path)
                create_structure(session, full_url, local_file_path)
