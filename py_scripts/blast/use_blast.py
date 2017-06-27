#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
sys.path.insert(0, "/home/nenarokova/ngs/")
from py_scripts.blast.classes.blast import Blast
from py_scripts.bioscripts.best_hits import *
from py_scripts.helpers.parse_csv import *

def blast_many(blast_pairs, custom_outfmt):
    blast_csv_paths = []
    for pair in blast_pairs:
        new_blast = Blast(query_path=pair['query'], db_path=pair['subj_db'], db_type='prot')
        blast_csv_path = new_blast.blast(bl_type='blastp', evalue=10, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=2)
        print blast_csv_path
        blast_csv_paths.append(blast_csv_path)
    for blast_path in blast_csv_paths:
        print blast_path
    return 0

def add_qlen_alen (blast_csv_path, fieldnames):
    blast_hits = csv_to_list_of_dicts(blast_csv_path)[0]
    result = []
    for bh in blast_hits:
        bh['alen_qlen'] = float(bh['length'])/ float(bh['qlen'])
        result.append(bh)
    fieldnames = fieldnames.split(' ')
    write_list_of_dicts(result, blast_csv_path, fieldnames=fieldnames)
    return 0

def add_header(blast_csv_path, custom_outfmt):
    blast_hits = parse_csv(blast_csv_path)
    header = custom_outfmt.split(' ')
    write_list_of_lists(blast_hits, blast_csv_path, header=header)
    return blast_csv_path

query_paths= [
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Blechomonas_ayalai_aa.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Bodo_proteins_18190proteins_17_02_2016.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/E_gracilis_transcriptome_final.PROTEINS.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/jaculum_concatenated_companion_proteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Leptomonas_pyrrhocoris_aa.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Leptomonas_seymouri_plus_short_contigs_aa.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Mbr04_wallacemonas_companion_proteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Naegleria_gruberi_V1.0_protein.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Ndesignis_MMETSP1114_pep.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Novymonas_E262_proteins_Companion.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Paratrypanosoma_all_annotated_AA_final.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Perkinsela_sp_CCAP_1560_proteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Phytomonas_EM1_V1.protein_Steve_Kelly.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Phytomonas_Hart1_V1.protein_Steve_Kelly.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/PNG-M02_Ambiguus_companion_proteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_BayalaiB08-376_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_CfasciculataCfCl_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_EmonterogeiiLV88_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LaethiopicaL147_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LarabicaLEM1108_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LbraziliensisMHOMBR75M2903_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LbraziliensisMHOMBR75M2904_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LdonovaniBPK282A1_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LenriettiiLEM3045_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LgerbilliLEM452_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LinfantumJPCM5_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LmajorFriedlin_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LmajorLV39c5_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LmajorSD75.1_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LmexicanaMHOMGT2001U1103_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LpanamensisMHOMCOL81L13_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LseymouriATCC30220_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LspMARLEM2494_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LtarentolaeParrotTarII_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LtropicaL590_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_LturanicaLEM423_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TbruceigambienseDAL972_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TbruceiLister427_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TbruceiTREU927_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TcongolenseIL3000_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TcruziCLBrener_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TcruziCLBrenerNon-Esmeraldo-like_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TcruziDm28c_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TcruzimarinkelleiB7_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TcruziSylvioX10-1_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TevansiSTIB805_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TgrayiANR4_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TrangeliSC58_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/TriTrypDB-32_TvivaxY486_AnnotatedProteins.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Trypanoplasma_borreli_contigs_20120411_ORF50.fasta",
    "/media/4TB1/blastocrithidia/datasets/all_kinetoplastid_references/Trypanosoma_grayi_V1.protein_Steve_Kelly.fasta"
    ]

custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
subj_paths = [
"/media/4TB1/blastocrithidia/p57_DNA_translated_all_ref_blast/blast_db/p57_DNA_transla.db"
]

for query_path in query_paths:
    for subj_path in subj_paths:
        new_blast = Blast(query_path=query_path,db_path=subj_path, db_type='prot', threads=30)
        blast_csv_path = new_blast.blast(
                                         bl_type='blastp',
                                         evalue=1,
                                         outfmt='comma_values',
                                         custom_outfmt=custom_outfmt,
                                         word_size=3
                                         )
        add_header(best_hits(blast_csv_path), custom_outfmt)
        add_header(blast_csv_path, custom_outfmt)
