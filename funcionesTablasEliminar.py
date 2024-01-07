import funcionesDelete as fd
import funcionesRead as fr

def ingresar_informacion_foro():
  print("Ingresar Informacion para Eliminar Foro")
  id_foro = input("Ingrese el ID del foro: ")
  fd.eliminar_por_id('foro', id_foro)


def ingresar_informacion_comentario():
  print("Ingresar Información para Eliminar Comentario")
  id_comentario = input("Ingrese el ID del comentario: ")
  fd.eliminar_por_id('comentario', id_comentario)


def ingresar_informacion_modulo():
  print("Ingresar Información para Eliminar Módulo")
  id_modulo = input("Ingrese el ID del módulo: ")
  fd.eliminar_por_id('modulo', id_modulo)



def ingresar_informacion_profesor():
  print("Ingresar Información para Eliminar Profesor")
  usuario_espol = input("Ingrese el Usuario ESPOL del profesor: ")
  fd.eliminar_por_id('profesor', usuario_espol)



def ingresar_informacion_estudiante():
  print("Ingresar Información para Eliminar Estudiante")
  usuario_espol = input("Ingrese el Usuario ESPOL del estudiante: ")
  fd.eliminar_por_id('estudiante', usuario_espol)



def ingresar_informacion_anuncio():
  print("Ingresar Información para Eliminar Anuncio")
  id_anuncio = input("Ingrese el ID del anuncio: ")
  fd.eliminar_por_id('anuncio', id_anuncio)


def ingresar_informacion_curso():
  print("Ingresar Información para Eliminar Curso")
  id_curso = input("Ingrese el ID del curso: ")
  fd.eliminar_por_id('curso', id_curso)



def ingresar_informacion_evaluacion():
  print("Ingresar Informacion para Eliminar Evaluacion")
  id_evaluacion = input("ID: ")
  fd.eliminar_por_id('evaluacion', id_evaluacion)



def ingresar_informacion_facultad():
  print("Ingresar Información para Eliminar facultad")
  id_facultad = input("Ingrese el ID de la facultad: ")
  fd.eliminar_por_id('facultad', id_facultad)



def ingresar_informacion_mensaje_enviado():
  print("Ingresar Información para Eliminar mensaje")
  id_mensaje = input("Ingrese el ID del mensaje: ")
  fd.eliminar_por_id('enviado', id_mensaje)



def ingresar_informacion_mensaje_recibido():
  print("Ingresar Información para Eliminar mensaje")
  id_mensaje = input("Ingrese el ID del mensaje: ")
  fd.eliminar_por_id('recibido', id_mensaje)


def ingresar_informacion_entrega():
  print("Ingresar Informacion para Eliminar Entrega")
  id_entrega = input("ID Entrega: ")
  fd.eliminar_por_id('entrega', id_entrega)

def ingresar_informacion_carrera():
  print("Ingresar Informacion para Eliminar Carrera")
  id_carrera = input("ID: ")
  fd.eliminar_por_id('carrera', id_carrera)
