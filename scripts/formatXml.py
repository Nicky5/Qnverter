# data must be stored in JSON format

# data: 
{
  "name": "format xml",
  "author": "nicky",
  "icon": "xml.png",
  "tags": "xml format",
  "description": "pretty prints a xml",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/136/136526.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    import xml.dom.minidom
    return xml.dom.minidom.parseString(text.full_text).toprettyxml()
# script: 
