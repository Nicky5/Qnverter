import base64
import datetime
import json
import os
import subprocess
import time
from random import shuffle

from IPython.utils.tz import utcfromtimestamp
from colormap import rgb2hex
from curl2pyreqs.ulti import parseCurlString
import xml.dom.minidom

from lxml import etree
from soupsieve.util import lower

from main import Text, Item

def jsonFormat(text: Text):
    return json.dumps(json.loads(text.full_text), indent=2, sort_keys=True)

def jsonMinify(text: Text):
    return json.dumps(json.loads(text.full_text), separators=(',', ':'))

def base64Encode(text: Text):
    return base64.b64encode(text.text.encode('ascii')).decode('ascii')

def base64Decode(text: Text):
    return base64.b64decode(text.text.encode('ascii')).decode('ascii')

def binToDec(text: Text):
    return int(int(text.text, 2))

def decToBin(text: Text):
    return bin(int(text.text))

def binToHex(text: Text):
    return hex(int(text.text, 2))

def hexToBin(text: Text):
    return bin(int(text.text, 16))

def decToHex(text: Text):
    return hex(int(text.text))

def hexToDec(text: Text):
    return int(int(text.text, 16))

def camelCase(text: Text):
    result = []
    temp = text.text.lower()
    arr = temp.split(' ')
    if temp.count('_'):
        arr = temp.split('_')
    for i in arr:
        result.append(i[0].upper())
        result.append(i[1:].lower())
    result = ''.join(result)
    return lower(result[0]) + result[1:]

def collapseLines(text: Text):
    return text.full_text.replace('\n', ' ')

def countCharacters(text: Text):
    return len(text.text)

def countLines(text: Text):
    return text.full_text.count('\n') + 1

def countWords(text: Text):
    while '  ' in  text.text:
        text.text.replace('  ', '')
    return text.text.count(' ') + text.text.count('\n')

def dateToTimestampe(text: Text):
    if text.text.count(':'):
        return time.mktime(datetime.datetime.strptime(text.text, "%d:%m:%Y").timetuple())
    if text.text.count('/'):
        return time.mktime(datetime.datetime.strptime(text.text, "%d/%m/%Y").timetuple())
    if text.text.count('.'):
        return time.mktime(datetime.datetime.strptime(text.text, "%d.%m.%Y").timetuple())
    if text.text.count('-'):
        return time.mktime(datetime.datetime.strptime(text.text, "%d-%m-%Y").timetuple())
    else:
        raise ValueError

