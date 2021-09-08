# data must be stored in JSON format

# data: 
{
  "name": "sum all",
  "author": "nicky",
  "icon": "numbers.png",
  "tags": "sum add",
  "description": "sums up all numbers it finds",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3402/3402135.png"
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    arr = text.text.split(' ')
    if text.text.count(', '):
        arr = text.text.split(', ')
    if text.text.count(','):
        arr = text.text.split(',')
    return sum(map(float, arr))
# script: 
