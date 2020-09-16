# DecoyNinja: The Decoy Submission Generator

## Description & Usage
A super dope tool that takes the following as input:

- Number of assignments you want to decoy
- Number of experiments you want to decoy

...and then outputs .PDF files that are all unique in file size and combination of bytes in them; so no two files will ever be of the same size or byte combination, *ever*. These generated .PDFs will always show as corrupted/damaged in PDF viewers. If the generated .PDFs are opened using the Notepad (or any other text editor) by a slightly smarter person than the average lot, the content within each file shall be found to be consistent with that of a typical corrupted/damaged file's attributes; ideal for online submissions without any *actual* submission material.

This project was created in Python, for the fellow comrades and homies.

## Optimization
Multithreading was implemented in this program to generate the assignments and experiments simultaneously

## Dependencies to PIP-Install
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: http://bit.do/SHUR1KN
