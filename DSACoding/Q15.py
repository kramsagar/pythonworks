#Check if a word is present in a sentence
"""
Given a sentence as a string str and a word word, the task is to check if the word 
is present in str or not. A sentence is a string comprised of multiple words and each word is separated with spaces.
Examples: 

Input: str = “Geeks for Geeks”, word = “Geeks” 
Output: Word is present in the sentence 

Input: str = “Geeks for Geeks”, word = “eeks” 
Output: Word is not present in the sentence 
"""

str = "Geeks for Geeks"
word = "Geeks"
"""
for i in str.split(" "):
    if word == i:
        print("yes the word is exist in input str")
    else:
        print("not exist")
"""

def isexist(str,word):
    for i in str.split(" "):
        if word == i:
            return True
        else:
            return False

if (isexist(str,word)):
    print("Yes")
else:
    print("No")