# data must be stored in JSON format

# data: 
{
  "name": "collapse lines",
  "author": "nicky",
  "icon": "sort.png",
  "tags": "line",
  "description": "deletes new line characters",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3576/3576411.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return text.full_text.replace('\n', ' ')
# script: 
