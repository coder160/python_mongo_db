import mongo_db_handler as Handler
import mongo_models as Model
    

_host_name = "127.0.0.1"
_port = 9030
_db_name = "new_dummy_db"
usuario = Model.usuario(correo="juan@perez.com",
                          password="secret")
usuario.set_nombre("Juan Perez")


cliente = Handler.client_handler(hostname = _host_name,
                                 port = _port)
database = Handler.database_handler(db_name=_db_name,
                                    client=cliente.get_client())
colecciones = Handler.collection_handler(database=database.get_database(),
                                         collection=usuario.get_collection())

_l_docs = list()
pedro = Model.usuario(correo="pedro@mcpato.com",
                          password="secret")
pedro.set_nombre("Pedro McPato")

_l_docs.append(pedro.to_dict())

paco = Model.usuario(correo="paco@mcpato.com",
                          password="secret")
paco.set_nombre("Paco McPato")

_l_docs.append(paco.to_dict())

luis = Model.usuario(correo="luis@mcpato.com",
                          password="secret")
luis.set_nombre("Luis McPato")
_l_docs.append(luis.to_dict())

new_doc_id = colecciones.add_document(document=usuario.to_dict())

_usuarios_data = colecciones.add_many_documents(documents=_l_docs)

print(_usuarios_data)
for _usuario in _usuarios_data:
    _usuario_data = colecciones.get_document(document_id=_usuario)
    print(_usuario_data)

