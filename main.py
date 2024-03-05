import os
import random as rd

def story_selector():
    
    path_of_program = os.getcwd()      #automatically find the current path
    path_of_folder = "Madlibs_generator_python\stories"
    path = os.path.join(path_of_program,path_of_folder)  
                          
    list_of_stories = os.listdir(path)  #make the list of all txt files
    story_ = rd.choice(list_of_stories) #make the random story
    story = os.path.join(path,story_)

    return story


with open(story_selector(),"r") as f:
    story = f.read()
print(story)
start_word ="<"
end_word =">"
lst_of_words = set()
checker = 0

for i,character in enumerate(story): #find the list of all the words with character '<' and '<'
    if character == start_word:
        checker = i
        
    if character == end_word:
        word = story[checker:i+1]
        lst_of_words.add(word)
        checker=0
        

words_dict = {}  #make the dictionary of all words and their replaced words

for word in lst_of_words:
    inp = input(f"Enter the words which should be place at the place of {word}: ")
    words_dict[word] =inp
print(words_dict)

for word in words_dict:
    story = story.replace(word,words_dict[word])  #replace all the words here word is the key values (adjective,noun) and other part is the 
print(story)

