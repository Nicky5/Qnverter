# data must be stored in JSON format

# data: {
  "name": "hex to rgb",
  "author": "nicky",
  "icon": "rgb.png",
  "tags": "rgb hex",
  "description": "converts hex to rgb values",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/936/936936.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    h = text.text.lstrip('#')
    return str(tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))).lstrip('(').rstrip(')')
# script: 
