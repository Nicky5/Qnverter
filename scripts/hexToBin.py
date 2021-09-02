# data must be stored in JSON format

# data: {
  "name": "hex to bin",
  "author": "nicky",
  "icon": "binary.png",
  "tags": "bin hex",
  "description": "transforms a Hexadecimal number into a binary one",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/2742/2742010.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return bin(int(text.text, 16))
# script: 
