# data must be stored in JSON format

# data: 
{
  "name": "minify xml",
  "author": "nicky",
  "icon": "xml.png",
  "tags": "xml minify",
  "description": "removes unnessesary space in your xml",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/136/136526.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    from xml.etree import cElementTree
    return cElementTree.tostring(cElementTree.XML(text.full_text, parser=cElementTree.XMLParser()))
# script: 
