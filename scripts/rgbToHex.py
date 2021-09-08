# data must be stored in JSON format

# data: 
{
  "name": "rgb to hex",
  "author": "nicky",
  "icon": "rgb.png",
  "tags": "rgb hex",
  "description": "converts rgb to hex values",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/936/936936.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    def clamp(x):
        return max(0, min(x, 255))
    colors = text.text.split(' ')
    if text.text.count(', '):
        colors = text.full_text.split(', ')
    if text.text.count(','):
        colors = text.full_text.split(',')
    return '#{0:02x}{1:02x}{2:02x}'.format(clamp(int(colors[0])), clamp(int(colors[1])), clamp(int(colors[2]))).upper()
# script: 
