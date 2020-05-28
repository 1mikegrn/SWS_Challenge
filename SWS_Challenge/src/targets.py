class Targets():
    '''target object for the words passed to module'''
    def __init__(self, data_input):
        if isinstance(data_input, str) is True:
            with open(data_input, 'r') as f:
                data = f.read()
                
            self.words = data.split('\n')

        else:
            self.words = data_input

        for index, word in enumerate(self.words):
            self.words[index] = word.upper()

    def get_words(self):
        return self.words