##版本要求

windows: python 3.0 以上
linux: python 2.0

## block_delete.py

功能：批量删除多个文件序列中的空格

注意：需要修改文件夹路径：输入文件夹<inDIR1>，输出文件夹<outDIR2>

## form.py

功能：将原不规范fasta序列文件（一条序列存在空行，多行）转为规范的格式（一条序列只占一行）

注意：需要修改路径：不规范文件<inDIR>，输出规范文件<outDIR>

## form_all.py

功能：批量将多个不规范fasta序列文件（一条序列存在空行，多行）转为规范的格式（一条序列只占一行）

注意：需要修改路径：不规范文件所在的文件夹<inDIR>，输出规范文件所在的文件夹<outDIR>

## gen_translate_pro.py

功能：批量将基因序列转为相应的蛋白质序列

注意：需要修改文件夹路径：输入基因序列文件夹<inDIR1>，输出蛋白质序列文件夹<outDIR2>

## mafft_pro.py

功能：用mafft批量对多序列进行比对

注意：需要在服务器端运行，上传用于多序列比对的（.fas结尾）序列文件到服务器的特定文件夹路径<inDIR>,比对好的文件输出到文件夹路径<outDIR>,具体执行语句如下：

python mafft_wrapper.py <inDIR> <outDIR> .fas --thread aa

## one_pro_gen_select.py

功能：给定一个蛋白序列库文件，一个基因序列库文件，查找指定蛋白序列对应的基因序列文件并输出结果（查找蛋白名字对应的基因名字的序列）

注意：需要修改文件路径：输入的蛋白序列<inDIR1>，输入的基因序列<inDIR1>，输出的基因序列<outDIR>

## open_notepad.py

功能：打开指定文件夹下的所有文件

注意：需要修改文件夹路径：<inDIR>

## paml_1_nucl_seq.py

功能：批量生成符合paml计算格式要求的基因序列文件

注意：需要修改文件夹路径：初始基因序列文件所在文件夹<inDIR>，输出paml格式基因序列的文件夹路径<outDIR>

## paml_2_tree.py

功能：批量生成符合paml计算格式要求的树文件

注意：需要修改文件夹路径：初始树文件所在文件夹<inDIR>，输出paml格式树文件夹路径<outDIR>

## paml_3_control.py

功能：批量生成paml控制文件

注意：
1.需要修改num值（需要生成的控制文件的数量）
2.需要修改初始控制文件路径：<inDIR>（具体格式参考example_data中codeml_site.ctl,特别注意文件的后缀名：.fas，.fasttree，.out）
3.修改输出文件夹路径<outDIR>

## paml_codeml_wrapper.py

功能：codeml批量计算ka/ks

注意：
1.需要在命令行执行（win+R+cmd，切换到脚本所在的路径后，输入下方执行语句）。
2.需要修改文件及文件夹路径：codeml.exe插件所在路径<inDIR1>，控制文件所在文件夹<inDIR2>

具体执行语句如下：

python paml_codeml_wrapper.py

## paml_fasttree_wrapper.py

功能：fasttree批量建树

注意：需要在服务器运行，上传用于建树的（.fas结尾）序列文件到服务器的特定文件夹路径<inDIR>,建好的树文件输出到文件夹路径<outDIR>,具体执行语句如下：

python paml_fasttree_wrapper.py <inDIR> <outDIR> aa

## paml_find_star.py

功能：查找codeml计算结果文件中存在阳性选择位点（存在*）的文件

注意：存在阳性选择位点的文件名直接打印到工作空间，结果不以文档方式输出，需要修改<inDIR>

## pro_translate_geno.py

功能：批量进行蛋白质到核酸序列的转换。（根据Gblock提取的保守蛋白序列在初始蛋白序列中的位置，按照1：3，输出对应位置的基因序列）

注意：
1.需要初始的蛋白质序列，所在的文件夹路径<DIR2>
2.GBLOCK提取出来的保守蛋白序列，所在文件夹的路径<DIR1>
3.初始的基因序列，所在文件夹的路径：<outDIR>
4.基因序列的输出文件夹<DIR4>

## rename.py

功能：对指定文件夹下的所有文件重命名（在每个文件名前加上geno尾部加上.fas）

注意：需要修改文件夹路径：<path>(根据需要修改代码中的命名规则)

## reverse_complement.py

功能：批量对存在提前终止子的基因序列，进行反转互补操作

注意需要修改文件夹路径：
1.存在提前终止密码子的基因序列文件，所在的文件夹<DIR1>
2.用于转换为基因序列的蛋白质序列，所在的文件夹路径<DIR2>
3.反转互补后的基因序列文件，所在的文件夹路径<DIR1_1>

## select_tir_site.py

功能：提取序列中特定位点区间的序列

注意：需要修改文件路径：位点文件<inDIR1>、原序列文件<inDIR2>，和输出文件<outDIR3>，以及位点文件的格式，特别注意包含位点文件中空格的数量（具体格式参照 li_site.fas, li_seq.fas）

## sigle_family.py

功能：筛选出全基因组中的单拷贝基因家族

注意：需要修改文件路径：全基因组序列文件所在的文件夹<root>，输出的单拷贝基因家族所在的文件夹<inDIR2>