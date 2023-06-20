from mongo_controller import database_controller, models_controller

#DEFINIR VARIABLES INICIALES: HOSTNAME, PUERTO Y NOMBRE DE LA DB.
_host_name = "127.0.0.1"
_port = 9030
_db_name = "my_database"


#INICIAR EL CONTROLADOR PRINCIPAL DE LA BASE DE DATOS.
my_database = database_controller(host_name=_host_name,
                                  port=_port,
                                  db_name = _db_name)

#CARGA E INSTANCIA LAS COLECCIONES PRINCIPALES
usuarios = my_database.get_usuarios()
sesiones = my_database.get_sesiones()
imagenes = my_database.get_imagenes()
estilos  = my_database.get_estilos()


#AGREGAR Y RECUPERAR UN USUARIO POR ID
_new_user = models_controller.usuario(correo="pedro@mcpato.com",password="secret")
_new_user.set_nombre("Pedro McPato")
_new_user_id = usuarios.add_document(document=_new_user.to_dict())
_usuario_data = usuarios.get_document(document_id=_new_user_id)
#_usuarios_data = usuarios.add_many_documents(documents=_new_user_id)
print("Su usuario")
print(_usuario_data)



#AGREGAR Y RECUPERAR UNA SESION POR ID
_new_sesion = models_controller.sesion(auth_token=_usuario_data.get('auth_token'))
_new_sesion.set_hugging_key(new_key="hf-iasjdiasdasdjoasod")
_new_sesion.set_storage_name(new_path="my_storage")
_new_sesion_id = sesiones.add_document(document=_new_sesion.to_dict())
_sesion_data = sesiones.get_document(document_id=_new_sesion_id)
print("Su sesion")
print(_sesion_data)


#AGREGAR Y RECUPERAR UNA IMAGEN POR ID
_new_imagen = models_controller.imagen(ruta_almacenamiento="custom_path")
_new_imagen.set_image_input("Una imagen rara")
_new_imagen_id = imagenes.add_document(document=_new_imagen.to_dict())
_imagen_data = imagenes.get_document(document_id=_new_imagen_id)
print("Su imagen")
print(_imagen_data)


#AGREGAR Y RECUPERAR UN ESTILO POR ID
_new_estilo = models_controller.estilo(tag="disney",value="in Disney style, full HD.")
_new_estilo_id = estilos.add_document(document=_new_estilo.to_dict())
_estilo_data = estilos.get_document(document_id=_new_estilo_id)
print("Su estilo")
print(_estilo_data)





