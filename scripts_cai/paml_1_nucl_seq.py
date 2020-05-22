import os

list_paml_geno=[]
list_ori_geno=[]
list_DIR1=[]
list_DIR2=[]
DIR1 = 'C:\PycharmProjects\scripts_cai\example_data\paml_1_nucl_seq'
DIR2 = 'C:\PycharmProjects\scripts_cai\example_out\paml_1_nucl_seq'

for ori_geno in os.listdir(DIR1):
    geno = DIR1 + '\\' + ori_geno
    list_DIR1.append(geno.strip())
    paml_geno = DIR2 + '\\' +'paml_'+ori_geno
    list_DIR2.append(paml_geno.strip())

for i in range(len(list_DIR1)) :
    ori_geno = open(list_DIR1[i], 'r')
    for line1 in ori_geno:
        list_ori_geno.append(line1.strip())
    out = open(list_DIR2[i], 'w')
    m = int(len(list_ori_geno) / 2)
    n = len(list_ori_geno[1])
    print(m,'\t',n,'\n', file=out)
    for j in range(len(list_ori_geno)):
        if list_ori_geno[j][0:1]=='>':
            out.write(list_ori_geno[j][1:]+'\n')
        else:
            out.write(list_ori_geno[j]+'\n')
    out.close()
    list_ori_geno = []









