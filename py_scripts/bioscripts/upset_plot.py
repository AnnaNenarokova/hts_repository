#!python
import pandas
from upsetplot import plot
from upsetplot import UpSet
from upsetplot import from_indicators
from matplotlib import pyplot

og_counts_path = "/Users/annanenarokova/work/myxo_local/Orthogroups.GeneCount.tsv"

og_counts = pandas.read_csv(og_counts_path, delimiter="\t").convert_dtypes()
og_counts_bin = og_counts.drop(["Orthogroup", "Total"], axis=1).astype(bool)
#species_order = ["Sphaerospora_molnari","Myxidium_liberkuehni","Thelohanellus_kitauei","Henneguya_salminicola","Myxobolus_squamalis","Ceratonova_shasta","Kudoa_iwatai","Tetracapsuloides_bryosalmonae","Polypodium_hydriforme","Hydra_vulgaris","Actinia_tenebrosa","Exaiptasia_pallida","Nematostella_vectensis","Orbicella_faveolata","Pocillopora_damicornis","Stylophora_pistillata","Acropora_millepora","Amphimedon_queenslandica"]
#og_counts_bin = og_counts_bin[species_order]

og_counts_data = from_indicators(og_counts_bin, data=og_counts)
# upset_plot = UpSet(og_counts_data, sort_by="cardinality", sort_categories_by=None, show_counts=True, min_subset_size=300).plot()
upset_plot = UpSet(og_counts_data, sort_by="cardinality", show_counts=True, max_subset_size=30, min_subset_size=20).plot()

pyplot.show()