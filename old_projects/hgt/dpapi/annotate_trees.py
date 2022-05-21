#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict
from ete3 import Tree
from Bio import SeqIO

def add_lineages(taxid_dict):
    taxids = list(taxid_dict.keys())

    ncbi_xml_record = Entrez.efetch(db="taxonomy", id=taxids).read()

    ncbi_dict = XML2Dict().parse(ncbi_xml_record)

    taxa_dict_list = ncbi_dict['TaxaSet']['Taxon']

    for taxon in taxa_dict_list:
        taxid = taxon['TaxId'].decode("utf-8")
        name = taxon['ScientificName'].decode("utf-8")
        try:
            lineage = taxon['Lineage'].decode("utf-8")
        except:
            lineage = taxon['Lineage']
        taxid_dict[taxid]["name"] = name
        taxid_dict[taxid]["lineage"] = lineage
    taxid_dict['0']["name"] = "none"
    taxid_dict['0']["lineage"] = "none"
    return taxid_dict

def annotate_ncbi_set(ncbi_set, name_replace_dict):
    ncbi_list = list(ncbi_set)
    handle = Entrez.efetch(db="protein", id=ncbi_list, rettype="gb", retmode="text")
    ncbi_records = SeqIO.parse(handle, 'genbank')
    for ncbi_record in ncbi_records:
        name_replace_dict[ncbi_record.id] = ncbi_record.id + "_" + ncbi_record.description
    return name_replace_dict

