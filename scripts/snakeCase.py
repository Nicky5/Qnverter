# data must be stored in JSON format

# data: {
  "name": "snake case",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "snake case snakecase",
  "description": "converts_your_text_to_snake_text",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return text.text.lower().replace(' ', '_')
# script: 
