import socket as soc
from colorama import Fore
from tabulate import tabulate 

porte_note = {
  20: {
    "protocollo": "FTP (File Transfer Protocol) - Dati",
    "descrizione": "Trasferimento dei dati nei trasferimenti FTP."
  },
  21: {
    "protocollo": "FTP (File Transfer Protocol) - Controllo",
    "descrizione": "Controllo dei trasferimenti FTP."
  },
  22: {
    "protocollo": "SSH (Secure Shell)",
    "descrizione": "Connessioni sicure a server tramite terminale."
  },
  23: {
    "protocollo": "Telnet",
    "descrizione": "Accesso remoto non sicuro a dispositivi di rete."
  },
  25: {
    "protocollo": "SMTP (Simple Mail Transfer Protocol)",
    "descrizione": "Invia email tra server di posta."
  },
  53: {
    "protocollo": "DNS (Domain Name System)",
    "descrizione": "Risoluzione dei nomi di dominio in indirizzi IP."
  },
  67: {
    "protocollo": "DHCP (Dynamic Host Configuration Protocol) - Server",
    "descrizione": "Configurazione automatica degli indirizzi IP sui client."
  },
  68: {
    "protocollo": "DHCP (Dynamic Host Configuration Protocol) - Client",
    "descrizione": "Ricezione delle configurazioni DHCP."
  },
  69: {
    "protocollo": "TFTP (Trivial File Transfer Protocol)",
    "descrizione": "Versione semplificata di FTP senza autenticazione."
  },
  80: {
    "protocollo": "HTTP (Hypertext Transfer Protocol)",
    "descrizione": "Trasferimento di pagine web non crittografate."
  },
  110: {
    "protocollo": "POP3 (Post Office Protocol v3)",
    "descrizione": "Recupero di email da server di posta."
  },
  119: {
    "protocollo": "NNTP (Network News Transfer Protocol)",
    "descrizione": "Trasferimento di articoli di newsgroup."
  },
  123: {
    "protocollo": "NTP (Network Time Protocol)",
    "descrizione": "Sincronizzazione oraria tra computer."
  },
  143: {
    "protocollo": "IMAP (Internet Message Access Protocol)",
    "descrizione": "Recupero di email con gestione avanzata delle cartelle."
  },
  161: {
    "protocollo": "SNMP (Simple Network Management Protocol)",
    "descrizione": "Monitoraggio e gestione di dispositivi di rete."
  },
  194: {
    "protocollo": "IRC (Internet Relay Chat)",
    "descrizione": "Servizio di chat in tempo reale."
  },
  443: {
    "protocollo": "HTTPS (Hypertext Transfer Protocol Secure)",
    "descrizione": "Trasferimento sicuro di pagine web."
  },
  445: {
    "protocollo": "SMB (Server Message Block)",
    "descrizione": "Condivisione di file e stampanti in rete."
  },
  465: {
    "protocollo": "SMTPS (Secure SMTP)",
    "descrizione": "Invia email in modo sicuro."
  },
  587: {
    "protocollo": "SMTP (Simple Mail Transfer Protocol)",
    "descrizione": "Invia email con autenticazione."
  },
  993: {
    "protocollo": "IMAPS (Secure IMAP)",
    "descrizione": "Versione sicura di IMAP."
  },
  995: {
    "protocollo": "POP3S (Secure POP3)",
    "descrizione": "Versione sicura di POP3."
  },
  1433: {
    "protocollo": "MSSQL",
    "descrizione": "Accesso ai database Microsoft SQL Server."
  },
  3306: {
    "protocollo": "MySQL",
    "descrizione": "Accesso ai database MySQL."
  },
  3389: {
    "protocollo": "RDP (Remote Desktop Protocol)",
    "descrizione": "Accesso remoto ai desktop Windows."
  },
  5060: {
    "protocollo": "SIP (Session Initiation Protocol)",
    "descrizione": "Gestione di sessioni VoIP."
  },
  5432: {
    "protocollo": "PostgreSQL",
    "descrizione": "Accesso ai database PostgreSQL."
  },
  5900: {
    "protocollo": "VNC (Virtual Network Computing)",
    "descrizione": "Accesso remoto a desktop tramite VNC."
  },
  8080: {
    "protocollo": "HTTP Alternativo",
    "descrizione": "Spesso utilizzata per HTTP quando la porta 80 è occupata."
  },
  8443: {
    "protocollo": "HTTPS Alternativo",
    "descrizione": "Versione sicura dell'HTTP su porta alternativa."
  }
}

target = input("Inserire l'IP della macchina da scansionare: ")
portrange = input("Inserire un port range (default: 5-200): ")
lowport = 5
highport = 200

if "-" in portrange:
    lowport = int(portrange.split('-')[0])
    highport = int(portrange.split('-')[1])

print("Scansiono host:", target, "dalla porta", lowport, "alla porta", highport)

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
s.settimeout(0.5)

chiuse = 0
aperte = 0

for porta in range(lowport, highport + 1):
    result = s.connect_ex((target, porta))
    if result == 0:
        aperte +=1
        print(f"Porta numero: {porta} Stato:", Fore.GREEN + "APERTA" + Fore.RESET)
        if porta in porte_note:
            protocolloPorta = porte_note[porta]['protocollo']
            infoPorta = porte_note[porta]['descrizione']
            print("Questa e' una porta nota. Ecco le informazioni:\n")
            print(tabulate([[protocolloPorta, infoPorta]], headers=["Protocollo Di rete", "Informazioni"]) +'\n')
    else:
        chiuse += 1
        print(f"Porta numero: {porta} Stato:", Fore.RED + "CHIUSA" + Fore.RESET)

print("Porte " + Fore.GREEN + "APERTE" + Fore.RESET + ":", str(aperte) +"\nPorte " + Fore.RED + "CHIUSE" + Fore.RESET + ":", str(chiuse))