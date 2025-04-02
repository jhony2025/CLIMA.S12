# Trabajo con Archivos de Texto en Python

# Escritura en el archivo
with open("my_notes.txt", "w") as file:
    file.write("1. Aprender más sobre manipulación de archivos en Python.\n")
    file.write("   Ejemplo: Uso de 'with open' para escribir y leer archivos de manera segura.\n")
    file.write("2. Practicar el uso de estructuras de control y funciones.\n")
    file.write("   Ejemplo: Uso de bucles y condicionales dentro de funciones para procesar datos.\n")
    file.write("3. Mejorar la organización y documentación del código.\n")
    file.write("   Ejemplo: Uso de comentarios adecuados y formato PEP8 para un código más legible.\n")

# Lectura del archivo línea por línea
with open("my_notes.txt", "r") as file:
    for line in file:  # Leer y mostrar cada línea del archivo
        print(line.strip())  # strip() elimina los saltos de línea adicionales

# Explicación del código:
# 1. Se abre un archivo en modo escritura ('w') y se agregan tres notas con ejemplos prácticos.
# 2. Luego, se abre el archivo en modo lectura ('r') y se lee línea por línea, mostrando cada línea en la consola.
# 3. Se usa 'with open' para garantizar que el archivo se cierre correctamente después de cada operación.
# 4. Los comentarios y la estructura clara del código facilitan su comprensión y mantenimiento.
