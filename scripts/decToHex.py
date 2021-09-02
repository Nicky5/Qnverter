# data must be stored in JSON format

# data: {
  "name": "dec to hex",
  "author": "nicky",
  "icon": "numbers.png",
  "tags": "dec hex",
  "description": "transforms a decimal number into a Hexadecimal one",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3402/3402135.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return hex(int(text.text))
# script: 
