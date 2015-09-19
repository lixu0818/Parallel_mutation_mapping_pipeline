import os
import glob
import numpy as np
from StringIO import StringIO

in_path = "C:\Users\FoldChange\\" ## change file path here
out_path = "C:\Users\GeneMap\\"

for file_name in glob.glob(os.path.join(in_path, '*.csv')):
    out_file = open(file_name+"_gene_analysis.csv", "a")
    out_file.write("Identifier, Gene, gene_length, FC, normalized FC, description\n")
    
    # load data
    my_file = open(file_name, "r")
    data_string = ''
    for line in my_file:
        data_string += line
    my_file.close()
            
    data = np.genfromtxt(StringIO(data_string), skip_header=1, delimiter=",")
    
    # load gene map
    my_file2 = open(out_path+"CDC_genome_map.csv", "r")
          
    gene_map = np.genfromtxt(my_file2, skip_header=1, delimiter=",", dtype=None)
    
    # map insertion site to gene
    count=gene_map.copy()
    
    for i in range(len(count)):
        count[i][2] = gene_map[i][3]-gene_map[i][2] + 1
        count[i][3] = 0
    
    for i in range(len(gene_map)):
        for j in range(len(data)):
            if data[j][0]>=gene_map[i][2] and data[j][0]<=gene_map[i][3]:
                count[i][3] += data[j][1]
    
    for i in range(len(count)):
        out_file.write(str(count[i][0])+','+str(count[i][1])+\
        ','+str(count[i][2])+','+str(count[i][3])+\
        ','+str(count[i][3]*1000.0/count[i][2])+','+count[i][4]+'\n')
    
    out_file.close()
    my_file2.close()