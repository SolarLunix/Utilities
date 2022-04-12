import pandas as pd
import yaml


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


# - - - - - - -  - - - - - - -  - - - - - - - RUN - - - - - - -  - - - - - - -  - - - - - - - 

file_path_in = "/home/solarlunix/Documents/test.csv"
file_path_out = "/home/solarlunix/Documents/test.tsv"

pandas_switch(file_path_in, file_path_out, separator_in=",", separator_out='\t')

