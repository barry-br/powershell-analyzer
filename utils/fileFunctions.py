
class FileFunctions(object):

    @staticmethod
    def read_file_whole(filename):
        with open(filename, "r") as f:
            payload = f.read()
        return payload
    
    @staticmethod
    def load_file_to_list(filename):
        output = []
        with open(filename, 'r', encoding="utf-8") as f:
            for line in f:
                output.append(line.strip('\n'))
        return output