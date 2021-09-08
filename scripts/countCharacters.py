# data must be stored in JSON format

# data: 
{
  "name": "count characters",
  "author": "nicky",
  "icon": "numbers.png",
  "tags": "count letter charchter",
  "description": "counts the letters in the text",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3402/3402135.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return len(text.text)
# script: 
