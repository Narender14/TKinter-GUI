Tkinter toolkit- Python API :
=============================

Tkinter is an interface to python GUI toolkit. This project is about creating an API for common widgets
like Button, RadioButton, CheckBox, TextField etc. This API file is named "tkinter.py" which has function ADD for adding/displaying any widget in the main window given the required parameters. Using this API of widgets, a application is made that can store the contact details of a user and can search among the contact list. It also allows a user to send message to another user and also view its own messages.


![ScreenShot](https://raw.github.com/Narender14/TKinter-GUI/master/Screen.png)



USAGE : 
-------
The API file is name as "tkinter.py" and a general demo file "finalapplication.py".
The API file is imported in finalapplication.py file by : "import tkinter as obj" command.
User can have different name of API file which then should be reflected in finalapplication.py file.

    On running the finalapplication.py file, Username, Password and toolkit is asked. Choose any username and password but
    please remember it if you want to login next time as the same user. Type anything for toolkit option.
    After that a main window is created with several widgets. A user can then add contact details of its friend or
    can search or can message any friend.
Login.txt, message.txt and a file corresponding to each user will be created that will store username - password, sender - receipient, and contact detail of users.



REQUIREMENT :
-------------
    You must have Python installed on your computer.
    Tkinter is default toolkit so it will be on your computer once you installed python.  
 

RUN (for Linux) : 
------------------

Download the files "tkinter.py" and "finalapplication.py"	into a directory.

    Run command : **python finalapplicatin.py**
    
For closing the application, simply close the window and the application will get closed.


CONTRIBUTION : 
---------------
Please fork this repository and contribute back. Any new idea for its extension is welcomed. 
Any bug report, patch is also welcomed.

A tutorial on how to contribute to github project is [HERE](https://help.github.com/articles/fork-a-repo/)



