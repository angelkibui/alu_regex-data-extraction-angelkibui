import re
import sys

class DataExtractor:
    def __init__(self):
        # Email regex - captures standard email formats and subdomains
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # URL regex - captures http/https URLs with optional subdomains and paths
        self.url_pattern = r'https?://(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?://(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}'
        
        # Phone number regex - captures common US/international formats with various separators
        self.phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        
        # Credit card regex - 16 digits in groups of 4, separated by spaces or hyphens
        self.credit_card_pattern = r'\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}'
        
        # Hashtag regex - captures hashtags starting with # followed by letters/numbers
        self.hashtag_pattern = r'#[A-Za-z0-9_]+'

    def extract_emails(self, text):
        """Extract all email addresses from text"""
        return re.findall(self.email_pattern, text)
    
    def extract_urls(self, text):
        """Extract all URLs from text"""
        return re.findall(self.url_pattern, text)
    
    def extract_phone_numbers(self, text):
        """Extract all phone numbers from text"""
        return re.findall(self.phone_pattern, text)
    
    def extract_credit_cards(self, text):
        """Extract all credit card numbers from text"""
        return re.findall(self.credit_card_pattern, text)
    
    def extract_hashtags(self, text):
        """Extract all hashtags from text"""
        return re.findall(self.hashtag_pattern, text)
    
    def extract_all(self, text):
        """Extract all supported data types from text"""
        results = {
            "emails": self.extract_emails(text),
            "urls": self.extract_urls(text),
            "phone_numbers": self.extract_phone_numbers(text),
            "credit_cards": self.extract_credit_cards(text),
            "hashtags": self.extract_hashtags(text)
        }
        return results

def main():
    # Example usage
    if len(sys.argv) < 2:
        print("Usage: python extractor.py <file_path>")
        print("Or pipe text: cat file.txt | python extractor.py")
        return
    
    extractor = DataExtractor()
    
    # Handle both file input and piped input
    if len(sys.argv) == 2 and sys.argv[1] != '-':
        try:
            with open(sys.argv[1], 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found.")
            return
    else:
        # Read from standard input if no file specified or '-' is specified
        text = sys.stdin.read()
    
    results = extractor.extract_all(text)
    
    # Display results
    print("\n===== Extraction Results =====")
    
    print("\nEmails found:")
    for i, email in enumerate(results["emails"], 1):
        print(f"{i}. {email}")
    
    print("\nURLs found:")
    for i, url in enumerate(results["urls"], 1):
        print(f"{i}. {url}")
    
    print("\nPhone numbers found:")
    for i, phone in enumerate(results["phone_numbers"], 1):
        print(f"{i}. {phone}")
    
    print("\nCredit card numbers found:")
    for i, cc in enumerate(results["credit_cards"], 1):
        print(f"{i}. {cc}")
    
    print("\nHashtags found:")
    for i, tag in enumerate(results["hashtags"], 1):
        print(f"{i}. {tag}")

if __name__ == "__main__":
    main()
