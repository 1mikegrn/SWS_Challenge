from os import path
import SWS_Challenge as SWS

def build():

    differentiate = False

    here = path.abspath(path.dirname(__file__))

    search_words = [
        'hello', 'sedona', 'california', 'goodbye', 'texas', 
        'supercalifragilisticexpialidocious'
    ]

    dummy_words = ['washington']

    if differentiate == True:
        search_words = [x.lower() for x in search_words]
        dummy_words = [x.lower() for x in dummy_words]

    else:
        search_words = [x.upper() for x in search_words]
        dummy_words = [x.upper() for x in dummy_words]

    grid = SWS.src.tools.build_test_grid.build_test_grid(
        23, 27,
        search_words,
        here,
        wrap=True
    )

    with open(path.join(here, 'grid.txt'), 'w') as w:
        lines = [''.join(row) for row in grid] 
        w.writelines(
            [x+'\n' if x != lines[-1] else x
            for x in lines]
        )

    with open(path.join(here, 'words.txt'), 'w') as w:
        lines = search_words + dummy_words
        w.writelines(
            [x+'\n' if x != lines[-1] else x 
            for x in lines]
        )

if __name__ == "__main__":
    build()