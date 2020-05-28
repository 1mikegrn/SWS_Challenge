import SWS_Challenge as SWS

def main():
    '''main CLI entry point, parses CLI inputs according to necessary module
    parameters'''
    reader = SWS.src.tools.cmd_reader.reader()

    if len(reader) == 1:
        grid, words, wrap = SWS.src.input_file.parse_input(reader['input_file'])
        grid_class = SWS.src.grid.Grid(grid, wrap)
        word_class = SWS.src.targets.Targets(words)

        SWS.super_word_search.main(grid_class, word_class)

    if len(reader) == 3:
        grid_class = SWS.src.grid.Grid(reader['grid_file'], reader['wrap'])
        word_class = SWS.src.targets.Targets(reader['search_file'])

        SWS.super_word_search.main(grid_class, word_class)
        