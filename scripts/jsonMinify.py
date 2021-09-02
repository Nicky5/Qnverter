# data must be stored in JSON format

# data: {
  "name": "json minify",
  "author": "nicky",
  "icon": "json.png",
  "tags": "json minify",
  "description": "removes unnessesary space in JSON objects",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/136/136525.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    import json
    return json.dumps(json.loads(text.full_text), separators=(',', ':'))
# script: 
