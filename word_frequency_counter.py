import os
stop_word=["a", "an", "the","in", "on", "at", "with", "and", "but", "or", "of"]
filtered_words=[]
def word_count(file_path,top_n): 
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return
    with open(file_path,"r",encoding="utf-8") as file:
        text=file.read()
    punctuation="{}()!?,."""
    for el in punctuation:
        text=text.replace(el,"")
    words=text.lower().split()
    for word in words:
        if word not in stop_word    :
            filtered_words.append(word)
        word_counts = {}
    for word in filtered_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    print(f"Top {top_n} most frequent words:")
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")
if __name__=="__main__":
    file_path = input("Enter the path to the text file: ")
    top_n = int(input("Enter the number of top frequent words to display: "))
    word_count(file_path, top_n)


    
    

     