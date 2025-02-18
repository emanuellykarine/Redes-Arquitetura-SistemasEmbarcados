import socket
import json
from Sistema import Sistema

class Servidor:
    def __init__(self) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria o socket utilizando IPv4 (protocolo de endereço) e TCP (tipo do socket)
        self.s.bind(("0.0.0.0", 5551)) #Socket vinculado a um endereço Ip e porta 0.0.0.0 é por que o servidor aceita conexão em qualquer rede
        self.s.listen(5) #maximo 5 conexões
        self.info = {}

    def ligar(self) -> None:
        while True:
            clientsocket, address = self.s.accept() #Quando a conexão é aceita ela retorna o socket de comunicação e o endereço ip
            print(f"Conexao estabelecida com {address}.")
            msg = clientsocket.recv(1024).decode("utf-8") #Recebe a mensagem do cliente em até 1024 bytes

            if msg == "get_info":
                self.coletar_informacoes()
            else:
                clientsocket.send(b"Comando invalido")

    def coletar_informacoes(self) -> str:
        self.info['espaco_livre_hd'] = Sistema.espaco_livre_hd()
        self.info['qtd_processadores'] = Sistema.qtd_processadores()
        self.info['espaco_memoria'] = Sistema.espaco_memoria()
        # self.info['temperatura'] = Sistema.temperatura()

        # Salva as informações no arquivo JSON
        self.salvar_em_json()

    def salvar_em_json(self):
        try:
            with open("informacoes_sistema.json", 'w') as file:
                json.dump(self.info, file, indent=3)
        except Exception as e:
            print(f"Erro ao salvar arquivo JSON: {e}")


def main():
    server = Servidor()
    server.ligar()

if __name__ == "__main__":
    main()
