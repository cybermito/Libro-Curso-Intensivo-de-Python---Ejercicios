# Ejercicio 2 -3: Mensaje personal. Usar una variable para representar
# el nombre de una persona e imprimir un mensaje para esa persona.
# El mensaje que sea sencillo.
# Ejemplo: Hola, Antonio, ¿te gustaría aprender Python hoy?

name = "Antonio"
message = f'Hola, {name}, ¿te gustaría aprender Python hoy?'
print(message)


# Ejercicio 2-4: Grafía de nombres. Use una variable para representar
# el nombre de una persona e imprima ese nombre en minúsculas, mayúsculas
# y con mayúscula inicial
name = "luna"
print(f'Nombre todo en mayúsculas {name.upper()}')
print(f'Nombre todo en minúsculas {name.lower()}')
print(f'Nombre primera letra en mayúsculas {name.title()}')


# Ejercicio 2-5: Cita célebre. Busque una cita de un personaje al que admire.
# Imprima la cita y el nombre del autor. La salida debería tener un aspecto similar
# a esto, incluidas las comillas.
#
# Albert Einstein once said, "A person who never made a mistake never tried anything
# new "

author = "Albert Einstein"
quote = "once said, \"A person who never made a mistake never tried anything new\""
print(f'{author} {quote}')

# Ejercicio 2-6: Cita célebre 2. Repita el ejercicio 2-5, peo esta vez, represente el nombre
# de la persona usando una variable llamada famous_person. Después, componga el mensaje y représentelo
# con una nueva variable llamada message. Imprima su mensaje.
famous_person = "Antoine de Saint-Exupêry"
quote = ", \"Solo con el corazón se puede ver bien; lo esencial es invisible a los ojos."
message = f'{famous_person} {quote}'
print(message)

# Ejercicio 2-7: Eliminar espacios de nombres. Use una variable para representar el nombre
# de una persona e incluya algunos carácteres de espacio en blanco al principio y al final del
# nombre. Asegúrese de usar cada combinación de carácteres, \t y \n, al menos una vez. Imprima
# el nombre una vez, de mode que se muestren los espacios alrededor.
# A continuación, imprima el nombre usando cada una de las tres funciones que hemos visto:
# lstrip(), rstrip(), strip().

name = " Nuria \t\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())


# Ejercicio 2-8: Extensiones de archivos. Python cuenta con el método removesuffix(), que funciona
# exactamente igual que el método removepreffix(). Asigne el valor 'python_notes.txt' a una variable.
# A continuación, utilice el método removesuffix() para mostrar el nombre de archivo sin la extensión
# de archivo, como ocurre con algunos exploradores de archivos.

filename = 'python_notes.txt'
print(f'Nombre del archivo: {filename.removesuffix(".txt")}')