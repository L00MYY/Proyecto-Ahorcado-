from words import load_words, get_random_word

words = load_words("words.txt")
print("Palabras cargadas:", words[:100], "...")

secret = get_random_word(words)
print("Palabra aleatoria:", secret)
