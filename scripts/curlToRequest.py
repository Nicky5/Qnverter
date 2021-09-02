# data must be stored in JSON format

# data: {
  "name": "curl to request",
  "author": "nicky",
  "icon": "python.png",
  "tags": "curl request",
  "description": "parses your curl command to a python request",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/1822/1822899.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    from curl2pyreqs.ulti import parseCurlString
    return parseCurlString(text.text)
# script: 
