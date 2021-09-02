# data must be stored in JSON format

# data: {
  "name": "json format",
  "author": "nicky",
  "icon": "json.png",
  "tags": "json format",
  "description": "pretty prints a JSON object",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/136/136525.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    import json
    return json.dumps(json.loads(text.full_text), indent=2, sort_keys=True)
# script: 
