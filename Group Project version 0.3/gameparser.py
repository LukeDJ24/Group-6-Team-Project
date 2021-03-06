import string
#imports string module for manipulating sentances

skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

def filter_words(words, skip_words):
    output = []
    for w in words:
        if w not in skip_words:
            output.append(w)
    return output

def remove_punct(text):
    return ''.join(ch for ch in text if ch not in string.punctuation)

def normalise_input(user_input):
    no_punct = remove_punct(user_input).lower()
    words = []
    for w in no_punct.split():
        words.append(w)
    return filter_words(words, skip_words)
    
