from datetime import datetime
import pandas as pd
import yaml
import json


t0 = datetime.now()

# - - - - - - -  - - - - - - -  - - - - - - - METHODS - - - - - - -  - - - - - - -  - - - - - - - 
def csv_to_md(path_in, path_out):
    myfilein = ''

    with open(path_in, 'r') as reader:
        myfilein = reader.readlines()

    count = 0
    for e, line in enumerate(myfilein):
        line = line.replace(',', '|')
        if e == 0:
            count = line.count('|') + 1
            if line[0] == '|':
                line = '-' + line
        myfilein[e] = '|' + line.replace('\n', '|\n')

    headder = '|' + ('---|')*count + '\n'
    myfilein.insert(1, headder)

    with open(path_out, 'w+') as writer:
        writer.writelines(myfilein)


def pandas_switch(path_in, path_out, separator_in="\t", separator_out=","):
    df = pd.read_csv(path_in, sep=separator_in)
    df.to_csv(path_out, sep=separator_out, index=False)

    
def pandas_to_yaml(path_in, path_out, separator=","):
    df = pd.read_csv(path_in, sep=separator)
    with open(path_out, 'w') as outfile:
        yaml.dump(
            df.reset_index().to_dict(orient='records'),
            outfile,
            sort_keys=False,
            default_flow_style=None,
        )


def pandas_to_json(df, path_out):
    data = df.to_dict('index')
    with open(path_out, 'w') as f:
        json.dump(data, f)


# - - - - - - -  - - - - - - -  - - - - - - - RUN - - - - - - -  - - - - - - -  - - - - - - - 

file_path_in = "/home/solarlunix/Documents/Code/PhD/Data/England/barcode.csv"
file_path_out = "/home/solarlunix/Documents/Code/PhD/Data/England/barcode.json"

df = pd.read_csv(file_path_in, index_col='id')
pandas_to_json(df, file_path_out)

# - - - - - - - END - - - - - - -
print("Program Complete:", (datetime.now() - t0))