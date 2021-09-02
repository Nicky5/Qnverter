# data must be stored in JSON format

# data: {
  "name": "start case",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "start case startcase",
  "description": "Converts Your Text To Start Case",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    arr = []
    for i in text.text.split(' '):
        arr.append(i[0].upper() + i[1:].lower())
    return ' '.join(arr)
# script: 
