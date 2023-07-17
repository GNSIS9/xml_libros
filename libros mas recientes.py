
#Consulta con XPATH: los 3 libros publicados más recientemente:
from lxml import etree

def leer_fichero(xml_file):
   
  # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    print(xml_tree)
    
  #libros = xml_tree.xpath("//libros/libro")
    libros = xml_tree.xpath("//libro[titulo and anio]")
    print(libros)

    libros.sort(key=lambda e: float(e.xpath("anio")[0].text), reverse=True)
   
    for libro in libros[:3]:
        titulo = libro.xpath("titulo")[0].text
        anio = libro.xpath("anio")[0].text
        print("Titulo:", titulo)
        print("Anio:", anio)
        print("---")

# Ruta al archivo XML y DTD
xml_file = "libro.xml"

# Llamar a la función para validar el XML con el DTD
leer_fichero(xml_file)