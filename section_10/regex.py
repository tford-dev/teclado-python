"""
. = "Anything" like letters, numbers, and symbols, but not new lines
+ = one or more of 
* = zero or more of
? = zero or one of

.* = anything and any amount of it - does not read anything on new lines
[ ] = match anything in the brackets 
[a-z] = match anything lowercase in those range of letters
[A-z] = match anything regardless of case in those range of letters
"""
import re;

email = 'terranceford@fiendbmx.com';
expression = '[a-z]+'
matches = re.findall(expression, email);
#print(matches); ['terranceford', 'fiendbmx', 'com']
domain = f'{matches[1]}.{matches[2]}'; #'fiendbmx.com'

price = 'MSRP: $45,000.50';
price_expression = 'MSRP: \$([0-9,]*\.[0-9]*)';
price_matches = re.search(price_expression, price);
price_matches.group(0); #MSRP: $45000.50
price_matches.group(1); #$45000.50

price_without_comma = price_matches.group(1).replace(',', ''); #replace comma with an empty string
price_number = float(price_without_comma);
print(price_number);