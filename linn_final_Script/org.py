
''' Following script is Generated the LINNAEUS output and append int into TSV file '''
''' Developer Nitin k.chauhan v1.0 ''' 




import os
import sys
import re
import csv
from prettytable import from_csv
from itertools import islice


def single_run():
    get_name=str(sys.argv[1]).split('/')
    return((get_name[-1]))

def batch_run():
	get_name=str(sys.argv[1])
	return(batch_run)

def org(files_in,out):
    os.system("java -jar ./linnaeus/bin/linnaeus-2.0.jar --textDir "+str(files_in)+" --automatons --default --out "+str(out)+"_out_org ")#>/dev/null 2>&1


#filein=os.getcwd()+"/"+str(filename())+"_raw.txt"
#filein=sys.argv[1]

sample=str('4000') #outfilenames
org(sys.argv[1],sample)

output = []
output_file=open('sql_append.tsv','w')
with open(str(sample)+'_out_org','r') as foin:
	for line in islice(foin, 1, sys.maxsize):	
		word=line.split()
		start=float(word[2])-150
		end=float(word[3])+150
		filename=(str(sys.argv[1])+'/'+str(word[1])+'.txt')
		with open(str(filename), 'r') as file:
			data = file.read()
			context=str((data[int(start):int(end)])).rstrip()
			#output.append([word[0],word[1],word[2],word[3],word[4],context])
                        output_file.write(str(line)+'\t'+str(context)+'\n')
#with open('raw.tsv', 'w', newline='') as f:
#    headers = ['entity', 'document','start','end','text','context']
#    writer = csv.writer(f, delimiter='\t')
#    writer.writerow(headers)
#    writer.writerows(output)


fp = open("raw.tsv", "r")
fout=open('final_'+str(sample),'w')
t= from_csv(fp)
t.align='l'
t.border=True
fout.write(str(t))
fp.close()
os.system('rm raw.tsv')




