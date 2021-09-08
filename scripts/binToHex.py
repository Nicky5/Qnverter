# data must be stored in JSON format

# data: 
{
  "name": "bin to hex",
  "author": "nicky",
  "icon": "binary.png",
  "tags": "bin hex",
  "description": "transforms a binary number into a Hexadecimal one",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/2742/2742010.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return hex(int(text.text, 2))
# script: 
