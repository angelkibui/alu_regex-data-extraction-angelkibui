import re

# Test string
text = """
Contact us at (123) 456-7890 or 123-456-7890 or 123.456.7890
"""

#pattern:
pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'


# Run the regex
matches = re.findall(pattern, text)

print("Phone Numbers Found:", matches)
