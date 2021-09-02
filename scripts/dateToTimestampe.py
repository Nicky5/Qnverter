# data must be stored in JSON format

# data: {
  "name": "date to timestampe",
  "author": "nicky",
  "icon": "numbers.png",
  "tags": "UNIX date timestamp",
  "description": "converts a date to a UNIX timestamp",
  "icon_link": "https://cdn-icons-png.flaticon.com/512/3402/3402135.png"
}# data:   


# any import statemnet directed to the main.py must be left outside the script tag
from main import Text

# script: 
def func(text: Text):
    import time
    import datetime
    if text.text.count(':'):
        return time.mktime(datetime.datetime.strptime(text.text, '%d:%m:%Y').timetuple())
    if text.text.count('/'):
        return time.mktime(datetime.datetime.strptime(text.text, '%d/%m/%Y').timetuple())
    if text.text.count('.'):
        return time.mktime(datetime.datetime.strptime(text.text, '%d.%m.%Y').timetuple())
    if text.text.count('-'):
        return time.mktime(datetime.datetime.strptime(text.text, '%d-%m-%Y').timetuple())
    else:
        raise ValueError
# script: 
