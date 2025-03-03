import os
import re
import socket
from collections import Counter

data_dir = "/home/data"
output_dir = "/home/data/output"
file1_path = os.path.join(data_dir, "IF-1.txt")
file2_path = os.path.join(data_dir, "AlwaysRememberUsThisWay-1.txt")
result_path = os.path.join(output_dir, "result.txt")

os.makedirs(output_dir, exist_ok=True)

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words)

def get_top_words(text, n=3):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(n)

def expand_contractions(text):
    expanded = re.sub(r'(\w+)\'(\w+)', r'\1 \2', text)
    return expanded

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            ip_address = s.getsockname()[0]
        except:
            ip_address = '127.0.0.1'
        finally:
            s.close()
        return ip_address

try:
    with open(file1_path, 'r', encoding='utf-8') as f:
        if_text = f.read()
    
    with open(file2_path, 'r', encoding='utf-8') as f:
        lady_gaga_text = f.read()
    
    if_word_count = count_words(if_text)
    lady_gaga_word_count = count_words(lady_gaga_text)
    
    total_words = if_word_count + lady_gaga_word_count
    
    top_if_words = get_top_words(if_text)
    
    expanded_lady_gaga = expand_contractions(lady_gaga_text)
    top_lady_gaga_words = get_top_words(expanded_lady_gaga)
    
    ip_address = get_ip_address()
    
    with open(result_path, 'w', encoding='utf-8') as f:
        print("Writing into result.txt")
        f.write("Word count analysis results:\n\n")
        f.write(f"a. Word count in IF-1.txt: {if_word_count}\n")
        f.write(f"   Word count in AlwaysRememberUsThisWay-1.txt: {lady_gaga_word_count}\n\n")
        f.write(f"b. Grand total of words across both files: {total_words}\n\n")
        f.write("c. Top 3 most frequent words in IF-1.txt:\n")
        for word, count in top_if_words:
            f.write(f"   '{word}': {count} occurrences\n")
        f.write("\n")
        f.write("d. Top 3 most frequent words in AlwaysRememberUsThisWay-1.txt (after handling contractions):\n")
        for word, count in top_lady_gaga_words:
            f.write(f"   '{word}': {count} occurrences\n")
        f.write("\n")
        f.write(f"e. IP address of the machine: {ip_address}\n")
        print("Completed writing into the file")


    with open(result_path, 'r', encoding='utf-8') as f:
        print(f.read())

except Exception as e:
    print(f"An error occurred: {e}")
