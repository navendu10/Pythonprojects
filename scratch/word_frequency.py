"""Tiny practice script: how often does a word appear in a sentence?"""


def word_frequency(text, word):
    """Return the percentage of words in ``text`` that equal ``word`` (case-insensitive)."""
    words = text.lower().split()
    if not words:
        return 0.0
    return words.count(word.lower()) / len(words) * 100


if __name__ == "__main__":
    sentence = "I like to like a game"
    print(f"{word_frequency(sentence, 'like'):.1f}%")  # -> 33.3%
