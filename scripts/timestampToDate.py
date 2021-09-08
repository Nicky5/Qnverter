# data must be stored in JSON format

# data: 
{
  "name": "timestamp to date",
  "author": "nicky",
  "icon": "numbers.png",
  "tags": "UNIX date timestamp",
  "description": "converts a UNIX timestamp to date",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3402/3402135.png",
  "dependecies": ["ipython"]
}


# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    from IPython.utils.tz import utcfromtimestamp
    try:
        return utcfromtimestamp(int(text.text)).strftime('%Y/%m/%d %H:%M:%S')
    except ValueError:
        return utcfromtimestamp(int(text.text) // 1000).strftime('%Y/%m/%d %H:%M:%S')
# script: 
