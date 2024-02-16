import sys
import os
import re
import nltk
import string
import random
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk import ne_chunk
from nltk import ngrams
from nltk import FreqDist
from nltk import RegexpParser
from nltk import Tree
from nltk import collocations


# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')


# Function to read file
def read_file(file_name):
    try:
        file = open(file_name, 'r')
        text = file.read()
        file.close()
        return text
    except:
        print("File not found")
        sys.exit(0)


# Function to remove comments from code
def remove_comments(text):
    # remove single line comments
    text = re.sub(re.compile("//.*?\n"), "", text)
    # remove multi line comments
    text = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", text)
    return text


# Function to remove punctuations from code
def remove_punctuations(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


# Function to remove numbers from code
def remove_numbers(text):
    text = re.sub(r'\d+', '', text)
    return text


# Function to remove whitespaces from code
def remove_whitespaces(text):
    text = text.strip()
    return text


# Function to remove stopwords from code
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [w for w in word_tokens if not w in stop_words]
    filtered_text = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_text.append(w)
    return filtered_text


# Function to lemmatize code
def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    lemmatized_text = [lemmatizer.lemmatize(w) for w in word_tokens]
    return lemmatized_text


# Function to stem code
def stem(text):
    ps = PorterStemmer()
    word_tokens = word_tokenize(text)
    stemmed_text = [ps.stem(w) for w in word_tokens]
    return stemmed_text


# Function to get POS tags
def get_pos_tags(text):
    word_tokens = word_tokenize(text)
    pos_tags = pos_tag(word_tokens)
    return pos_tags


# Function to get named entities
def get_named_entities(text):
    word_tokens = word_tokenize(text)
    named_entities = ne_chunk(pos_tag(word_tokens))
    return named_entities


# Function to get n-grams
def get_ngrams(text, n):
    word_tokens = word_tokenize(text)
    n_grams = ngrams(word_tokens, n)
    return n_grams


# Function to get frequency distribution
def get_freq_dist(text):
    word_tokens = word_tokenize(text)
    freq_dist = FreqDist(word_tokens)
    return freq_dist


# Function to get collocations
def get_collocations(text):
    word_tokens = word_tokenize(text)
    collocations = collocations.BigramCollocationFinder.from_words(word_tokens)
    return collocations.nbest(collocations.pmi, 10)


# Function to get chunks
def get_chunks(text):
    word_tokens = word_tokenize(text)
    pos_tags = pos_tag(word_tokens)
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = RegexpParser(grammar)
    result = cp.parse(pos_tags)
    return result


# Function to get synonyms
def get_synonyms(text):
    synonyms = []
    for syn in wn.synsets(text):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms


# Function to get antonyms
def get_antonyms(text):
    antonyms = []
    for syn in wn.synsets(text):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return antonyms


# Function to get hypernyms
def get_hypernyms(text):
    hypernyms = []
    for syn in wn.synsets(text):
        for l in syn.hypernyms():
            hypernyms.append(l.name())
    return hypernyms


# Function to get hyponyms
def get_hyponyms(text):
    hyponyms = []
    for syn in wn.synsets(text):
        for l in syn.hyponyms():
            hyponyms.append(l.name())
    return hyponyms



# Function to get meronyms
def get_meronyms(text):
    meronyms = []
    for syn in wn.synsets(text):
        for l in syn.part_meronyms():
            meronyms.append(l.name())
    return meronyms



# Function to get holonyms
def get_holonyms(text):
    holonyms = []
    for syn in wn.synsets(text):
        for l in syn.part_holonyms():
            holonyms.append(l.name())
    return holonyms



# Function to get entailments
def get_entailments(text):
    entailments = []
    for syn in wn.synsets(text):
        for l in syn.entailments():
            entailments.append(l.name())
    return entailments



# Function to get definitions
def get_definitions(text):
    definitions = []
    for syn in wn.synsets(text):
        definitions.append(syn.definition())
    return definitions



# Function to get examples
def get_examples(text):
    examples = []
    for syn in wn.synsets(text):
        examples.append(syn.examples())
    return examples



# Function to get similarity
def get_similarity(text1, text2):
    word1 = wn.synset(text1 + '.n.01')
    word2 = wn.synset(text2 + '.n.01')
    return word1.wup_similarity(word2)



# Function to get random comment
def get_random_comment():
    comments = ["This is a good code",
                "This code is not good",
                "This code is not readable",
                "This code is readable",
                "This code is not understandable",
                "This code is understandable",
                "This code is not maintainable",
                "This code is maintainable",
                "This code is not well documented",
                "This code is well documented",
                "This code is not well written",
                "This code is well written",
                "This code is not well commented",
                "This code is well commented",
                "This code is not well formatted",
                "This code is well formatted",
                "This code is not well structured",
                "This code is well structured",
                "This code is not well designed",
                "This code is well designed",
                "This code is not well tested",
                "This code is well tested",
                "This code is not well documented",
                "This code is well documented",
                ]
    return random.choice(comments)


# Function to get comment   
def get_comment(text):
    comment = ""
    text = remove_comments(text)
    text = remove_punctuations(text)
    text = remove_numbers(text)
    text = remove_whitespaces(text)
    text = remove_stopwords(text)
    text = lemmatize(text)
    text = stem(text)
    text = ' '.join(text)
    text = text.lower()
    text = text.replace(" ", "_")
    text = text.replace(".", "_")
    text = text.replace(":", "_")
    text = text.replace("-", "_")
    text = text.replace("(", "_")
    text = text.replace(")", "_")
    text = text.replace("[", "_")
    text = text.replace("]", "_")
    text = text.replace("{", "_")
    text = text.replace("}", "_")
    text = text.replace(",", "_")
    text = text.replace(";", "_")
    text = text.replace("'", "_")
    text = text.replace('"', "_")
    text = text.replace("!", "_")
    text = text.replace("?", "_")
    text = text.replace("/", "_")
    text = text.replace("\\", "_")
    text = text.replace("|", "_")
    text = text.replace("<", "_")
    text = text.replace(">", "_")
    text = text.replace("=", "_")
    text = text.replace("+", "_")
    text = text.replace("*", "_")
    text = text.replace("&", "_")
    text = text.replace("^", "_")
    text = text.replace("%", "_")
    text = text.replace("$", "_")
    text = text.replace("#", "_")
    text = text.replace("@", "_")
    text = text.replace("`", "_")
    text = text.replace("~", "_")
    text = text.replace(" ", "_")
    text = text.replace("__", "_")
    text = text.replace("__", "_")
    text = text.replace("__", "_")


    # print(text)
    # print(get_pos_tags(text))
    # print(get_named_entities(text))
    # print(get_ngrams(text, 2))

    # print(get_freq_dist(text))
    # print(get_collocations(text))
    # print(get_chunks(text))
    # print(get_synonyms(text))
    # print(get_antonyms(text))
    # print(get_hypernyms(text))
    # print(get_hyponyms(text))
    # print(get_meronyms(text))
    # print(get_holonyms(text))
    # print(get_entailments(text))
    # print(get_definitions(text))
    # print(get_examples(text))
    # print(get_similarity("code", "program"))
    # print(get_similarity("code", "software"))
    # print(get_similarity("code", "computer"))
    # print(get_similarity("code", "machine"))
    # print(get_similarity("code", "algorithm"))
    # print(get_similarity("code", "data"))
    # print(get_similarity("code", "information"))
    # print(get_similarity("code", "file"))
    # print(get_similarity("code", "document"))
    # print(get_similarity("code", "text"))
    # print(get_similarity("code", "string"))
    # print(get_similarity("code", "character"))
    # print(get_similarity("code", "number"))
    # print(get_similarity("code", "integer"))
    # print(get_similarity("code", "float"))
    # print(get_similarity("code", "double"))
    # print(get_similarity("code", "long"))
    # print(get_similarity("code", "short"))
    # print(get_similarity("code", "byte"))
    # print(get_similarity("code", "boolean"))
    # print(get_similarity("code", "true"))
    # print(get_similarity("code", "false"))
    # print(get_similarity("code", "if"))
    # print(get_similarity("code", "else"))
    # print(get_similarity("code", "while"))
    # print(get_similarity("code", "for"))
    # print(get_similarity("code", "do"))


    


