text = "this is a book which helps people to understand what is life and the best part is this is completely free so go now and shop for just 0$ on amazon.in thankyou :)"

newtext = text.split(" ")
seen = []
compressed = {}  # index: word  (for decompressing later)

# --- COMPRESS ---
result = []
for index, word in enumerate(newtext):
    if word in seen:
        result.append(str(index))       # replace word with its index
        compressed[str(index)] = word   # remember index → word
    else:
        seen.append(word)
        result.append(word)             # keep word as is

compressed_text = " ".join(result)
print("Compressed:", compressed_text)

# --- DECOMPRESS ---
words = compressed_text.split(" ")
decompressed = []
for word in words:
    if word in compressed:
        decompressed.append(compressed[word])  # swap index back to word
    else:
        decompressed.append(word)

print("Decompressed:", " ".join(decompressed))



"""OldFixednewtextagain = text.replace(...)Build a list, join at endzip variable namecompressedSecond loop overwrites newlist2Build list, append each word.replace() hits partial wordsSplit and compare whole words"""
