import nltk

# Definir la gramática para el análisis sintáctico
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'man' | 'dog' | 'park' | 'telescope'
    V -> 'saw' | 'walked'
    P -> 'in' | 'with'
""")

# Crear un analizador sintáctico CYK
parser = nltk.ChartParser(grammar)

# Función para analizar una oración y manejar la ambigüedad
def analyze_sentence(sentence):
    words = nltk.word_tokenize(sentence)  # Tokenizar la oración en palabras
    trees = list(parser.parse(words))  # Obtener todos los árboles de análisis posibles
    num_trees = len(trees)
    if num_trees == 0:
        print("No se pudo construir ningún árbol de análisis para la oración:", sentence)
    elif num_trees == 1:
        print("Se construyó un árbol de análisis para la oración:", sentence)
        print("Árbol de análisis:", trees[0])
    else:
        print("Se construyeron múltiples árboles de análisis para la oración:", sentence)
        for i, tree in enumerate(trees, start=1):
            print(f"Árbol de análisis {i}: {tree}")

# Ejemplo de una oración ambigua
ambiguous_sentence = "the man saw the dog with the telescope in the park"

# Analizar la oración y manejar la ambigüedad
analyze_sentence(ambiguous_sentence)
