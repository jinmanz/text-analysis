
def counter(item, text): #return a word's frequency
    count = 0
    for word in text:
        if item == word:
            count += 1
    return count

def counter2 (list): # return a dictionary
    counts = {}
    for word in list:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] =1
    return counts

def counter3 (list):

    unique_words = set(list)
    for word in unique_words:
        print(word, counter(word,list))



from os.path import splitext
from os import listdir

def clean_text(text):
    # insert your code here

    #punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'

   # for marker in punctuation:
   #     text = text.replace(marker, "")
    text = text.lower()
    return text

def clean_punctuation(text):
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'

    for marker in punctuation:
        text = text.replace(marker, "")
    return text

def list_textfiles(directory):
    "Return a list of filenames ending in '.txt' in DIRECTORY."
    textfiles = []
    for filename in listdir(directory):
        if filename.endswith(".txt"):
            textfiles.append(directory + "/" + filename)
    return textfiles

def read_file(filename):
    "Read the contents of FILENAME and return as a string."
    infile = open(filename) # windows users should use codecs.open after importing codecs
    contents = infile.read()
    infile.close()
    return contents

def end_of_sentence_marker(character):

    markers = ['.','?','!']

    for marker in markers:
        if character == marker:
            return True
    return False


def split_sentences(text):
    "Split a text string into a list of sentences. return a list"

    sentences = []
    start = 0
    for end, character in enumerate(text):

        if end_of_sentence_marker(character):
            sentence = text[start: end + 1]
            sentences.append(sentence)
            start = end + 1
    return sentences


def tokenize(text):
    """Transform TEXT into a list of sentences. Lowercase
    each sentence and remove all punctuation. Finally split each
    sentence into a list of words."""
    # insert your code here
    text = clean_text(text)
    text = split_sentences(text)

    index1 = 0
    index2 = 0
    for sentence in text:
        text[index1] = clean_punctuation(text[index1])
        index1 += 1

    for sentence in text:
        text[index2] = sentence.split()
        index2 += 1

    return text



def list_textfiles(directory):
    "Return a list of filenames ending in '.txt' in DIRECTORY."
    textfiles = []
    for filename in listdir(directory):
        if filename.endswith(".txt"):
            textfiles.append(directory + "/" + filename)
    return textfiles
"""
file_list = list_textfiles("data/arabian_nights")
corpus = []

for file in file_list:
    text = read_file(file)
    corpus.append(text)

index = 0
for text_single in corpus:
    corpus[index] = tokenize(corpus[index])
    index += 1

print(list_textfiles("data/arabian_nights")[:20])
"""


# remove filename extension
def remove_ext(filename):
    # insert your code here
    filename = splitext(filename)[0]
    return filename

from os.path import basename
# remove filename directory
def remove_dir(filepath):
    # insert your code here
    filepath = basename(filepath)
    return filepath

def get_filename(filepath):
    #get filename
    filepath = splitext(filepath)[0]
    filepath = basename(filepath)
    return filepath
