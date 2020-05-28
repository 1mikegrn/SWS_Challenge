import numpy as np
import SWS_Challenge as SWS

class Grid():
    def __init__(self, data_input, wrap):
        '''the grid object, which is ultimately a numpy array of letters. The
        grid also contains wrap condition as a binary'''
        if isinstance(data_input, str) is True:
            with open(data_input, 'r') as f:
                data = f.read()

            rows = data.split('\n')

            for index, row in enumerate(rows):
                rows[index] = list(row.upper())

            self.letters = np.array(rows)

        else:
            self.letters = np.array(data_input)

        self.wrap = wrap

        self.n_rows = self.letters.shape[0] # pylint: disable=E1136
        self.n_cols = self.letters.shape[1] # pylint: disable=E1136

        # index the letters in a dictionary so we don't have to actually search
        # the grid for initial letters.
        self.dict = dict()

        idx = [(row, col) 
            for row in range(self.n_rows) 
            for col in range(self.n_cols)
        ]

        for i in idx:
            try:
                self.dict[self.letters[i]].append(i)
            except:
                self.dict[self.letters[i]] = []
                self.dict[self.letters[i]].append(i)

    def get_letter(self, idx):
        return self.letters[idx]

    def get_dict(self, letter):
        return self.dict[letter]


                

        

