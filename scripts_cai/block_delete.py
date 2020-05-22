import os
list_pro=[]
list_pro_seq=[]
list_out=[]
list_out_seq=[]
inDIR1 = 'C:\PycharmProjects\scripts_cai\example_data\\block_delete'
outDIR2 = 'C:\PycharmProjects\scripts_cai\example_out\\block_delete'
for protein in os.listdir(inDIR1):
    pro = inDIR1 + '\\' +protein
    list_pro.append(pro.strip())
    out_pro =outDIR2 + '\\' +protein
    list_out.append(out_pro.strip())
for i in range(len(list_pro)):
    pro_seq = open(list_pro[i], 'r')
    for line1 in pro_seq:
        list_pro_seq.append(line1.strip())
    out= open(list_out[i],'w')
    out.write(list_pro_seq[0]+'\n')
    for j in range(1,len(list_pro_seq)):
        if list_pro_seq[j][0:1]=='>':
            out.write('\n'+list_pro_seq[j]+'\n')
        else:
            line = list_pro_seq[j].replace(' ','')
            out.write(line)
    out.close()
    list_pro_seq = []
