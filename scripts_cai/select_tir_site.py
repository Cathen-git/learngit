inDIR1 = 'C:\PycharmProjects\scripts_cai\example_data\select_tir_site\li_site.fas'
inDIR2 = 'C:\PycharmProjects\scripts_cai\example_data\select_tir_site\li_seq.fas'
outDIR3 = 'C:\PycharmProjects\scripts_cai\example_out\select_tir_site\out.fas'

list_DIR1=[]
list_DIR2=[]
list_site=[]
list_seq=[]

site = open(inDIR1, 'r')
for line1 in site:
    list_site.append(line1.strip())
seq = open(inDIR2, 'r')
for line2 in seq:
    list_seq.append(line2.strip())
out = open(outDIR3, 'w')
for i in range(len(list_site)):
    for j in range(len(list_seq)):
        if list_seq[j] in list_site[i]:
            out.write(list_seq[j]+'\n')
            m = list_site[i][-11:-5]
            n = list_site[i][-4:]
            p = int(m)
            q = int(n)
            out.write(list_seq[j+1][p-1:q]+'\n')
            break
out.close()



