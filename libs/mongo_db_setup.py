class client_setup:
    def __init__(self, hostname:str, port:int):
        """
        Inicializa un cliente para base de datos, en un hostname y un puerto definido por el usuario.

        args:

            hostname    (str)       :   El nombre del host a instanciar.
            port        (int)       :   El puerto donde escuchará la bd.
        """
        from pymongo import MongoClient
        self.__client = MongoClient(host = hostname,
                                    port = port)
    def get(self):
        """
        Obtiene la instancia del cliente para la base de datos.
        
        return:

            client        (object)    :   La instancia creada del cliente para la base de datos.
        """
        return self.__client

class database_setup:
    def __init__(self,client, db_name):
        """
        Crea una instancia de base de datos, a partir de un cliente.

        args:

            client      (object)    :   El objeto principal de la instancia cliente.
            db_name     (str)       :   El nombre de la base de datos a instanciar.
        """
        self.__client = client
        self.__database = self.get_client()[db_name]
    def get_client(self):
        """
        Recupera el cliente del cual fue instanciada la base de datos, para manejar distintas bases de datos.

        return:
            client        (object)    :   La instancia creada del cliente para la base de datos.
        """
        return self.__client
    def get(self):
        """
        Devuelve la base de datos inicializada.

        return:
            database        (object)    :   La instancia de base de datos actual.
        """
        return self.__database
    
class collection_handler:
    def __init__(self,database:object, collection:str):
        """
        Maneja una colección de datos a partir de la base de datos definida.

        args:

            database    (object)    :   La instancia de la Base de Datos a utilizar.
            collection  (str)       :   El nombre de la colección a obtener
        """
        self.__database = database
        self.__collection = self.get_database()[collection]
    def print_error(self,error:str,value):
        """
        Función para imprimir errores y setear valor default de respuesta.

        return:
            value       (var)       :   Devuelve el valor del parámetro recibido.
        """
        print(f"Collection_Error:\t{self.get_collection()}\n\t{error}")
        return value
    def add_document(self,document:dict):
        """
        Agrega un documento dentro de una colección, a partir de un diccionario.

        args:

            document    (dict)      :   Los valores a agregar en el documento.
        
        return:

            __id        (object)    :   El OBJETO ID del documento recién agregado.
        """
        try:
            __id = self.get_collection().insert_one(document).inserted_id
        except Exception as err:
            __id = self.print_error(err,dict())
        finally:
            return  __id
    def add_many_documents(self, documents:list)->list:
        """
        Agrega un documento dentro de una colección, a partir de un diccionario.

        args:

            collection  (str)       :   El nombre de la colección a obtener.
            document    (dict)      :   Los valores a agregar en el documento.
        
        return:

            __id        (object)    :   El OBJETO ID del documento recién agregado.
        """
        try:
            __ids =  self.get_collection().insert_many(documents).inserted_ids
        except Exception as err:
            __ids = self.print_error(err,list())
        finally:
            return  __ids
    def get_database(self):
        """
        Devuelve una instancia de la base de datos.

        return:
            database    (object)    :   La instancia de la base de datos
        """
        return self.__database
    def get_collection(self):
        """
        Devuelve la colección instanciada.

        return:
            collection  (object)    :   La instancia de la colección, desde base de datos
        """
        return self.__collection
    def get_document(self,document_id:object) -> dict:
        """
        Obtiene un documento dentro de una colección a partir de su ID.

        args:
            
            document_id (object)    :   El Objeto ID del documento a obtener, ref: find_document.

        return:

            _doc        (dict)      :   Un diccionario con el contenido del documento.
        """
        try:
            __doc = self.get_collection().find_one({"_id":document_id})
        except Exception as err:
            __doc = self.print_error(err,None)
        finally:
            return __doc
    def find_document(self, field:str, value:str)->dict:
        """
        Busca y obtiene un documento dentro de una colección a partir de ciertos campos.

        args:
            
            field       (str)       :   El campo válido dentro del documento.
            value       (str)       :   El valor del campo.
        
        return:

            _doc        (dict)      :   Un diccionario con el contenido del documento.
        """
        try:
            __doc = self.get_collection().find_one({field:value})
        except Exception as err:
            __doc = self.print_error(err,None)
        finally:
            return __doc
        


    
        
    