def timestampToDate(text: Text):
    try:
        return utcfromtimestamp(int(text.text)).strftime('%Y/%m/%d %H:%M:%S')
    except ValueError:
        return utcfromtimestamp(int(text.text) // 1000).strftime('%Y/%m/%d %H:%M:%S')

def digiToAscii(text: Text):
    result = ''
    for i in text.text.split(' '):
        result += f'{chr(int(i))}'
    return result

def asciiToDigi(text: Text):
    result = ''
    for i in text.text:
        result += f'{ord(i)} '
    return result

def downcase(text: Text):
    return text.text.lower()

def upcase(text: Text):
    return text.text.upper()

def evalPython(text: Text):
    f = open("tempscript.py", "w")
    f.write(text.full_text)
    proc = subprocess.Popen("tempscript.py", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    for i in proc.stdout:
        yield i.decode("utf-8").replace("\n", "")
    os.remove("tempscript.py")

def formatXml(text: Text):
    return xml.dom.minidom.parseString(text.full_text).toprettyxml()

def minifyXml(text: Text):
    return etree.tostring(etree.XML(text.full_text, parser=etree.XMLParser(remove_blank_text=True)))

def hexToRgb(text: Text):
    h = text.text.lstrip('#')
    return str(tuple(int(h[i:i+2], 16) for i in (0, 2, 4))).lstrip('(').rstrip(')')

def rgbToHex(text: Text):
    colors = text.text.split(' ')
    if text.text.count(', '):
        colors = text.full_text.split(', ')
    if text.text.count(','):
        colors = text.full_text.split(',')
    return rgb2hex(int(colors[0]), int(colors[1]), int(colors[2]))

def joinSpaceLines(text: Text):
    arr = text.full_text.split('\n')
    arr2 = []
    for i in arr:
        if i.count(' ') != len(i):
            arr2.append(i)
    return '\n'.join(arr2)

def joinCommaLines(text: Text):
    return text.full_text.replace(',\n', ', ')

def kebabCase(text: Text):
    return text.text.lower().replace(' ', '-')

def removeDuplicateLines(text: Text):
    return '\n'.join(set(text.full_text.split('\n')))

def removeDuplicateWords(text: Text):
    return ' '.join(set(text.text.split(' ')))

def reverseLines(text: Text):
    return '\n'.join(reversed(text.full_text.split('\n')))

def revgerseString(text: Text):
    return ''.join(reversed(text.text))

def reverseWords(text: Text):
    return ' '.join(reversed(text.text.split(' ')))

def shuffleLines(text: Text):
    arr = text.full_text.split('\n')
    shuffle(arr)
    return '\n'.join(arr)

def shuffleWords(text: Text):
    arr = text.text.split(' ')
    shuffle(arr)
    return ' '.join(arr)

def snakeCase(text: Text):
    return text.text.lower().replace(' ', '_')

def sortLines(text: Text):
    return '\n'.join(sorted(text.full_text.split('\n')))

def spongeCase(text: Text):
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

def startCase(text: Text):
    arr = []
    for i in text.text.split(' '):
        arr.append(i[0].upper() + i[1:].lower())
    return ' '.join(arr)

def sumAll(text: Text):
    arr = text.text.split(' ')
    if text.text.count(', '):
        arr = text.text.split(', ')
    if text.text.count(','):
        arr = text.text.split(',')
    return sum(map(float, arr))

def trim(text: Text):
    return text.full_text.rstrip(' ').lstrip(' ').rstrip('\n').lstrip('\n')

def curlToRequest(text: Text):
    return parseCurlString(text.text)

def newTest(text: Text):
    return 'hulllo this has been succcesfully bee written lol'

items = [
    Item(event=asciiToDigi, name='ascii to digi', author='nicky', icon='abc.png', tags='digits numbers ascii', description='converts characters to ascii numbers'),
    Item(event=base64Decode, name='base 64 decode', author='nicky', icon='locked.png', tags='base 64 base64 decode', description='decrypts a base64 byte message to ascii'),
    Item(event=base64Encode, name='base 64 encode', author='nicky', icon='locked.png', tags='base 64 base64 encode', description='encrypts a message to base64 bytes'),
    Item(event=binToDec, name='bin to dec', author='nicky', icon='binary.png', tags='bin dec', description='transforms a binary number into a decimal one'),
    Item(event=binToHex, name='bin to hex', author='nicky', icon='binary.png', tags='bin hex', description='transforms a binary number into a Hexadecimal one'),
    Item(event=camelCase, name='camel case', author='nicky', icon='abc.png', tags='camelcase case camel', description='converts_your_text_to_camelcase'),
    Item(event=collapseLines, name='collapse lines', author='nicky', icon='sort.png', tags='line', description='deletes new line characters'),
    Item(event=countCharacters, name='count characters', author='nicky', icon='numbers.png', tags='count letter charchter', description='counts the letters in the text'),
    Item(event=countLines, name='count lines', author='nicky', icon='numbers.png', tags='count line', description='counts the lines in the text'),
    Item(event=countWords, name='count words', author='nicky', icon='numbers.png', tags='count word', description='counts all words words in the text'),
    Item(event=curlToRequest, name='curl to request', author='nicky', icon='python.png', tags='curl request', description='parses your curl command to a python request'),
    Item(event=dateToTimestampe, name='date to timestampe', author='nicky', icon='numbers.png', tags='UNIX date timestamp', description='converts a date to a UNIX timestamp'),
    Item(event=decToBin, name='dec to bin', author='nicky', icon='binary.png', tags='bin dec', description='transforms a decimal number into a binary one'),
    Item(event=decToHex, name='dec to hex', author='nicky', icon='numbers.png', tags='dec hex', description='transforms a decimal number into a Hexadecimal one'),
    Item(event=digiToAscii, name='digi to ascii', author='nicky', icon='abc.png', tags='digits numbers ascii', description='converts numbers to ascii characters'),
    Item(event=downcase, name='downcase', author='nicky', icon='abc.png', tags='case upper', description='set your text to lowercase'),
    Item(event=evalPython, name='eval python', author='nicky', icon='python.png', tags='python eval run exec', description='runs your python code'),
    Item(event=formatXml, name='format xml', author='nicky', icon='xml.png', tags='xml format', description='pretty prints a xml'),
    Item(event=hexToBin, name='hex to bin', author='nicky', icon='binary.png', tags='bin hex', description='transforms a Hexadecimal number into a binary one'),
    Item(event=hexToDec, name='hex to dec', author='nicky', icon='numbers.png', tags='dec hex', description='transforms a Hexadecimal number into a decimal one'),
    Item(event=hexToRgb, name='hex to rgb', author='nicky', icon='rgb.png', tags='rgb hex', description='converts hex to rgb values'),
    Item(event=joinCommaLines, name='join comma lines', author='nicky', icon='abc.png', tags='comma line join', description='deletes new line charachter after evry comma'),
    Item(event=joinSpaceLines, name='join space lines', author='nicky', icon='abc.png', tags='space line join', description='joins all just space lines to a single space line'),
    Item(event=jsonFormat, name='json format', author='nicky', icon='json.png', tags='json format', description='pretty prints a JSON object'),
    Item(event=jsonMinify, name='json minify', author='nicky', icon='json.png', tags='json minify', description='removes unnessesary space in JSON objects'),
    Item(event=kebabCase, name='kebab case', author='nicky', icon='abc.png', tags='kebab case', description='turns-your-text-to-kebab-case'),
    Item(event=minifyXml, name='minify xml', author='nicky', icon='xml.png', tags='xml minify', description='removes unnessesary space in your xml'),
    Item(event=newTest, name='new test', author='nicky', icon='abc.png', tags='new test', description='generates a new test'),
    Item(event=removeDuplicateLines, name='remove duplicate lines', author='nicky', icon='sort.png', tags='duplicate line', description='removes all duplicates lines it findes'),
    Item(event=removeDuplicateWords, name='remove duplicate words', author='nicky', icon='sort.png', tags='duplicate word', description='removes all duplicates words it findes'),
    Item(event=reverseLines, name='reverse lines', author='nicky', icon='sort.png', tags='reverse line', description='reverses all lines'),
    Item(event=reverseWords, name='reverse words', author='nicky', icon='abc.png', tags='reverse word', description='reverses the order of all words'),
    Item(event=revgerseString, name='revgerse string', author='nicky', icon='abc.png', tags='reverse', description='reverses everything'),
    Item(event=rgbToHex, name='rgb to hex', author='nicky', icon='rgb.png', tags='rgb hex', description='converts rgb to hex values'),
    Item(event=shuffleLines, name='shuffle lines', author='nicky', icon='random.png', tags='shuffle randomize lines', description='shuffles all lines'),
    Item(event=shuffleWords, name='shuffle words', author='nicky', icon='random.png', tags='shuffle randomize words', description='shuffles all words'),
    Item(event=snakeCase, name='snake case', author='nicky', icon='abc.png', tags='snake case snakecase', description='converts_your_text_to_snake_text'),
    Item(event=sortLines, name='sort lines', author='nicky', icon='sort.png', tags='sort line', description='sorts all lines alfabetically'),
    Item(event=spongeCase, name='sponge case', author='nicky', icon='abc.png', tags='sponge case spongecase', description='CoNvErTs YoUr TeXt To A hIgHeR fOrM oF cOmMuNiCaTiOn'),
    Item(event=startCase, name='start case', author='nicky', icon='abc.png', tags='start case startcase', description='Converts Your Text To Start Case'),
    Item(event=sumAll, name='sum all', author='nicky', icon='numbers.png', tags='sum add', description='sums up all numbers it finds'),
    Item(event=timestampToDate, name='timestamp to date', author='nicky', icon='numbers.png', tags='UNIX date timestamp', description='converts a UNIX timestamp to date'),
    Item(event=trim, name='trim', author='nicky', icon='abc.png', tags='trim space', description='trims spaces at both ends of text'),
    Item(event=upcase, name='upcase', author='nicky', icon='abc.png', tags='case lower', description='set your text to uppercase'),
]
