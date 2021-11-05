# Qnverter
Python application for quick text conversions.

proper install is only possible on linux. Windows and Mac user can still download and install through pip.

### What is Qnverter
It's a quick way of converting any text-based content in a fast and easy way, which also means you don't have to give up your data to some website on the internet just to be able to convert a few JSON files. 
The entire application is written in pure python and uses the PyQt module to generate the GUI. You can also install new scripts from inside the application with the press of a button.

I'm currently planning to add a syntax highlighter (even though it didn't end well last time I tried) and a proper script repository where everyone can post their scripts and contribute to the project. In the meantime feel to create your own scripts and share them with me. I'm curious to see how bored people can get nowadays

### Install 
**Linux only**
first, make sure to have a python interpreter installed on your computer and run `pip install -r requirements.txt` to make sure to have downloaded all python dependencies necessary for the program to run properly.

Additionally, clone or download the repository to get it on your local hard drive
and finally, run the following commands to set up the application
```
make
make install
```
to uninstall just run ```make uninstall```

**cross-platform**
```
pip install qnverter
```
The drawback is that you can only run the application by typing ```qnverter``` in a terminal. 

# Screenshots
![schreenshot1.png](schreenshot1.png)
![screenshot2.png](screenshot2.png))

### Guide to creating your own script
Do you have the impression your current scripts just aren't enough but are too lazy to see if someone else might do the work for you?
No Problem, you can create your own scripts by following this short guide.

Requirements:
- some basic python skills. (depends on what you need though)
- a text editor (even better would be an IDE)

First things first create a new python file (NAME.py) in a freshly downloaded or cloned copy of this repository. Then paste this template into the File
```python
# data: 
{
  "name": "my script",
  "author": "you",
  "icon": "icon.png",
  "tags": "tag other_tag even_more_tags",
  "description": "description",
  "icon_link": "https://url.icon.png"
  "dependencies": ["example-dependency"]
}
# data:   

from qnverter import Text
# script: 
def func(text: Text):
    return text.text
# script: 
```
What you should notice here are these strange comments like `data: ` or `script: `.These are used to delimit the executable python script from the other components of the file. To explain a bit more accurately let's look at the `# data:` comments.
You can find two of them, both enclosing what seems to be a python dictionary. Actually, everything in between these two comments will be interpreted as a JSON formatted string. what this means is it won't be executed or anything, just used to carry information. This information includes:
- name: choose a unique name for your script to represent it
- author: This is your time to shine! write your name in here to be credited in the application credits
- icon: this field represents the name of an icon. This icon must be located in /icons from the project root. 
- tags: here insert some tags to make it easier to find your script in the selection tab. tags must be delivered in a string and separated with a space
- description: I think this is pretty self-explanatory. 
- icon_link: when the program notices that there is no icon named after your icon it will try to download a fresh one from this link. this can be used to pass a script without having to manually download and relocate an icon yourself
- dependencies: Let's say you used a pip library to solve your problem (smart but in my days we used to code everything from scratch using Assembly). this is the place to list them so you don't get strange errors once you uninstall them from your computer. Qnverter will automatically check if any packages from this list are missing in the python interpreter and let you know by colouring the script red in the selection tab

Now let's turn to the `# script: ` tags. Make sure to leave the `from main qnverter Text` OUTSIDE of the tags. This is very important because we don't want the import statement to be executed by the application under any means. Since the executable part of the script will be executed using the `exec()` method, global variables will be passed directly through it as a parameter. any other import statements directed to the qnverter file must also be declared outside of the script tags or they will crash the Application. 
anything else you want the Application to execute is fine to be put inside the script tags. note that the program will extract all local variables declared during the loading of the script and execute the method called `func`. which means when you click on your script on the selection menu, everything inside that func method will be executed and any returned values will pop up on the left text editor. right now it just returns `text.text`. but what is that `text` object anyways?
well you can use it in three ways:
- `text.full_text` will return everything inside the right text editor as a string object.
- `text.selected` returns everything in the right text editor that is currently selected
- `text.text` on the other side will only return `text.full_text` if `text.selected` is empty. Else it return `text.selected`
Using these tools you can create any script you want. 

Once you are done just place the script in the ~/Qnverter/scripts folder (~ being the home directory) and restart the application or use the built-in button on the top-left of the application to import a new script

Thanks for reading the whole documentation. most people don't.

