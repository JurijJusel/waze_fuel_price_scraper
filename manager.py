
class Manager:
    def __init__(self, status=False):
        self.status = status
 
    def is_activate(self):
        if self.status:
            return True
        else:
            return False
