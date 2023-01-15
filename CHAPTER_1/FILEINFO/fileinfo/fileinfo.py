import os

class Fileinfo():
    

    def __init__(self, path) -> None:
        self.original_path = path
        self.filename = os.path.basename(path)
    
    def get_info(self) -> None:
        
        return (
            self.filename, 
            self.original_path, 
            os.path.abspath(self.original_path),
            os.path.getsize(self.original_path)    
        )