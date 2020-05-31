
''' Following script is Removes the Reference section from the inout file for LINNAEUS to work as an preprocessing step   '''
''' Developer Nitin k.chauhan v1.0 ''' 

import os
import sys
import re
import csv
from prettytable import from_csv
from itertools import islice


#inpreprocessing
#removing ref
#merging entire doc into one for correct spans
def preproc():
    foin_complete=open(sys.argv[1],'r')
    foin_without_ref=open("raw.txt",'a')
    #Ref=['References\n','REFERENCES\n','references\n','REFERENCES\n']
    with foin_complete as f:
        data= " ".join(line.strip() for line in f) 

    word=data.split('REFERENCES' or 'References' or 'REFERENCES' or 'references'or'REFERENCES')
    foin_without_ref.write(str(word[0]))

 


#def excution DONE
preproc()




