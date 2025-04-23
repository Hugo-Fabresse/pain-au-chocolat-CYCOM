import subprocess
from urllib.parse import urlparse
import subprocess

def run_nmap(url):
    parsed = urlparse(url)
    host = parsed.hostname
    print(f"Running Nmap on: {url}")
    try:
        result = subprocess.run(['nmap', '-sC', '-sV', '-T5', '-Pn',
        host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Nmap command failed with error code {e.returncode}")
        print(f"Error message: {e.stderr}")
    except FileNotFoundError:
        print("Error: nmap command not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def run_gobuster(url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = 'http://' + url
    print(f"Running Gobuster on: {url}")
    try:
        result = subprocess.run(['gobuster', 'dir', '-u', url, '-w',
        'wordlists/rockyou_2k.txt', '--exclude-length', '2245'], capture_output=True, text=True, check=True)
        print("result: ", result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Gobuster failed: {e.stderr}")
    except FileNotFoundError:
        print("Gobuster not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")
