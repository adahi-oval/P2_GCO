import argparse

def Parser():
  parser = argparse.ArgumentParser(description="Parser para el sistema de recomendación")

  grupoRequeridas = parser.add_argument_group('Argumentos Requeridos', 'Nombres de los archivos necesarios:')

  grupoRequeridas.add_argument('-f', '--file', nargs='?',required=True, type=str, help='Ruta del archivo de documentos de entrada')
  parser.add_argument('-o', '--output', type=str, default="Documento",help='Nombre archivo de salida (opcional), sin terminación', required=False)
  grupoRequeridas.add_argument('-s', '--stopwords', nargs='?',required=True, type=str, help='Ruta del archivo de stop words de entrada')
  grupoRequeridas.add_argument('-l', '--lematization', nargs='?',required=True, type=str, help='Ruta del archivo de lematización de entrada')

  return parser.parse_args()