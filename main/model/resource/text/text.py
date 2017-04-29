#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.resource.resource import Resource
from nltk.stem.snowball import SnowballStemmer
from langdetect import detect
import string
import re

__author__ = 'Ivan de Paz Centeno'


class Text(Resource):

    def __init__(self, uri="", text_id="", metadata=None, content=None):
        Resource.__init__(self, uri=uri, doc_id=text_id, metadata=metadata)

        if content is None:
            content = []

        self.content = content
        self.stop_word_list_file = "data/classifier/text/stops.txt"
        self.stops = None

    def __str__(self):
        return "[Text {}] \"{}\"; {} metadata elements".format(self.doc_id, self.uri, len(self.metadata))

    def load_from_uri(self):
        filename = self.uri
        stemmer = SnowballStemmer("english")

        if not self.stops:
            self.__load_stopword_list()

        # Remove header and tailer
        with open(filename, 'r', encoding='utf-8') as temp_file:
            lines = temp_file.readlines()

        header_index= 0
        ref_index = len(lines)

        found_header = False
        for i, line in zip(range(len(lines)), lines):

            line = line.strip()

            if len(line)==0 and not found_header:
                found_header = True
                header_index = i+1

            if line=='References':
                ref_index = i
                break

        lines = lines[header_index:ref_index]
        lines = ' '.join(lines).strip()

        # remove words between 1 and 2 and betwen 12 and 1000, rmove digits, remove special chars
        shortword = re.compile(r'\b\w{12,10000}\b|\b\w{1,2}\b|\d{2,}|\b\d+\b|[^a-zA-Z]|\b\w\b')
        lines = shortword.sub(' ', lines)

        # remove single letter (some letters could not be removed in the previous step)
        shortword = re.compile(r'\b\w{1,2}\b')
        lines = shortword.sub(' ', lines)
        lines = ' '.join(lines.split())

        # convert all to lower case
        lines= lines.lower()

        # Stemming
        lines = [stemmer.stem(word) for word in lines.split()]
        lines = ' '.join (lines)

        # Remove empty sting and english language detector
        if len(lines) > 0:
            if detect(lines) == 'en':
                # filter stop words and non-accii
                lines = [word for word in lines.split() if not word in self.stops and self._is_ascii(word) and len(word) > 2]
                lines = ' '.join(lines)

        self.content = lines

    @staticmethod
    def _is_ascii(s):
        for c in s:
            if c not in string.ascii_letters:
                return False
        return True

    def __load_stopword_list(self):
        with open(self.stop_word_list_file, 'r') as f:
            stops = [line.strip() for line in f]

        self.stops = stops

    def is_loaded(self):
        return len(self.content) > 0

    def get_content(self):

        return self.content