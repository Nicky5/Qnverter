# data must be stored in JSON format

# data: {
  "name": "ascii to digi",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "digits numbers ascii",
  "description": "converts characters to ascii numbers",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    result = ''
    for i in text.text:
        result += f'{ord(i)} '
    return result
# script: 
