class usuario:
    def __init__(self, correo:str,password:str,nombre:str=None, avatar:str=None,auth_token:str=None):
        self.__correo = correo
        self.__password = password
        self.__nombre = self.set_nombre(nombre)
        self.__avatar = self.set_avatar(avatar)
        self.__auth_token = self.set_auth_token(auth_token)
        self.__collection = "usuarios"
    def get_collection(self):
        return self.__collection
    def set_nombre(self,new_name):
        self.__nombre = new_name
    def set_avatar(self,new_path):
        self.__avatar = new_path
    def set_auth_token(self, new_value):
        self.__auth_token = new_value
    def get_nombre(self):
        return self.__nombre
    def get_correo(self):
        return self.__correo
    def get_password(self):
        return self.__password
    def get_avatar(self):
        return self.__avatar
    def get_auth_token(self):
        return self.__auth_token
    def to_dict(self):
        return {"nombre":self.get_nombre(),
                "correo":self.get_correo(),
                "password":self.get_password(),
                "avatar":self.get_avatar(),
                "auth_token":self.get_auth_token()}

