import os

list_gblock_pro=[]
list_ori_pro=[]
list_ori_geno=[]
list_DIR1=[]
list_DIR2=[]
list_DIR3=[]
list_DIR4=[]

DIR1 = 'C:\PycharmProjects\scripts_cai\example_data\pro_translate_geno\gb_pro'
DIR2 = 'C:\PycharmProjects\scripts_cai\example_data\pro_translate_geno\ori_pro'
DIR3 = 'C:\PycharmProjects\scripts_cai\example_data\pro_translate_geno\ori_geno'
DIR4 = 'C:\PycharmProjects\scripts_cai\example_out\pro_translate_geno'

for gblock_pro in os.listdir(DIR1):
    pro = DIR1 + '\\' +gblock_pro
    list_DIR1.append(pro.strip())
for ori_pro in os.listdir(DIR2):
    pro = DIR2 + '\\' +ori_pro
    list_DIR2.append(pro.strip())
for ori_geno in os.listdir(DIR3):
    geno = DIR3 + '\\' +ori_geno
    list_DIR3.append(geno.strip())
    re=DIR4 + '\\' +'pro_re_geno_'+ori_geno[7:]
    list_DIR4.append(re.strip())

for l in range(len(list_DIR3)) :
    gblock_pro = open(list_DIR1[l], 'r')
    for line1 in gblock_pro:
        list_gblock_pro.append(line1.strip())
    ori_pro = open(list_DIR2[l], 'r')
    for line2 in ori_pro:
        list_ori_pro.append(line2.strip())
    ori_geno = open(list_DIR3[l], 'r')
    for line3 in ori_geno:
        list_ori_geno.append(line3.strip())
    out = open(list_DIR4[l], 'w')
    for i in range(len(list_gblock_pro)):
        if list_gblock_pro[i][0:1] != '>':
            for j in range(len(list_ori_pro)):
                if list_gblock_pro[i - 1] in list_ori_pro[j]:
                    for k in range(0, len(list_ori_geno)):
                        if list_ori_geno[k] in list_ori_pro[j]:
                            if k == 0:
                                out.write(list_ori_geno[0] + '\n')
                            else:
                                out.write('\n' + list_ori_geno[k] + '\n')
                            p = 0
                            for q in range(len(list_gblock_pro[i]), p + 2, -1):
                                if list_gblock_pro[i][p:q] in list_ori_pro[j + 1]:
                                    pp = list_ori_pro[j + 1].find(list_gblock_pro[i][p:q])
                                    qq = pp + q - p
                                    out.write(list_ori_geno[k + 1][3 * pp:3 * qq])
                                    def re(q):
                                        if q < len(list_gblock_pro[i]):
                                            p = q
                                            for q in range(len(list_gblock_pro[i]), p + 2, -1):
                                                if list_gblock_pro[i][p:q] in list_ori_pro[j + 1]:
                                                    pp = list_ori_pro[j + 1].find(list_gblock_pro[i][p:q])
                                                    qq = pp + q - p
                                                    out.write(list_ori_geno[k + 1][3 * pp:3 * qq])
                                                    break
                                            re(q)
                                    re(q)
                                    break
    out.close()
    list_gblock_pro = []
    list_ori_pro = []
    list_ori_geno = []









