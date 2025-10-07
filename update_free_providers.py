import json
import requests
from pathlib import Path

JS_URL = "https://raw.githubusercontent.com/sr-26/email-inspector/master/free_providers.js"
OUTPUT_FILE = Path(__file__).parent / "email_inspector" / "data" / "free_providers.json"

def fetch_js():
    resp = requests.get(JS_URL, timeout=10)
    resp.raise_for_status()
    return resp.text

def get_provider_name(domain):
    """
    Extract provider name from domain.
    Returns the main provider name or 'other' if unknown.
    """
    domain = domain.lower()
    
    # Major provider patterns - check exact matches first
    exact_matches = {
        'gmail.com': 'gmail',
        'googlemail.com': 'gmail',
        'outlook.com': 'outlook',
        'hotmail.com': 'outlook',
        'live.com': 'outlook',
        'msn.com': 'outlook',
        'yahoo.com': 'yahoo',
        'yahoo.co.uk': 'yahoo',
        'yahoo.fr': 'yahoo',
        'yahoo.de': 'yahoo',
        'yahoo.it': 'yahoo',
        'yahoo.es': 'yahoo',
        'yahoo.ca': 'yahoo',
        'yahoo.com.au': 'yahoo',
        'yahoo.com.br': 'yahoo',
        'yahoo.com.mx': 'yahoo',
        'yahoo.com.sg': 'yahoo',
        'yahoo.com.hk': 'yahoo',
        'yahoo.com.tw': 'yahoo',
        'yahoo.co.jp': 'yahoo',
        'yahoo.co.in': 'yahoo',
        'yahoo.co.kr': 'yahoo',
        'yahoo.co.th': 'yahoo',
        'yahoo.co.id': 'yahoo',
        'yahoo.co.my': 'yahoo',
        'yahoo.co.za': 'yahoo',
        'yahoo.co.nz': 'yahoo',
        'yahoo.co.ph': 'yahoo',
        'yahoo.co.ve': 'yahoo',
        'yahoo.com.ar': 'yahoo',
        'yahoo.com.co': 'yahoo',
        'yahoo.com.pe': 'yahoo',
        'yahoo.com.uy': 'yahoo',
        'yahoo.com.ec': 'yahoo',
        'yahoo.com.gt': 'yahoo',
        'yahoo.com.hn': 'yahoo',
        'yahoo.com.ni': 'yahoo',
        'yahoo.com.pa': 'yahoo',
        'yahoo.com.py': 'yahoo',
        'yahoo.com.sv': 'yahoo',
        'yahoo.com.do': 'yahoo',
        'yahoo.com.pr': 'yahoo',
        'yahoo.com.bo': 'yahoo',
        'yahoo.com.cr': 'yahoo',
        'yahoo.ru': 'yahoo',
        'yahoo.cn': 'yahoo',
        'icloud.com': 'icloud',
        'me.com': 'icloud',
        'mac.com': 'icloud',
        'aol.com': 'aol',
        'aol.it': 'aol',
        'aol.es': 'aol',
        'aol.ru': 'aol',
        'aol.cn': 'aol',
        'aol.co.kr': 'aol',
        'protonmail.com': 'protonmail',
        'proton.me': 'protonmail',
        'yandex.com': 'yandex',
        'yandex.ru': 'yandex',
        'yandex.ua': 'yandex',
        'yandex.by': 'yandex',
        'yandex.kz': 'yandex',
        'mail.com': 'mail',
        'email.com': 'mail',
        'mail.ru': 'mail',
        'bk.ru': 'mail',
        'inbox.ru': 'mail',
        'list.ru': 'mail',
        'gmx.com': 'gmx',
        'gmx.de': 'gmx',
        'gmx.at': 'gmx',
        'gmx.ch': 'gmx',
        'web.de': 'web',
        't-online.de': 't-online',
        'orange.fr': 'orange',
        'orange.com': 'orange',
        'free.fr': 'free',
        'laposte.net': 'laposte',
        'sfr.fr': 'sfr',
        'wanadoo.fr': 'wanadoo',
        'voila.fr': 'voila',
        'club-internet.fr': 'club-internet',
        'libero.it': 'libero',
        'virgilio.it': 'virgilio',
        'alice.it': 'alice',
        'tiscali.it': 'tiscali',
        'wind.it': 'wind',
        'fastweb.it': 'fastweb',
        'telecom.it': 'telecom',
        'tin.it': 'tin',
        'inwind.it': 'inwind',
        'iol.it': 'iol',
        'mclink.it': 'mclink',
        'supereva.it': 'supereva',
        'terra.es': 'terra',
        'telefonica.net': 'telefonica',
        'ya.ru': 'ya',
        'rambler.ru': 'rambler',
        'qq.com': 'qq',
        'vip.qq.com': 'qq',
        '163.com': '163',
        '126.com': '126',
        'sina.com': 'sina',
        'sohu.com': 'sohu',
        'tom.com': 'tom',
        'yeah.net': 'yeah',
        'foxmail.com': 'foxmail',
        'naver.com': 'naver',
        'daum.net': 'daum',
        'hanmail.net': 'hanmail',
    }
    
    # Check exact matches first
    if domain in exact_matches:
        return exact_matches[domain]
    
    # Check pattern matches for common providers
    if 'gmail' in domain:
        return 'gmail'
    elif any(x in domain for x in ['outlook', 'hotmail', 'live', 'msn']):
        return 'outlook'
    elif 'yahoo' in domain:
        return 'yahoo'
    elif any(x in domain for x in ['icloud', 'me.com', 'mac.com']):
        return 'icloud'
    elif 'aol' in domain:
        return 'aol'
    elif 'proton' in domain:
        return 'protonmail'
    elif 'yandex' in domain:
        return 'yandex'
    elif 'gmx' in domain:
        return 'gmx'
    elif 'web.de' in domain:
        return 'web'
    elif 't-online' in domain:
        return 't-online'
    elif 'orange' in domain:
        return 'orange'
    elif 'free.fr' in domain:
        return 'free'
    elif 'laposte' in domain:
        return 'laposte'
    elif 'sfr' in domain:
        return 'sfr'
    elif 'wanadoo' in domain:
        return 'wanadoo'
    elif 'voila' in domain:
        return 'voila'
    elif 'club-internet' in domain:
        return 'club-internet'
    elif 'libero' in domain:
        return 'libero'
    elif 'virgilio' in domain:
        return 'virgilio'
    elif 'alice' in domain:
        return 'alice'
    elif 'tiscali' in domain:
        return 'tiscali'
    elif 'wind' in domain:
        return 'wind'
    elif 'fastweb' in domain:
        return 'fastweb'
    elif 'telecom' in domain:
        return 'telecom'
    elif 'tin' in domain:
        return 'tin'
    elif 'inwind' in domain:
        return 'inwind'
    elif 'iol' in domain:
        return 'iol'
    elif 'mclink' in domain:
        return 'mclink'
    elif 'supereva' in domain:
        return 'supereva'
    elif 'terra' in domain:
        return 'terra'
    elif 'telefonica' in domain:
        return 'telefonica'
    elif 'ya.ru' in domain:
        return 'ya'
    elif 'rambler' in domain:
        return 'rambler'
    elif any(x in domain for x in ['mail.ru', 'bk.ru', 'inbox.ru', 'list.ru']):
        return 'mail'
    elif 'qq' in domain:
        return 'qq'
    elif '163' in domain:
        return '163'
    elif '126' in domain:
        return '126'
    elif 'sina' in domain:
        return 'sina'
    elif 'sohu' in domain:
        return 'sohu'
    elif 'tom' in domain:
        return 'tom'
    elif 'yeah' in domain:
        return 'yeah'
    elif 'foxmail' in domain:
        return 'foxmail'
    elif 'naver' in domain:
        return 'naver'
    elif 'daum' in domain:
        return 'daum'
    elif 'hanmail' in domain:
        return 'hanmail'
    
    return 'other'

