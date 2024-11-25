#25
def word_vowels_count(ml):
    vowels="auoie"
    maxc=0
    word=ml[0]
    for el in ml:
        count=0
        for char in el: 
            if char in vowels:
                count+=1
    if count>maxc:
        maxc=count
        word= el  

    return word
print(word_vowels_count(ml=["hello","gouuud","sosotoo"]))