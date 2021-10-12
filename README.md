# DecoyNinja: Fake Submissions Generator

## Description & Usage
A unique and super-dope tool that can batch-generate genuinely corrupted-seeming PDF files that are all uniquely random in file size & the bytes in them — no two files will ever be of the same size or byte combination, *ever*. These generated PDFs also have genuine PDF file signatures for the more computer-smart testers, and will always show as corrupted or damaged in PDF viewers — ideal for online submissions without any *actual* submission material.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/DecoyNinja-Fake-Submissions-Generator/master/Images/Example.png" >
<p>Example Execution</p>
</div>

Since the generated PDF files are all additionally equipped with genuine *and also* randomized PDF file headers (signatures), even if they are opened using Notepad (or any other text editor) by a slightly computer-smart person than the average lot, the content within each PDF file shall be found to be consistent with that of a typical corrupted/damaged PDF file's attributes.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/DecoyNinja-Fake-Submissions-Generator/master/Images/Notepad%20Example.png" >
<p>Generated PDF opened using Notepad</p>
</div>

*Even* if the PDF files generated by DecoyNinja are signature-tested using general Linux tools by a significantly smarter computer-smart person than the regular Notepad-smart one, the content within each PDF file shall be found to be consistent with that of a typical corrupted/damaged PDF file's attributes.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/DecoyNinja-Fake-Submissions-Generator/master/Images/Signature%20Test.png" >
<p>Generated PDF's signature tested</p>
</div>

This project was created in Python, for the fellow comrades and homies.

## Optimization
Multithreading was implemented in this program to generate all PDF files concurrently instead of sequentially.

## Dependencies to PIP-Install
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
