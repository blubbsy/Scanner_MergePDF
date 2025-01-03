# -*- coding: utf-8 -*-
"""
Script Name: MergePDF
Author: Adrian Schiffer
Date: 2025-01-03

Description:
This script provides functionality to merge two PDF files containing front-side and back-side scanned pages of a document.
It ensures that the pages are merged in alternating order and performs basic checks to verify consistency.

Features:
- Opens and reads the specified PDF files.
- Validates that the number of pages in the two files are equal.
- Optionally rotates pages of a specific PDF file.
- Merges the two PDF files in alternating order (front-back-front-back).
- Moves the original input files into a 'archive' folder with the current date added to their filenames.

Dependencies:
- PyPDF2: For reading, manipulating, and writing PDF files.
- datetime: For generating unique filenames based on the current date and time.
- os: For file management operations.

Usage:
Ensure that the PDF files are named and placed in the working directory before running the script.
The script looks for `PRT_FRONT_000975.pdf` and `PRT_BACK_000995.pdf` as default filenames.
"""

from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime
import os
import shutil

class MergePDF:
    """
    A class to handle merging of two PDF files, representing front-side and back-side scanned pages of a document.
    """

    def __init__(self):
        """
        Initialize the MergePDF class, define input and output filenames, and execute merging steps.
        """
        self.odd = 'PRT_FRONT_000975.pdf'  # Front-side scans.
        self.even = 'PRT_BACK_000995.pdf'  # Back-side scans.
        self.merged = f'merged_{datetime.now().strftime("%Y%m%d_%H%M")}.pdf'
        self.archive_folder = 'archive'
        self.open_files()
        self.check_pages()
        if self.check:
            # Uncomment the following line to rotate even pages if needed.
            # self.rotate_pages(target='even', angle=180)
            self.merge_files()
            self.move_files()
            print('Finished successfully.')

    def open_files(self):
        """
        Open and read the specified PDF files, and count their pages.
        """
        self.odd_reader = PdfReader(self.odd)
        self.even_reader = PdfReader(self.even)
        self.odd_pages = len(self.odd_reader.pages)
        self.even_pages = len(self.even_reader.pages)

    def check_pages(self):
        """
        Verify that the number of pages in the front-side and back-side PDF files are equal.
        If not, abort the merging process.
        """
        if self.odd_pages == self.even_pages:
            self.check = True
            print("Odd pages are equal to even pages: executing merge.")
        else:
            self.check = False
            print("Odd pages are not equal to even pages: aborting.")

    def rotate_pages(self, target, angle):
        """
        Rotate pages in the specified document (odd or even) by the given angle.

        Args:
            target (str): 'odd' or 'even', indicating which set of pages to rotate.
            angle (int): The angle to rotate the pages, must be a multiple of 90.
        """
        if target == 'odd':
            for page in self.odd_reader.pages:
                page.rotate(angle)
            print(f"Rotated all odd pages by {angle} degrees.")
        elif target == 'even':
            for page in self.even_reader.pages:
                page.rotate(angle)
            print(f"Rotated all even pages by {angle} degrees.")
        else:
            print("Invalid target specified. Use 'odd' or 'even'.")

    def merge_files(self):
        """
        Merge the front-side and back-side PDF files in alternating order.
        Reverse the order of back-side pages to match the sequence.
        """
        self.merge = PdfWriter()

        # Reverse even pages
        reversed_even_pages = [self.even_reader.pages[i] for i in range(self.even_pages - 1, -1, -1)]

        for x in range(self.odd_pages):
            self.merge.add_page(self.odd_reader.pages[x])
            self.merge.add_page(reversed_even_pages[x])

        with open(self.merged, 'wb') as output_file:
            self.merge.write(output_file)
        print(f'Documents merged successfully into {self.merged}')

    def move_files(self):
        """
        Move the original input PDF files into a 'archive' folder, adding the current date to their filenames.
        """
        if not os.path.exists(self.archive_folder):
            os.makedirs(self.archive_folder)

        current_date = datetime.now().strftime("%Y-%m-%d")
        odd_new_name = os.path.join(self.archive_folder, f"{current_date}_{self.odd}")
        even_new_name = os.path.join(self.archive_folder, f"{current_date}_{self.even}")

        try:
            shutil.move(self.odd, odd_new_name)
            shutil.move(self.even, even_new_name)
            print(f"Moved input files to '{self.archive_folder}' with updated names.")
        except OSError as e:
            print(f"Error while moving files: {e}")

if __name__ == '__main__':
    oMerge = MergePDF()
