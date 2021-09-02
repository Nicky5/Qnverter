# data must be stored in JSON format

# data: {
  "name": "count words",
  "author": "nicky",
  "icon": "numbers.png",
  "tags": "count word",
  "description": "counts all words words in the text",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3402/3402135.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    while '  ' in text.text:
        text.text.replace('  ', '')
    return text.text.count(' ') + text.text.count('\n')
# script: 
