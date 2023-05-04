# Importando a biblioteca TextBlob
from textblob import TextBlob

# Definindo a frase a ser analisada
frase = "Eu amo programação!"

# Criando um objeto TextBlob para a frase
blob = TextBlob(frase)

# Imprimindo a polaridade da frase
print('Polaridade:', blob.sentiment.polarity)