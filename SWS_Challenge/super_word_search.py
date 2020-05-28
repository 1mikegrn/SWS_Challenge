import SWS_Challenge as SWS
from os import path

here = path.abspath(path.dirname(__file__))

def main(grid_class, word_class):
    '''main function, brings everything together'''
    for word in word_class.get_words():
        res = find_word(word, grid_class)
        print_result(word, res)

        
def find_word(word, grid_class):
    '''handle word finding in check_space, parse response'''
    letters = list(word)

    matching_first_letter = grid_class.get_dict(letters[0])

    for spot in matching_first_letter:
        check = SWS.check_space.check_space(grid_class, spot, letters)

        if isinstance(check, str) is True: pass
        else: return check

    return 'NOT FOUND'

def print_result(word, res):
    if isinstance(res, str) is True:
        print(
            'the word {} was not found in the grid'.format(word)
        )
    else:
        print(
            'the word {} was found between the coordinates '.format(word) 
            + str(res[0]) + ' and ' + str(res[1])
        )