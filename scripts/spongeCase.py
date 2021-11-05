# data must be stored in JSON format

# data: 
{
  "name": "sponge case",
  "author": "nicky",
  "icon": "abc.png",
  "tags": "sponge case spongecase",
  "description": "CoNvErTs YoUr TeXt To A hIgHeR fOrM oF cOmMuNiCaTiOn",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/164/164691.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    time = False
    result = []
    for i in text.text:
        if time:
            result.append(i.lower())
            time = False
        else:
            result.append(i.upper())
            time = True
    return ''.join(result)
# script: 
