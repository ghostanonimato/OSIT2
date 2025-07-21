# README.md
# ScanYeux - Scanner de Portas Suspeitas (OSHINT)

## Descrição

O **ScanYeux** é um script em Python para escanear portas de um host e identificar portas que normalmente **não deveriam estar abertas** em sistemas comuns. Ele é voltado para fins **educacionais** e **OSINT** (Open Source Intelligence), ajudando a identificar possíveis exposições de serviços sensíveis em redes.

---

## Como funciona

- O script solicita ao usuário um IP ou domínio de destino.
- Ele tenta resolver o nome do host (DNS reverso).
- Realiza um scan nas portas consideradas suspeitas (ex: FTP, Telnet, SMB, RDP, VNC, etc).
- Exibe na tela todas as portas abertas que podem representar riscos de segurança.

---

## Portas escaneadas

O script verifica as seguintes portas, associadas a serviços que **raramente devem estar expostos**:

- 21 (FTP)
- 23 (Telnet)
- 25 (SMTP)
- 69 (TFTP)
- 110 (POP3)
- 135 (MS RPC)
- 139 (NetBIOS)
- 143 (IMAP)
- 445 (SMB)
- 512 (exec)
- 513 (login)
- 514 (shell)
- 1433 (MS SQL)
- 3306 (MySQL)
- 3389 (RDP)
- 5900 (VNC)
- 8080 (Proxy/HTTP-alt)

---

## Como usar
0. **instalação**
```
git clone https://github.com/ghostanonimato/OSIT2.git
cd OSIT2
ls
```
1. **Pré-requisitos:**  
   - Python 3 instalado no sistema.

2. **Execução:**  
   Salve o script como `ScanYeux.py` e execute no terminal:

   ```
   python ScanYeux.py
   ```

3. **Informe o alvo:**  
   Digite o IP ou domínio do host que deseja analisar quando solicitado.

---

## Exemplo de uso

```
Informe o IP ou domínio do alvo para análise OSHINT (ex: 192.168.1.1 ou scanme.nmap.org)
Alvo: 192.168.1.10

Alvo: 192.168.1.10 (meu-servidor.local)

[+] Escaneando 192.168.1.10 por portas suspeitas abertas...

  [!] Porta 21 (FTP) ABERTA!
  [!] Porta 445 (SMB) ABERTA!

Resumo das portas suspeitas abertas:
  - Porta 21 (FTP)
  - Porta 445 (SMB)
```

---

## Aviso Legal

> **Use este script apenas em sistemas e redes para os quais você tem permissão explícita!  
> O uso não autorizado pode ser ilegal.  
> O objetivo deste projeto é exclusivamente educacional.**

---

## Autor
Yeux

         ((((c,               ,7))))
        (((((((              ))))))))
         (((((((            ))))))))
          ((((((@@@@@@@@@@@))))))))
           @@@@@@@@@@@@@@@@)))))))
        @@@@@@@@@@@@@@@@@@))))))@@@@
       @@/,:::,\/,:::,\@@@@@@@@@@@@@@
       @@|:::::||:::::|@@@@@@@@@@@@@@@
       @@\':::'/\':::'/@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@@\
             /    \        (     \
            (      )        \     \
             \    /          \
