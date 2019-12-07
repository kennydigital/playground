Why the playground?

-Our new users want to use a basic ide like atom.
-They want to get the basics of source control github
-They want to get a sample hands on with python


How to get started

-Download atom (https://atom.io/)
-Install homebrew (From terminal window, paste below)
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
-From terminal: brew install python3
-Done!

Let's "clone" a repo. This is simply "downloading" a copy of that repo to your harddrive

1. From atom, let's grab a basic repo so you can begin
2. Within atom, use hotkeys: Command +Shift + P
3. Type : Github clone
4. From the results, click Github clone
5. Paste in this repo: https://github.com/kennydigital/playground.git

TODO:
-Show how to authorize atom + github, and copy/pasting token into the introduce
https://github.atom.io/login

Now you will notice in left pane of Atom, the "Playground" project loaded and some sample files

Tips:

Hot keys in atom (for mac)
Commmand + I  : Run my python ```
Command  + S  : Save my current code

```

What we will cover together:

-Quick introduction to check-ins, branches
-Quick way of using the ide to run python
-Quick way of understanding basic functions (sample_pyfunc.py)
-I will give you basics, you try yourself (sample_rest.py, chinhook.db)

How to execute the samples:

Sample - Rest Api

From command line :

python sample_rest.py
This will initialize flask, and provide an endpoint you can hit from your webbrowser
http://127.0.0.1:5002/employees
