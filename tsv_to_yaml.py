import pandas as pd
import yaml

tsv_file = "/home/solarlunix/Documents/Code/data/PDMice/metadata.tsv"
yml_file = "/home/solarlunix/Documents/Code/data/PDMice/metadata.yml"

df = pd.read_csv(tsv_file, sep="\t")

with open(yml_file, 'w') as outfile:
    yaml.dump(
        df.reset_index().to_dict(orient='records'),
        outfile,
        sort_keys=False,
        default_flow_style=None,
    )