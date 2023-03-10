# tetrad_polyglot

Information for creating a devcontainer to support using vscode for 
writing python and R code with tetrad.

A prerequisite is that you have installed vscode and docker on your system. 
This has been tested on:
1. macOS 
2. ubuntu 20.04
3. Windows 11 under WSL (Windows Subsystem for Linux)

In vscode, be sure you have the extensions installed for Dev Containers and Python; both from Microsoft

When you open this folder from vscode, it will detect that there is a .devcontainer folder and ask if you would like to open the folder in a container.  If you say yes, then it will proceed to build the cointainer which will take a few minutes. This build will only occur the first time.  

Once the Container is built you can then open a terminal window in the container by going to the Terminal tab in the Menu Bar and selecting new terminal.  

At this point, you can run the demo_code.py program from the command line which will
load a dataset and run several searches using tetrad.

```
./demo_code.py
 
 # or
 python demo_code.py

```

Need some R code examples here.

## jpype supports python access to Java

https://jpype.readthedocs.io/en/latest/install.html


## datafile for Bryan's sample code
https://www.opennn.net/documentation/approximation_example.html#DataSet

https://www.opennn.net/files/airfoil_self_noise.csv

fields are separated by semi colons so give this in argument to pd.read_csv

## Javadocs for tetrad

https://s01.oss.sonatype.org/content/repositories/releases/io/github/cmu-phil/tetrad-lib/7.2.2/tetrad-lib-7.2.2-javadoc.jar

Unpack these into a directory and the open the index.html file from a browser.

```
mkdir tetrad_docs
cd tetrad_docs
tar zxf ~/Downloads/7.2.2/tetrad-lib-7.2.2-javadoc.jar
```

