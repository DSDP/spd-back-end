from rest_framework import status 
from apirest.utils.constants import Constants
import logging    
    
class NoAuthorizationException(Exception):
    
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = Constants().NO_AUTH_EXCP
    
    def __init__(self):
        logger = logging.getLogger('apirest')
        logger.warning(Constants().NO_AUTH_EXCP)
        
        Exception.__init__(self, Constants().NO_AUTH_EXCP)
        
        
class NotAuthorizedException(Exception):
    
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = Constants().NOT_AUTHORIZED_EXCP
    
    def __init__(self):
        logger = logging.getLogger('apirest')
        logger.warning(Constants().NOT_AUTHORIZED_EXCP)
        Exception.__init__(self, Constants().NOT_AUTHORIZED_EXCP)
        
        
class AuthorizationFormatException(Exception):
    
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = Constants().AUTH_FORMAT_EXCP
    
    def __init__(self):
        logger = logging.getLogger('apirest')
        logger.warning(Constants().AUTH_FORMAT_EXCP)
        Exception.__init__(self, Constants().AUTH_FORMAT_EXCP)
        
class ServerAuthConnectionException(Exception):
    
    
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = Constants().AUTH_CONNECTION_EXCP
    
    def __init__(self):
        logger = logging.getLogger('apirest')
        logger.warning(Constants().AUTH_CONNECTION_EXCP)
        Exception.__init__(self, Constants().AUTH_CONNECTION_EXCP)  
        


