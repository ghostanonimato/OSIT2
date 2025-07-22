# ScanYeux - Scanner de Portas Suspeitas (OSHINT)
# Uso educacional - Python 3
# Autor: YEUX

import socket
import sys
import time
import os
import argparse

banner = [
    "",
    "                               .                .         ",
    "                       `      > <      .       > <   '    ",
    "                               '                '         ",
    "                         .             .                  ",
    "                        > <     ,     > <                 ",
    "                   .     '             '      .      .    ",
    "                            __.--._          > <          ",
    "                    .     .'   L   `.--._     '           ",
    "                   > <    `/ c '`    \   `.                ",
    "                    '     :           ;    `.    `     ,  ",
    "                          |           ;      \            ",
    "                         /`.     | ' /        \     .     ",
    "                    '   / -.\ \  ^ ;/   _      \   > <    ",
    "                       :    \`.:/ \|     `.|    ;   '     ",
    "                       |     :''   '       ;    |         ",
    "                       |     |`.         _/_    ;         ",
    "            [by]      :     :  `-._____/   `. /           ",
    "                        \    |         :/ ,   V\          ",
    "              /\"\\   __.--; _ :         `./ /  ; ;         ",
    "             :  |\\_/     |  \\L  _..--.   `.L.'  |`.   __  ",
    "             |  | ;`.    ; _ \\\\'      `.          /`+'.'`.",
    "             |  | |      | \\CT_;        `-.      ' / /   |",
    "             |-_| |   .-'`.___.            `-.    / /    ;",
    "             :  ; :.-'                        `-./ /.   / ",
    "              \\/_/         _                     \\/  `./  ",
    "",
    "        ScanYeux - Scanner de Portas Suspeitas (OSHINT)",
    "        Uso educacional e OSINT",
    "        -----------------------------------",
    ""
]

for linha in banner:
    print("\033[91m" + linha + "\033[0m")
    time.sleep(0.05)

# Lista de portas que normalmente NÃO deveriam estar abertas em hosts comuns
portas_suspeitas = {
    21: "FTP",
    23: "Telnet",
    25: "SMTP",
    69: "TFTP",
    110: "POP3",
    135: "MS RPC",
    139: "NetBIOS",
    143: "IMAP",
    445: "SMB",
    512: "exec",
    513: "login",
    514: "shell",
    1433: "MS SQL",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    8080: "Proxy/HTTP-alt"
}

def animacao_scan(porta, servico, silencioso=False):
    if silencioso:
        return
    anim = ['|', '/', '-', '\\']
    for i in range(8):
        sys.stdout.write(f"\r  Escaneando porta {porta} ({servico})... {anim[i % len(anim)]}")
        sys.stdout.flush()
        time.sleep(0.07)
    sys.stdout.write("\r" + " " * 50 + "\r")  # Limpa a linha

def scan_portas(ip, portas, silencioso=False):
    if not silencioso:
        print(f"\n[+] Escaneando {ip} por portas suspeitas abertas...\n")
    abertas = []
    for porta, servico in portas.items():
        animacao_scan(porta, servico, silencioso)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            resultado = sock.connect_ex((ip, porta))
            if resultado == 0:
                if not silencioso:
                    print(f"\033[92m  [!] Porta {porta} ({servico}) ABERTA!\033[0m")
                abertas.append((porta, servico))
            else:
                if not silencioso:
                    print(f"\033[91m  [-] Porta {porta} ({servico}) FECHADA\033[0m")
            sock.close()
        except Exception as e:
            if not silencioso:
                print(f"\033[91m  [x] Erro ao escanear porta {porta}: {e}\033[0m")
    if not abertas and not silencioso:
        print("\033[94mNenhuma porta suspeita aberta encontrada.\033[0m")
    elif abertas and not silencioso:
        print("\nResumo das portas suspeitas abertas:")
        for porta, servico in abertas:
            print(f"  - Porta {porta} ({servico})")

def obter_nome_host(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "Desconhecido"

def proxima_pasta_resultados(base="resultados_"):
    n = 1
    while os.path.exists(f"{base}{n}"):
        n += 1
    return f"{base}{n}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ScanYeux - Scanner de Portas Suspeitas (OSHINT)")
    parser.add_argument("--s", action="store_true", help="Modo silencioso (sem animação e sem mensagens coloridas)")
    args = parser.parse_args()

    print("Informe o IP ou domínio do alvo para análise OSHINT (ex: 192.168.1.1 ou scanme.nmap.org)")
    alvo = input("Alvo: ").strip()
    nome = obter_nome_host(alvo)
    if not args.s:
        print(f"\nAlvo: {alvo} ({nome})")

    # Captura toda a saída da varredura
    from io import StringIO
    saida_original = sys.stdout
    buffer = StringIO()
    sys.stdout = buffer

    scan_portas(alvo, portas_suspeitas, silencioso=args.s)
    if not args.s:
        print("\n[!] Lembre-se: Use este script apenas em sistemas que você tem permissão para testar.")

    sys.stdout = saida_original
    resultado_texto = buffer.getvalue()
    print(resultado_texto)  # Mostra normalmente no terminal

    # Cria pasta numerada e salva o arquivo, com animação
    import time

    pasta = proxima_pasta_resultados()
    if not args.s:
        print(f"\nCriando a pasta '{pasta}' para salvar os resultados...", end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print(f"\nPasta criada: {os.path.abspath(pasta)}")
        print(f"Salvando resultados em: {os.path.join(pasta, 'resultados.txt')}")
    os.makedirs(pasta, exist_ok=True)
    caminho_arquivo = os.path.join(pasta, "resultados.txt")

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(f"Alvo: {alvo} ({nome})\n")
        f.write(resultado_texto)

    if not args.s:
        print(f"\n[✔] Resultado salvo em: {caminho_arquivo}")