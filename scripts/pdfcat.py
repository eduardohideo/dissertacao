from pyPdf import PdfFileWriter, PdfFileReader
import sys

def main(argv = None):
    """
    funcao para pegar uma pagina de um pdf
    argumentos:
	nome_do_arquivo_de_entrada nome_do_arquivo_de_saida numero_da_pagina_inicial [numero_da_pagina_final]
    """
    if argv is None:
	argv = sys.argv[1:]
    output = PdfFileWriter()
    input = PdfFileReader(file(argv[0],"rb"))
    output.addPage(input.getPage(int(argv[2])))
    if len(argv) >= 4:
	for i in range(int(argv[2])+1,int(argv[3])+1):
	    output.addPage(input.getPage(i))
    output.write(file(argv[1],"wb"))


if __name__ == "__main__":
    import sys
    sys.exit(main())
