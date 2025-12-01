from pathlib import Path
from datetime import datetime


class Logger():
    """Responsável por registrar logs de operações."""
    def __init__(self, log_file: str):
        self.log_file = Path(log_file)

    def log(self, tipo,  mensagem: str):
        """Registra uma mensagem de log com timestamp."""
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{agora}] [{tipo}] {mensagem}\n"
        with self.log_file.open("a") as file:
            file.write(log_message)

    def info(self, mensagem: str):
        self.log("INFO", mensagem)
    
    def error(self, mensagem: str):
        self.log("ERRO", mensagem)
    
    def create(self, mensagem: str):
        self.log("CREATE", mensagem)
    
    def update(self, mensagem: str):
        self.log("UPDATE", mensagem)
    
    def delete(self, mensagem: str):
        self.log("DELETE", mensagem)
        
