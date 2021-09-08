# data must be stored in JSON format

# data: 
{
  "name": "shuffle lines",
  "author": "nicky",
  "icon": "random.png",
  "tags": "shuffle randomize lines",
  "description": "shuffles all lines",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/1160/1160231.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    arr = text.full_text.split('\n')
    from random import shuffle
    shuffle(arr)
    return '\n'.join(arr)
# script: 
