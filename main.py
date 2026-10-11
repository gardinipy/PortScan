import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    """Tenta conectar a uma porta específica no host."""
    # O bloco 'with' garante que o socket seja fechado (client.close()) automaticamente
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(0.5)
        try:
            # Tenta conectar. Retorna 0 se houver sucesso.
            code = client.connect_ex((host, port))
            if code == 0:
                print(f"[+] Porta {port:X<5} aberta") # Formatação alinhada
        except socket.gaierror:
            # Erro de resolução de DNS (ex: host não existe)
            pass
        except Exception:
            # Ignora outros erros específicos de conexão
            pass

def main():
    # Substitui o sys.argv manual por argparse, o padrão do Python para CLIs
    parser = argparse.ArgumentParser(description="Port Scanner Rápido em Python")
    parser.add_argument("host", help="O host alvo (ex: google.com ou 192.168.0.1)")
    parser.add_argument("-p", "--ports", help="Portas separadas por vírgula (ex: 22,80,443)", default="")
    
    args = parser.parse_args()
    host = args.host
    
    if args.ports:
        try:
            # Separa por vírgula, remove espaços vazios e converte para int
            ports = [int(p.strip()) for p in args.ports.split(',')]
        except ValueError:
            print("Erro: As portas devem ser números inteiros separados por vírgula.")
            return
    else:
        # Portas padrão caso o usuário não forneça a flag -p
        ports = [21, 22, 23, 25, 80, 443, 8080, 8443, 3306, 139, 135]

    print(f"[*] Iniciando scan em {host}...")
    
    # Executa o scan utilizando múltiplas threads simultaneamente
    # max_workers dita quantas portas são verificadas ao mesmo tempo
    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in ports:
            executor.submit(scan_port, host, port)

if __name__ == "__main__":
    main()
