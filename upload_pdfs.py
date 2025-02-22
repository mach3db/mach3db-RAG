from phi.document.reader.pdf import PDFReader
from typing import List
from phi.document import Document
from assistant import get_rag_assistant
import os
import glob

rag_assistant = get_rag_assistant(model='exaone3.5:32b')

def upload_pdf(filepath):
    filename = os.path.basename(filepath)
    rag_name = filename.split(".")[0]

    with open(filepath, 'rb') as uploaded_file:
        reader = PDFReader()
        rag_documents: List[Document] = reader.read(uploaded_file)

        if rag_documents:
            rag_assistant.knowledge_base.load_documents(rag_documents, upsert=True)

    print(f'uploaded {filepath}')


def upload_pdfs_from_directory(directory_path):
    glob_string = os.path.join(directory_path, '*.pdf')

    pdf_locations = glob.glob(glob_string)

    number_of_pdfs = len(pdf_locations)

    for index, pdf_location in enumerate(pdf_locations):
        print(f'uploading #{index+1} of {number_of_pdfs}')
        upload_pdf(pdf_location)
        

