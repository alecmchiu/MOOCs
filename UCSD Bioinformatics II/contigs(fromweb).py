import collections   
import itertools

in_file = open('dataset_205_5.txt', 'r')

line = 0
in_kmer=[]
bkmer=[]
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    else:
        in_kmer.append(ldata)
    line+=1

bkmer=[False]*len(in_kmer)
nkmer=[]
pos = len(in_kmer[0])-1
inout=[]
for i,im in enumerate(in_kmer):
    sim = im[0:pos]
    eim = im[len(im)-pos:len(im)]
    ii = 0
    io = 0
    for j,jm in enumerate(in_kmer):
        sjm = jm[0:pos]
        ejm = jm[len(jm)-pos:len(jm)]
        if(sim==sjm):
            ii+=1
        if(sim==ejm):
            io+=1
    if(ii==1 and io==1):
        inout.append(im)
    else:
        if(not bkmer[i]):
            bkmer[i]=True
            nkmer.append(im)

i=0
while(len(inout)>0):
    iv=inout[i]
    liv = iv[0:pos]
    #print iv, liv
    for x in nkmer:
        if liv in x:
            nkmer.append(x+iv[pos:len(iv)])
            nkmer.remove(x)
            inout.remove(iv)
            i=-1
            break
    i+=1
        
output = open('contigweb.txt','w')
    
for i,im in enumerate(sorted(nkmer)):
    output.write(im)
    output.write('\n')

output.close()