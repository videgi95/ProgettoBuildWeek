import socket as soc

ServerAddress = input("Inserisci l'IP della macchina: ") #Input della macchina su cui si vuole catturare il socket di rete
ServerPort = int(input("Inserisci il numero della porta nell'intervallo 1024-49151: ")) #porta che si vuole occupare

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM) #porta TCP
s.bind((ServerAddress, ServerPort)) #richiesta al SO di occupare la porta con il mio programma
backlog = int(input("Quante macchine al massimo si possono collegare con me? (Default: 1): "))
if not backlog: backlog = 1
s.listen(backlog) #quante macchine max si possono collegare con me?
print(f"Attendo connessioni in entrata su {ServerPort}")

connection, address = s.accept() #questo blocca il programma
print("Si e' connesso l'indirizzo:", address)

while True:
    data = connection.recv(1024) #1024 caratteri per volta, cosi' non rimane troppo in attesa.
    if not data: break #si e' interrotta la connesione, liberiamo la porta
    print(data.decode("UTF-8")) #stampo cio' che e' arrivato
connection.close() #Chiudo la connessione

