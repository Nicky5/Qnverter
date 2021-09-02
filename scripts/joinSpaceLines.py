# data must be stored in JSON format

# data: {
  "name": "join space lines",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "space line join",
  "description": "joins all just space lines to a single space line",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    arr = text.full_text.split('\n')
    arr2 = []
    for i in arr:
        if i.count(' ') != len(i):
            arr2.append(i)
    return '\n'.join(arr2)
# script: 
