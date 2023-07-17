from lxml import etree

def leer_fichero(xml_file):
   
    # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    print(xml_tree)

   
    #libros = xml_tree.xpath("//libros/libro")
    libros = xml_tree.xpath("//libro[titulo and anio]")
    print(libros)
    for libro in libros:
        t = libro.find("titulo").text
        a =libro.find("anio").text
        print(t)
        print(a)
        print("---")
       #print(libro.text)
    print(len(libros))

# Ruta al archivo XML y DTD
xml_file = "libro.xml"


# Llamar a la función para validar el XML con el DTD
leer_fichero(xml_file)