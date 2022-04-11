import pandas as pd

tsv_file = "/home/solarlunix/Documents/Code/data/PDMice/data/MANIFEST"
csv_file = "/home/solarlunix/Documents/Code/data/PDMice/demultiplexed_seqs/MANIFEST"

item_to_remove = 'demultiplexed_seqs/'

df = pd.read_csv(tsv_file, sep="\t")

#df["filename"] = df["filename"].map(lambda x: x.replace(item_to_remove, ''))

df.to_csv(csv_file)
