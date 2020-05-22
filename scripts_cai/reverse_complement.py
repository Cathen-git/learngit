import os
list_protein=[]
list_genome=[]
list_re_genome=[]
list_pro_seq=[]
list_geno_seq=[]
a = ''
DIR1 = 'C:\PycharmProjects\pro_genome\geno1'
DIR2 = 'C:\PycharmProjects\pro_genome\pro1'
DIR1_1 = 'C:\PycharmProjects\pro_genome\geno_re'
for protein in os.listdir(DIR2):
    pro = DIR2 + '\\' +protein
    list_protein.append(pro.strip())
for genome in os.listdir(DIR1):
    geno = DIR1 + '\\' +genome
    list_genome.append(geno.strip())
    re = DIR1_1 + '\\' +'re_'+genome
    list_re_genome.append(re.strip())
for i in range(len(list_protein)):
    pro_seq = open(list_protein[i],'r')
    for line1 in pro_seq:
        list_pro_seq.append(line1.strip())
    geno_seq = open(list_genome[i],'r')
    for line2 in geno_seq:
        list_geno_seq.append(line2.strip())
    out = open(list_re_genome[i],'w')
    for k in range(0,len(list_geno_seq),2):
        out.write(list_geno_seq[k] + '\n')
        for j in range(len(list_pro_seq)-1):
            if list_geno_seq[k] in list_pro_seq[j]:
                if list_pro_seq[j + 1][0:-1].count('*') > 0 or list_pro_seq[j + 2][0:-1].count('*') > 0:
    #                out.write(list_geno_seq[k] + '\n')
                    b = list_geno_seq[k+1]
                    b = b.replace('A', '{A}').replace('T', '{T}').replace('C', '{C}').replace('G', '{G}')
                    a = b.format(A='T', T='A', C='G', G='C')[::-1]
                    out.write(a + "\n")
                else :
                    out.write(list_geno_seq[k + 1] + "\n")
        #out.write(a + "\n")
    out.close()
    list_geno_seq=[]
    list_pro_seq=[]
