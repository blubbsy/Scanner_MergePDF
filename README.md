# Scanner_MergePDF
My scanner cant scan both sides at once, so this script merges the front and back sides from two PDFs into one.both sides at once, i 


## Description:
This script provides functionality to merge two PDF files containing front-side and back-side scanned pages of a document.
It ensures that the pages are merged in alternating order and performs basic checks to verify consistency.

## Features:
- Opens and reads the specified PDF files.
- Validates that the number of pages in the two files are equal.
- Optionally rotates pages of a specific PDF file.
- Merges the two PDF files in alternating order (front-back-front-back).
- Moves the original input files into a 'archive' folder with the current date added to their filenames.

## Dependencies:
- PyPDF2: For reading, manipulating, and writing PDF files.
- datetime: For generating unique filenames based on the current date and time.
- os: For file management operations.

## Usage:
Ensure that the PDF files are named and placed in the working directory before running the script.
The script looks for `PRT_FRONT_000975.pdf` and `PRT_BACK_000995.pdf` as default filenames.
