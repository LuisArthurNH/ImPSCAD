###########################################################################
# Libraries and packages
###########################################################################
import os
import re
import math
import pandas as pd
import numpy as np


###########################################################################
# Definition of class
###########################################################################

class PSCADVar(object):
    """ Documentation: 
        This class reads the .out files and returns all of the variables in it contained, as well as the header of the variables, time step and number of variables imported.

        INF_path: str, mandatory. 
        It's the path of the .inf file

        writecsv: bool, optional. 
        Creates a new .CSV file with the .OUT variables
        
        delout:   bool, optional. 
        Deletes the .OUT files once they were already read
        
       """

    def __init__(self, INF_path, **kwargs):
        
        # Default definitions of arguments:
        # It WILL create a CSV file
        # It WILL NOT delete the .OUT files

        try:
            kwargs['writecsv']
        except KeyError:
            kwargs['writecsv'] = True

        try:
            kwargs['delout']
        except KeyError:
            kwargs['delout'] = False
   

        with open(INF_path) as myfile:  # Open all the lines in the inf path
            lines = myfile.readlines()


        ############################################################################
        # Take the header of the values
        ############################################################################

        n_col = 11                                 # Number of columns that the txt has
        n_var = len(lines)                         # Number of PSCAD Variables
        n_files = int(math.ceil(n_var / 10.0))     # Number of .out Files exported (the floating is important)
        n_var_tot = n_var + n_files                # Number of variables INCLUDING additional time column FOR EACH .OUT
        n_var_last = n_var_tot -(n_files-1)*n_col  # Number of variables in the last file
        n_var_exp = n_var + 1                      # Number of variables that will be exported 

        self.number_var = n_var_exp                

        # This "for" gets the number of columns of every file which will be all 11,
        # but the last, which value can vary

        last_col = [0]*n_files

        for ii in range(0,n_files):     

            if ii != n_files-1:         
                b = n_col
            else:
                b = n_var_last

            last_col[ii] = b

        # last_col = [11, 11, 11, 1]

        pattern = "Desc=\"(.*?)\""  # Patter that holds the variable name
        header1 = [0] * (n_var_exp)  # create a LIST of zeros that will be filled with the variables names later
        self.header  = [0] * (n_var_exp)  

        b = 0  # to "freeze" the time when storing the "TIME"
        c = 1  # used in the index: from 1 to 11

        # "For" Logic: each file can take 11 variables, and the first one is TIME
        # so this for writes time if it is the time column, or takes the header from
        # the array "header"

        for a in range(0, n_var_exp):

            if  a == 0 :                    # if it is the first value of all files, storage the time name
                header1[a] = 'self.time'    # 1 header has the 'self.' in order to create variables to send
                self.header[a] = 'time'     # to the object outside
                b = b - 1
                if a != 0:
                    c = 1
            else:
                header1[a] = 'self.' + re.search(pattern, lines[b]).group(1)  # gets the name of the variable from the line
                header1[a] = header1[a].replace(" ", "_")                     # If the header has spaces, it will be replaced
                self.header[a] = re.search(pattern, lines[b]).group(1)  
                self.header[a] = self.header[a].replace(" ", "_")  
            # print a, self.header[a]     # USE "a+1" for range 1 to numb_variables, "c" for range 1 to 11

            
            b = b + 1
            c = c + 1

        ############################################################################
        # Take all the paths of the .out files
        ############################################################################

        # Create the path of each file so you can open it and read the values
        # The "for" takes off the ending .inf and replace it with "_0NUMBER".out
        
        OUT_name  = [0] * n_files
        OUT_path  = [0] * n_files

        for ii in range(0, n_files):
            if ii < 9:
                OUT_name[ii] = "_0" + str(ii + 1) + ".out"             # Create ending "_0ii".out
                OUT_path[ii] = INF_path.replace(".inf", OUT_name[ii])  # replace in INF_path the.inf for the new end
            else:
                
                OUT_name[ii] = "_" + str(ii + 1) + ".out"             # Create ending "_0ii".out
                OUT_path[ii] = INF_path.replace(".inf", OUT_name[ii])  # replace in INF_path the.inf for the new end


            # print CSV_path[ii]

        # Creates the path of the .CSV that's gonna be writen
        CSV_path = INF_path.replace(".inf", ".csv") # Replaces the ending .inf with .csv

        ############################################################################
        # SAVE header and Variables in one .CSV file
        ############################################################################

        df_csv = pd.DataFrame()    # Create an empty pandas dataframe that will storage all the data from the .outs

        c  = 0    # freezes the header if you skip time
        jj = 0

        for ii in range(0,n_files):  # For each file, read it and storage its columns in the .CSV file

            df = pd.read_csv(OUT_path[ii], delim_whitespace=True, header=None)    # Read the .OUT file and storage it in a pandas data frame
            
            if (jj == 0) or (jj % 11 == 0):                # if it is a multiple of 11, means that it's another file
                jj = 0                                     # so you reset the counter 

            while jj < last_col[ii]:                       # While you are inside the file, save values

                if (jj == 0) and (ii == 0):                # It is the first column of the first file: storage time
                    df_csv[self.header[c]] = df[jj]
                elif (jj == 0) and (ii != 0):              # It is the first column of some other file: don't storage time
                    jj = jj + 1
                    df_csv[self.header[c]] = df[jj]
                    # print 'just skipped time'
                else:
                    df_csv[self.header[c]] = df[jj]        # It is other column: storage column
                
                exec('%s = np.array(%s)' % (header1[c],'df[jj]'))
                # print df_csv.head()
                
                # print c
                c = c + 1
                jj = jj + 1


            if kwargs['delout'] == True:                 # If user wants to delete the .OUT files:
                os.remove(OUT_path[ii])

        ############################################################################
        # Gets the step of simulation - PSCAD
        ############################################################################

        self.step = self.time[1] - self.time[0]

              
        ############################################################################
        # Storage data in a.CSV file with all the variables
        ############################################################################
      
        if (kwargs['writecsv'] == True): 
            
            df_csv.to_csv(CSV_path,index=False)          # Storage all the dataframe into one csv file with header




