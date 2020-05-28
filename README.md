# SWS_Challenge

[![Build Status](https://travis-ci.com/1mikegrn/SWS_Challenge.svg?branch=master)](https://travis-ci.com/1mikegrn/SWS_Challenge)
[![DocSite](https://img.shields.io/badge/Docs-Site-blue)](https://1mikegrn.github.io/SWS_Challenge/)

## A Python module for the SuperWordSearch Challenge portion from Karagozian and Case

---

This module is the first of two challenge submissions to be provided on behalf of Michael Green, candidate for employment with Karagozian and Case.

This module accepts from the command line commands of the following structure:

```
SWS_Challenge <input.txt>
```

or

```
SWS_Challenge <grid.txt> <words.txt> <condt>
```

where <input.txt> is the full path to the input file as specified by the challenge instructions. This file should be of format:

```
N M
XXX
XXX
XXX
P
ZZZ
ZZZ
ZZZ
```

where N, M is the dimensionality of the grid of letters in space XXX, and P is the length of the words in space ZZZ.

Alternatively, the grid and words can be provided in separate .txt files, with <grid.txt> for the XXX grid and <words.txt> for the ZZZ words respectively, with the <condt> tag for wrapping appended to the end of the console command as `WRAP` or `NO_WRAP`.