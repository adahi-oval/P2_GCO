import json

# Como cada linea es un documento, los separa por lineas usando \n como marcador. Crea un array de documentos
def readDocs(filename):
  with open(filename, "r") as documentos:
    file = documentos.read()
    documentos = file.split("\n")

    return documentos
  

# Version para la lista de lematizacion, lo lee como un diccionario JSON y crea una lista de tuplas de dos elementos
# para que sea más fácil usarlo como queremos
def readLema(filename):
  with open(filename, "r") as doc:
    data = json.load(doc)

  listaTuplas = [(key, value) for key, value in data.items()]

  return listaTuplas

  
# Funcion para limpiar el documento de stop words, le pasamos la lista de stopwords leida con readDocs
# y el documento que queremos limpiar, busca las palabras que no coinciden y las mete en un array de palabras que luego une  
def clearStopWords(documento, stopWords):

  palabras = documento.split()

  filtered_words = [word for word in palabras if word.lower() not in stopWords]

  cleanDoc = ' '.join(filtered_words)
  
  return cleanDoc


# Version de la limpieza de stopwords que recorre la lista de palabras buscando las que coinciden con el primer elemento
# de las tuplas de la lista de lematización para reemplazarlo por el segundo.
def lematizacion(cleanDoc, listaLematizacion):
  palabras = cleanDoc.split()

  for i in range(len(palabras)):

    word = palabras[i].lower()

    for lema, sustituto in listaLematizacion:
      if word == lema:
        palabras[i] = sustituto

  updatedDoc = ' '.join(palabras)

  return updatedDoc


documentos = readDocs("documents-01.txt")
stopwords = readDocs("stop-words-en.txt")
listalema = readLema("corpus-en.txt")

cleanDoc1 = clearStopWords(documentos[1], stopwords)
lemaDoc1 = lematizacion(cleanDoc1, listalema)

print(lemaDoc1)