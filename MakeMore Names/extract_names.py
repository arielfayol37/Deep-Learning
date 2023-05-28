# Extacting the names from a pdf file
#import os
#os.chdir(r'C:\Users\HP\Downloads')
import PyPDF2 as pf
import re
name_of_pdf_file = '2021-GCE-AL-Results.pdf'
pdfFileObj  = open(name_of_pdf_file, 'rb')
pdfReader = pf.PdfReader(pdfFileObj)
# Regex to select the lines with the names and removing numbers
pattern = re.compile(r'\(\d+\)\n([A-Z\s-]+)')

lines_list = []
for i in range(len(pdfReader.pages)):
    lines_list.append(pattern.findall(pdfReader.pages[i].extract_text()))

names = [] # some items in this list will be subjects and grades.
for line in lines_list:
    for string in line:
        names.extend(string.split(" "))

for index, name in enumerate(names):
    if (len(name) == 4 or (len(name)==6 and name[0] == '\n')) and name[-2] == "-":
        del names[index]
names = list(set(names))        
with open('cameroon_names.txt', 'w') as file:
    # Write each name to a separate line in the file
    for name in names:
        file.write(name.strip() + '\n')
