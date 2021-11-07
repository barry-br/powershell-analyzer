
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