def prepare_name_replace_dict(in_treedir):
    ref_species = ["AAHeimHlc2","AAHeimHlc3","AALokiLmir","AAOdinOlcb","AAThorTab2","ADAeniAfil","ADAeniAlan","ADDiapDrev","ADDiapDar1","ADHubeHcry","ADMicrMac2","ADMicrMdke","ADMicrMmia","ADNanoNano","ADNanoNj07","ADNanoNsg9","ADPaceAr13","ADPaceAar1","ADPaceAar6","ADParvPac4","ADParvPac5","ADWoesAr15","ADWoesAr20","ADWoesAar4","ADNaNaNequ","ADNaNaNste","ADNaNaNaci","ADAlAlAcg4","ADAlAlA1fi","ADAlAlA2wo","ADAlAlA1ms","ADAlAlAex4","AEAcDHAboo","AEAgAgAful","AEAgAgAsul","AEHadeHn21","AEHadeHade","AEHaHbNpha","AEHaHbHmar","AEHaHbHsal","AEHaHbHmuk","AEHaHfHvol","AEHaNaNamy","AEHaNaNgre","AEMbMbMbry","AEMbMbMfor","AEMbMbM421","AEMbMbMsub","AEMbMbMmar","AEMbMbMthe","AEMbMbMarb","AEMbMbMcut","AEMbMbMfil","AEMbMbMora","AEMbMbMmil","AEMbMbMrum","AEMbMbMsmI","AEMbMbMcun","AEMbMbMsta","AEMbMbMfer","AEMcMcMjan","AEMcMcMfor","AEMcMcMmar","AEMcMcMthe","AEMmMcMarv","AEMmMcMpal","AEMmMmMpar","AEMmMmMlab","AEMmMmMbou","AEMmMmMhun","AEMmMsMnit","AEMmMsMsoe","AEMmMsMthe","AEMmMsMmet","AEMmMsMmah","AEMmMsMace","AEMmMsMbaF","AEMmMsMbaC","AEMmMsMmaz","AEMmMsMspe","AEMmMsMshe","AEMmMsM138","AEMmMsMa44","AEMmMsScal","AEMmMsANM2","AEMmUnANM1","AEMmMfArc1","AEMnatMthe","AEMpMpMkan","AEMpMpMKOL","AETheiThe1","AETheiThe0","AETcTcPfur","AETcTcPaby","AETcTcPhor","AETcTcTkod","AETpMmMlum","AETpMmMint","AETpMmMter","AETpTpAaeo","AETpTpFacI","AETpTpPtor","AETpTpTvol","AETpTpTSG5","AETpTpTDKE","AETpTpCDKE","AEUnM2Mar2","AEUnM3Mar3","AEUnclMSBL","ATBathMCG1","ATBathMCG6","ATBathMC15","ATBathBat2","ATGeotGoet","ATKoraKcry","ATVeMmMmes","ATVeMmMpet","ATCrAcAsac","ATCrDsAcam","ATCrDsAper","ATCrDsHbut","ATCrDsIagg","ATCrDsIhos","ATCrDsIisl","ATCrDsSmar","ATCrFeFfon","ATCrSuSsol","ATCrTpCmaq","ATCrTpPaer","ATCrTpTpen","ATAigaCsub","ATTaCeCsym","ATTaNpNkor","ATTaNpNmar","ATTaNpNlim","ATTaNpNcat","ATTaNsNgar","ATTaNsNole","ATTaNsNisl","ATTaUnMISR","ATTaUnTarc","ATTaUnTBS4","ATTaUnTFn1","AUUnclMar2","AUUnclMar1","AEMbMbMWGK","BOrpAciHfo","BTerActBan","BTerActRla","BProAlpTmo","BCPRBerBe4","BCPRBerBe5","BCPRBerBe6","BCPRBerBe7","BPVCChlCab","BPVCChlChl","BTerCyaTel","BCPRDojWS2","BOrpFusFnu","BProGamFte","BProGamHru","BProGamLmi","BTerMelMEL","BOrpSpiLbi","BOrpTdeTin","BProAciTte","BOrpAciAc1","BOrpAciAc2","BOrpAciAci","BTerActAkw","BTerActAha","BTerActCar","BTerActEgg","BTerActEma","BTerActGmo","BProAlpAma","BProAlpCit","BProAlpGra","BProAlpKgw","BProAlpPha","BProAlpRho","BOrpAmiAmi","BOrpAquHth","BOrpAquTam","BOrpArmArm","BOrpBacArc","BOrpBacBfr","BOrpBacCma","BOrpBacEte","BOrpBacGal","BOrpBacGra","BOrpBacIal","BOrpBacMsa","BCPRBerBe1","BCPRBerBe2","BCPRBerBe3","BCPRBerBe8","BCPRBerBe9","BProBetBbr","BProBetCte","BProBetDri","BProBetGca","BProBetMet","BFBCChlCth","BTerChlAth","BTerChlChl","BTerChlDeh","BOrpChrCar","BTerCyaAfa","BTerCyaCep","BTerCyaOsc","BTerCyaScy","BOrpDefDac","BTerDeTDge","BProDelBma","BProDelDpo","BProDelMxa","BProDelSac","BCPRDojWS1","BProEpsLeb","BTerFirBan","BTerFirFal","BTerFirFfr","BTerFirMha","BTerFirOma","BTerFirSmu","BTerFirVpa","BTerFirYfr","BProGamAil","BProGamAsu","BProGamAaq","BProGamAna","BProGamMmo","BProGamPpr","BProGamSim","BFBCGemGem","BOrpGraGra","BFBCIgnIgn","BCPRKazKa1","BCPRKazKa2","BPVCLenLen","BTerMelMe1","BCPRMicAme","BCPRMicBec","BCPRMicCol","BCPRMicCur","BCPRMicDav","BCPRMicGot","BCPRMicLev","BCPRMicPac","BCPRMicRoi","BCPRMicSha","BCPRMicWe1","BCPRMicWe2","BCPRMicWy1","BCPRMicWy2","BCPRMicWy3","BCPRMicMic","BOrpModVgr","BOrpNitNsn","BOrpNitNde","BOrpNitNsr","BPVCOmnOmn","BCPRParFal","BCPRParGio","BCPRParJo1","BCPRParJo2","BCPRParKai","BCPRParMa1","BCPRParMa2","BCPRParMo1","BCPRParMo2","BCPRParNo1","BCPRParNo2","BCPRParUh1","BCPRParUh2","BCPRParUh3","BCPRParWol","BCPRParYan","BCPRParPar","BCPRPerPe1","BCPRPerPe2","BPVCPlaPla","BPVCPlaPhy","BCPRSacSa1","BCPRSacSa2","BOrpSpiBmu","BOrpSynTac","BTerTenMfl","BOrpTtoKol","BOrpWirWir","BCPRWWEWWE","BProZetMfe","BFBCZixZix","EAbAcastgm","EAbAcastgn","EAbDdiscgm","EAbDdiscgn","EAbEdispgn","EAbPpolytm","EAbPpolytn","EApAmasptn","EApTtrahgn","EAvAcarttn","EAvNscintn","EAvOtrifgn","EAvPglactn","EAvPretign","EAvPtetrgn","EAvScoergn","EAvSlemngn","EAvTjolltn","EAvTthergn","EAyAsigmtn","EAyFtroptn","EAyNlongtn","EChAcasptn","EChChosptn","EChRerintn","EChRhetetn","ECRDrotatm","ECRDrotatn","ECRMplastn","ECRRramotn","ECyCrypsgn","ECyGavontn","ECyGthetgc","ECyGthetgn","EEFApalutn","EEFCcusptn","EEFCmembtn","EEFDbrevtn","EEFEcyprtn","EEFKbialtn","EEFTrepotn","EEHNgrubgm","EEHNgrubgn","EEJSincatn","EEKBsaltgn","EEPTmaritn","EHmHkukwtn","EHmSmulttn","EHpChrspgn","EHpEhuxlgc","EHpEhuxlgm","EHpEhuxlgn","EMwGokeltn","EOCMbrevgm","EOCMbrevgn","EOCSrosegn","EOFAmacrgm","EOFAmacrgn","EOFLtrangn","EOFSpombgm","EOFSpombgn","EOFSpuncgm","EOFSpuncgn","EOMAqueegm","EOMAqueegn","EOMLgigagn","EOMLpolygm","EOMLpolygn","EOMNvectgn","EOMXtropgm","EOMXtropgn","EONPaltagn","EOrAtwistm","EOrAtwistn","EOYFalbagn","EPCAprotgc","EPCAprotgm","EPCAprotgn","EPCBprasgc","EPCBprasgm","EPCBprasgn","EPCCreingc","EPCCreingm","EPCCreingn","EPCMneglgc","EPCMneglgm","EPCMneglgn","EPCMpusign","EPCOtaurgc","EPCOtaurgm","EPCOtaurgn","EPCTselmgn","EPCVcartgn","EPGCparagc","EPGCparagm","EPGCparagn","EPRCcrisgc","EPRCcrisgm","EPRCcrisgn","EPRCmerogc","EPRCmerogm","EPRCmerogn","EPRGsulpgc","EPRGsulpgm","EPRGsulpgn","EPRPumbigc","EPRPumbigm","EPRPumbign","EPSAthalgc","EPSAthalgm","EPSAthalgn","EPSKnitegc","EPSKnitegm","EPSKnitegn","EPSOsatigc","EPSOsatigm","EPSOsatign","EPSPpategc","EPSPpategm","EPSPpategn","EPSSmoelgc","EPSSmoelgn","ERzBnatagc","ERzBnatagm","ERzBnatagn","ERzEmarggn","ERzRfilogn","ESmAanopgc","ESmAanopgn","ESmBpacitn","ESmEsiligc","ESmEsiligm","ESmEsilign","ESmFcylign","ESmFsolagc","ESmFsolagm","ESmFsolagn","ESmLdanitc","ESmLdanitn","ESmNgadigc","ESmNgadigm","ESmNgadign","ESmNitzstn","ESmOauritn","ESmPtricgc","ESmPtricgm","ESmPtricgn","ESmTclavgm","ESmTclavgn","ESmToceagc","ESmToceagn","ESmTpseugc","ESmTpseugm","ESmTpseugn","EteTspP1tn","EteTspP2tn","EteTsubttn","EEDDpapign","EEEEgractn","EEDHphaetn","EEDRhumrtn","EEDSspectn","EEEEgracgc","EEEEgracgm","EEEEgymntn","EEERcosttn","EEKAhoyatn","EEKLmajogn","EEKLpyrrgn","EEKNdesitn","EEKPconfgn","EEKPerkign","EEKProk4tn","EEKProk6tn","EEKTborrtn","EEKTbrucgn","EEKTgraign"]
    ncbi_set = set()
    name_replace_dict = {}
    for tree_file in listdir_nohidden(in_treedir):
        tree_path = in_treedir + tree_file
        tree = Tree(tree_path)
        for leaf in tree.iter_leaves():
            leaf_name = leaf.name
            if leaf_name.split("_")[0] in ref_species:
                name_replace_dict[leaf_name] = leaf_name
            else:
                ncbi_set.add(leaf_name)
    print ("annotating ncbi leaves")
    name_replace_dict = annotate_ncbi_set(ncbi_set, name_replace_dict)
    return name_replace_dict

def annotate_result_tree(tree, name_replace_dict):
    for leaf in tree.iter_leaves():
        leaf.name = name_replace_dict[leaf.name]
    return tree

def annotate_result_trees(in_treedir, out_treedir):
    print ("preparing name_replace_dict")
    name_replace_dict = prepare_name_replace_dict(in_treedir)
    print ("annotating trees")
    for tree_file in listdir_nohidden(in_treedir):
        tree_path = in_treedir + tree_file 
        tree = Tree(tree_path)   
        new_tree = annotate_result_tree(tree, name_replace_dict)
        new_tree_path = out_treedir + tree_file
        tree.write(format=2, outfile=new_tree_path)
    return out_treedir

in_treedir = "/Users/anna/work/dpapi_local/trees/hgt_trees/"
out_treedir = "/Users/anna/work/dpapi_local/trees/hgt_trees_renamed/"

annotate_result_trees(in_treedir, out_treedir)