#TO-DO Registro -> created_at
#TO-DO Actualicaziones -> updated_at
#TO-DO Borrado lógico -> deleted_at
class Usuario:
    """
    Crea una clase de Usuario, se inicializa con correo y contraseña.

    args:
            correo      (str)       :   Recibe un correo en formato correo@ejemplo.com
            password    (str)       :   Recibe una contraseña to-do hashing.
    """
    def __init__(self, correo:str,password:str):
        """
        Crea una nueva instancia del usuario a partir de su correo y contraseña.

        args:
            correo      (str)       :   Recibe un correo en formato correo@ejemplo.com
            password    (str)       :   Recibe una contraseña to-do hashing.
        """
        self.__correo = correo
        self.__password = password
        self.__nombre = None
        self.__avatar = None
        self.__auth_token = None
    def set_nombre(self,new_name:str):
        """
        Asigna un nuevo nombre al Usuario.

        args

            new_name    (str)       :   Nuevo nombre de usuario.
        """
        self.__nombre = new_name
    def set_avatar(self,new_path:str):
        """
        Asigna un nuevo avatar para el Usuario.

        args

            new_avatar    (str)       :   Nuevo avatar de usuario.
        """
        self.__avatar = new_path
    def set_auth_token(self, new_value):
        """
        Asigna un nuevo auth_token al Usuario.

        args

            new_value    (str)       :   Nuevo valor del auth_token de usuario.
        """
        self.__auth_token = new_value
    def get_nombre(self):
        """
        Obtiene el nombre del usuario.

        return

            nombre    (str)       :   El nombre asignado del usuario.
        """
        return self.__nombre
    def get_correo(self):
        """
        Obtiene el correo del usuario.

        return

            correo    (str)       :   El correo asignado del usuario.
        """
        return self.__correo
    def get_password(self):
        """
        Obtiene la contraseña del usuario.

        return

            password    (str)       :   La contraseña del usuario.
        """
        return self.__password
    def get_avatar(self):
        """
        Obtiene el avatar del usuario.

        return

            avatar    (str)       :   La avatar del usuario.
        """
        return self.__avatar
    def get_auth_token(self):
        """
        Obtiene el auth_token del usuario.

        return

            auth_token    (str)       :   El auth_token del usuario.
        """
        return self.__auth_token
    def to_dict(self):
        """
        Transforma el objeto en un diccionario de datos.

        return

            user_data    (dict)       :   Los datos del usuario.
        """
        return {"nombre":self.get_nombre(),
                "correo":self.get_correo(),
                "password":self.get_password(),
                "avatar":self.get_avatar(),
                "auth_token":self.get_auth_token()}

class Sesion:
    """
    Crea una clase de Sesion, se inicializa con auth_token.

    args:
            auth_token      (str)       :   Recibe un token_auth de autorización del usuario.
            
    """
    def __init__(self, auth_token:str):
        """
        Crea una nueva instancia de la sesión de usuario a partir de su auth_token.

        args:
            auth_token      (str)       :   Recibe un token_auth de autorización del usuario.
        """
        self.__auth_token = auth_token
        self.__hugging_key = None
        self.__storage_name = None
    def set_hugging_key(self,new_key:str):
        """
        Asigna una nueva llave de HuggingFace. Visite https://huggingface.co/ para mas información.

        args

            new_key    (str)       :   Nueva llave
        """
        self.__hugging_key = new_key
    def set_storage_name(self,new_path:str):
        """
        Asigna una nueva ruta para los archivos del Usuario.

        args

            new_path    (str)       :   Nuevo avatar de usuario.
        """
        self.__storage_name = new_path
    def get_auth_token(self):
        """
        Obtiene el token de autorización del usuario.

        return

            auth_token    (str)       :   El token de autorización asignado del usuario.
        """
        return self.__auth_token
    def get_hugging_key(self):
        """
        Obtiene la llave HuggingFace del usuario.

        return

            hugging_key    (str)       :   La llave HugginFace asignada del usuario.
        """
        return self.__hugging_key
    def get_storage_name(self):
        """
        Obtiene el nombre del almacenamiento del usuario.

        return:

            storage_name    (str)       :   El nombre del almacenamiento.
        """
        return self.__storage_name
    def to_dict(self):
        """
        Transforma el objeto en un diccionario de datos.

        return

            sesion_data    (dict)       :   Los datos de la sesion.
        """
        return {"auth_token":self.get_auth_token(),
                "hugging_key":self.get_hugging_key(),
                "storage_name":self.get_storage_name()}

