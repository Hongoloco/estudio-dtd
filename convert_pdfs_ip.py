from pdf2docx import Converter
import os

# Lista de PDFs a convertir en Material estudio IP
pdfs = [
    'Material estudio IP/BERT_Manual.pdf',
    'Material estudio IP/manual_introduccion_redes_tcp_ip.pdf',
    'Material estudio IP/Modulo 1 Tipos de Fibras Opticas.pdf',
    'Material estudio IP/RFC2544_Manual.pdf',
    'Material estudio IP/Transceptores ópticos.pdf'
]

# Convertir cada PDF
for pdf_file in pdfs:
    try:
        docx_file = pdf_file.replace('.pdf', '.docx')
        print(f'\nConvirtiendo: {os.path.basename(pdf_file)}...')
        
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        
        print(f'✓ Convertido exitosamente: {os.path.basename(docx_file)}')
    except Exception as e:
        print(f'✗ Error al convertir {os.path.basename(pdf_file)}: {str(e)}')

print('\n¡Conversión completada!')
