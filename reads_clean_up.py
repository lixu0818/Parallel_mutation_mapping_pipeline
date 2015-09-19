import tkinter.filedialog
from sys import argv

def truncate_fastq():
    


def trim_fastq():
    ''' (file) -> NoneType
    Identify the reads containing the Himar1 ITR sequence, trim the reads to retain the 25bp immediately following the ITR sequence. 
    '''

    from_filename = tkinter.filedialog.askopenfilename()
    to_filename = tkinter.filedialog.asksaveasfilename()
    #stat_filename = tkinter.filedialog.asksaveasfilename()
    
    file = open (from_filename, 'r')
    fileOutput = open (to_filename, 'w')
    fileStatistics = open ('C:/Users/RussellLab/Desktop/Yancheng/Tn-Seq-1-28-15/Tn4_Stats.txt', 'a')

    line1 = 'start'
    total = 0
    match_AGCCAACCTGTTA = 0
    match_0b = 0
    match_1b = 0
    match_4b = 0
    match_5b = 0
    while (line1):
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        line4 = file.readline()
        total += 1

        if levenshtein(line2[16:29],'AGCCAACCTGTTA') < 2:
            fileOutput.write(line1)
            fileOutput.write(line2[29:59]+'\n')
            fileOutput.write(line3)
            fileOutput.write(line4[29:59]+'\n')
            match_AGCCAACCTGTTA +=1
            match_0b += 1
        if levenshtein(line2[17:30],'AGCCAACCTGTTA') < 2:
            fileOutput.write(line1)
            fileOutput.write(line2[30:60]+'\n')
            fileOutput.write(line3)
            fileOutput.write(line4[30:60]+'\n')
            match_AGCCAACCTGTTA +=1
            match_1b += 1
        if levenshtein(line2[20:33],'AGCCAACCTGTTA') < 2:
            fileOutput.write(line1)
            fileOutput.write(line2[33:63]+'\n')
            fileOutput.write(line3)
            fileOutput.write(line4[33:63]+'\n')
            match_AGCCAACCTGTTA +=1
            match_4b += 1
        if levenshtein(line2[21:34],'AGCCAACCTGTTA') < 2:
            fileOutput.write(line1)
            fileOutput.write(line2[34:64]+'\n')
            fileOutput.write(line3)
            fileOutput.write(line4[34:64]+'\n')
            match_AGCCAACCTGTTA +=1
            match_5b += 1
            
    fileStatistics.write('total sequences: ')
    fileStatistics.write(str(total))
    fileStatistics.write(' ')
    fileStatistics.write('match_AGCCAACCTGTTA sequences: ')
    fileStatistics.write(str(match_AGCCAACCTGTTA))
    fileStatistics.write(' ')
    fileStatistics.write('match_0b sequences: ')
    fileStatistics.write(str(match_0b))
    fileStatistics.write(' ')
    fileStatistics.write('match_1b sequences: ')
    fileStatistics.write(str(match_1b))
    fileStatistics.write(' ')
    fileStatistics.write('match_4b sequences: ')
    fileStatistics.write(str(match_4b))
    fileStatistics.write(' ')
    fileStatistics.write('match_5b sequences: ')
    fileStatistics.write(str(match_5b))
    fileStatistics.write('\n')
    file.close()
    fileOutput.close()
    fileStatistics.close()

def head_fastq():
    ''' (file) -> NoneType
    Write the first 200 lines in from_filename into to_filename.
    '''

    #tkinter.filedialog.askopenfilename()
    from_filename = tkinter.filedialog.askopenfilename()
    to_filename = tkinter.filedialog.asksaveasfilename()

    from_file = open(from_filename, 'r')
    head_contents = ''
    for i in range (200):
        head_contents += from_file.readline()
    from_file.close()

    to_file = open(to_filename, 'w')
    to_file.write('first 200 lines:\n\n')
    to_file.write(head_contents)
    to_file.close()

def count_reads():
    ''' (file) -> NoneType
    Count how many reads in a selected .fastq file. 
    '''

    from_filename = tkinter.filedialog.askopenfilename()
    to_filename = tkinter.filedialog.asksaveasfilename()
    
    
    file = open (from_filename, 'r')
    fileOutput = open (to_filename, 'a')
    

    line1 = 'start'
    total = 0
    match_TGTTA = 0
    match_TGTTTA = 0
    while (line1):
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        line4 = file.readline()
        total += 1

    fileOutput.write('total sequences: ')
    fileOutput.write(str(total))
    fileOutput.write('\n')
    file.close()
    fileOutput.close()
    print ("Done")
    
def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]