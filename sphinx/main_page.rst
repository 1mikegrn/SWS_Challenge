This site is a docstring repository for the Super Word Search 
Challenge, written by Michael Green in part for a technical challenge submission 
to Karagozian and Case.

Use the tabs on the left-hand side of the page to navigate to the
various document sections.

**Connect:**

Michael Green
`@Website <https://1mikegrn.github.io>`_
`@Github <https://github.com/1mikegrn>`_
`@StackOverflow <https://stackoverflow.com/users/10881573/michael-green?tab=profile>`_

Getting Started
===============

From the command prompt, the latest version this library can be installed 
via pip and git.

:code:`pip install git+https://github.com/1mikegrn/SWS_Challenge`

Where the setup file will automatically check dependencies and install
to the main module library. Once installed, calling
:code:`SWS_Challenge <input.txt>` or
:code:`SWS_Challenge <grid.txt> <words.txt> <condt>` from the command prompt 
will execute the calculation.

The :code:`<input.txt>` file should be the full path to the input file as 
specified by the challenge instructions. This file should be of format:


::

    N M
    XXX
    XXX
    XXX
    P
    ZZZ
    ZZZ
    ZZZ


where :code:`N M` is N-row M-column dimensionality of the grid of letters in 
space `XXX`, and P is the length of the words in space `ZZZ`.

Alternatively, the grid and words can be provided in separate .txt files, with
:code:`<grid.txt>` for the `XXX` grid and :code:`<words.txt>` for the `ZZZ` 
words respectively, with the :code:`<condt>` tag for wrapping appended to the 
end of the console command as :code:`WRAP` or :code:`NO_WRAP`

Library Structure
=================

::

    SWS_Challenge/
        __init__.py                         # initialize SWS_Challenge
        __main__.py                         # CLI access point
        check_space.py                      # checks space b/t ctr and bounds
        super_word_search.py                # handles CLI to module interaction
        src/                                # source module
            __init__.py                     # initialize src                    
            grid.py                         # grid class
            targets.py                      # target words class
            input_file.py                   # parse CLI input
            tools/                          # tools module
                __init__py                  # initialize tools
                cmd_reader.py               # CLI reader
                build_test_grid.py          # script to build test grids
                interpolate_space.py        # interpolate grid space
