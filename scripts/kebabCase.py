# data must be stored in JSON format

# data: 
{
  "name": "kebab case",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "kebab case",
  "description": "turns-your-text-to-kebab-case",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return text.text.lower().replace(' ', '-')
# script: 
