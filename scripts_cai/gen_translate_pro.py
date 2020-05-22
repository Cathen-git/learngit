"""
从Bio导入 4 个模块
Seq 用来创建序列对象
IUPAC用来定义一个序列对象用的生物字符集
SeqRecord 创建一个包含ID,注释，描述等的序列记录对象
SeqIO 提供了方法来读写格式化的序列文件
"""
import os
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
list_geno=[]
inDIR = 'C:\PycharmProjects\scripts_cai\example_data\gen_translate_pro'
outDIR = 'C:\PycharmProjects\scripts_cai\example_out\gen_translate_pro'

for i in os.listdir(inDIR):
    pro_name =outDIR+'\\'+ 'pro_' + i
    geno = open( inDIR+'\\'+i,'r')
    out = open(pro_name,'w')
    for line in geno:
        list_geno.append(line.strip())
    for j in range(len(list_geno)-1):
        if list_geno[j][0:1] == '>':
  #          out.write(list_geno[j]+'\n')
            dna = list_geno[j+1]
            dna = Seq.Seq(dna, IUPAC.unambiguous_dna)
            m_rna = dna.transcribe()
            protein = m_rna.translate()
            protein_record = SeqRecord(protein, id=list_geno[j][1:],description='')
            SeqIO.write(protein_record, out, "fasta")
  #          out.write('\n')
    out.close()
    list_geno=[]

