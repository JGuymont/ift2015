import gzip
from tqdm import tqdm
import pickle
import time
from graph import DeBrujinGraph
from multiprocessing import Pool

FASTA_PATH = './data/GCF_000002985.6_WBcel235_rna.fna.gz'
FASTQ_PATH = './data/reads.fastq.gz'
BED_PATH = './example.bed'

def read_fasta(path):
    with gzip.open(path, 'rt') as f:
        accession, description, seq = None, None, None
        for line in f:
            if line[0] == '>':
                if accession is not None:
                    yield accession, description, seq
                accession, description = line[1:].rstrip().split(maxsplit=1)
                seq = ''
            else:
                seq += line.rstrip()

def read_fastq(path):
    with gzip.open(path, 'rt') as f:
        for line in f:
            seqid, description = line[1:].rstrip().split(maxsplit=1)
            sequence = f.readline().rstrip()
            _ = f.readline()
            quality = f.readline().rstrip()
            yield seqid, description, sequence, quality

def read_bed(path):
    with open(path) as f:
        ref, start, end, name = f.readline().rstrip().split('\t')
        yield ref, int(start) - 1, int(end), name

def save_contigs(contigs, filename):
    fasta = []
    for contig_id, contig in enumerate(contigs): 
        fasta.append('>{} {}'.format('contig{}'.format(contig_id), contig))
    with open(filename, 'w') as f:
        f.write('\n'.join(fasta))

def read_contigs(path):
    """
    Read the contigs created in question 3
    """
    with open(path) as f:
        for line in f:
            ref, contig = line[1:].rstrip().split(maxsplit=1)
            yield ref, contig

#
# Question 3 ----------------------------------------------------------
#

def _get_contig(segment):
    """
    Encode les k-mers de segment dans une instance du
    graphe De Brujin et parcour le graphe pour obtenir 
    le segment contigues
    """
    kmers = DeBrujinGraph.get_kmers(segment)
    graph = DeBrujinGraph(kmers)
    contig = DeBrujinGraph.kmer_walk(graph)
    return contig

def get_contigs(fastq_path=FASTQ_PATH):
    """
    Encode toutes les k-mers des fragments fournis dans le 
    fichier FASTQ dans une instance du graphe De Brujin et 
    parcour tous les graphes pour obtenir les contigs. 
    Appel _get_contig() en parallel pour accelerer le calcul.
    """
    segments = iter([seq[2] for seq in list(read_fastq(fastq_path))])
    with Pool(processes=4) as pool:
        contigs = pool.map(_get_contig, segments)
    return contigs

#
# Question 4 ----------------------------------------------------------
#

def find_match(contig):
    """
    Question 4
    ~~~~~~~~~~
    Compare une contig avec toutes les sequences
    du fichier FASTA et retourne la contig, l'indice 
    ou elle commence, l'indice ou elle termine et la 
    reference FASTA si un match est trouve, sinon
    retourne None.
    """
    for seq in read_fasta(FASTA_PATH):
        contig_ref = contig[0]
        contig_seq = contig[1]
        start = seq[2].find(contig_seq)
        if not start == -1:
            fasta_ref = seq[0]
            end = start + len(contig)
            return '{}\t{}\t{}\t{}'.format(fasta_ref, start, end, contig_ref)
    return None

def get_occurences(contigs):
    """
    Question 4
    ~~~~~~~~~~
    Retourn les occurences des contigs trouves
    a la question 3 dans les sequences originales
    du fichier FASTA
    """
    with Pool(processes=4) as pool:
        occurences = pool.map(find_match, contigs)
    return [occurence for occurence in occurences if occurence]

def save_occurences(occurences):
    with open('occurences.bed', 'w') as f:
        f.write('\n'.join(occurences))

def question_2_3():
    """
    Encoder toutes les k-mers des fragments fournis dans le 
    fichier FASTQ dans une instance du
    graphe De Brujin. Chaque fragment possède l-k+1 k-mers.
    
    Parcourir le graphe pour obtenir des segments contiguës que 
    vous devrez stocker dans un fichier FASTA nommé contigs.fa 
    avec un identifiant unique pour chacun.
    """
    contigs = get_contigs()
    save_contigs(contigs, filename='contigs.fa')

def question4():
    contigs = read_contigs(path='contigs.fa')
    occurences = get_occurences(contigs)
    save_occurences(occurences)

if __name__ == '__main__':
    #question_2_3()
    question4()




    

    

    
