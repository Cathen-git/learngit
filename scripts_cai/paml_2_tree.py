import os
list_ori_tree=[]
list_DIR1=[]
list_DIR2=[]
DIR1 = 'C:\PycharmProjects\scripts_cai\example_data\paml_2_tree'
DIR2 = 'C:\PycharmProjects\scripts_cai\example_out\paml_2_tree'

for ori_tree in os.listdir(DIR1):
    tree = DIR1 + '\\' + ori_tree
    list_DIR1.append(tree.strip())
    paml_tree = DIR2 + '\\' +'paml_'+ori_tree
    list_DIR2.append(paml_tree.strip())
for c in range(len(list_DIR1)):
    out = open(list_DIR2[c], 'w')
    ori_tree = open(list_DIR1[c], 'r')
    for line1 in ori_tree:
        list_ori_tree.append(line1.strip())
    m = list_ori_tree[0].count(',')
    n = 1
    print(m + 1, '\t', n, '\n', file=out)
    p = 0
    k = list_ori_tree[0].count(':')
    j = 0
    for i in range(p, len(list_ori_tree[0])):
        l = str(j)
        if j < 10 and k - j > 1:
            if list_ori_tree[0][i] == ':' and list_ori_tree[0][i - 6] != ')':
                b = list_ori_tree[0].replace(list_ori_tree[0][i:i + 8], '#' + l)
                out.write(b[p:i + 2])
                p = i + 8
                j = j + 1
            if list_ori_tree[0][i] == ':' and list_ori_tree[0][i - 6] == ')':
                b = list_ori_tree[0].replace(list_ori_tree[0][i - 5:i + 8], '#' + l)
                out.write(b[p:i - 3])
                p = i + 8
                j = j + 1
            continue
        if j < 10 and k - j == 1:
            if list_ori_tree[0][i] == ':' and list_ori_tree[0][i - 6] != ')':
                b = list_ori_tree[0].replace(list_ori_tree[0][i:i + 8], '#' + l)
                out.write(b[p:])
            if list_ori_tree[0][i] == ':' and list_ori_tree[0][i - 6] == ')':
                b = list_ori_tree[0].replace(list_ori_tree[0][i - 5:i + 8], '#' + l)
                out.write(b[p:])
            continue
        if j > 9 and k - j > 1:
            if list_ori_tree[0][i] == ':' and list_ori_tree[0][i - 6] != ')':
                b = list_ori_tree[0].replace(list_ori_tree[0][i:i + 8], '#' + l)
                out.write(b[p:i + 3])
                p = i + 8
                j = j + 1
            if list_ori_tree[0][i] == ':' and list_ori_tree[0][i - 6] == ')':
                l = str(j)
                b = list_ori_tree[0].replace(list_ori_tree[0][i - 5:i + 8], '#' + l)
                out.write(b[p:i - 2])
                p = i + 8
                j = j + 1
            continue
        if j > 9 and k - j == 1:
            if list_ori_tree[0][i] == ':' and list_ori_tree[0][i - 6] != ')':
                b = list_ori_tree[0].replace(list_ori_tree[0][i:i + 8], '#' + l)
                out.write(b[p:])
            if list_ori_tree[0][i] == ':' and list_ori_tree[0][i - 6] == ')':
                b = list_ori_tree[0].replace(list_ori_tree[0][i - 5:i + 8], '#' + l)
                out.write(b[p:])
            continue
    out.close()
    list_ori_tree=[]


