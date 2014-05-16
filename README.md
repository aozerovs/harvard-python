# Harvard python

A script for generating Harvard referencing.

## Get the script and run it
```
git clone https://github.com/wilsonand1/harvard-python.git
cd harvard-python
python h.py
```

One the script is running you'll be asked:
```
Name of file:
```
This is the name of the out Markdown file.

Next question will be what you're referencing. Currently harvard-python supports referencing for books, websites, and articles. More to come.

Next will be questions about what you're referencing. The questions will be (questions vary based on type):

```
Author:
More authors:
Year:
Title:
Edition:
Publication location:
Publisher:
Page numbers (Can be blank):
```

Once you've filled in the last one you will see a print out of the reference in the terminal and it will be written to the Markdown file.

## Example

```
Name of file: python
Type: book
Author: Danny Wilson
More authors: yes
Author: Grace Elizabeth Day
More authors: no
Year: 2012
Title: How to be awesome with Python
Edition: 1st
Publication location: Manchester
Publisher: Penguin
Page numbers (can be blank):
```

And the output put for this would be:

```
Wilson, D. Day, G.E., 2012. *How To Be Awesome With Python.* 1st ed. Manchester: Penguin.
```

Also, the code is pretty filthy.

[@wilsonand1](http://twitter.com/wilsonand1)
