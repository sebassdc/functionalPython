#  2
# Functions as first-class objects
from decimal import Decimal

def remove(str, chars):
    if chars: return remove(str.replace(chars[0], ""), chars[1:])
    return str

# oldway
def clean_decimal(text):
    if text is None: return text
    try:
        return Decimal(text.replace("$", "").replace(",", ""))
    except InvalidOperation:
        return text

#funcway
# clean_decimal = lambda x: Decimal(x.replace(replace(x, "$", ""), ",", ""))

print(remove("$12,000,234.45"))
