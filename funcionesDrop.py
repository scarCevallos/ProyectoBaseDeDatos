import mysql.connector

def eliminar_por_id(tabla, id_a_eliminar):
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
        consulta = f"DELETE FROM {tabla} WHERE id = %s"
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


