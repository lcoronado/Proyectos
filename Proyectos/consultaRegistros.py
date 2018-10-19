
import mysql.connector as maria
import _mysql as _maria

def consultar():
    '''
    Ejemplo para hacer una consulta basica por medio de Python en una 
    base de datos desarrollada en HeidiSQL
    '''
    print "Estas en la funcion Consultar"
    mariadb_conexion = maria.connect(
        host='192.168.0.5', 
        port='3306',
        user='root', 
        password='hola', 
        database='poo')
    cursor = mariadb_conexion.cursor()
    try:
        cursor.execute("SELECT id,nombre,autor,anio FROM novelas")
        for id, nombre, autor, anio in cursor:
            data = "id = {}, nombre = {}, autor = {}, anio = {}".format(id,
                nombre,
                autor,
                anio)
            
            print data

    except maria.Error as error:
        print("Error: {}".format(error))
    mariadb_conexion.close()

def _consulta():
    '''
    Uso de libreria alterna para hacer consultas
    '''
    print "Funcion de consulta alterna..."
    mariadb_conexion = _maria.connect(
        host='localhost', 
        user='root',
        passwd='hola', 
        db='poo',
        port=3306)
    cursor = mariadb_conexion.cursor()
    try:
        cursor.execute("SELECT id,nombre,autor,anio FROM novelas")
        for id, nombre, autor, anio in cursor:
            data = "id = {}, nombre = {}, autor = {}, anio = {}".format(id,
                nombre,
                autor,
                anio)
            
            print data

    except _maria.Error as error:
        print("Error: {}".format(error))
    mariadb_conexion.close()


if __name__ == "__main__":
    consultar()
    #_consulta()
    raw_input("El programa finalizo, presiona enter para cerrar...")
    pass
