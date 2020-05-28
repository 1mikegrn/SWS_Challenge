
def parse_input(file_name):
    '''parse input in accordance to the challenge parameters. Accepts a single
    input file and partitions data to a len(3) tuple for the grid, words, and 
    wrap argument.'''
    with open(file_name, 'r') as f:
        data = f.read()

    rows = data.split('\n')    
    
    n_rows, n_cols = (int(x) for x in rows[0].split(' '))

    grid = []
    for index in range(1, n_rows + 1):
        grid.append(list(rows[index].upper()))

    if rows[n_rows+1] == 'NO_WRAP':
        wrap = False
    else:
        wrap = True

    words = []
    for index in range(n_rows+3, len(rows)):
        words.append(rows[index])

    return grid, words, wrap