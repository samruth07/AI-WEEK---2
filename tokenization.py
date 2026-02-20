import re
import math

def sentence_to_matrix(sentence, columns):
    
    words = re.findall(r'\b\w+\b', sentence)
    total_words = len(words)
    
    rows = math.ceil(total_words / columns)
    
    matrix = []
    index = 0
    
    for i in range(rows):
        row = []
        for j in range(columns):
            if index < total_words:
                row.append(words[index])
                index += 1
            else:
                row.append("")
        matrix.append(row)
    
    return matrix


# Main Program
sentence = input("Enter a sentence: ")
columns = int(input("Enter number of columns for matrix: "))

matrix = sentence_to_matrix(sentence, columns)

print("\nMatrix Representation:\n")
for row in matrix:
    print(row)