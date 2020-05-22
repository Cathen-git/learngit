import os

inDIR = 'C:\PycharmProjects\scripts_cai\example_data\paml_find_star'
#inDIR_2 = 'C:\PycharmProjects\project_2_paml\paml_ctrl_1'
list_paml_out=[]
list_paml_seq=[]

for out in os.listdir(inDIR):
    paml_out = inDIR + '\\' + out
    list_paml_out.append(paml_out.strip())
for i in range(len(list_paml_out)):
    p = 0
    paml_seq=open(list_paml_out[i],'r')
    for line in paml_seq:
        list_paml_seq.append(line.strip())
    for j in range(len(list_paml_seq)):
        if list_paml_seq[j][0:21] == 'Bayes Empirical Bayes':
            for k in range(6,20):
                q=list_paml_seq[j + k].count('*')
                p=p+q
    if p>0:
        print(list_paml_out[i][-11:])
    list_paml_seq=[]
