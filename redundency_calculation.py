import os
import glob
import numpy as np
from StringIO import StringIO

in_path = "C:\Users\NormalizedReads\\" ## change file path here
out_path = "C:\Users\AnalyzedData\\"

for file_name in glob.glob(os.path.join(in_path, '*.csv')):

    out_file = open(file_name+"_insertion_site_analysis.csv", "a")
    out_file.write("insertion_site, fold_change\n")
    
    # load data
    my_file = open(file_name, "r")
    data_string = ''
    for line in my_file:
        data_string += line
    my_file.close()
        
    data = np.genfromtxt(StringIO(data_string), skip_header=1, delimiter=",")
    
    #Filter: non-zero value in at least one sample
    index=[]
    for i in range(len(data)):
        if data[i][1]==0 and data[i][2]==0:
            index.append(i)
    
    data = np.delete(data, (index), axis=0)
    
    # zero transformation: if value = 0, set value = min(this.sample)
    DMSO_min = 1
    Drug_min = 1
    
    for i in range(len(data)):
        if (data[i][1]!=0 and DMSO_min > data[i][1]):
            DMSO_min = data[i][1]
    for i in range(len(data)):
        if (data[i][2]!=0 and Drug_min > data[i][2]):
            Drug_min = data[i][2]
    
    for i in range(len(data)):
        if data[i][1]==0:
            data[i][1] = DMSO_min
    
    for i in range(len(data)):
        if data[i][2]==0:
            data[i][2] = Drug_min
    
    #Division: Drug-treated/DMSO-treated 
    data_normalized = data[:, 0:2]
    for i in range(len(data)):
        data_normalized[i][1] = data[i][2]/data[i][1]
    
    #if value < 1, let value = - 1/value
    for i in range(len(data_normalized)):
        if data_normalized[i][1] < 1:
            data_normalized[i][1] = - 1/data_normalized[i][1]
    
    #output insertion_site_analysis 
    #(calculate mean, SD | output items whose value > mean+3*SD or < mean-3*SD)
    insertion_site_mean = np.mean(data_normalized[:,1])
    insertion_site_stDev = np.std(data_normalized[:,1], ddof=1)
    
    for i in range(len(data_normalized)):
        if data_normalized[i][1] > 0 + 3*insertion_site_stDev or data_normalized[i][1] < 0 - 3*insertion_site_stDev:
            out_file.write(str(data_normalized[i][0]) + ',' + str(data_normalized[i][1]) + '\n')
    
    out_file.close()