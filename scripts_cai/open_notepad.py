import os

inDIR = 'C:\PycharmProjects\scripts_cai\example_data\open_notepad'
#inDIR = 'C:\PycharmProjects\project_2_paml\paml_ctrl_1'
list_paml_out=[]

for out in os.listdir(inDIR):
    paml_out = inDIR + '\\' + out
    list_paml_out.append(paml_out.strip())
for i in range(len(list_paml_out)):
    com = list_paml_out[i]
    print(com)
    os.system(com)
