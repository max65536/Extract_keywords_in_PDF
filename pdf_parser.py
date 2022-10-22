from itertools import count
import os
import PyPDF2
from IPython import embed
 
# def count_pdf(file, ):

def parse_pdf(filename, keywords):
    file = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(file)
    counts = {}
    for word in keywords:
        counts[word] = 0
    for page in range(pdfReader.numPages):
        # for page in range(1):    
        pageObj = pdfReader.getPage(page)
        # extracting text from page
        text = pageObj.extractText()
        lines = text.split('\n')
        for line in lines:
            for word in keywords:
                counts[word] += line.count(word)
    # embed()     
    # print(text)           
    return counts
    
#################################
keywords = ["药","上"]
#################################


files = [x for x in os.listdir() if x.endswith(".pdf")]
print(files)
all_counts = {}
for file in files:
    counts = parse_pdf(file, keywords)  
    print(file, ':', counts)
    for k, v in counts.items():
        if k in all_counts.keys():
            all_counts[k] += counts[k]
        else:
            all_counts[k] = counts[k]
print("Total:", all_counts)            
# embed()
