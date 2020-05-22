import os
list_pro=[]
list_pro_seq=[]
list_out=[]
list_out_seq=[]
inDIR = 'C:\PycharmProjects\scripts_cai\example_data\\form_all'
outDIR = 'C:\PycharmProjects\scripts_cai\example_out\\form_all'
for protein in os.listdir(inDIR):
    pro = inDIR + '\\' +protein
    list_pro.append(pro.strip())
    out_pro =outDIR + '\\' +protein
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
            out.write(list_pro_seq[j])
    out.close()
    list_pro_seq = []


# list_clm=[]
# list_pro_seq=[]
# DIR1 = 'C:\PycharmProjects\project_3_paml\XZ.gene.fas'
# DIR2 = 'C:\PycharmProjects\project_3_paml'
# clm=open(DIR1,'r')
# for line1 in clm:
#     list_clm.append(line1.strip())
# out=open(DIR2+'\\'+'XZ.fas','w')
# out.write(list_clm[0]+'\n')
# for j in range(1,len(list_clm)-1):
#     if list_clm[j][0:1] == '>':
#         out.write('\n' + list_clm[j] + '\n')
#     else:
#         out.write(list_clm[j])
# out.close()


