from collections import Counter

def word_count(text: str) -> dict:
    return dict(Counter(text.lower().split()))

if __name__ == "__main__":
    print(word_count("the cat sat on the mat the cat"))
