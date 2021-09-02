# data must be stored in JSON format

# data: {
  "name": "sort lines",
  "author": "nicky",
  "icon": "sort.png",
  "tags": "sort line",
  "description": "sorts all lines alfabetically",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3576/3576411.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return '\n'.join(sorted(text.full_text.split('\n')))
# script: 
