from clases import Encargado, Profesor,Inscripciones

# Leemos el archivo txt de encargados
with open("Encargados.txt", "r") as archivo:
    lineas = archivo.readlines()

# Leemos el archivo txt de profesores
with open("profesores.txt", "r") as archivoDos:
    lineasDos = archivoDos.readlines()
    
# Leemos el archivo txt de inscripciones
with open("Inscripciones.txt", "r") as archivoTres:
    lineasTres = archivoTres.readlines()        

profesores=[]
encargados = []
inscripciones=[]



# Iteramos sobre las líneas del archivo y creamos objetos Encargado
for linea in lineas:
    partes = linea.strip().split(",")
    if len(partes) >= 2:
        nombre = partes[0]
        dni = partes[1]
        encargado = Encargado(nombre, dni)#se crea el objeto encargado
        encargados.append(encargado)#se añade a la lista encargados, los objetos que se vayan creando. 

# Iteramos sobre las líneas del archivo y creamos objetos profesores
for linea in lineasDos:
    partes = linea.strip().split(",")
    if len(partes) >= 4:
        nombre = partes[0]
        materia = partes[1]
        curso = partes[2]
        division = partes[3]
        profesor = Profesor(nombre, materia, curso, division)
        profesores.append(profesor)


# Iteramos sobre las líneas del archivo y creamos objetos Inscripciones
for linea in lineasTres:
    partes = linea.strip().split(",")
    if len(partes) >= 7:
        fecha = partes[0]
        nombre = partes[1]
        dni=partes [2]
        profesor = partes[3]
        curso = partes[4]
        division = partes[5]
        nota=partes[6] 
               
        inscripcion = Inscripciones(fecha,nombre,dni, profesor,curso, division, nota)
        inscripciones.append(inscripcion)
        #linea = f"{fecha_A},{nombre_A},{dni_A},{profesor_A},{curso_A},{division_A},{nota_A}\n"

# print(profesores)
# print(encargados)
# print(inscripciones)


####################################MENU PRINCIPAL################################################################
#FUNCION LAMBDA PARA EL COLOR DE UN TEXTO
colorize=lambda text, color: f"\033[{color}m{text}\033[0m"
texto="Acceso denegado. Por favor, vuelva a ingresar sus datos."
texto_rojo=colorize(texto,"31")#cambia el color rojo (31 es el codigo para rojo)

