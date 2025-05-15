#!/usr/bin/env python3

import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+(?:/[^\s]*)?'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)

def main():
    # Load the test strings from a file or define directly
    try:
        with open("test_strings.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("Test file not found. Please create 'test_strings.txt'")
        return

    # Run extractions
    emails = extract_emails(text)
    urls = extract_urls(text)
    phones = extract_phone_numbers(text)
    hashtags = extract_hashtags(text)

    # Save results to a file
    with open("results.txt", "w") as out_file:
        out_file.write("Email Addresses:\n")
        out_file.write('\n'.join(emails) + '\n\n')

        out_file.write("URLs:\n")
        out_file.write('\n'.join(urls) + '\n\n')

        out_file.write("Phone Numbers:\n")
        out_file.write('\n'.join(phones) + '\n\n')

        out_file.write("Hashtags:\n")
        out_file.write('\n'.join(hashtags) + '\n')
    
    print("Extraction completed. Results saved to 'results.txt'")

if __name__ == "__main__":
    main()
