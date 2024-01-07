import funcionesAdd as fa

def ingresar_informacion_foro():
  print("Ingresar Informacion para crear Foro")
  id_foro = input("Ingrese el ID del foro: ")
  titulo = input("Ingrese el título del foro: ")
  archivo = input("Ingrese el nombre del archivo: ")
  texto = input("Ingrese el texto del foro: ")
  fecha = input("Ingrese la fecha del foro: ")
  tiempo_disponibilidad = input("Ingrese el tiempo de disponibilidad del foro: ")
  id_curso = input("Ingrese el ID del curso al que pertenece el foro: ")
  foro = (int(id_foro),titulo,archivo,texto,fecha,tiempo_disponibilidad,int(id_curso))
  fa.insertar_foro(foro)


def ingresar_informacion_comentario():
  print("Ingresar Información para crear Comentario")
  id_comentario = input("Ingrese el ID del comentario: ")
  descripcion = input("Ingrese la descripción del comentario: ")
  id_del_foro = input("Ingrese el ID del foro: ")
  comentario = (int(id_comentario), descripcion, int(id_del_foro))
  fa.insertar_comentario(comentario)

def ingresar_informacion_modulo():
  print("Ingresar Información para crear Módulo")
  id_modulo = input("Ingrese el ID del módulo: ")
  contenido = input("Ingrese el contenido del módulo: ")
  id_del_curso = input("Ingrese el ID del curso al que pertenece el módulo: ")
  modulo = (int(id_modulo), contenido, int(id_del_curso))
  fa.insertar_modulo(modulo)

def ingresar_informacion_profesor():
  print("Ingresar Información para crear Profesor")
  usuario_espol = input("Ingrese el Usuario ESPOL del profesor: ")
  nombre = input("Ingrese el nombre del profesor: ")
  apellido = input("Ingrese el apellido del profesor: ")
  facultad = input("Ingrese el ID de la Facultad: ")
  profesor = (usuario_espol, nombre, apellido, int(facultad))
  fa.insertar_profesor(profesor)

def ingresar_informacion_estudiante():
  print("Ingresar Información para crear Estudiante")
  usuario_espol = input("Ingrese el Usuario ESPOL del estudiante: ")
  matricula = input("Ingrese la matrícula del estudiante: ")
  carreraID = input("Ingrese el ID de la carrera del estudiante: ")
  nombre = input("Ingrese el nombre del estudiante: ")
  apellido = input("Ingrese el apellido del estudiante: ")
  estudiante = (usuario_espol, nombre, apellido, int(matricula), int(carreraID))
  fa.insertar_estudiante(estudiante)

def ingresar_informacion_anuncio():
  print("Ingresar Información para crear Anuncio")
  id_anuncio = input("Ingrese el ID del anuncio: ")
  fecha_publicacion = input("Ingrese la fecha de publicación del anuncio: ")
  autor = input("Ingrese el autor del anuncio: ")
  titulo = input("Ingrese el título del anuncio: ")
  texto = input("Ingrese el texto del anuncio: ")
  id_curso = input("Ingrese el ID del curso al que pertenece el anuncio: ")
  profesor = input("Ingrese el nombre del profesor que publica el anuncio: ")
  anuncio = (int(id_anuncio), fecha_publicacion, autor, titulo, texto, int(id_curso), profesor)
  fa.insertar_anuncio(anuncio)
  

def ingresar_informacion_curso():
  print("Ingresar Información para crear Curso")
  id_curso = input("Ingrese el ID del curso: ")
  paralelo = input("Ingrese el paralelo del curso: ")
  periodo = input("Ingrese el período académico del curso: ")
  materia = input("Ingrese la materia del curso: ")
  curso = (int(id_curso),int(paralelo),periodo,materia)
  fa.insertar_curso(curso)

def ingresar_informacion_evaluacion():
  print("Ingresar Informacion para crear Evaluacion")
  id_evaluacion = input("ID: ")
  tipo = input("Tipo: ")
  titulo = input("Titulo: ")
  comentario = input("Comentario: ")
  calificacion = input("Calificacion: ")
  profesor = input("Profesor: ")
  id_curso = input("ID del curso: ")
  evaluacion = (int(id_evaluacion), tipo, titulo, comentario, float(calificacion), profesor, int(id_curso))
  fa.insertar_evaluacion(evaluacion)

def ingresar_informacion_facultad():
  print("Ingresar Información para crear facultad")
  id_facultad = input("Ingrese el ID de la facultad: ")
  nombre_facultad = input("Ingrese el nombre de la facultad: ")
  facultad = (int(id_facultad), nombre_facultad)
  fa.insertar_facultad(facultad)

def ingresar_informacion_mensaje_enviado():
  print("Ingresar Información para crear y enviar mensaje")
  id_mensaje = input("Ingrese el ID del mensaje: ")
  texto_mensaje = input("Ingrese el texto del mensaje: ")
  fecha_envio = input("Ingrese la fecha de envío del mensaje: ")
  destinatario = input("Ingrese el destinatario del mensaje: ")
  autor = input("Ingrese el autor del mensaje: ")
  mensajeEnviado = (int(id_mensaje), texto_mensaje, fecha_envio, destinatario,autor)
  fa.insertar_mensaje_enviado(mensajeEnviado)

def ingresar_informacion_mensaje_recibido():
  print("Ingresar Información para crear y recibir mensaje")
  id_mensaje = input("Ingrese el ID del mensaje: ")
  texto_mensaje = input("Ingrese el texto del mensaje: ")
  fecha_envio = input("Ingrese la fecha de envío del mensaje: ")
  destinatario = input("Ingrese el destinatario del mensaje: ")
  autor = input("Ingrese el autor del mensaje: ")
  mensajeRecibido = (int(id_mensaje),texto_mensaje,fecha_envio,destinatario,autor)
  fa.insertar_mensaje_recibido(mensajeRecibido)

def ingresar_informacion_entrega():
  print("Ingresar Informacion para crear Entrega")
  id_entrega = input("ID Entrega: ")
  fecha_entrega = input("Fecha de Entrega: ")
  fecha_publicacion = input("Fecha de publicación: ")
  tiempo_disponibilidad = input("Tiempo de Disponibilidad: ")
  fecha_subida = input("Fecha de subida: ")
  esta_pendiente = input("¿Está Pendiente? (Sí/No): ")
  id_evaluacion = input("ID de Evaluación: ")
  entrega = (int(id_entrega),fecha_entrega,fecha_publicacion,tiempo_disponibilidad,fecha_subida,bool(esta_pendiente),int(id_evaluacion)) 
  fa.insertar_entrega(entrega)

def ingresar_informacion_carrera():
  print("Ingresar Informacion para crear Carrera")
  id_carrera = input("ID: ")
  nombre_carrera = input("Nombre de la Carrera: ")
  carrera = (int(id_carrera),nombre_carrera)
  fa.insertar_carrera(carrera)
  
