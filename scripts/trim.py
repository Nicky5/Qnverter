# data must be stored in JSON format

# data: 
{
  "name": "trim",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "trim space",
  "description": "trims spaces at both ends of text",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return text.full_text.rstrip(' ').lstrip(' ').rstrip('\n').lstrip('\n')
# script: 
