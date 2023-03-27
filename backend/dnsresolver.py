from validmailchecker import *

class EmailServer:
    
    def __init__(self,domain) -> None:
        self.domain = domain
        self.valid_mail_server = main(domain)

    def __str__(self) -> str:
        return self.valid_mail_server
    
    def __repr__(self) -> str:
        return self