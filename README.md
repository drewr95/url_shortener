# Weekly Report Email Automation 

This project can send a weekly status report document in an email to the 
a specified email. A window will pop up first, warning the user that 
they have 30 seconds until it will be sent automatically, but they also 
have the choice of a 'send now' button and a 'cancel' button. Once the 
30 seconds have been reached or if the 'send now' button is pressed, the 
program will open Microsoft Outlook if it is not already open. After 
Outlook is open, it will create a new email message. Once it creates a 
new email message, the program will search in the user's Documents/ 
directory for a file that contains the words 'weekly' and 'report' in 
it. It will attach that file, add the recipient of the email message, 
and add a subject line. If there is an email signature, it will be added 
as well (no body text will be sent). 

## Getting Started Through Terminal 

You need Python 3 installed on your local machine to begin which will 
need to include pip. It would also be wise to install virtualenv so that 
you can install your own python virtual environment. Once the above 
requirements are met: 

You need to navigate to the project directory where setup.py is through 
terminal: 

``` cd <path to the project where setup.py is located> ``` 

Then through terminal you'll need to: 

``` <path to your virtual env>/Scripts/pip install -e . ``` 

Setup.py lists project essentials and dependencies that you will need in 
order to run the application. Your virtual environment's version of pip 
will notice that in the setup.py file the extra needed dependencies and 
will install them based on your computer's specifications. 

Setup.py file will install modules in .exe format that you will be able 
to execute. If you want to run the __main__.py file, you will have to 
use terminal: 

``` <path to your virtual env>/Scripts/<python.exe> __main__.py ``` 

## Getting Started Through Pycharm 

In Pycharm you should browse to the SVN repository and check it out. *** 
You should almost never edit trunk directly unless it is for a small 
change. If there is a big change, you should be branching and 
merging/rebasing ***. Or what you can do is 'Open' from pycharm and 
select the branch you checked out on your machine locally.

### Prerequisites

(from above)

```
pip install -e .
```

## Deployment

Deployment of the application is in the release directory.  If you have made a change to your code, merged it back in trunk, and want to update the release, you need to run the install.bat file.  

## Built With

* [PyQt5] (https://pypi.org/project/PyQt5/) - The gui framework used
* [PyCharm] (https://www.jetbrains.com/pycharm/) - The python development environment

## Authors

* **Drew Rife**
