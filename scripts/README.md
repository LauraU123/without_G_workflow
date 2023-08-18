

### cut.py

This code cuts out G or other specified genes from an aligned fasta of sequences. Input: aligned fasta and reference for CDS locations


### align_for_tree.py

This code replaces the G gene from a full genome fasta with an MSA realigned G gene.

### glycosylation.py

This script finds N-linked glycosylation motifs in glycosylated genes and adds the motif number to the annotated json tree file.

### cut_g_out.py

This script does the reverse of cut.py - instead of keeping G as output, it replaces the G gene with unknown sequences ("NNNNN...") 

### newreference.py

This script writes a genbank and fasta reference file based on the input full genome reference for a specific gene (G or F for example).
