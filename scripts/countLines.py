# data must be stored in JSON format

# data: 
{
  "name": "count lines",
  "author": "nicky",
  "icon": "numbers.png",
  "tags": "count line",
  "description": "counts the lines in the text",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3402/3402135.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    return text.full_text.count('\n') + 1
# script: 
