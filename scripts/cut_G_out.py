from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import Seq
import argparse 
    
def cut_G_out(oldalignment, newalignment, referencefile, gene='G'):
        list1 = []

        ref = SeqIO.read(referencefile, "genbank")
        for feature in ref.features:
            if feature.type =='gene':
                a =str((list(feature.qualifiers.items())[0])[-1])[2:-2]
                if a == gene:
                    startofgene = int(list(feature.location)[0])
                    endofgene =  int(list(feature.location)[-1])+1
        string_ = 'N'* (endofgene-startofgene)
        oldalignment =SeqIO.parse(oldalignment, 'fasta')
        for entry in oldalignment:
            new_sequence = entry.seq.replace(entry.seq[startofgene:endofgene], string_)
            newrecord = SeqRecord(Seq(new_sequence), id=entry.id, description=entry.description)
            list1.append(newrecord)
            
        SeqIO.write(list1, newalignment, "fasta")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="make new reference depending on whether the entire genome or only part is to be used for the tree",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--oldalignment", required=True, help="fasta input with alignment of entire genome")
    parser.add_argument("--newalignment", required=True, help="fasta output with alignment of relevant part of geome")
    parser.add_argument("--reference", required=True, help="reference genbank file of entire genome")
    args = parser.parse_args()

    cut_G_out(args.oldalignment, args.newalignment, args.reference)
