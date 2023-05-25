import PyPDF2 as pdf
import os
from PyPDF2 import PdfReader, PdfWriter,PdfMerger

print(pdf.__version__)

print(dir(pdf)) 

file = open("C:\\Users\\subed\\Desktop\\python 100 days of code\Exercise\\Clut_pdf.py\\sample_pdf.pdf","rb")

reader = PdfReader(file)

# reader.getDocumentInfo()

info = reader.metadata #gets all info of the pdf
print(info)

print(info.title) #prints out the title of the pdf

print(info.author) #prints out the author of the pdf

print(len(reader.pages)) #prints out the total no of pages of the pdf

#to extract the texts

print(reader.pages[0].extract_text())

#A function to get metadata
def get_pdf_metadata(pdf_path):
    with open(pdf_path,"rb") as f:
        reader = PdfReader(f)
        info = reader.metadata

    return info
# print(get_pdf_metadata("C:\\Users\\subed\\Desktop\\python 100 days of code\Exercise\\Clut_pdf.py\\sample_pdf.pdf"))


#func to extract texts

def extract_pdf_text(pdf_path):
    with open("C:\\Users\\subed\\Desktop\\python 100 days of code\\Exercise\\Clut_pdf.py\\Unit-5.pdf","rb") as f:
        reader = PdfReader(f)
        results = []
        for i in range(0,len(reader.pages)):
            selected_pages = reader.pages[i]
            Texts = selected_pages.extract_text()
            results.append(Texts)
    return " ".join(results)

# print(extract_pdf_text("C:\\Users\\subed\\Desktop\\python 100 days of code\Exercise\\Clut_pdf.py\\sample_pdf.pdf"))

#func to split pdf

def split_pdf(pdf_path):
    with open(pdf_path,"rb") as f:
        reader = PdfReader(f)
    #get all pages
        for page_num in range(len(reader.pages)):  #looop through pages
            selected_page = reader.pages[page_num]

            #writer to write
            writer = PdfWriter()
            writer.add_page(selected_page)  #add/embedding of the page
            filename = os.path.splitext(pdf_path)[0]
            output_filename = f"{filename}_page_{page_num+1}.pdf"
            #save and compile to pdf
            with open (output_filename,"wb") as out:
                writer.write(out)

            print("created a pdf:{}".format(output_filename))

split_pdf("C:\\Users\\subed\\Desktop\\python 100 days of code\\Exercise\\Clut_pdf.py\\Unit-5.pdf")


#merging pdf
# step 1 = get a list of pdfs
# step 2 = pdfMerger

def fetch_all_files(parent_folder: str):
    target_files = []
    for path,subdirs,files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path,name))
            
    return target_files

# print(fetch_all_files("C:\\Users\\subed\\Desktop\\python 100 days of code\\Exercise\\Clut_pdf.py\\Out"))

def merge_pdf(target_files,output_filename="final_merged_file.pdf"):
    merger = PdfMerger
    with open(output_filename,"wb") as f:
        for file in target_files:
            merger.append(file)

        merger.write(f)

merge_pdf()



