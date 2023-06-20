
import mongo_models as Model

class models_controller:
    def usuario(correo:str,password:str)  ->  Model.Usuario:
        """
        Obtiene una nueva instancia de la clase Usuario.

        args:
                correo      (str)       :   Recibe un correo en formato correo@ejemplo.com
                password    (str)       :   Recibe una contraseña to-do hashing.
        """
        return Model.Usuario(correo=correo, password=password)
    def sesion(auth_token:str)  ->  Model.Sesion:
        """
        Obtiene una nueva instancia de la clase Sesión.

        args:
                auth_token      (str)       :   Recibe un token_auth de autorización del usuario.
                
        """
        return Model.Sesion(auth_token=auth_token)
    def imagen(ruta_almacenamiento:str)  ->  Model.Imagen:
        """
        Obtiene una nueva instancia de la clase Imagen.

        args:
                ruta_almacenamiento      (str)       :   La ruta de la imagen almacenada en la bd_files.
                
        """
        return Model.Imagen(ruta_almacenamiento=ruta_almacenamiento)
    def estilo(tag:str, value:str)  ->  Model.Estilo:
        """
        Obtiene una nueva instancia de la clase Estilo.

        args:
                tag         (str)       :   Recibe un tag o etiqueta del estilo.
                value       (str)       :   Recibe el valor del estilo.
                
        """
        return Model.Estilo(tag = tag,value = value)
    
class database_controller:
    def __init__(self, host_name:str,port:int, db_name:str):
        """
        Inicia un controlador para base de datos, con un host, puerto y cliente definidos.

        args:

            host_name   (str)       :   El nombre del host a instanciar.
            port        (int)       :   El puerto donde escuchará la bd.
            db_name     (str)       :   El nombre de la base de datos a controlar.
        """
        import mongo_db_setup as Setup
        self.__cliente = Setup.client_setup(hostname = host_name,
                                            port = port)
        self.__database = Setup.database_setup(client=self.get_cliente(),
                                               db_name=db_name)
        self.__usuarios = Setup.collection_handler(database=self.get_database(),
                                                   collection='usuarios')
        self.__sesiones = Setup.collection_handler(database=self.get_database(),
                                                   collection='sesiones')
        self.__estilos = Setup.collection_handler(database=self.get_database(),
                                                  collection='estilos')
        self.__imagenes = Setup.collection_handler(database=self.get_database(),
                                                   collection='imagenes')
    def get_cliente(self):
        """
        Obtiene el cliente de la base de datos.

        return:
            client        (object)    :   El cliente actual de la base de datos.
        """
        return self.__cliente.get()
    def get_database(self):
        """
        Obtiene la base de datos actual.

        return:
            database        (object)    :   La base de datos actual.
        """
        return self.__database.get()
    def get_usuarios(self):
        """
        Obtiene la colección de usuarios de la base de datos.

        return:
            usuarios        (object)    :   Colección de usuarios
        """
        return self.__usuarios
    def get_sesiones(self):
        """
        Obtiene la colección de sesiones de la base de datos.

        return:
            sesiones        (object)    :   Colección de sesiones
        """
        return self.__sesiones
    def get_estilos(self):
        """
        Obtiene la colección de estilos de la base de datos.

        return:
            estilos        (object)    :   Colección de estilos
        """
        return self.__estilos
    def get_imagenes(self):
        """
        Obtiene la colección de imágenes de la base de datos.

        return:
            imagenes        (object)    :   Colección de imágenes
        """
        return self.__imagenes
