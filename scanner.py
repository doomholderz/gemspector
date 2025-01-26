import re
import requests
import whois
from datetime import datetime
import argparse
import os

def check_domain_expiry(domain):
    try:
        w = whois.whois(domain)
        if w.expiration_date:
            expiration_date = w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date

            if expiration_date < datetime.now():
                return f"The domain '{domain}' is expired."
            else:
                return f"The domain '{domain}' is valid until {expiration_date}"
        else:
            return f"No expiration date found for the domain '{domain}'. It may not be registered."
    except Exception as e:
        return f"Error checking domain '{domain}': {e}"

def extract_email_domain(email):
    pattern = r'(?<=@)[^.]+\.[^.]+'
    
    match = re.search(pattern, email)
    
    if match:
        return match.group(0)
    else:
        return None

def extract_gems(gemfile_path):
    gems = set()
    gem_regex = re.compile(r"^\s*gem\s+['\"]([^'\"]+)['\"]")

    with open(gemfile_path, 'r') as file:
        for line in file:
            match = gem_regex.match(line)
            if match:
                gems.add(match.group(1))

    return sorted(gems)

def get_gem_owners(gem_name, output_format='json', base_url='https://rubygems.org'):
    url = f"https://rubygems.org/api/v1/gems/{gem_name}/owners.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f"Error fetching data: {e}"

def get_gem_downloads_count(gem_name):
    #url = f"https://rubygems.org/api/v1/downloads/{gem_name}.json"
    url = f"https://rubygems.org/api/v1/gems/{gem_name}.json"
    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f"Error fetching data: {e}"

def main2():
    parser = argparse.ArgumentParser(description="Scan a Gemfile for listed gems.")
    parser.add_argument("-d", "--directory", required=True, help="Path to the Gemfile")
    args = parser.parse_args()
    gemfile_path = args.directory
    if not os.path.exists(gemfile_path):
        print(f"Error: The specified Gemfile does not exist: {gemfile_path}")
        return

    used_gems = extract_gems(gemfile_path)
    for gem in used_gems:
        gem_owners = get_gem_owners(gem)
        if type(gem_owners) == list:
            print(f"{gem} has {len(gem_owners)} maintainer(s).")
            for owner in gem_owners:
                if "email" in owner and owner["email"]:
                    email_domain = extract_email_domain(owner["email"])
                    print(f"\temail: {owner["email"]}")
                    active_email_domain = check_domain_expiry(email_domain)
                    print(f"\t{active_email_domain}")
                else:
                    print(owner)

def main():
    malicious_packages = open("examples/ossf-malicious-gems.txt", "r")
    for package in malicious_packages:
       
        download_count = get_gem_downloads_count(package.strip())
        print(download_count)
        

if __name__ == "__main__":
    main()