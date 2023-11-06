import re

class preprocesor:

    def __init__(self, input_string):
        while re.search(r'\n( +)?#(.+)?', input_string) != None:
            match = re.search(r'\n( +)?#(.+)?', input_string)
            input_string = input_string.replace(match.group(),'')

        while re.search(r'#(.+)?', input_string) != None:
            match = re.search(r'#(.+)?', input_string)
            input_string = input_string.replace(match.group(),'')

        self.conv = input_string
        print("Comments delated\n")