def parse_js(js_text):
    """
    Convert JS list of strings into Python dict
    """
    lines = js_text.splitlines()
    
    # Find the start and end of the array
    start_idx = None
    end_idx = None
    
    for i, line in enumerate(lines):
        if 'const free_providers = [' in line:
            start_idx = i
        elif ']' in line and i > start_idx:
            end_idx = i
            break
    
    if start_idx is None or end_idx is None:
        raise ValueError("Could not find array boundaries in JS file")
    
    # Extract array lines
    array_lines = lines[start_idx:end_idx+1]
    
    # Clean lines: strip whitespace, remove empty lines and trailing commas
    clean_lines = []
    for line in array_lines:
        line = line.strip()
        if line and not line.startswith('const'):
            # Handle the last line which might contain both item and closing bracket
            if line.endswith(']'):
                line = line[:-1]  # Remove the closing bracket
            # Remove trailing comma
            if line.endswith(','):
                line = line[:-1]
            if line:  # Only add non-empty lines
                clean_lines.append(line)
    
    # Wrap with [] to make valid JSON
    json_text = "[" + ",".join(clean_lines) + "]"
    
    # Parse JSON
    domains = json.loads(json_text)
    
    # Normalize and convert to dict with proper provider names
    return {d.lower(): get_provider_name(d.lower()) for d in domains}

def save_json(data):
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} domains to {OUTPUT_FILE}")

def main():
    print("Fetching JS file...")
    js_text = fetch_js()
    print("Parsing JS text...")
    data = parse_js(js_text)
    print("Saving JSON...")
    save_json(data)
    print("Done!")

if __name__ == "__main__":
    main()
