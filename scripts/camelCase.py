# data must be stored in JSON format

# data: {
  "name": "camel case",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "camelcase case camel",
  "description": "converts_your_text_to_camelcase",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    result = []
    temp = text.text.lower()
    arr = temp.split(' ')
    if temp.count('_'):
        arr = temp.split('_')
    for i in arr:
        result.append(i[0].upper())
        result.append(i[1:].lower())
    result = ''.join(result)
    return result[0].lower() + result[1:]
# script: 