while True:
    print("********************************************\n"
          "*   Bienvenidos al sistema institucional   * \n"
          "*    Selecciona cómo quieres ingresar:     *\n"
          "*          1 - Encargado                   *\n"
          "*          2 - Profesor                    *\n"
          "*          3 - Salir                       *\n"
          "*                                          *\n"
          "********************************************")
    op1 = int(input())

    if op1 == 1:
        while True:
            # Código para el caso del encargado
            nombre_usuario = input("Ingrese el nombre: ")
            dni_usuario = input("Ingrese el DNI: ")
            usuario_valido = False  # Variable para verificar si el usuario es válido
            
            
            # Verificamos si el usuario tiene acceso iterando en la lista de encargados
            for encargado in encargados:
                if encargado.nombre == nombre_usuario and encargado.dni == dni_usuario:
                   usuario_valido = True
                   break  # Salir del bucle si el usuario es válido

            if usuario_valido:
                break  # Si el usuario es válido, salir del bucle de acceso
                
                
            print(texto_rojo)

        while True:
            print("********************************************\n"
                  "*       Sistema de inscripción             *\n"
                  "*                                          *\n"
                  "*          1 - Alta                        *\n"
                  "*          2 - Editar                      *\n"
                  "*          3 - Borrar                      *\n"
                  "*          4 - Salir                       *\n"
                  "********************************************")
            op2 = int(input())
            # fecha, nombre, dni,  profesor, curso, division, (nota=1 inicializada aparte)
           
            if op2 == 1:
                fecha_A = input("Fecha (DD/MM/YYYY): ")
                nombre_A = input("Nombre del estudiante: ")
                dni_A=input("DNI: ")
                profesor_A = input("Profesor: ")
                curso_A = input("Curso: ")
                division_A = input("División: ")
                nota_A = "-1"
               
                
                # Crear una cadena que represente una línea en formato CSV
                linea = f"{fecha_A},{nombre_A},{dni_A},{profesor_A},{curso_A},{division_A},{nota_A}\n"
            
                # Abrir el archivo "Inscripciones.txt" en modo apendizaje y escribir la línea
                with open("Inscripciones.txt", "a") as archivo:
                   archivo.write(linea)
            
                print("Inscripción exitosa")
            
            #revision (1)
            elif op2 == 2:
                #SECCION DE EDICION 
                ingrese_el_dni=input("ingrese el dni del estudiante para editar sus datos: ")
                alumno_valido=False #variable para verificar si el usuario es valido
                
                # Verificamos si el usuario tiene acceso iterando en la lista de inscripciones. 
                for inscripcion  in inscripciones:
                    if inscripcion.dni == ingrese_el_dni:
                       alumno_valido = True
                       break  # Salir del bucle si el usuario es válido
                 # fecha, nombre, dni,  profesor, curso, division, (nota=1 inicializada aparte)
                   
                if alumno_valido:
                     print("********************************************\n"
                           "*        Seleccione los datos              *\n"
                           "*     del alumno que desea modificar       *\n"
                           "*          1 - Fecha de inscripcion        *\n"
                           "*          2 - Nombre                      *\n"
                           "*          3 - DNI                         *\n"
                           "*          4 - Profesor                    *\n"
                           "*          5 - Curso                       *\n"
                           "*          6 - Division                    *\n"
                           "*          7-  salir                       *\n" 
                           "*                                          *\n"
                           "********************************************")
                     opcion=int(input())
                    
                     if opcion==1:
                          fecha_nueva=input("Ingrese la fecha correcta")
                          inscripcion.fecha=fecha_nueva
                          print("cambio exitoso")
                          
                          cantidad_inscripciones = len(inscripciones)   
                          if cantidad_inscripciones == 0:
                             print("La lista de inscripciones está vacía. No se realizarán cambios en el archivo.")
                          else: 
                              ## fecha, nombre, dni,  profesor, curso, division, (nota=1 inicializada aparte)
                              # Abre el archivo en modo escritura y sobreescribe los datos
                               with open("Inscripciones.txt", "w") as archivo:
                                    for inscripcion in inscripciones:
                                     # Escribe los atributos de cada objeto en el formato deseado
                                     archivo.write(
                                     f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                                     f"{inscripcion.profesor},{inscripcion.curso},"
                                     f"{inscripcion.division},{inscripcion.nota}\n"
                                                  )
                              #print(f"Se sobreescribió el archivo con {cantidad_inscripciones} inscripciones.")
                          
                          
                          
                          
                     elif opcion==2:
                          nombre_nuevo=input("Ingrese el nombre correcto")
                          inscripcion.nombre=nombre_nuevo
                          print("cambio exitoso")
                          
                          cantidad_inscripciones = len(inscripciones)   
                          if cantidad_inscripciones == 0:
                             print("La lista de inscripciones está vacía. No se realizarán cambios en el archivo.")
                          else: 
                              ## fecha, nombre, dni,  profesor, curso, division, (nota=1 inicializada aparte)
                              # Abre el archivo en modo escritura y sobreescribe los datos
                               with open("Inscripciones.txt", "w") as archivo:
                                    for inscripcion in inscripciones:
                                     # Escribe los atributos de cada objeto en el formato deseado
                                     archivo.write(
                                     f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                                     f"{inscripcion.profesor},{inscripcion.curso},"
                                     f"{inscripcion.division},{inscripcion.nota}\n"
                                                  )
                              #print(f"Se sobreescribió el archivo con {cantidad_inscripciones} inscripciones.")
                          
                          
                          
                          
                     elif opcion==3:
                         dni_nuevo=input("Ingrese el dni correcto")
                         inscripcion.dni=dni_nuevo
                         print("cambio exitoso")
                         
                         cantidad_inscripciones = len(inscripciones)   
                         if cantidad_inscripciones == 0:
                             print("La lista de inscripciones está vacía. No se realizarán cambios en el archivo.")
                         else: 
                              ## fecha, nombre, dni,  profesor, curso, division, (nota=1 inicializada aparte)
                              # Abre el archivo en modo escritura y sobreescribe los datos
                               with open("Inscripciones.txt", "w") as archivo:
                                    for inscripcion in inscripciones:
                                     # Escribe los atributos de cada objeto en el formato deseado
                                     archivo.write(
                                     f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                                     f"{inscripcion.profesor},{inscripcion.curso},"
                                     f"{inscripcion.division},{inscripcion.nota}\n"
                                                  )
                              #print(f"Se sobreescribió el archivo con {cantidad_inscripciones} inscripciones.")
                          
                         
                    
                          
                     elif opcion==4:
                          profesor_nuevo=input("Ingrese el profesor correcto")
                          inscripcion.profesor=profesor_nuevo
                          print("cambio exitoso")
                          
                          cantidad_inscripciones = len(inscripciones)   
                          if cantidad_inscripciones == 0:
                             print("La lista de inscripciones está vacía. No se realizarán cambios en el archivo.")
                          else: 
                              ## fecha, nombre, dni,  profesor, curso, division, (nota=1 inicializada aparte)
                              # Abre el archivo en modo escritura y sobreescribe los datos
                               with open("Inscripciones.txt", "w") as archivo:
                                    for inscripcion in inscripciones:
                                     # Escribe los atributos de cada objeto en el formato deseado
                                     archivo.write(
                                     f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                                     f"{inscripcion.profesor},{inscripcion.curso},"
                                     f"{inscripcion.division},{inscripcion.nota}\n"
                                                  )
                              #print(f"Se sobreescribió el archivo con {cantidad_inscripciones} inscripciones.")
                          
                          
                          
                     elif opcion==5:
                          curso_nuevo=input("Ingrese el curso correcto")
                          inscripcion.curso=curso_nuevo
                          print("cambio exitoso")
                          
                          cantidad_inscripciones = len(inscripciones)   
                          if cantidad_inscripciones == 0:
                             print("La lista de inscripciones está vacía. No se realizarán cambios en el archivo.")
                          else: 
                              ## fecha, nombre, dni,  profesor, curso, division, (nota=1 inicializada aparte)
                              # Abre el archivo en modo escritura y sobreescribe los datos
                               with open("Inscripciones.txt", "w") as archivo:
                                    for inscripcion in inscripciones:
                                     # Escribe los atributos de cada objeto en el formato deseado
                                     archivo.write(
                                     f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                                     f"{inscripcion.profesor},{inscripcion.curso},"
                                     f"{inscripcion.division},{inscripcion.nota}\n"
                                                  )
                              #print(f"Se sobreescribió el archivo con {cantidad_inscripciones} inscripciones.")
                          
                          
                          
                     elif opcion==6: 
                          division_nuevo=input("Ingrese el nuevo nombre")
                          inscripcion.division=division_nuevo
                          print("cambio exitoso") 
                          
                          cantidad_inscripciones = len(inscripciones)   
                          if cantidad_inscripciones == 0:
                             print("La lista de inscripciones está vacía. No se realizarán cambios en el archivo.")
                          else: 
                              ## fecha, nombre, dni,  profesor, curso, division, (nota=1 inicializada aparte)
                              # Abre el archivo en modo escritura y sobreescribe los datos
                               with open("Inscripciones.txt", "w") as archivo:
                                    for inscripcion in inscripciones:
                                     # Escribe los atributos de cada objeto en el formato deseado
                                     archivo.write(
                                     f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                                     f"{inscripcion.profesor},{inscripcion.curso},"
                                     f"{inscripcion.division},{inscripcion.nota}\n"
                                                  )
                              #print(f"Se sobreescribió el archivo con {cantidad_inscripciones} inscripciones.")
                          
                     elif opcion==8:
                           
                           break  
                         
                else:
                    print ("El DNI no se encuentra en el registro de alumnos")
                    print(type(ingrese_el_dni))
                    print(type(inscripcion.dni))
             
                             
                                 

            elif op2 == 3:
                # Código para borrar inscripciones no me funciona
                dni_nuevo=input("Ingrese el dni del inscripto para eliminarlo")
                eliminado = False  # Variable para verificar si se eliminó alguna inscripción
                
                
                for inscripcion in inscripciones:
                    if alumnos.dni==dni_nuevo:
                       #aliminar el objeto completo de la lista Inscripciones[]
                       inscripciones.remove(alumnos)
                       eliminado=True
       
                       
                       # Abre el archivo en modo escritura y sobreescribe los datos
                       with open("Inscripciones.txt", "w") as archivo:
                                    for inscripcion in inscripciones:
                                     # Escribe los atributos de cada objeto en el formato deseado
                                     archivo.write(
                                     f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                                     f"{inscripcion.profesor},{inscripcion.curso},"
                                     f"{inscripcion.division},{inscripcion.nota}\n"
                                                  )
                              
                    
                       
                       
                       break 

                
                if eliminado:
                    print("Inscripción eliminada exitosamente")
                else:
                    print("No se encontró ninguna inscripción con ese DNI")
              
              
              
                    

            elif op2 == 4:
                break  # Salir del bucle del sistema de inscripción

    elif op1 == 2:
        
        while True:
           #codigo para el acceso al profesor
           nombre = input("Nombre: ")
           materia = input("Materia: ")
           curso = input("Curso: ")
           division = input("División: ")
           usuario_valido_dos=False #variable para verificar si el usuario es valido

           # Verificamos si el usuario profesor tiene acceso itinerando la lista profesores
           for profesor in profesores:
             if profesor.nombre == nombre and profesor.materia == materia and profesor.curso == curso and profesor.division == division:
                usuario_valido_dos=True
                break #salir del bucle si el usuario es valido
                # Realiza las operaciones necesarias cuando el acceso es concedido
        
           if usuario_valido_dos:
                break  # Si el usuario es válido, salir del bucle de acceso

           print(texto_rojo)
           
        #BUCLE DEL MENU DOCENTE
        while True:
            print("********************************************\n"
                  "*       Sistema de Calificaciones          *\n"
                  "*          1 - subir nota                  *\n"
                  "*          2 - editar                      *\n"
                  "*          3 - Borrar                      *\n"
                  "*          4 - Salir                       *\n"
                  "********************************************")
            op3 = int(input())
            #OPCION 1 DEL SISTEMA DE ASIGNACION DE NOTAS DEL DOCENTE
            if op3 == 1:
               
                curso_del_estudiante=input("ingrese el curso: ")
                ingrese_el_dni=input("ingrese el dni del estudiante: ")
                alumno_valido=False #variable para verificar si el usuario es valido
                
                # Verificamos si el usuario tiene acceso iterando en la lista de inscripciones. 
                for inscripcion in inscripciones:
                  if inscripcion.curso == curso_del_estudiante and inscripcion.dni == ingrese_el_dni:
                    alumno_valido = True
                    break  #Salir del bucle si el usuario es válido
                  


                if alumno_valido:
                   nueva_nota=input("Ingrese la nota del estudiante: ")
                   inscripcion.nota=nueva_nota
                   
                   print("La nota ha sido cambiada con éxito")
                   print(inscripciones)
                   # Verifica la cantidad deobjetos en la lista inscripciones
                   cantidad_inscripciones = len(inscripciones)

                   if cantidad_inscripciones == 0:
                      print("La lista de inscripciones está vacía. No se realizarán cambios en el archivo.")
                   else:
                     # Abre el archivo en modo escritura y sobreescribe los datos
                      with open("Inscripciones.txt", "w") as archivo:
                          for inscripcion in inscripciones:
                              # Escribe los atributos de cada objeto en el formato deseado
                              archivo.write(
                               f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                               f"{inscripcion.profesor},{inscripcion.curso},"
                               f"{inscripcion.division},{inscripcion.nota}\n"
                                 )
                      print(f"Se sobreescribió el archivo con {cantidad_inscripciones} inscripciones.")
                 
 
            
              
            #OPCION 2 DEL DOCENTE: EDICION DE NOTA
            elif op3 == 2:
                
                curso_del_estudiante=input("ingrese la materia: ")
                ingrese_el_dni=input("ingrese el dni del estudiante: ")
                alumno_valido=False #variable para verificar si el usuario es valido
                
                # Verificamos si el usuario tiene acceso iterando en la lista de inscripciones. 
                for inscripcion in inscripciones:
                  if inscripcion.curso == curso_del_estudiante and inscripcion.dni == ingrese_el_dni:
                     alumno_valido = True
                     break  # Salir del bucle si el usuario es válido

                if alumno_valido:
                   print (f"la nota actual del estudiante {inscripcion.nombre} es: {inscripcion.nota}")
                   nueva_nota=input(f"Ingrese la nueva nota del estudiante: ")
                   inscripcion.nota=nueva_nota
                   print("La nota ha sido cambiada con éxito")
                   print(inscripciones)
                   
                   # Verifica la cantidad de objetos en la lista inscripciones
                   cantidad_inscripciones = len(inscripciones)

                   if cantidad_inscripciones == 0:
                      print("La lista de inscripciones está vacía. No se realizarán cambios en el archivo.")
                   else:
                     # Abre el archivo en modo escritura y sobreescribe los datos
                      with open("Inscripciones.txt", "w") as archivo:
                          for inscripcion in inscripciones:
                              # Escribe los atributos de cada objeto en el formato deseado
                              archivo.write(
                               f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                               f"{inscripcion.profesor},{inscripcion.curso},"
                               f"{inscripcion.division},{inscripcion.nota}\n"
                                 )
                      print(f"Se sobreescribió el archivo con {cantidad_inscripciones} inscripciones.")
                   
                
            #OPCION 3 DEL DOCENTE: ELIMINAR NOTA
            elif op3==3:
                  
                materia_del_estudiante=input("ingrese la materia: ")
                ingrese_el_dni=input("ingrese el dni del estudiante: ")
                alumno_valido=False #variable para verificar si el usuario es valido
                
                # Verificamos si el usuario tiene acceso iterando en la lista de inscripciones. 
                for inscripcion in inscripciones:
                  if inscripcion.curso == curso_del_estudiante and inscripcion.dni == ingrese_el_dni:
                    alumno_valido = True
                    break  # Salir del bucle si el usuario es válido

                if alumno_valido:
                   
                   #Se aclara al profesor que la nota es -1, tambien para asegurarse que el proceso se realizo bien. 
                   print (f"la nota del estudiante {inscripcion.nombre} es: {inscripcion.nota}")
                   inscripcion.nota=-1
                   print(f"Con los cambios realizados, la nota actual de {inscripcion.nombre} es {inscripcion.nota} ")
                   print(inscripciones)
                   
                   #Verifica la cantidad de objetos en la lista inscripciones
                   cantidad_inscripciones = len(inscripciones)

                   if cantidad_inscripciones == 0:
                      print("La lista de inscripciones está vacía. No se realizarán cambios en el archivo.")
                   else:
                     # Abre el archivo en modo escritura y sobreescribe los datos
                      with open("Inscripciones.txt", "w") as archivo:
                          for inscripcion in inscripciones:
                              #Escribe los atributos de cada objeto en el formato deseado
                              archivo.write(
                               f"{inscripcion.fecha},{inscripcion.nombre},{inscripcion.dni},"
                               f"{inscripcion.profesor},{inscripcion.curso},"
                               f"{inscripcion.division},{inscripcion.nota}\n"
                                 )
                      print(f"Se sobreescribió el archivo con {cantidad_inscripciones} inscripciones.")
                
     


    elif op1 == 3:
        print("Saliendo del programa.")
        break  #SALE DEL BLOQUE PRINCIPAL Y DEL PROGRAMA

    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")



