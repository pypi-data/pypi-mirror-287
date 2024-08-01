# __version__ = 'dev'

import re
from .custom_rake import BanglaRake
from sbnltk.Tokenizer import wordTokenizer, sentenceTokenizer
from collections import defaultdict, Counter
import numpy as np
import networkx as nx
from tqdm import tqdm
import os

class KeywordExractor:
    def __init__(self, input_text_list, stop_words = None):
        self.text_list = input_text_list
        if stop_words is None:
            with open(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "stopwords.txt"))) as f:
                self.stopwords = f.read().split("\n")
            print(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "stopwords.txt")))
        else:
            self.stopwords = stop_words
        if isinstance(self.text_list, str):
            self.corpus = self.text_list
        elif isinstance(self.text_list, list):
            self.corpus = " ".join(self.text_list)
        else:
            raise TypeError("The inputs must be string or list of strings.")
        self.word_tokenizer = wordTokenizer()
        self.sentence_tokenizer = sentenceTokenizer()

    def clean_data(self, text):
        clean_text = re.sub(r"[^\u0980-\u09FF\u09E6-\u09EF\s]", "", text)
        clean_text = re.sub(r"\s+", " ", clean_text)
        return clean_text
    
    def get_keywords_using_rake(self):
        rake = BanglaRake(
            stopwords=self.stopwords,
            max_length=3,
            include_repeated_phrases=False,
            sentence_tokenizer=self.sentence_tokenizer,
            word_tokenizer=self.word_tokenizer
        )
        rake.extract_keywords_from_text(self.corpus)
        ranks = rake.get_word_degrees()
        pairs = []
        for key, value in ranks.items():
            pairs.append((key, value))
        sorted_pairs = sorted(pairs, key = lambda x:x[1], reverse=True)
        return sorted_pairs
    
    def get_keywords_using_pagerank(self):
        clean_corpus = self.clean_data(self.corpus)
        words = self.word_tokenizer.basic_tokenizer(clean_corpus)
        words = [word for word in words if not word in self.stopwords]
        unique_words = list(set(words))
        co_occurrences = self.build_co_occurances(window_size=2, words=words)
        co_occurrences_matrix = self.build_co_occurrences_matrix(unique_words=unique_words, co_occurrences=co_occurrences)
        pagerank_scores = self.get_pagerank_scores(unique_words=unique_words, co_occurrences_matrix=co_occurrences_matrix)
        return pagerank_scores

    def build_co_occurances(self, window_size, words):
        window_size = window_size

        co_occurrences = defaultdict(Counter)

        for i, word in enumerate(words):
            for j in range(max(0, i - window_size), min(len(words), i + window_size + 1)):
                # print(word, words[j])
                if i != j:
                    co_occurrences[word][words[j]] += 1
        return co_occurrences
    
    def build_co_occurrences_matrix(self, unique_words, co_occurrences):
        co_matrix = np.zeros((len(unique_words), len(unique_words)), dtype=int)

        word_index = {word: idx for idx, word in enumerate(unique_words)}
        for word, neighbors in tqdm(co_occurrences.items(), total = len(co_occurrences)):
            for neighbor, count in neighbors.items():
                co_matrix[word_index[word]][word_index[neighbor]] = count
        return co_matrix
    
    def get_pagerank_scores(self, unique_words, co_occurrences_matrix):
        G = nx.Graph()
        for word in unique_words:
            G.add_node(word)
        for i in tqdm(range(len(unique_words)), total = len(unique_words)): 
            for j in range(len(unique_words)): 
                if co_occurrences_matrix[i][j]>0:
                    G.add_edge(unique_words[i], unique_words[j], weight = co_occurrences_matrix[i][j])
        pagerank_scores = nx.pagerank(G, weight='weight')
        sorted_pagerank = sorted(pagerank_scores.items(), key=lambda item: item[1], reverse=True)
        return sorted_pagerank