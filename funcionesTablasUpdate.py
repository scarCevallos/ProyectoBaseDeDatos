import funcionesUpdate as fu

def ingresar_informacion_foro():
  print("Ingresar Informacion para Actualizar Foro")
  id_foro = input("Ingrese el ID del foro: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el nuevo valor: ")
  fu.actualizar_campo_por_id('foro', id_foro, campo,valor)


def ingresar_informacion_comentario():
  print("Ingresar Información para Actualizar Comentario")
  id_comentario = input("Ingrese el ID del comentario: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el nuevo valor: ")
  fu.actualizar_campo_por_id('comentariocomentario', id_comentario, campo, valor)


def ingresar_informacion_modulo():
  print("Ingresar Información para Actualizar Módulo")
  id_modulo = input("Ingrese el ID del módulo: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el nuevo valor: ")
  fu.actualizar_campo_por_id('modulo', id_modulo, campo, valor)



def ingresar_informacion_profesor():
  print("Ingresar Información para Actualizar Profesor")
  usuario_espol = input("Ingrese el Usuario ESPOL del profesor: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el nuevo valor: ")
  fu.actualizar_campo_por_usuario('profesor', usuario_espol, campo, valor)


def ingresar_informacion_estudiante():
  print("Ingresar Información para Actualizar Estudiante")
  usuario_espol = input("Ingrese el Usuario ESPOL del estudiante: ")  
  print("Ingresar Campo a Actualizar")  
  campo = input("Ingrese el campo: ")  
  valor = input("Ingrese el nuevo valor: ")  
  fu.actualizar_campo_por_usuario('estudiante',usuario_espol, campo,valor)


def ingresar_informacion_anuncio():
  print("Ingresar Información para Actualizar Anuncio")
  id_anuncio = input("Ingrese el ID del anuncio: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el nuevo valor: ")
  fu.actualizar_campo_por_id('anuncio', id_anuncio, campo, valor)

def ingresar_informacion_curso():
  print("Ingresar Información para Actualizar Curso")
  id_curso = input("Ingrese el ID del curso: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el nuevo valor: ")
  fu.actualizar_campo_por_id('curso', id_curso, campo,valor)


def ingresar_informacion_evaluacion():
  print("Ingresar Informacion para Actualizar Evaluacion")
  id_evaluacion = input("ID: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el nuevo valor: ")
  fu.actualizar_campo_por_id('evaluacion', id_evaluacion, campo, valor)


def ingresar_informacion_facultad():
  print("Ingresar Información para Actualizar Facultad")
  id_facultad = input("Ingrese el ID de la facultad: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el nuevo valor: ")
  fu.actualizar_campo_por_id('facultad', id_facultad, campo, valor)


def ingresar_informacion_mensaje_enviado():
  print("Ingresar Información para Actualizar mensaje")
  id_mensaje = input("Ingrese el ID del mensaje: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el valor: ")
  fu.actualizar_campo_por_id('enviado', id_mensaje, campo, valor)


def ingresar_informacion_mensaje_recibido():
  print("Ingresar Información para Actualizar mensaje")
  id_mensaje = input("Ingrese el ID del mensaje: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el valor: ")
  fu.actualizar_campo_por_id('recibido', id_mensaje, campo, valor)

def ingresar_informacion_entrega():
  print("Ingresar Informacion para Actualizar Entrega")
  id_entrega = input("Ingrese el ID de la Entrega: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el valor: ")
  fu.actualizar_campo_por_id('entrega', id_entrega, campo, valor)


def ingresar_informacion_carrera():
  print("Ingresar Informacion para Actualizar Carrera")
  id_carrera = input("Ingrese el ID de la Carrera: ")
  print("Ingresar Campo a Actualizar")
  campo = input("Ingrese el campo: ")
  valor = input("Ingrese el valor: ")
  fu.actualizar_campo_por_id('carrera', id_carrera, campo, valor)