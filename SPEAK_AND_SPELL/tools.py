import nltk

nltk.download('brown')
nltk.download('names')

from nltk.corpus import brown
from nltk.corpus import names


def save_common_words(fnaem, min_length=4, max_length=10):
    # Get the 5000 most common English words from the Brown corpus
    freq_dist = nltk.FreqDist(w.lower() for w in brown.words())
    common_words = [word for word in list(freq_dist.keys())[:5000] if min_length <= len(word) <= max_length]
    
    # Remove words with punctuation or numbers
    common_words = [word for word in common_words if word.isalpha()]

    #save common words to file
    with open(fname, 'w') as f:
        for word in common_words:
            f.write(word + '\n')

if __name__ == '__main__':
    save_common_words("common_words.txt")