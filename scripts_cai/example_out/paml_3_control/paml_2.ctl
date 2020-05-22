seqfile = C:\PycharmProjects\scripts_cai\example_out\paml_2_nucl_seq\paml_geno_2.fas
treefile = C:\PycharmProjects\scripts_cai\example_out\paml_2_tree\paml_2.fasttree
outfile = C:\PycharmProjects\scripts_cai\example_out\paml_codeml_wrapper\paml_2.out

noisy = 9  * 0,1,2,3,9: how much rubbish on the screen
verbose = 1  * 0: concise; 1: detailed, 2: too much
runmode = 0  * 0: user tree

seqtype = 1  * 1:codons; 2:AAs; 3:codons-->AAs
CodonFreq = 0  * 0:1/61 each, 1:F1X4, 2:F3X4, 3:codon table
clock = 0  * 0:no clock, 1:clock; 2:local clock; 3:CombinedAnalysis

* Model C: model = 3  NSsites = 2
* Model D: model = 3  NSsites = 3

model = 0
NSsites = 7 8

icode = 0  * 0:universal code; 1:mammalian mt; 2-10:see below

fix_kappa = 0  * 1: kappa fixed, 0: kappa to be estimated
kappa = 2  * initial or fixed kappa

fix_omega = 0  * 1: omega or omega_1 fixed, 0: estimate
omega = 1  * initial or fixed omega, for codons or codon-based AAs


ncatG = 10  * # of categories in dG of NSsites models

getSE = 0  * 0: don't want them, 1: want S.E.s of estimates
RateAncestor = 0  * (0,1,2): rates (alpha>0) or ancestral states (1 or 2)

Small_Diff = .5e-6
cleandata = 0  * remove sites with ambiguity data (1:yes, 0:no)?
