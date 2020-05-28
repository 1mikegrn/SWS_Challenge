import sys

def reader():
    '''reader which parses CLI arguments'''
    assert len(sys.argv) >= 2, (
        '\n\nExpected CLI input: SWS_Challenge <input_file.txt> '
        +'or SWS_Challenge <grid.txt> <words.txt> <condt>'
    )

    res = dict()

    if len(sys.argv) == 2:
        res['input_file'] = sys.argv[1]

    elif len(sys.argv) == 4:
        res['grid_file'] = sys.argv[1]
        res['search_file'] = sys.argv[2]
        cond = sys.argv[3]
        if cond == 'WRAP':
            res['wrap'] = True
        elif cond == 'NO_WRAP':
            res['wrap'] = False
        else: AssertionError('wrap condition must be WRAP or NO_WRAP')

    return res