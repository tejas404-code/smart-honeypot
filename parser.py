import re, json

def parse_log(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if 'login attempt' in line:
                print(f"[!] Login attempt: {line.strip()}")
