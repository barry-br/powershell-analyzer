
from os import stat
import re
from collections import Counter

class Featurizer(object):

    @staticmethod
    def length(payload):
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
    def special_characters(payload):
        special_chars = ["`", '"',"'","(",")","[","]","{", "}", "!", "+", "@", "/", "\\", "?", "$", "%", "_", "-", "&", "^", "|", ";", ":"]
        alphabet = {}
        for i in special_chars:
            if not i in alphabet.keys():
                alphabet[i] = 0

        for i in payload.lower():
            if i in special_chars:
                alphabet[i] += 1

        return alphabet

    @staticmethod
    def special_characters_count(payload):
        count = 0
        special_chars = ["`", '"',"'","(",")","[","]","{", "}", "!", "+", "@", "/", "\\", "?", "$", "%", "_", "-", "&", "^", "|", ";", ":"]      
        for i in payload:
            if i in special_chars:
                count += 1
        return count

    @staticmethod
    def count_words(payload, lowercase=True):
        if lowercase:
            payload = payload.lower()
        return len(re.findall("\w+", payload))
    
    @staticmethod
    def word_distribution(payload, lowercase=True):
        if lowercase:
            payload = payload.lower()
        distribution = {}
        m = re.findall("\w+", payload)
        for w in m:
            if w not in distribution.keys():
                distribution[w] = 1
            else:
                distribution[w] += 1
        return distribution

    @staticmethod
    def count_unique_words(payload, lowercase=True):
        if lowercase:
            payload = payload.lower()
        m = re.findall("\w+", payload)
        return len(set(m))

    @staticmethod
    def longest_string(payload, lowercase=True):
        if lowercase:
            payload = payload.lower()
        longest = 0
        m = re.findall("\w+", payload)
        for w in m:
            if len(w) > longest:
                longest = len(w)
        return longest

    @staticmethod
    def bigram_frequencies(payload, lowercase=True):
        if lowercase:
            payload = payload.lower()
        bigrams = Counter(payload[idx : idx + 2] for idx in range(len(payload) - 1))
        return dict(bigrams)