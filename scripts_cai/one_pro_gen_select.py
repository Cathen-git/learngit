inDIR1 = 'C:\PycharmProjects\scripts_cai\example\cluster120.fas'
inDIR2 = 'C:\PycharmProjects\scripts_cai\example\geno.fas'
outDIR3 = 'C:\PycharmProjects\scripts_cai\example\c1_out.fas'
c1=open(inDIR1,'r')
g1=open(inDIR2,'r')
list_c=[]
list_g=[]
out=open(outDIR3,'w')
for line1 in c1:
    list_c.append(line1.strip())
#i=len(list_c)
for line2 in g1:
    list_g.append(line2.strip())
#j=len(list_g)
for i in range(len(list_c)):
    for j in range(len(list_g)):
        if list_c[i][0:-2] in list_g[j]:
            out.write(list_c[i]+"\n")
            out.write(list_g[j+1]+"\n")
out.close()
