
import re

class Featurizer(object):

    @staticmethod
    def raw_length(payload):
        return len(payload)

    @staticmethod
    def count_lines(payload):
        return payload.count('\n')

    @staticmethod
    def count_comments(payload):
        lines = payload.split('\n')
        count = 0
        for line in lines:
            if line.strip(" ").startswith("#"):
                count += 1
        return count

    @staticmethod
    def count_ticks(payload):
        return payload.count("`")

    @staticmethod
    def count_variables(payload):
        return len(re.findall("\$\w+", payload))

    @staticmethod
    def count_booleans(payload):
        count = 0
        count += payload.lower().count("$true")
        count += payload.lower().count("$false")
        return count

    @staticmethod
    def lowercase_alphabet(payload):
        alphabet = {}

        for i in payload.lower():
            if not i in alphabet.keys():
                alphabet[i] = 1
            else:
                alphabet[i] +=1
        return alphabet

    @staticmethod
    def count_words(payload):
        return len(re.findall("\w+", payload))
    
    @staticmethod
    def word_distribution(payload):
        distribution = {}
        m = re.findall("\w+", payload.lower())
        for w in m:
            if w not in distribution.keys():
                distribution[w] = 1
            else:
                distribution[w] += 1
        return distribution

    @staticmethod
    def count_unique_words(payload):
        m = re.findall("\w+", payload.lower())
        return len(set(m))

    @staticmethod
    def longest_string(payload):
        longest = 0
        m = re.findall("\w+", payload.lower())
        for w in m:
            if len(w) > longest:
                longest = len(w)
        return longest