# data must be stored in JSON format

# data: {
  "name": "hex to dec",
  "author": "nicky",
  "icon": "numbers.png",
  "tags": "dec hex",
  "description": "transforms a Hexadecimal number into a decimal one",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3402/3402135.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return int(int(text.text, 16))
# script: 
