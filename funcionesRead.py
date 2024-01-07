import mysql.connector

def consultar_por_id(tabla, id_a_consultar):
  try:
        conexion = mysql.connector.connect(
          'user': 'tu_usuario',
        'password': 'tu_contraseña',
        'host': 'localhost',
        'database': 'tu_base_de_datos',
        'raise_on_warnings': True
      )
        cursor = conexion.cursor()
    
        listaTablas=["foro","comentario","modulo","anuncio","curso","evaluacion","entrega","carrera","facultad","enviado","recibido","profesor","estudiante"]
        listaids=["idforo","idcomentario","idmodulo","idanuncio","idcurso","idevaluacion","identrega","id_carrera","id_facultad","idenviado", "idrecibido","usuarioespol","usuarioespol"]

        id = "Nombre del id"
        for i in range(len(listaTablas)):
            if tabla == listaTablas[i]:
                id = listaids[i]
            break;  
      # Ejecutar la consulta
        consulta = f"SELECT * FROM {tabla} WHERE {id} = %s"
        cursor.execute(consulta, (id_a_consultar,))

        # Obtener los resultados
        resultados = cursor.fetchall()

        # Imprimir los resultados
        for fila in resultados:
            print(fila)

  except mysql.connector.Error as err:
      print(f"Error: {err}")

  finally:
      if 'conexion' in locals() and conexion.is_connected():
          cursor.close()
          conexion.close()
