def interpolate_space(ctr, bound, word_length, n_rows, n_cols, wrap):
    '''interpolates space from center node to bounding node. returns the list of
    index values which are between the center node and the bound node.'''
    res = dict()
    for idx in range(len(ctr)):
        # if indexes are horizontal/vertical
        if ctr[idx] == bound[idx]:
            res[idx] = [ctr[idx] for x in range(word_length)]

        # if indexes are diagonal
        else:
            if ctr[idx] < bound[idx]:
                res[idx] = [x for x in range(ctr[idx], bound[idx])]
            else:
                res[idx] = [x for x in range(ctr[idx], bound[idx], -1)]

    # use modular math to wrap around the edge of the grid.
    if wrap == True:
        spots = [
            (x%n_rows, y%n_cols) 
            for (x,y) in zip(res[0], res[1])
        ]

    # if wrap is false, then return None when interpolation extends over the
    # edge of the grid. 
    else:
        spots = [
            (x, y) if (n_rows > x >= 0 and n_cols > y >= 0) else None 
            for (x, y) in zip(res[0], res[1])
        ]

    return spots