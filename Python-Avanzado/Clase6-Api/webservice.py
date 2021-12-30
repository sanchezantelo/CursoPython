import json

from klein import klein
from werkzeug.exceptions import BadRequest, MethodNotAllowed, NotFound

class RestAPI:
    app=klein()
    students={}
    fields= ("name","courses")

    def response(self,request,status=200,**kwargs):
        """
        Build the response body as JSON and set the proper content type
        header.
        """
        request.setResponseCode(status)
        if kwargs:
            request.setHeader("Content type","aplication/json")
            return json.dump(kwargs)
        
    def getStudentOr404(self,studentID):
        try:
            return self students[studentID]
            except KeyError:
                raise NotFound
