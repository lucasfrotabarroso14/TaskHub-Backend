class DefaultResponse():

    def __init__(self,status_code, status, message,result):
        self.status_code = status_code
        self.status =status
        self.message = message
        self.result = result

    def to_json(self):
        return {
            "status_code": self.status_code,
            "status": self.status,
            "message": self.message,
            "result": self.result
        }


