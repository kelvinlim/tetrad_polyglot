# tetrad_python

Information for creating a devcontainer to support using vscode for 
writing python code with tetrad.

A prerequisite is that you have installed vscode and docker on your system. 
This has been tested on macOS but also works with windows 11 under WSL (Windows Subsystem for Linux). 

In vscode, be sure you have the extensions installed for Dev Containers.

When you open this folder from vscode, it will detect that there is a .devcontainer folder and ask if you would like to open the folder in a container.  If you say yes, then it will proceed to build the cointainer which will take 5-10 minutes.  You can then open a terminal window in the container.

At this point, you can run the demo_code.py program from the command line which will
load a dataset and run several searches using tetrad.

## jpype supports python access to Java

https://jpype.readthedocs.io/en/latest/install.html


## datafile for Bryan's sample code
https://www.opennn.net/documentation/approximation_example.html#DataSet

https://www.opennn.net/files/airfoil_self_noise.csv

fields are separated by semi colons
