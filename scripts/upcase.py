# data must be stored in JSON format

# data: {
  "name": "upcase",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "case lower",
  "description": "set your text to uppercase",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return text.text.upper()
# script: 
