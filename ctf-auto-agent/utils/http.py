import requests

def send_request(url, params=None, timeout=5):
    try:
        r = requests.get(url, params=params, timeout=timeout)
        return r.text
    except:
        return ""
