from os import path
import SWS_Challenge as SWS

def main():
    
    here = path.abspath(path.dirname(__file__))

    data_in = (
        path.join(here, 'grid.txt'),
        path.join(here, 'words.txt'),
        True
    )
    
    grid_class = SWS.src.grid.Grid(data_in[0], data_in[2])
    word_class = SWS.src.targets.Targets(data_in[1])

    SWS.super_word_search.main(grid_class, word_class)

    return 1    

def test_main():
    test = main()
    assert test == 1

if __name__ == "__main__":
    main()