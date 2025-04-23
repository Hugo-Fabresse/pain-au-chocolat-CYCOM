import subprocess
from urllib.parse import urlparse


def run_nmap(url):
    parsed = urlparse(url)
    host = parsed.hostname
    print("Running nmap on host:", host)
    try:
        result = subprocess.run(['nmap', '-sC', '-sV', '-T5', '-Pn', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Nmap command failed with error code {e.returncode}")
        print(f"Error message: {e.stderr}")
    except FileNotFoundError:
        print("Error: nmap command not found. Please ensure nmap is installed and in your system's PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def run_gobuster(url):
    parsed = urlparse(url)
    host = parsed.hostname
    print("Running nmap on host:", host)
    try:
        result = subprocess.run(['gobuster', 'dir', '-u', host, '-w', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Gobuster command failed with error code {e.returncode}")
        print(f"Error message: {e.stderr}")
    except FileNotFoundError:
        print("Error: gobuster command not found. Please ensure nmap is installed and in your system's PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
