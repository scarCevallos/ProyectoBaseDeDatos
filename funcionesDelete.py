import mysql.connector

def eliminar_por_id(tabla, id_a_eliminar):
    try:
        listaTablas=["foro","comentario","modulo","anuncio","curso","evaluacion","entrega","carrera","facultad","enviado","recibido","profesor","estudiante"]
        listaids=["idforo","idcomentario","idmodulo","idanuncio","idcurso","idevaluacion","identrega","id_carrera","id_facultad","idenviado", "idrecibido","usuarioespol","usuarioespol"]

        id = "Nombre del id"
        for i in range(len(listaTablas)):
            if tabla == listaTablas[i]:
                id = listaids[i]
            break;  
          
        conexion = mysql.connector.connect(
            'user': 'tu_usuario',
            'password': 'tu_contraseña',
            'host': 'localhost',
            'database': 'tu_base_de_datos',
            'raise_on_warnings': True
        )
        cursor = conexion.cursor()

        # Ejecutar la eliminación
        consulta = f"DELETE FROM {tabla} WHERE {id}  = %s"
        cursor.execute(consulta, (id_a_eliminar,))

        # Confirmar los cambios y cerrar la conexión
        conexion.commit()
        print(f"Fila con ID {id_a_eliminar} eliminada correctamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()



def eliminar_por_usuario(tabla, usuarioEliminar):
  try:
      conexion = mysql.connector.connect(
            'user': 'tu_usuario',
            'password': 'tu_contraseña',
            'host': 'localhost',
            'database': 'tu_base_de_datos',
            'raise_on_warnings': True
        )
      cursor = conexion.cursor()

      # Ejecutar la eliminación
      consulta = f"DELETE FROM {tabla} WHERE usuarioespol = %s"
      cursor.execute(consulta, (usuarioEliminar,))

      # Confirmar los cambios y cerrar la conexión
      conexion.commit()
      print(f"Fila con usuario {usuarioEliminar} eliminada correctamente.")

  except mysql.connector.Error as err:
      print(f"Error: {err}")

  finally:
      if 'conexion' in locals() and conexion.is_connected():
          cursor.close()
          conexion.close()



