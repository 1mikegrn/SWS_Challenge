import numpy as np
from SWS_Challenge.src.tools.interpolate_space import interpolate_space

def build_test_grid(n_rows, n_cols, words_to_hide, output_path, wrap):
    '''build dummy test files'''
    reserved_idx = []
    attempts = 0

    grid_letters = [chr(x) for x in np.random.randint(65,91,size=n_rows*n_cols)]
    grid = np.array(grid_letters).reshape((n_rows, n_cols))

    for word in words_to_hide:
        while attempts < 1000:
            try:
                random_center = np.random.randint((n_rows, n_cols))
                letters = list(word)
                
                bound = find_bound(
                    random_center, 
                    random_direction(), 
                    letters
                )

                idx_vals = interpolate_space(
                    random_center, bound, 
                    len(letters), n_rows, n_cols,
                    wrap
                )

                if len(set(idx_vals)) != len(idx_vals):
                    print('overlap error')
                    raise AssertionError('overlap error')                   

                for idx in idx_vals:
                    if idx is None:
                        print('bounds error')
                        raise AssertionError('bounds error')
                    if idx in reserved_idx:
                        print('reserved index error')
                        raise AssertionError('reserved index error')

                print(
                    'adding '+ word +' between index ' 
                    + str(idx_vals[0]) + ' and ' + str(idx_vals[-1])
                )

                for i, l in enumerate(letters):
                    
                    grid[idx_vals[i]] = l
                    reserved_idx.append(idx_vals[i])

                break

            except:
                if attempts < 1000:
                    attempts += 1

                else:
                    string = ('Runtime Error: Attempts to '
                    +'place word in grid exceeded 1000')

                    print(
                        string
                        )
                        
                    raise RuntimeError(
                        string
                    )

    return grid

def find_bound(ctr, direction, letters):
    return (
        direction[0]*len(letters)+ctr[0], 
        direction[1]*len(letters)+ctr[1]
    )

def random_direction():

    options = [
        (row, col)
        for row in range(-1,+2) 
        for col in range(-1,+2)
        if (row, col) != (0, 0)
    ]

    idx = np.random.randint(len(options))

    return options[idx]