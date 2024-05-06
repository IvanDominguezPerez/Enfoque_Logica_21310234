import nltk

# Definición de la gramática causal definida (DCG)
grammar = nltk.CFG.fromstring("""
    S -> 'if' CAUSE 'then' EFFECT
    CAUSE -> 'the' 'rain' | 'the' 'wind'
    EFFECT -> 'the' 'grass' 'gets' 'wet' | 'the' 'trees' 'sway'
""")

# Crear un analizador sintáctico utilizando la gramática
parser = nltk.ChartParser(grammar)

# Función para analizar una oración y determinar si sigue la gramática definida
def analyze_sentence(sentence):
    words = nltk.word_tokenize(sentence)  # Tokenizar la oración en palabras
    for tree in parser.parse(words):
        return True  # Si el árbol de análisis se puede construir, la oración es válida
    return False  # Si no se puede construir ningún árbol de análisis, la oración es inválida

# Ejemplos de oraciones para probar el analizador
sentences = [
    "if the rain then the grass gets wet",
    "if the wind then the trees sway",
    "if the sun then the flowers bloom"
]

# Probar el analizador con las oraciones de ejemplo
for sentence in sentences:
    if analyze_sentence(sentence):
        print(f"'{sentence}' es una oración válida según la gramática definida.")
    else:
        print(f"'{sentence}' no es una oración válida según la gramática definida.")
