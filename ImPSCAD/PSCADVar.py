import os
import re
import math
import pandas as pd
import numpy as np
from functools import reduce

def PSCADVar(INF_path):

    with open(INF_path) as myfile:  # Open all the lines in the inf path
            lines = myfile.readlines()

    n_col = 11                                 # Number of columns that the txt has
    n_var = len(lines)                         # Number of PSCAD Variables
    n_files = int(math.ceil(n_var / 10.0))     # Number of .out Files exported (the floating is important)
    n_var_tot = n_var + n_files                # Number of variables INCLUDING additional time column FOR EACH .OUT
    n_var_last = n_var_tot -(n_files-1)*n_col  # Number of variables in the last file
    n_var_exp = n_var + 1                      # Number of variables that will be exported 

    # Create list to store the number of columns of each file
    last_col = [0]*n_files

    for ii in range(0,n_files):     

        if ii != n_files-1:         
            b = n_col
        else:
            b = n_var_last

        last_col[ii] = b

    pattern = "Desc=\"(.*?)\""  # Patter that holds the variable name
    header  = [0] * (n_var_tot)  

    b = 0  # to "freeze" the time when storing the "TIME"
    c = 1  # used in the index: from 1 to 11

    # "For" Logic: each file can take 11 variables, and the first one is TIME
    # so this "for" writes time if it is the time column, or takes the header from
    # the array "header"

    for a in range(0, n_var_tot):

        if  ((a == 0) | (a % 11 == 0)):                    # if it is the first value of all files, store the time name
            header[a] = 'time'     # to the object outside
            b = b - 1
            if a != 0:
                c = 1
        else:
            header[a] = re.search(pattern, lines[b]).group(1)  
            header[a] = header[a].replace(" ", "_")  
        
        b = b + 1
        c = c + 1

    ############################################################################
    # Take all the paths of the .out files
    ############################################################################

    OUT_name  = [0] * n_files
    OUT_path  = [0] * n_files

    for ii in range(0, n_files):
        if (ii < 9):
            OUT_name[ii] = "_0" + str(ii + 1) + ".out"             # Create ending "_0ii".out
            OUT_path[ii] = INF_path.replace(".inf", OUT_name[ii])  # replace in INF_path the.inf for the new end
        else:
            OUT_name[ii] = "_" + str(ii + 1) + ".out"              # Create ending "_0ii".out
            OUT_path[ii] = INF_path.replace(".inf", OUT_name[ii])  # replace in INF_path the.inf for the new end

    # Creates the path of the .CSV that's gonna be writen
    CSV_path = INF_path.replace(".inf", ".csv") # Replaces the ending .inf with .csv

    ########################################################
    ### Treat the data
    ########################################################

    # Create an empty list to store all of the pandas dataframes
    dff = []

    # Read all of the .out files and append them to the empty list
    for path in OUT_path:
        dff.append(pd.read_csv(path, delim_whitespace=True, header=None))

    # Create auxiliar variables
    ii = 0
    jj = 0

    # Rename the header of each file (which is now 0,1,2,3,4...) for the names that are storage at the variable header
    for file in range(0, n_files):
        for ii in range(0, last_col[file]):
            dff[file].rename(columns = {ii:header[ii+jj]}, inplace = True)
        jj = jj + 11

    # Now that the headers are ok, merge all of them (2 by 2) using the column 'time' as reference
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on='time'), dff)

    # Storage all the dataframe into one csv file with header
    df_merged.to_csv(CSV_path,index=False)          
