import os
root = 'C:\PycharmProjects\pro_genome\cl_gen_all'
root1 = 'C:\PycharmProjects\pro_genome\single_family'
cluster1_all = os.listdir(root)
cluster1_all_list = []
out_list=[]

for cluster in cluster1_all:
    cluster1 = root+'\\'+cluster
    cluster1_all_list.append(cluster1)
    out_name = cluster
    out_list.append(out_name)
for k in range(len(cluster1_all_list)):
    c1 = open(cluster1_all_list[k], 'r')
    print(cluster1_all_list[k])
    all_lines=c1.read()
    if all_lines.count('>Lcr')<=1 and all_lines.count('>CLaf')<=1 and all_lines.count('>CLam')<=1 and all_lines.count('>CLas')<=1\
            and all_lines.count('>CLso')<=1:
#    if list_c.count('>Lcr')<=1 and list_c.count('>CLaf')<=1 and list_c.count('>CLam')<=1 and list_c.count('>CLas') and list_c.count('>CLso')<=1:
        out = open(out_list[k], 'w')
        out.write(all_lines)
        out.close()



