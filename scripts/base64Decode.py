# data must be stored in JSON format

# data: {
  "name": "base 64 decode",
  "author": "nicky",
  "icon": "locked.png",
  "tags": "base 64 base64 decode",
  "description": "decrypts a base64 byte message to ascii",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/1691/1691940.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    import base64
    return base64.b64decode(text.text.encode('ascii')).decode('ascii')
# script: 
