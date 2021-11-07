from utils.fileFunctions import FileFunctions
from components.featurizer import Featurizer

from pprint import pprint


if __name__ == '__main__':

    filename = "D:\\work\\data\\powershell\\PoshCode\\3c9c5d54-adf5-44bb-bf12-ab18d089e443.ps1"

    payload = FileFunctions.read_file_whole(filename)

    features = {
        "raw_length": Featurizer.raw_length(payload),
        "count_lines": Featurizer.count_lines(payload),
        "count_comments": Featurizer.count_comments(payload),
        "count_ticks": Featurizer.count_ticks(payload),
        "count_variables": Featurizer.count_variables(payload),
        "count_booleans": Featurizer.count_booleans(payload),

    }

    print(filename)    
    for k,v in features.items():
        print(k, ":", v)



# TODO
# analyze scripts
# remove comments but count the fact that there were comments and how many lines of 
# break and tokenize

# character frequency by char
# special character frequency by char
# ratio of special char to non-special
# existence of <special> commands and count
# bigram of chars within commandlets
# bigram of commandlets/words
# $variable name bigram
# case sensitive character entropy within commandlets
# longest non-delimited string (excluding "+", `,'+')
# ratio between previous longest and entire script
# variable count