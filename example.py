from os import path
import SWS_challenge as SWS
import time

here = path.abspath(path.dirname(__file__))

def example(data_in):

    if len(data_in) != 3:

        grid, words, wrap = SWS.src.input_file.parse_input(data_in)

        grid_class = SWS.src.grid.Grid(grid, wrap)
        word_class = SWS.src.targets.Targets(words)

        SWS.super_word_search.main(grid_class, word_class)

    else:

        grid_class = SWS.src.grid.Grid(data_in[0], data_in[2])
        word_class = SWS.src.targets.Targets(data_in[1])

        SWS.super_word_search.main(grid_class, word_class)

if __name__ == "__main__":

    data_in = path.join(here, 'input.txt')

    # data_in = (
    #     path.join(here, 'grid.txt'),
    #     path.join(here, 'words.txt'),
    #     True
    # )

    example(data_in)
