# data must be stored in JSON format

# data: {
  "name": "join comma lines",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "comma line join",
  "description": "deletes new line charachter after evry comma",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return text.full_text.replace(',\n', ', ')
# script: 
