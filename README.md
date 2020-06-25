# GetVar

**Motivation**

PSCAD/EMTDC exports its variables in a .out file which contain ten variables plus the column with the simulation time. If your project has more than 10 variables, another .out file will be created, in order to fit them all. PSCAD/EMTDC also creates a .inf file with the name of the variables and its order in the .out files, once these files does not have a header. It may be boring to check which column belongs to each variable and also open each .out file to import these variables to your python/MATLAB etc project. 

__________________

**Description**

In order to solve this problem, this package was created: by using it, one can read all of the .out files, storage its variables and also create a .csv file with all the columns and header in a unique file.

The class PSCADVar import all the variables data from the output of both programs simulations and returns it in a object.

PSCADVar reads data from .out files: just give the .INF path as argument

**Parameters**:

INF_path: str, mandatory. 
It's the path of the .inf file

writecsv: bool, optional. Default: True
Creates a .CSV file with all the .OUT variables and a header. 

delout:   bool, optional. Default: False
Deletes the .OUT files once they were already read
