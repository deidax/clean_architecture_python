
class InvalidRoomListRequestException(Exception):
    
    
    def __init__(self,error={}, *args: object) -> None:
        super().__init__(*args)
        self._errors = []
        if bool(error): self._errors.append(error)
    
    
    def parameter_error(self, parameter: str, message: str):
        self._errors.append({'parameter': parameter, 'message': message})
    
    @property
    def errors(self):
        return self._errors
    
    def __bool__(self):
        return len(self.errors) > 0

    def __str__(self) -> str:
        err_m = ''
        for err in self.errors:
            ms = ''
            for e_key in err:
                ms +="{0}: {1}\n".format(e_key, err[e_key])
            err_m +=ms+"\n"
            
        return err_m