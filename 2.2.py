import pymysql

class MySQLConnect:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conectado a la base de datos:", self.database)
            return self.connection
        except pymysql.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def desconectar(self):
        if self.connection is not None:
            try:
                self.connection.close()
                print("Desconectado de la base de datos:", self.database)
            except pymysql.Error as e:
                print(f"Error al desconectar de la base de datos: {e}")

class PaisMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, nombre):
        global conexion
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            sql = "INSERT INTO Pais (id, nombre) VALUES (%s, %s)"
            valores = (id, nombre)
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Registro insertado en la Tabla Pais: id={id}, nombre={nombre}")
            return True
        except pymysql.Error as e:
            print(f"Error al insertar registro en la Tabla Pais: {e}")
            return False
        finally:
            if conexion:
                conexion.close()

    def editar(self, nombre, nuevo_nombre):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "UPDATE Pais SET nombre = %s WHERE nombre = %s"
                cursor.execute(query, (nuevo_nombre, nombre))
                conexion.commit()
                return True
            except pymysql.Error as error:
                print("Error al editar en la tabla Pais:", error)
                return False
            finally:
                if cursor:
                    cursor.close()
                self.desconectar()

    def eliminar(self, id):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM Pais WHERE id = %s"
                cursor.execute(query, (id,))
                conexion.commit()
                return True
            except pymysql.Error as error:
                print("Error al eliminar en la tabla Pais:", error)
                return False
            finally:
                if cursor:
                    cursor.close()
                self.desconectar()

    def consultar(self, filtro):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT * FROM Pais WHERE " + filtro
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
            except pymysql.Error as error:
                print("Error al consultar en la tabla Pais:", error)
                return None
            finally:
                if cursor:
                    cursor.close()
                self.desconectar()

class OlimpiadaMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, year):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            sql = "INSERT INTO Olimpiada (id, year) VALUES (%s, %s)"
            valores = (id, year)
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Registro insertado en la Tabla Olimpiada: id={id}, year={year}")
            return True
        except pymysql.Error as e:
            print(f"Error al insertar registro en la Tabla Olimpiada: {e}")
            return False
        finally:
            if conexion:
                conexion.close()

    def editar(self, year, nuevo_year):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "UPDATE Olimpiada SET year = %s WHERE year = %s"
                cursor.execute(query, (nuevo_year, year))
                conexion.commit()
                return True
            except pymysql.Error as error:
                print("Error al editar en la tabla Olimpiada:", error)
                return False
            finally:
                if cursor:
                    cursor.close()
                self.desconectar()

    def eliminar(self, id):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM Olimpiada WHERE id = %s"
                cursor.execute(query, (id,))
                conexion.commit()
                return True
            except pymysql.Error as error:
                print("Error al eliminar en la tabla Olimpiada:", error)
                return False
            finally:
                if cursor:
                    cursor.close()
                self.desconectar()

    def consultar(self, filtro):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT * FROM Olimpiada WHERE " + filtro
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
            except pymysql.Error as error:
                print("Error al consultar en la tabla Olimpiada:", error)
                return None
            finally:
                if cursor:
                    cursor.close()
                self.desconectar()

class ResultadosMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            sql = "INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (idOlimpiada, idPais, idGenero, oro, plata, bronce)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Registro insertado en la Tabla Resultados")
            return True
        except pymysql.Error as e:
            print(f"Error al insertar registro en la Tabla Resultados: {e}")
            return False
        finally:
            if conexion:
                conexion.close()

    def editar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        if oro >= 0 and plata >= 0 and bronce >= 0:
            conexion = self.conectar()
            if conexion:
                try:
                    cursor = conexion.cursor()
                    query = "UPDATE Resultados SET oro = %s, plata = %s, bronce = %s WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
                    valores = (oro, plata, bronce, idOlimpiada, idPais, idGenero)
                    cursor.execute(query, valores)
                    conexion.commit()
                    return True
                except pymysql.Error as error:
                    print("Error al editar en la tabla Resultados:", error)
                    return False
                finally:
                    if cursor:
                        cursor.close()
                    self.desconectar()
        else:
            print("Los valores de oro, plata y bronce deben ser enteros positivos.")
            return False

    def eliminar(self, idOlimpiada, idPais, idGenero):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
                valores = (idOlimpiada, idPais, idGenero)
                cursor.execute(query, valores)
                conexion.commit()
                return True
            except pymysql.Error as error:
                print("Error al eliminar en la tabla Resultados:", error)
                return False
            finally:
                if cursor:
                    cursor.close()
                self.desconectar()

    def consultar(self, filtro):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT * FROM Resultados WHERE " + filtro
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
            except pymysql.Error as error:
                print("Error al consultar en la tabla Resultados:", error)
                return None
            finally:
                if cursor:
                    cursor.close()
                self.desconectar()

# Ejemplo de uso:
pais_db = PaisMySQL("localhost", "root", "quesadillas1", "programacion")
print(pais_db.insertar(10, "MexicO"))
print(pais_db.editar("MexicO", "Mexico"))
print(pais_db.eliminar(2))
print(pais_db.consultar("nombre LIKE '%A%'"))

olimpiada_db = OlimpiadaMySQL("localhost", "root", "quesadillas1", "programacion")
print(olimpiada_db.insertar(1, 2024))
print(olimpiada_db.editar(2024, 2028))
print(olimpiada_db.eliminar(1))
print(olimpiada_db.consultar("year > 1990"))

resultados_db = ResultadosMySQL("localhost", "root", "quesadillas1", "programacion")
print(resultados_db.insertar(1, 1, 1, 10, 5, 3))
print(resultados_db.editar(1, 1, 1, 12, 6, 4))
print(resultados_db.eliminar(1, 1, 1))
print(resultados_db.consultar("idPais = 1"))
