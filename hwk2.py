# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:44:06 2022

@author: luisa
"""
import re

file= open("C:\\Users\\luisa\\Documents\\Spring 2022\\Bio Structures\\prog_rev_ref_list.txt", "r")
references_points= file.read()

references= references_points.replace(".", "") #Remove periods
ref_string= references.splitlines() #List of strings

ref_list= [] #List of lists containing strings
for line in ref_string: 
    ref_list.append(line.split())

#Function to get authors lastname
def get_author (pattern, file, start, end):
    for arr in file:
        if len(arr) > 0:
            for word in arr:
                if re.search ("(%s:)" % pattern, word):
                    s= " "
                    s= s.join(arr[start:end])
                    return s

author_num= 1
authors= []
for arr in ref_list:
    if len(arr) > 0:
        lastname= get_author(str(author_num), ref_list, 1, 2)
        if lastname == None:
            break
        authors.append(lastname)
        author_num +=1
        
#Journals
pattern_jr= re.compile(r"\D{4,29}?(?=20)")
jrrs= pattern_jr.findall(references)


pattern_next= r"\b[A-Z].*?\b"
empty= []
for word in jrrs:
    empty.append(re.findall(pattern_next, word))
    

#remove blank spaces by creating new list
remove= ["Epub", "T", "NK", "", "Like", "Cell", "Phenotype", "Cells", "Cluster", "Learning", "Approach", "Vesicle", "Transport", "A", "Meta", "Analysis", "Indian", "Follicles", "Methods", "HO", "Univ", "FHC"]
journals= []
for line in empty:
    full_word = ""
    for word in line:
        if word not in remove:
            full_word += " " + word 
    if len(full_word) > 0:    
        journals.append(full_word)

#PMIDS
pattern = re.compile(r"(24)(\d{6})")
numbers= pattern.findall(references)

#function to convert tuple to string
def join_tuple_string(strings_tuple):
   return ''.join(strings_tuple)

result = map(join_tuple_string, numbers)
pmids= list(result)

#print all variables = "authors", "journals", "pmids"
length= len(authors)

for i in range(length):
    print(authors[i] + "," + journals[i] + ", " + pmids[i] + "\n")
    