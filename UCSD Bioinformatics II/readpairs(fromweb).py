import collections   
import itertools

in_file = open('dataset_204_14.txt', 'r')

line = 0
in_pkmer=[]
in_skmer=[]
in_kmer={}
bkmer=[]
in_distance = 0
okmer=[]
i=0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    elif (line==0):
        in_distance =int(ldata)
    else:
        ls = ldata.split("|")
        in_kmer[i]=[ls[0],ls[1]]
        i+=1
    line+=1

bkmer=[False]*len(in_kmer)
#print in_kmer
#print bkmer

i=0
pos = len(in_kmer[0][0])-1
#print pos
while(bkmer.count(False)>1):    
    if(not bkmer[i]):
        ikmer = in_kmer[i][0]
        ikmer1 = in_kmer[i][1]
        ek = ikmer[len(ikmer)-pos:len(ikmer)]
        ek1 = ikmer1[len(ikmer1)-pos:len(ikmer1)]
        for j in range(0,len(in_kmer)):
            if(not bkmer[j]):
                jkmer = in_kmer[j][0]
                jkmer1 = in_kmer[j][1]
                sk = jkmer[0:pos]
                sk1 = jkmer1[0:pos]
                if(ek==sk and ek1==sk1):
                    npref =ikmer+jkmer[pos:len(jkmer)]
                    nsuff =in_kmer[i][1]+in_kmer[j][1][pos:len(jkmer)]
                    in_kmer[i][0]=npref
                    in_kmer[i][1]=nsuff
                    bkmer[j]=True
                    i=-1
                    break
    i+=1

output = open('readpairs(fromweb).txt','w')

bpos = bkmer.index(False)
pre = in_kmer[bpos][0]
suf = in_kmer[bpos][1]
res = pre+suf[len(suf)-(pos+1+in_distance):len(suf)]
output.write(res)
output.close()