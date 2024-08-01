class QueryWords:

    weights = [4, 4, 4, 3, 3, 2, 2, 1, 1, 1]

    def __init__(self, query: str, language_dict: dict) -> None:
        query_list = query.lower().split(" ")

        # Convertir listas de palabras a conjuntos para búsquedas rápidas
        dict_sets = {key: set(words) for key, words in language_dict.items()}

        # Inicializar listas para cada categoría
        names = []
        verbs = []
        nouns = []
        adverbs = []
        adjectives = []
        pronouns = []
        determiners = []
        prepositions = []
        interjections = []
        conjunctions = []

        # Clasificar palabras en categorías
        for word in query_list:
            for category in dict_sets:
                if word in dict_sets[category]:
                    locals()[category].append(word)
                    break
            else:
                names.append(word)

        # Lista de listas de palabras
        self.words = [
            names,
            verbs,
            nouns,
            adverbs,
            adjectives,
            pronouns,
            determiners,
            prepositions,
            interjections,
            conjunctions
        ]

        # Suponiendo que `self.weights` se define en otro lugar y corresponde a la longitud de `self.words`
        word_weights = [
            {word: self.weights[i] for word in words}
            for i, words in enumerate(self.words)
        ]

        # Calcular el puntaje máximo
        self.max_score = sum(
            weight
            for words in word_weights
            for weight in words.values()
        )

language_dict = {
    "verbs": ["hacer"],
    "adverbs": ["como"],
    "determiners": ["un"],
    "interjections": ["y"]
}

query = "Como"

query_words = QueryWords(query, language_dict)

print(query_words.max_score)