# Import PSCAD Variables - ImPSCAD

## Motivation

PSCAD/EMTDC exports its variables in a .out file which contain ten variables plus the column with the simulation time. 
If your project has more than 10 variables, another .out file will be created, in order to fit them all.
 PSCAD/EMTDC also creates a .inf file with the name of the variables and its order in the .out files (once the .out files does not have a header). 
 It may be boring to check which column belongs to each variable and also open each .out file to import these variables to your python/MATLAB etc project. 

__________________

## Description

In order to solve this problem, this package was created: by using the function PSCADVar, it will create a unique .csv file which contains all of the variables with
the proper header. In the previous version (ImPSCAD_v01) PSCADVar was a class, but in order to improve performance, it is now a function.

Once one execute the function PSCADVar, the .csv file will be created in the same folder as the .inf/.out files are. It is recommended that one use the package Pandas
in order to use all this data.


### Parameters

**INF_path:** str, mandatory. 

 - It's the path of the .inf file 
 - Example: "C:\Users\Your_Name\PSCAD\simulation_project.gf46\noname.inf"

___________________

## Usage

In the following paragraphs, one can learn how to get and use ImPSCAD in your own projects.

###  Getting it

To download it, use Pypi via pip.
```sh
$ pip install ImPSCAD
```

### Using it

```Python
from ImPSCAD import PSCADVar

path = r"C:\Users\Your_Name\PSCAD/simulation_project.gf46\noname.inf"
PSCADVar(path) # after running this line, just read the .csv file using Pandas
```


___________________

## License

MIT License
Copyright (c) 2020 Luis Arthur Novais Haddad


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.