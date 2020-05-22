import os

inDIR1 = 'C:\PycharmProjects\scripts_cai\example_data\paml_codeml_wrapper\codeml.exe'
inDIR2 = 'C:\PycharmProjects\scripts_cai\example_out\paml_3_control'
list_paml_ctrl=[]

for ctrl in os.listdir(inDIR2):
    paml_ctrl = inDIR2 + '\\' + ctrl
    list_paml_ctrl.append(paml_ctrl.strip())
for i in range(len(list_paml_ctrl)):
    com = inDIR1 + " " + list_paml_ctrl[i]
    print(com)
    os.system(com)

#os.system('notepad')