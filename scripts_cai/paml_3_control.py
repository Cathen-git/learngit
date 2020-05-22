import os
inDIR = 'C:\PycharmProjects\scripts_cai\example_data\paml_3_control\codeml_site.ctl'
outDIR = 'C:\PycharmProjects\scripts_cai\example_out\paml_3_control'
num = 3

list_site=[]
site=open(inDIR,'r')
for line1 in site:
    list_site.append(line1.strip())
for i in range(1,num+1):
    j=str(i)
    out=open(outDIR + '\\' +'paml_'+j+'.ctl','w')
    p=list_site[0].replace(list_site[0][-5], j)
    out.write(p+'\n')
    p = list_site[1].replace(list_site[1][-10], j)
    out.write(p+'\n')
    p = list_site[2].replace(list_site[2][-5], j)
    out.write(p+'\n')
    for k in range(3,len(list_site)):
        out.write(list_site[k]+'\n')
    out.close()
