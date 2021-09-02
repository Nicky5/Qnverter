# data must be stored in JSON format

# data: {
  "name": "base 64 encode",
  "author": "nicky",
  "icon": "locked.png",
  "tags": "base 64 base64 encode",
  "description": "encrypts a message to base64 bytes",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/1691/1691940.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    import base64
    return base64.b64encode(text.text.encode('ascii')).decode('ascii')
# script: 
