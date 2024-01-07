import mysql.connector
import funcionesTablas as ft



def conectar():
    config = {
        'user': 'tu_usuario',
        'password': 'tu_contraseña',
        'host': 'localhost',
        'database': 'tu_base_de_datos',
        'raise_on_warnings': True
    }


    conexion = mysql.connector.connect(**config)
    return conexion, conexion.cursor()

def cerrar_conexion(conexion, cursor):
    if conexion.is_connected():
        cursor.close()
        conexion.close()

def insertar_foro(foro):
    try:
        conexion, cursor = conectar()

        # Insertar datos en la tabla foro
        cursor.execute("""
            INSERT INTO foro
            (idforo, titulo, archivo, texto, fecha, tiempodisponibilidad, idcurso)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, foro) 
      #foro

        # Confirmar los cambios y cerrar la conexión
        conexion.commit()
        print("Datos del foro insertados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cerrar_conexion(conexion, cursor)

def insertar_comentario(comentario):
    #conexion, cursor = conectar()
    try:
        conexion, cursor = conectar()


        # Insertar datos en la tabla comentario
        cursor.execute("""
            INSERT INTO comentario
            (idcomentario, descripcion, foro)
            VALUES (%s, %s, %s)
        """, comentario)
        
        # Confirmar los cambios y cerrar la conexión
        conexion.commit()
        print("Datos del comentario insertados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cerrar_conexion(conexion, cursor)

# Ejemplo de uso



def insertar_modulo(modulo):
  try:
      conexion, cursor = conectar()

      # Insertar datos en la tabla modulo
      cursor.execute("""
          INSERT INTO modulo
          (idcurso,idmodulo, contenidodelcurso)
          VALUES (%s, %s, %s)
      """, modulo)

      # Confirmar los cambios y cerrar la conexión
      conexion.commit()
      print("Datos del módulo insertados correctamente.")

  except mysql.connector.Error as err:
      print(f"Error: {err}")

  finally:
      cerrar_conexion(conexion, cursor)

def insertar_profesor(profesor):
  try:
      conexion, cursor = conectar()

      # Insertar datos en la tabla profesor
      cursor.execute("""
          INSERT INTO profesor
          (usuarioespol, nombre, apellido, facultad)
          VALUES (%s, %s, %s, %s)
      """,profesor)
      
      # Confirmar los cambios y cerrar la conexión
      conexion.commit()
      print("Datos del profesor insertados correctamente.")

  except mysql.connector.Error as err:
      print(f"Error: {err}")

  finally:
      cerrar_conexion(conexion, cursor)

def insertar_estudiante(estudiante):
  try:
      conexion, cursor = conectar()

      # Insertar datos en la tabla estudiante
      cursor.execute("""
          INSERT INTO estudiante
          (usuarioespol, nombre, apellido, matricula, carrera)
          VALUES (%s, %s, %s, %s, %s)
      """, estudiante)

      # Confirmar los cambios y cerrar la conexión
      conexion.commit()
      print("Datos del estudiante insertados correctamente.")

  except mysql.connector.Error as err:
      print(f"Error: {err}")

  finally:
      cerrar_conexion(conexion, cursor)

def insertar_anuncio(anuncio):
  try:
      conexion, cursor = conectar()

      # Insertar datos en la tabla anuncio
      cursor.execute("""
          INSERT INTO anuncio
          (idanuncio, fechapublicacion, autor, idcurso,profesor,autor,titulo,texto)
          VALUES (%s, %s, %s, %s, %s, %s, %s,%S)
      """, anuncio)

      # Confirmar los cambios y cerrar la conexión
      conexion.commit()
      print("Datos del anuncio insertados correctamente.")

  except mysql.connector.Error as err:
      print(f"Error: {err}")

  finally:
      cerrar_conexion(conexion, cursor)


def insertar_curso(curso):
  try:
      conexion, cursor = conectar()

      # Insertar datos en la tabla curso
      cursor.execute("""
          INSERT INTO curso
          (idcurso, paralelo, materia, periodoacademico)
          VALUES (%s, %s, %s, %s)
      """, curso)

      # Confirmar los cambios y cerrar la conexión
      conexion.commit()
      print("Datos del curso insertados correctamente.")

  except mysql.connector.Error as err:
      print(f"Error: {err}")

  finally:
      cerrar_conexion(conexion, cursor)


def insertar_evaluacion(evaluacion):
  try:
      # Conectar a la base de datos
      conexion, cursor = conectar()
      

      # Construir la consulta INSERT
      consulta_insert = "INSERT INTO evaluacion (idevaluacion, tipo, titulo, comentario, calificacion, profesor, idcurso) VALUES (%s, %s, %s, %s, %s, %s, %s)"

      # Ejecutar la consulta
      cursor.execute(consulta_insert, evaluacion)

      # Confirmar la transacción
      conexion.commit()


  except mysql.connector.Error as error:
      print(f"Error al insertar en evaluacion: {error}")

  finally:
      # Cerrar la conexión
      cerrar_conexion(conexion, cursor)


def insertar_facultad(facultad):
  try:
       # Conectar a la base de datos
      conexion,cursor = conectar()


      # Construir la consulta INSERT
      consulta_insert = "INSERT INTO facultad (id_facultad, nombre_facultad) VALUES (%s, %s)"

      # Ejecutar la consulta
      cursor.execute(consulta_insert, facultad)

      # Confirmar la transacción
      conexion.commit()

  except mysql.connector.Error as error:
      print(f"Error al insertar en facultad: {error}")

  finally:
      # Cerrar la conexión
      cerrar_conexion(conexion, cursor)


def insertar_mensaje_enviado(enviado):
  try:
       # Conectar a la base de datos
      conexion, cursor = conectar()

      # Construir la consulta INSERT
      consulta_insert = "INSERT INTO mensaje_enviado (idenviado, texto, fechaenvio, destinatario, autor) VALUES (%s, %s, %s, %s, %s)"

      # Ejecutar la consulta
      cursor.execute(consulta_insert, enviado)

      # Confirmar la transacción
      conexion.commit()

  except mysql.connector.Error as error:
      print(f"Error al insertar en mensaje_enviado: {error}")

  finally:
      # Cerrar la conexión
      cerrar_conexion(conexion, cursor)


def insertar_mensaje_recibido(recibir):
  try:
      # Conectar a la base de datos
      conexion, cursor = conectar()


      # Construir la consulta INSERT
      consulta_insert = "INSERT INTO mensaje_recibido (idrecibido, texto, fechaenvio, destinatario, autor) VALUES (%s, %s, %s, %s, %s)"

      # Ejecutar la consulta
      cursor.execute(consulta_insert, recibir)

      # Confirmar la transacción
      conexion.commit()

  except mysql.connector.Error as error:
      print(f"Error al insertar en mensaje_recibido: {error}")

  finally:
      # Cerrar la conexión
      cerrar_conexion(conexion, cursor)


def insertar_entrega(entrega):
  try:
       # Conectar a la base de datos
      conexion, cursor = conectar()


      # Construir la consulta INSERT
      consulta_insert = "INSERT INTO entrega (identrega, fechaentrega, fechapublicacion, tiempodisponibilidad, fechasubida, estapendiente, idevaluacion) VALUES (%s, %s, %s, %s, %s, %s, %s)"

      # Ejecutar la consulta
      cursor.execute(consulta_insert, entrega)

      # Confirmar la transacción
      conexion.commit()
      
  except mysql.connector.Error as error:
      print(f"Error al insertar en la entrega: {error}")

  finally:
      # Cerrar la conexión
      cerrar_conexion(conexion, cursor)



def insertar_carrera(carrera):
  try:
       # Conectar a la base de datos
      conexion,cursor = conectar()


      # Construir la consulta INSERT
      consulta_insert = "INSERT INTO carrera (id_carrera, nombrecarrera) VALUES (%s, %s)"

      # Ejecutar la consulta
      cursor.execute(consulta_insert, carrera)

      # Confirmar la transacción
      conexion.commit()

  except mysql.connector.Error as error:
      print(f"Error al insertar en la carrera: {error}")

  finally:
      # Cerrar la conexión
      cerrar_conexion(conexion, cursor)
