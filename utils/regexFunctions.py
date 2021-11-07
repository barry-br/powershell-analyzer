import re

class RegexFunctions(object):

    @staticmethod
    def remove_comments(payload):
        regexp_list = [
            "(\s+#[^\n]+\n)",
            "(#[^\n]+\n)",
            "(#\n)",
        ]
        for r in regexp_list:
            payload = re.sub(r,"", payload)
        return payload