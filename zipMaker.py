text = "this is a book which helps people to understand what is life and the best part is this is completly free so go now and shop for just 0$ on amzon.in thankyou :)"
newtext = text.split(" ")
listofwords = []
zip = {}
for index , words  in enumerate(newtext) :
    print(words)
    index = str(index)
    if words  in  listofwords:
        zip[index] = words
        newtextagain = text.replace(words , index)
    else :
        listofwords.append(words)
print(newtextagain)
        
for key , value in zip.items():
        newlist2 = newtextagain.replace(key , value)
print(newlist2)
