from urllib.parse import urlparse
import requests
from datetime import datetime


def get_html(url: str) -> str | None:
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        return response.text
    
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

        return None


def reformat_date(date_str: str, input_format: str, output_format: str = "%Y/%m/%d %H:%M") -> str:
    date_obj = datetime.strptime(date_str, input_format)
    
    return date_obj.strftime(output_format)


def get_domain_name(url: str) -> str:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if "." in domain:
        domain_parts = domain.split(".")
        # print(domain_parts)
        if len(domain_parts) > 2:
            domain = ".".join(domain_parts[-2:])

    return domain.replace('.', '_') + '.txt'
