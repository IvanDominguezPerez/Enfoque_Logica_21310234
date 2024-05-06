import nltk

# Datos de texto sin etiquetar para la inducción gramatical
unlabeled_data = [
    "the cat sat on the mat",
    "the dog chased the cat",
    "the mouse ran away from the cat",
    "the cat slept on the mat"
]

# Función para realizar la inducción gramatical
def induct_grammar(unlabeled_data):
    productions = []  # Lista para almacenar las producciones gramaticales
    
    # Tokenizar y etiquetar cada oración en el conjunto de datos
    for sentence in unlabeled_data:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        
        # Agregar las producciones gramaticales de cada oración
        for i in range(len(tagged_words) - 1):
            production = (tagged_words[i][1], tagged_words[i+1][1])  # Producción de la forma (POS1, POS2)
            productions.append(production)
    
    # Construir la gramática probabilística a partir de las producciones
    grammar = nltk.induce_pcfg(nltk.Nonterminal('S'), productions)
    return grammar

# Realizar la inducción gramatical
induced_grammar = induct_grammar(unlabeled_data)

# Imprimir la gramática inducida
print("Gramática inducida:")
print(induced_grammar)
