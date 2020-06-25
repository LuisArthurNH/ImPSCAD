# GetVar

**Motivation**

PSCAD/EMTDC exports its variables in a .out file which contain ten variables plus the time of simulation. If your project has more than 10 variables, another .out file will be created, in order to fit them all. PSCAD/EMTDC also creates a .inf file with the name of the variables and its order in the .out files, once these files does not have a header. It may be boring to check which column belongs to each variable and also open each .out file to import these variables to your python/MATLAB etc project. 

**Description**
In order to solve this problem, this package was created: by using it, one can read all of the .out files, storage its variables and also create a .csv file with all the columns and header in a unique file.

The class PSCADVar import all the variables data from the output of both programs simulations and returns it in a object.

PSCADVar reads data from .out: just give the .INF path as argument

__________________

**Requirements**

- **Python 3.8**
- **Packages**: all of them are listed in "requirements.txt"
  - To install all of them use: **pip install -r requirements.txt**
