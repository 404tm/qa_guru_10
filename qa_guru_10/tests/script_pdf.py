import os.path
import pytest
import pypdf

def test_pdf_file():
    reader = pypdf.PdfReader("extract_dir/Python Testing with Pytest (Brian Okken) (1).pdf")


    print(reader.pages[1].extract_text())
    print(os.path.getsize("extract_dir/Python Testing with Pytest (Brian Okken) (1).pdf"))