class Imagen:
    """
    Crea una clase de Imagen, se inicializa con la ruta del almacenamiento.

    args:
            ruta_almacenamiento      (str)       :   La ruta de la imagen almacenada en la bd_files.
            
    """
    def __init__(self, ruta_almacenamiento:str):
        """
        Crea una nueva instancia de imagen a partir de su ruta de almacenamiento.

        args:
            ruta_almacenamiento      (str)       :   La ruta de la imagen almacenada en la bd_files.
        """
        self.__image_file_path= ruta_almacenamiento
        self.__image_input = None
        self.__image_style = None
        self.__image_prompt = None
        self.__image_base = None
        self.__image_mask = None
        self.__image_output = None
    def set_image_file_path(self,new_path:str):
        """
        Actualiza la ruta de almacenamiento de las imágenes utilizadas.

        args

            new_name    (str)       :   Nuevo nombre de usuario.
        """
        self.__image_file_path = new_path
    def get_image_file_path(self):
        """
        Obtiene la ruta de almacenamiento de las imágenes utilizadas.

        return

            image_file_path    (str)       :   La ruta de almacenamiento de las imágenes utilizadas para crear esta imagenia.
        """
        return self.__image_file_path
    def set_image_input(self,new_input:str):
        """
        Asigna el valor del input dado por el usuario para la imagen creada.

        args

            new_input    (str)       :   Nuevo input del usuario.
        """
        self.__image_input = new_input
    def get_image_input(self):
        """
        Obtiene el valor del input dado por el usuario para la imagen creada.

        return:

            image_input    (str)       :   El input del usuario para crear la imagen.
        """
        return self.__image_input
    def set_image_style(self, new_value):
        """
        Asigna el nuevo valor para el estilo de la imagen.

        args

            new_value    (str)       :   Nuevo estilo de imagen.
        """
        self.__image_style = new_value
    def get_image_style(self):
        """
        Obtiene el nuevo valor para el estilo de la imagen.

        args

            image_style    (str)       :   Nuevo estilo de imagen.
        """
        return self.__image_style
    def set_image_prompt(self, new_value):
        """
        Asigna prompt final usado para crear la imagen.

        args

            new_value    (str)       :   Prompt a partir el cual se crea la imagen.
        """
        self.__image_prompt = new_value
    def get_image_prompt(self):
        """
        Obtiene el prompt final usado para crear la imagen.

        args

            image_prompt    (str)       :   Prompt utilizado para crear la imagen.
        """
        return self.__image_prompt
    def set_image_base(self, new_value):
        """
        Asigna la imagen base para editar o transformar su imagen.

        args

            new_value    (str)       :   Nuevo valor para la base de la imagen.
        """
        self.__image_base = new_value
    def get_image_base(self):
        """
        Obtiene la imagen base utilizada.

        args

            image_base    (str)       :   Valor de la imagen base utilizada.
        """
        return self.__image_base
    def set_image_mask(self, new_value):
        """
        Asigna la imagen máscara para editar su imagen.

        args

            new_value    (str)       :   Nuevo valor para la máscara de la imagen a editar.
        """
        self.__image_mask = new_value
    def get_image_mask(self):
        """
        Obtiene la imagen máscara utilizada para editar su imagen.

        args

            image_mask    (str)       :   Valor de la máscara de imagen utilizada para editar.
        """
        return self.__image_mask
    def set_image_output(self, new_value):
        """
        Asigna el valor de la imagen creada

        args

            new_value    (str)       :   Imagen creada
        """
        self.__image_output = new_value
    def get_image_output(self):
        """
        Obtiene el valor de la imagen creada.

        args

            image_output    (str)       :   Valor de la imagen creada.
        """
        return self.__image_output
    def to_dict(self):
        """
        Transforma el objeto en un diccionario de datos.

        return

            imagen_data    (dict)       :   Los datos de la imagen.
        """
        return {"image_file_path":self.get_image_file_path(),
                "image_input":self.get_image_input(),
                "image_style":self.get_image_style(),
                "image_prompt":self.get_image_prompt(),
                "image_base":self.get_image_base(),
                "image_mask":self.get_image_mask(),
                "image_output":self.get_image_output()}

class Estilo:
    """
    Crea una clase de Estilo, se inicializa con una etiqueta y su valor.

    args:
            tag         (str)       :   Recibe un tag o etiqueta del estilo.
            value       (str)       :   Recibe el valor del estilo.
            
    """
    def __init__(self, tag:str, value:str):
        """
        Crea una nueva instancia del estilo a partir de su etiqueta/tag.

        args:
            tag         (str)       :   Recibe un tag o etiqueta del estilo.
            value       (str)       :   Recibe el valor del estilo.
        """
        self.__tag = tag
        self.__value = value
    def set_value(self,new_value:str):
        """
        Actualiza el valor del estilo.

        args

            new_value    (str)       :   Nuevo valor para el estilo.
        """
        self.__value = new_value
    def get_value(self):
        """
        Obtiene el valor del estilo.

        return

            value    (str)       :   Valor completo del estilo.
        """
        return self.__value
    def get_tag(self):
        """
        Obtiene el tag del estilo

        return

            tag    (str)       :   Tag o Etiqueta del estilo.
        """
        return self.__tag
    def to_dict(self):
        """
        Transforma el objeto en un diccionario de datos.

        return

            estilo_data    (dict)       :   Los datos del estilo.
        """
        return {"tag":self.get_tag(),
                "value":self.get_value()}
