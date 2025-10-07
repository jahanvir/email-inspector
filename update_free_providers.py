import json
import requests
from pathlib import Path

JS_URL = "https://raw.githubusercontent.com/sr-26/email-inspector/master/free_providers.js"
OUTPUT_FILE = Path(__file__).parent / "email_inspector" / "data" / "free_providers.json"

def fetch_js():
    resp = requests.get(JS_URL, timeout=10)
    resp.raise_for_status()
    return resp.text

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
    
    # Normalize and convert to dict {domain: "other"}
    return {d.lower(): "other" for d in domains}

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
