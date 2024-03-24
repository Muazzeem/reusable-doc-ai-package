import os
import logging
from pikepdf import Pdf
from io import BytesIO


def read_files_content(file_path, extract_page_number):
    """
    Reads the content of a file and returns it as bytes.

    Args:
        extract_page_number:
        file_path (str): The path to the file to be read.

    Returns:
        bytes: The content of the file as bytes.
            For PDF files, if the file has more than one page, it returns the content of the second page.
            For other file types, it reads the entire content of the file.
            Returns None if an error occurs during reading.
    """
    file_extension = os.path.splitext(file_path)[1]
    try:
        if file_extension == '.pdf':
            # Open the PDF file
            pdf = Pdf.open(file_path)

            # Extract content from the second page if available, otherwise from the first page
            """TODO
                Write a code block if this function has no extract_page_number arg it will extract all pages.
            """
            if len(pdf.pages) >= 2:
                content = pdf.pages[extract_page_number]
            elif len(pdf.pages) == 1:
                content = pdf.pages[0]

            # Save the content to an in-memory PDF
            in_mem = BytesIO()
            dst = Pdf.new()
            dst.pages.append(content)
            dst.save(in_mem)

            # Get the content as bytes
            image_content = in_mem.getvalue()
            return image_content
        else:
            # Read content of non-PDF files
            with open(file_path, "rb") as image:
                image_content = image.read()
            return image_content
    except Exception as e:
        # Log the error without saving it to a file
        logging.error(f"Error reading file at {file_path}: {str(e)}")
        return None
