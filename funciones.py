import funcionesTablas as ft
import funcionesTablasConsultar as fr
import funcionesTablasEliminar as fd
import funcionesTablasUpdate as fu


def añadir():
  print("Seleccionar la opcion a Añadir")
  print_opciones_tablas()
  ejecutar_opcion_tablas_add(seleccionar_opcion_tablas())
  
  
  
def consultar():
  print("Seleccionar la opcion a Consultar")
  print_opciones_tablas()
  ejecutar_opcion_tablas_consultar(seleccionar_opcion_tablas())

def editar():
  print("Seleccionar la opcion a editar")
  print_opciones_tablas()
  ejecutar_opcion_tablas_editar(seleccionar_opcion_tablas())

  

def eliminar():
  print("Seleccionar la opcion a Eliminar")
  print_opciones_tablas()
  ejecutar_opcion_tablas_eliminar(seleccionar_opcion_tablas())



def imprimir_opciones():
  print("¡Bienvenido a la administrador de datos de Aula Virtual!")
  print("Opciones:")
  print("1. Añadir")
  print("2. Consultar")
  print("3. Editar")
  print("4. Eliminar")

def print_opciones_tablas():
  opciones = [
      "Foro",
      "Comentario",
      "Modulo",
      "Profesor",
      "Estudiante",
      "Anuncio",
      "Curso",
      "Evaluacion",
      "Entrega",
      "Carrera",
      "Facultad",
      "Mensaje Enviado",
      "Mensaje Recibido"
  ]
  
  print("Opciones:")
  for i, opcion in enumerate(opciones, start=1):
      print(f"{i}. {opcion}")

def seleccionar_opcion():
  while True:
      try:
          opcion = int(input("Por favor, elija una opción del 1 al 4: "))
          if 1 <= opcion <= 4:
              return opcion
          else:
              print("Opción no válida. Por favor, elija un número del 1 al 4.")
      except ValueError:
          print("Por favor, ingrese un valor valido.")


def ejecutar_opcion(opcion):
  if opcion == 1:
      añadir()
  elif opcion == 2:
      consultar()
  elif opcion == 3:
      editar()
  elif opcion == 4:
      eliminar()
  else:
      print("Opción no válida. Por favor, elija una opción del 1 al 4.")


def seleccionar_opcion_tablas():
  while True:
      try:
          opcion = int(input("Por favor, elija una opción del 1 al 13: "))
          if 1 <= opcion <= 13:
              return opcion
          else:
              print("Opción no válida. Por favor, elija un número del 1 al 13.")
      except ValueError:
          print("Por favor, ingrese un valor valido.")


#aqui
def ejecutar_opcion_tablas_add(opcion):
  if opcion == 1:
      ft.ingresar_informacion_foro()
  elif opcion == 2:
      ft.ingresar_informacion_comentario()
  elif opcion == 3:
      ft.ingresar_informacion_modulo()
  elif opcion == 4:
      ft.ingresar_informacion_profesor()
  elif opcion == 5:
      ft.ingresar_informacion_estudiante()
  elif opcion == 6:
      ft.ingresar_informacion_anuncio()
  elif opcion == 7:
      ft.ingresar_informacion_curso()
  elif opcion == 8:
      ft.ingresar_informacion_evaluacion()
  elif opcion == 9:
      ft.ingresar_informacion_entrega()
  elif opcion == 10:
      ft.ingresar_informacion_carrera()
  elif opcion == 11:
      ft.ingresar_informacion_facultad()
  elif opcion == 12:
    ft.ingresar_informacion_mensaje_enviado()
  elif opcion == 13:
    ft.ingresar_informacion_mensaje_recibido()
  else:
      print("Opción no válida. Por favor, elija una opción del 1 al 13.")
      
def ejecutar_opcion_tablas_consultar(opcion):
  if opcion == 1:
    fr.ingresar_informacion_foro()
  elif opcion == 2:
    fr.ingresar_informacion_comentario()
  elif opcion == 3:
    fr.ingresar_informacion_modulo()
  elif opcion == 4:
    fr.ingresar_informacion_profesor()
  elif opcion == 5:
    fr.ingresar_informacion_estudiante()
  elif opcion == 6:
    fr.ingresar_informacion_anuncio()
  elif opcion == 7:
    fr.ingresar_informacion_curso()
  elif opcion == 8:
    fr.ingresar_informacion_evaluacion()
  elif opcion == 9:
    fr.ingresar_informacion_entrega()
  elif opcion == 10:
    fr.ingresar_informacion_carrera()
  elif opcion == 11:
    fr.ingresar_informacion_facultad()
  elif opcion == 12:
    fr.ingresar_informacion_mensaje_enviado()
  elif opcion == 13:
    fr.ingresar_informacion_mensaje_recibido()
  else:
    print("Opción no válida. Por favor, elija una opción del 1 al 13.")
    
      
def ejecutar_opcion_tablas_eliminar(opcion):
  if opcion == 1:
    fd.ingresar_informacion_foro()
  elif opcion == 2:
    fd.ingresar_informacion_comentario()
  elif opcion == 3:
    fd.ingresar_informacion_modulo()
  elif opcion == 4:
    fd.ingresar_informacion_profesor()
  elif opcion == 5:
    fd.ingresar_informacion_estudiante()
  elif opcion == 6:
    fd.ingresar_informacion_anuncio()
  elif opcion == 7:
    fd.ingresar_informacion_curso()
  elif opcion == 8:
    fd.ingresar_informacion_evaluacion()
  elif opcion == 9:
    fd.ingresar_informacion_entrega()
  elif opcion == 10:
    fd.ingresar_informacion_carrera()
  elif opcion == 11:
    fd.ingresar_informacion_facultad()
  elif opcion == 12:
    fd.ingresar_informacion_mensaje_enviado()
  elif opcion == 13:
    fd.ingresar_informacion_mensaje_recibido()
  else:
    print("Opción no válida. Por favor, elija una opción del 1 al 13.")
      
      
      
      
def ejecutar_opcion_tablas_editar(opcion):
  if opcion == 1:
    fu.ingresar_informacion_foro()
  elif opcion == 2:
    fu.ingresar_informacion_comentario()
  elif opcion == 3:
    fu.ingresar_informacion_modulo()
  elif opcion == 4:
    fu.ingresar_informacion_profesor()
  elif opcion == 5:
    fu.ingresar_informacion_estudiante()
  elif opcion == 6:
    fu.ingresar_informacion_anuncio()
  elif opcion == 7:
    fu.ingresar_informacion_curso()
  elif opcion == 8:
    fu.ingresar_informacion_evaluacion()
  elif opcion == 9:
    fu.ingresar_informacion_entrega()
  elif opcion == 10:
    fu.ingresar_informacion_carrera()
  elif opcion == 11:
    fu.ingresar_informacion_facultad()
  elif opcion == 12:
    fu.ingresar_informacion_mensaje_enviado()
  elif opcion == 13:
    fu.ingresar_informacion_mensaje_recibido()
  else:
    print("Opción no válida. Por favor, elija una opción del 1 al 13.")
      
