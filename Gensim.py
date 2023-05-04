from gensim import corpora, models

# Define os documentos
documents = [
    "O céu é azul",
    "O sol é brilhante",
    "O céu é azul e o sol é brilhante"
]

# Tokeniza os documentos
tokenized_documents = [doc.lower().split() for doc in documents]

# Cria um dicionário dos termos
dictionary = corpora.Dictionary(tokenized_documents)

# Cria um corpus dos documentos
corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

# Cria um modelo LDA de 2 tópicos
lda_model = models.LdaModel(corpus, num_topics=2, id2word=dictionary)

# Imprime os tópicos
for topic in lda_model.print_topics():
    print(topic)
