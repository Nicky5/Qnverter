# data must be stored in JSON format

# data: {
  "name": "digi to ascii",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "digits numbers ascii",
  "description": "converts numbers to ascii characters",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    result = ''
    for i in text.text.split(' '):
        result += f'{chr(int(i))}'
    return result
# script: 
