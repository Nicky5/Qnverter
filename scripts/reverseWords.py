# data must be stored in JSON format

# data: {
  "name": "reverse words",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "reverse word",
  "description": "reverses the order of all words",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return ' '.join(reversed(text.text.split(' ')))
# script: 
