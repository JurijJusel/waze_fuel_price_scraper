
class Manager:
    def __init__(self, status=True) -> None:#TODO by deafult=false turi but,nes yra noras manager aktyvuot kai reik,nereik kad jis visada veiktu
        self.status = status
 
    def is_activate(self):
        if self.status:
            return True
        else:
            return False
