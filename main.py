from json import load, decoder, dump
lista_notas =[]

data = {
    'alumnos_creados':[],
    'docentes_creados':[]
}

class Persona():

    def __init__(self,nombre,apellido):

        self.nombre = nombre
        self.apellido =apellido
class Docente(Persona):

    def __init__(self,nombre,apellido,edad,Dni):
        Persona.__init__(self,nombre,apellido)

        self.edad = edad
        self.Dni = Dni


class Alumno(Persona):

    def __init__(self,nombre,apellido,lista_notas,nota_mayor,nota_menor,promedio):
        Persona.__init__(self,nombre,apellido)
        self.lista_notas = lista_notas
        self.nota_mayor = nota_mayor
        self.nota_menor = nota_menor
        self.promedio = promedio
class Registro():

 
    def menu(self):
        while True:
            print('''
                Bienvenido al registro de alumnos y docentes : 
                ¿Que desea hacer?
                1) Registrar Alumno
                2) Registrar Docente
                3) Salir del programa\n
            ''')

            opcion = input("> ")

            if opcion == "1":

                
                self.cargar_alumnos()
                self.registro_alumno()
            elif opcion == "2": 

                self.cargar_docente()
                self.registro_docente()
            
            elif opcion == "3":
                print("\nGracias por usar el programa")
                quit()
            else:
                print("\nIntroduciste una opcion incorrecta")



    def cargar_alumnos(self):

        try:
            archivo = open("registro_alumno.json","r")

            data["datos_creados"] = load(archivo)

            archivo.close()

        except FileNotFoundError:
            
            print("\n Creando registro de datos: \n")

            archivo = open("registro_alumno.json","w")

            archivo.close()

        except decoder.JSONDecodeError:

            print("\nNo hay registros creados\n")



    def cargar_docente(self):
        try:
            archivo = open("registro_docente.json","r")

            data["datos_creados"] = load(archivo)

            archivo.close()
        except FileNotFoundError:
            print("\n Creando registro de datos: \n")

            archivo = open("registro_docente.json","w")

            archivo.close()

        except decoder.JSONDecodeError:

            print("\nNo hay registros creados\n")


    def registro_alumno(self):

            
        nombre= input("\nIngrese el nombre del alumno que desea registrar:\n")

        apellido =input(f'\n¿Cuál es el apellido del alumno {nombre}?\n')

        while True:
            try:
                cantidad_notas = int(input(f"\n¿Cuántas notas tiene el alumno ?\n"))

                for notas in range(cantidad_notas):
                    notas = int(input(f"Nota {notas+1}: \n"))

                    lista_notas.append(notas)
                        
                break
                
            except (TypeError, ValueError) :

                print('Ocurrio un problema: El valor ingresado es incorrecto\nIngrese un dato correcto')
        
        suma_notas = 0
        promedio= 0
        for i in lista_notas:

            suma_notas= suma_notas + i
            promedio = suma_notas / len(lista_notas)

            nota_menor= min(lista_notas)
            nota_mayor =max(lista_notas)

        # print("\n-------------Lista de Notas---------------------\n")
        # print(lista_notas)
        # print()
        # print(f'\nEl promedio es: {promedio}')
        # print(f"\n'Nota mayor: {nota_mayor}'")
        # print(f"\n'Nota menor: {nota_menor}'\n")
    
        alumno = Alumno(nombre, apellido, lista_notas, nota_mayor,nota_menor,promedio)


        datos = {
            "Nombre": alumno.nombre,
            "Apellido": alumno.apellido,
            "Lista de notas": alumno.lista_notas,
            "Nota mayor": int(alumno.nota_mayor),
            "Nota menor": int(alumno.nota_menor),
            "Promedio del Alumno":int(alumno.promedio)
         }


        self.guardar_alumnos(datos)
        print(f'\nSe creó con éxito al alumno {nombre} {apellido}')

    def registro_docente(self):


        nombre = input("\nIngrese el nombre del docente que desea registrar: \n")
        apellido = input(f"\nIngrese el apellido del docente {nombre}:\n")


        while True:
            try:
                edad = int(input(f"\nIngrese la edad del docente {nombre}: \n"))
                
            except ValueError:
                print("\nOcurrio un problema, por favor ingrese una edad correcta\n")

            break

        while True:
            try:

                Dni = int(input(f"\nIngrese el DNI del docente {nombre} {apellido}: \n"))
                
            except ValueError:
                
                print("\nOcurrió un problema, por favor ingrese el dato correctamente.\n")
                
            break
        
        docente = Docente(nombre, apellido, edad, Dni)

        datos = {
            "Nombre": docente.nombre,
            "Apellido": docente.apellido,
            "Edad": int(docente.edad),
            "Dni": int(docente.Dni)
        }

        self.guardar_docente(datos)
        print(f'\nSe creó con exito al docente {nombre} {apellido}')
    
    def guardar_alumnos(self,datos):
        
        data['alumnos_creados'].append(datos)

        almns = data['alumnos_creados']

        archivo = open("registro_alumno.json","w")

        dump(almns,archivo, indent = 4)
        
        archivo.close()

    def guardar_docente(self,datos):
        
        data['docentes_creados'].append(datos)

        almns = data['docentes_creados']

        archivo = open("registro_docente.json","w")

        dump(almns,archivo, indent = 4)
        
        archivo.close()

class Inicio(Registro):

    def __init__(self):

        try:
            
            self.menu()
            
            
        
        except KeyboardInterrupt:

            print("\nAplicacion Interrumpida")


Inicio()

