import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_Producto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_Producto) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_Producto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_Producto) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_Producto, **k):

    @staticmethod
    def POST_DELETE(id_Producto, **k):
    '''

    def GET(self, id_Producto, **k):
        message = None # Error message
        id_Producto = config.check_secure_val(str(id_Producto)) # HMAC id_Producto validate
        result = config.model.get_productos(int(id_Producto)) # search  id_Producto
        result.id_Producto = config.make_secure_val(str(result.id_Producto)) # apply HMAC for id_Producto
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_Producto, **k):
        form = config.web.input() # get form data
        form['id_Producto'] = config.check_secure_val(str(form['id_Producto'])) # HMAC id_Producto validate
        result = config.model.delete_productos(form['id_Producto']) # get productos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_Producto = config.check_secure_val(str(id_Producto))  # HMAC user validate
            id_Producto = config.check_secure_val(str(id_Producto))  # HMAC user validate
            result = config.model.get_productos(int(id_Producto)) # get id_Producto data
            result.id_Producto = config.make_secure_val(str(result.id_Producto)) # apply HMAC to id_Producto
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/productos') # render productos delete.html 
