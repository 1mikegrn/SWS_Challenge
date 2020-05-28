
import SWS_Challenge as SWS

def check_space(grid, ctr, letters):
    '''checks the space in the grid for the set of letters which extend from
    the first letter's center space, through the length of the word. '''
    word_length = len(letters)

    # directions to search
    bounds = [
        (row*word_length+ctr[0], col*word_length+ctr[1]) 
        for row in range(-1,+2) 
        for col in range(-1,+2)
        if (row, col) != (0, 0)
    ]

    # go through all the directions checking the space
    for b in bounds:
        coords = SWS.src.tools.interpolate_space.interpolate_space(
            ctr, b, word_length, 
            grid.n_rows, grid.n_cols, grid.wrap
        )
        
        # check for duplicate coordinates
        if len(set(coords)) == len(coords):
            check_letters = [grid.get_letter(idx) for idx in coords]
            
            # match if letters are the same
            if check_letters == letters:
                return (coords[0], coords[-1])

    else:
        return 'NOT FOUND'