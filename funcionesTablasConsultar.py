import funcionesRead as fr

def ingresar_informacion_foro():
  print("Ingresar Informacion para Consultar Foro")
  id_foro = input("Ingrese el ID del foro: ")
  fr.consultar_por_id('foro', id_foro)


def ingresar_informacion_comentario():
  print("Ingresar Información para Consultar Comentario")
  id_comentario = input("Ingrese el ID del comentario: ")
  fr.consultar_por_id('comentario', id_comentario)


def ingresar_informacion_modulo():
  print("Ingresar Información para Consultar Módulo")
  id_modulo = input("Ingrese el ID del módulo: ")
  fr.consultar_por_id('modulo', id_modulo)



def ingresar_informacion_profesor():
  print("Ingresar Información para Consultar Profesor")
  usuario_espol = input("Ingrese el Usuario ESPOL del profesor: ")
  fr.consultar_por_id('profesor', usuario_espol)



def ingresar_informacion_estudiante():
  print("Ingresar Información para Consultar Estudiante")
  usuario_espol = input("Ingrese el Usuario ESPOL del estudiante: ")
  fr.consultar_por_id('estudiante', usuario_espol)



def ingresar_informacion_anuncio():
  print("Ingresar Información para Consultar Anuncio")
  id_anuncio = input("Ingrese el ID del anuncio: ")
  fr.consultar_por_id('anuncio', id_anuncio)




def ingresar_informacion_curso():
  print("Ingresar Información para Consultar Curso")
  id_curso = input("Ingrese el ID del curso: ")
  fr.consultar_por_id('curso', id_curso)



def ingresar_informacion_evaluacion():
  print("Ingresar Informacion para Consultar Evaluacion")
  id_evaluacion = input("ID: ")
  fr.consultar_por_id('evaluacion', id_evaluacion)



def ingresar_informacion_facultad():
  print("Ingresar Información para Consultar facultad")
  id_facultad = input("Ingrese el ID de la facultad: ")
  fr.consultar_por_id('facultad', id_facultad)



def ingresar_informacion_mensaje_enviado():
  print("Ingresar Información para Consultar mensaje")
  id_mensaje = input("Ingrese el ID del mensaje: ")
  fr.consultar_por_id('enviado', id_mensaje)



def ingresar_informacion_mensaje_recibido():
  print("Ingresar Información para Consultar mensaje")
  id_mensaje = input("Ingrese el ID del mensaje: ")
  fr.consultar_por_id('recibido', id_mensaje)


def ingresar_informacion_entrega():
  print("Ingresar Informacion para Consultar Entrega")
  id_entrega = input("ID Entrega: ")
  fr.consultar_por_id('entrega', id_entrega)

def ingresar_informacion_carrera():
  print("Ingresar Informacion para Consultar Carrera")
  id_carrera = input("ID: ")
  fr.consultar_por_id('carrera', id_carrera)

