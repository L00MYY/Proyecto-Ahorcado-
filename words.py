import random
def remove_accents(word): # remove_accents(word) reemplaza caracteres acentuados por sus equivalentes sin acento
    replacements = {'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ü': 'U', 'Ñ':'N',}
    
    new_word = ""
    
    #Loop para reemplazar caracteres
    
    for ch in word:
        if ch in replacements:
            new_word += replacements[ch]
        else:
            new_word += ch

    return new_word


def load_words(path):
    words = []
    
    file = open(path, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    
    # Este for recorre las palabras, quita los acentos y vuelve todos los caracteres en mayúsculas.
    for line in lines:
        line = line.strip()#Eliminia todo espacio entre cada palabra
        if line != "":
            upper = line.upper()#Los hace mayuscula
            clean = remove_accents(upper)#Quitamos los acentos
            words.append(clean)#Guardamos las palabras sin acentos, sin espacios y en mayúsculas
            
    return words

def get_random_word(word):
    index = random.randint(0, len(word) - 1) #Random Index
    return word[index]
    return word[index]
