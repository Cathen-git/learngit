
inDIR = 'C:\PycharmProjects\scripts_cai\example_data\\form\plant_TIR_my0703.fas'
outDIR = 'C:\PycharmProjects\scripts_cai\example_out\\form\out.fas'
list_1=[]

site = open(inDIR, 'r')
for line1 in site:
    list_1.append(line1.strip())
out = open(outDIR, 'w')
out.write(list_1[0]+'\n')
for j in range(1,len(list_1)):
    if list_1[j][0:1] == '>':
        out.write('\n' + list_1[j] + '\n')
    else:
        out.write(list_1[j])
out.close()




