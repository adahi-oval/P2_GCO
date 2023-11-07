import modules.docReader as functions
import modules.myParser as myParser


args = myParser.Parser()

filename = args.file
outputname = args.output

stopname = args.stopwords
lemaname = args.lematization

# Funcion principal del programa
def main():
  documentos = functions.readDocs(filename)
  stopwords = functions.readDocs(stopname)
  listalema = functions.readLema(lemaname)
  palabrasPorDocumento = []
  # Genera tabla de palabras separadas por documentos
  for document in documentos:
    cleanDoc1 = functions.clearStopWords(document, stopwords)
    documentoLimpio = functions.lematizacion(cleanDoc1, listalema)
    palabrasPorDocumento.append(functions.convertirAMinusculas(functions.separarPalabras(documentoLimpio)))
  
  # Creo un set con los terminos de los documentos
  # setTerminos = set()
  # for documento in palabrasPorDocumento:
  #   setTerminos = agregarTerminosConjunto(setTerminos, documento)
  
  j = 0

  for documento in palabrasPorDocumento:
    tablaDocumento = [] 
    i = 0
    for termino in documento:
      if not functions.terminoPerteneceMatriz(termino, tablaDocumento):
        tf = functions.calcularTF(termino, documento)
        idf = functions.calcularIDF(termino, palabrasPorDocumento)
        tablaDocumento.append([i, termino, tf, idf, tf * idf])
        i = i + 1
    functions.crearTablaDocumento(tablaDocumento, "tablas/" + outputname + str(j) + ".csv")
    j = j + 1


main()