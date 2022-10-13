from datetime import datetime
import pandas as pd
import yaml
import json


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


def pandas_to_json(path_in, path_out, separator=","):
    df = pd.read_csv(path_in, sep=separator)
    data = df.to_dict('index')
    with open(path_out, 'w') as f:
        json.dump(data, f)


def write_list(data: list, fname: str, sep: str) -> None:
    with open(fname, "w") as f:
        for item in data:
            for i, part in enumerate(item):
                f.write(f"{sep}{part}") if i>0 else f.write(f"{part}")
            f.write("\n")


# - - - - - - -  - - - - - - -  - - - - - - - RUN - - - - - - -  - - - - - - -  - - - - - - - 
if __name__ == "__main__":
    t0 = datetime.now()

    # - - - - - - - Variables - - - - - - - 
    file_path_in = "/home/solarlunix/Documents/Code/PhD/Data/AFBI/data/metadata.tsv"
    file_path_out = "/home/solarlunix/Documents/Code/PhD/Data/AFBI/data/demux/metadata.yml"

    # - - - - - - - Logic - - - - - - - 
    pandas_to_yaml(file_path_in, file_path_out, '\t')

    # - - - - - - - END - - - - - - -
    print("Program Complete:", (datetime.now() - t0))