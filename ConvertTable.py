import pandas as pd
import yaml


# - - - - - - -  - - - - - - -  - - - - - - - METHODS - - - - - - -  - - - - - - -  - - - - - - - 
def csv_to_md(IN, OUT):
    myfilein = ''

    with open(IN, 'r') as reader:
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

    with open(OUT, 'w+') as writer:
        writer.writelines(myfilein)


def pandas_switch(IN, OUT, separator_in="\t", separator_out=","):
    df = pd.read_csv(IN, sep=separator_in)
    df.to_csv(OUT, sep=separator_out)

    
def pandas_to_yaml(IN, OUT, separator=","):
    df = pd.read_csv(IN, sep=separator)
    with open(OUT, 'w') as outfile:
        yaml.dump(
            df.reset_index().to_dict(orient='records'),
            outfile,
            sort_keys=False,
            default_flow_style=None,
        )


# - - - - - - -  - - - - - - -  - - - - - - - RUN - - - - - - -  - - - - - - -  - - - - - - - 

file_path_in = ""
file_path_out = ""

