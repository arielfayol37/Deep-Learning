#Extacting the names from a pdf file
import os
os.chdir(r'C:\Users\Noella\Downloads')
import PyPDF2 as pf
import re
pdfFileObj  = open('2021-GCE-AL-Results.pdf', 'rb')
pdfReader = pf.PdfReader(pdfFileObj)
# Regex to select the lines with the names and removing numbers
pattern = re.compile(r'\(?\d+\)?\n([A-Z\s-]+)')

lines_list = []
for i in range(len(pdfReader.pages)):
    lines_list.append(pattern.findall(pdfReader.pages[i].extract_text()))
assert len(lines_list) > 0
names = [] # some items in this list will be subjects and grades.
for line in lines_list:
    for string in line:
        names.extend(string.split(" "))

new_names = []
for name in names:
    if (len(name) == 5 or (len(name) == 6 and name[0] == '\n')) and name[-2] == "-":
        continue
    if name == "-" or name=='\n':
        continue
    if len(name) > 0:
        if name[0] == "-":
            name = name[1:]
        if name[-1] == "-":
            name = name[:-1]
        new_names.append(name.strip())
new_names = list(set(new_names))
new_names.sort()
with open('cameroon_names.txt', 'w') as file:
    # Write each name to a separate line in the file
    for name in new_names:
        file.write(name.strip() + '\n')
