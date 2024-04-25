import re
import zipfile

class TextAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        with open(self.input_file, 'r') as file:
            self.text = file.read()
    
    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.text)
        return len(sentences)

    def count_sentence_types(self):
        narr_sentences = re.findall(r'\b[A-Z][^.!?]*[.!?]', self.text)
        interrogative_sentences = re.findall(r'[A-Z][^.!?]*\?+', self.text)
        imperative_sentences = re.findall(r'[A-Z][^.!?]*!+', self.text)

        return len(narr_sentences), len(interrogative_sentences), len(imperative_sentences)

    def average_sentence_length(self):
        words = re.findall(r'\b\w+\b',self.text)
        total_chars = sum(len(word) for word in words)
        total_sentences = self.count_sentences()

        if total_sentences > 0:
            return int(total_chars / total_sentences)
        else:
            return 0

    def average_word_length(self):
        words = re.findall(r'\b\w+\b',self.text)
        total_chars = sum(len(word) for word in words)
        total_words = len(words)

        if total_words > 0:
            return int(total_chars / total_words)
        else:
            return 0

    def count_smileys(self):
        smileys = re.findall(r'([;:]-*[\(\)\[\]])',self.text)
        return len(smileys)
    
    def get_hex_numbers(self):
        hex_numbers = re.findall(r'\b(?:0x)?[0-9A-Fa-f]+\b',self.text)
        return hex_numbers

    def check_plus_numbers(self):
        plus_numbers = re.findall(r'\+\d+',self.text)
        return len(plus_numbers) > 0

    def count_words_length_four(self):
        words = re.findall(r'\b\w{4}\b',self.text)
        return len(words)

    def find_vowel_consonant_words(self):
        words = re.findall(r'\b\w+\b',self.text)
        result = []

        for idx, word in enumerate(words):
            vowels = re.findall(r'[aeiou]', word, re.IGNORECASE)
            consonants = re.findall(r'[bcdfghjklmnpqrstvwxyz]', word, re.IGNORECASE)

            if len(vowels) == len(consonants):
                result.append((word, idx))

        return result

    def sort_words_by_length(self):
        words = re.findall(r'\b\w+\b',self.text)
        sorted_words = sorted(words, key=len, reverse=True)
        return sorted_words

    def analyze_text(self):

        result = {
            'sentences': self.count_sentences(),
            'narrative_sentences': 0,
            'interrogative_sentences': 0,
            'imperative_sentences': 0,
            'average_sentence_length': self.average_sentence_length(),
            'average_word_length': self.average_word_length(),
            'smileys': self.count_smileys()
        }

        result['narrative_sentences'], result['interrogative_sentences'], result['imperative_sentences'] = \
            self.count_sentence_types()

        with open(self.output_file, 'w') as file:
            for key, value in result.items():
                file.write(f'{key}: {value}\n')

        with zipfile.ZipFile('result.zip', 'w') as zipf:
            zipf.write(self.output_file)

        return result