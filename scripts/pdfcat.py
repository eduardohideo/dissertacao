from pyPdf import PdfFileWriter, PdfFileReader
import sys

def main(argv = None):
    """
    funcao para pegar uma pagina de um pdf
    argumentos:
	nome_do_arquivo_de_entrada nome_do_arquivo_de_saida numero_da_pagina
    """
    if argv is None:
	argv = sys.argv[1:]
    output = PdfFileWriter()
    input = PdfFileReader(file(argv[0],"rb"))
    output.addPage(input.getPage(int(argv[2])))
    output.write(file(argv[1],"wb"))


if __name__ == "__main__":
    import sys
    sys.exit(main())
