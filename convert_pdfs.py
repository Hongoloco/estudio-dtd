from pdf2docx import Converter
import os

# Lista de PDFs a convertir
pdfs = [
    'Material estudio radio/Configuraciones y Capacidades de Radios Ericsson Minilink - 2024.pdf',
    'Material estudio radio/manual_introduccion_redes_tcp_ip.pdf',
    'Material estudio radio/MW Radio Propagation.pdf'
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
