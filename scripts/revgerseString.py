# data must be stored in JSON format

# data: {
  "name": "revgerse string",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "reverse",
  "description": "reverses everything",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return ''.join(reversed(text.text))
# script: 
