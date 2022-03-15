l=[]

st="naman study in aba school"


for word in st.split():
    
    if word==word[::-1]:
        l.append(word)
print(st)
print("Total  number of palindrome words in a sentence:",len(l))
