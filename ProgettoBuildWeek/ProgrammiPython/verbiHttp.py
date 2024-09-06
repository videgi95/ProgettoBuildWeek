import requests

url = input("Inserire l'url interessato: ")
#'http://192.168.70.100/phpMyAdmin/1'

while True:
    print("\nScegliere quale verbo HTTP si vuole verificare")
    print("\n1 per la richiesta OPTIONS")
    print("2 per la richiesta GET")
    print("3 per la richiesta POST")
    print("4 per la richiesta PUT")
    print("5 per la richiesta DELETE")
    print("6 per la richiesta HEAD")
    print("7 per la richiesta TRACE")
    print("8 per inserire un nuovo url")
    inp = input("Digitare 9 per uscire: ")


    if inp == '1':
        #Metodo OPTIONS
        response_options = requests.options(url)
        print("\n-----------------------------------------------------------------------")
        print("OPTIONS Status Code:", response_options.status_code)
        print("OPTIONS Allowed Methods:", response_options.headers.get('Allow'))
        print("-----------------------------------------------------------------------")
    elif inp == '2':
        # Metodo GET
        print("\n-----------------------------------------------------------------------")
        response_get = requests.get(url)
        print("GET Status Code:", response_get.status_code)
        print("-----------------------------------------------------------------------")
    elif inp == '3':
        # Metodo POST
        print("\n-----------------------------------------------------------------------")
        response_post = requests.post(url)
        print("POST Status Code:", response_post.status_code)
        print("-----------------------------------------------------------------------")
    elif inp == '4':
        # Metodo PUT -> Aggiorna una risorsa esistente
        print("\n-----------------------------------------------------------------------")
        response_put = requests.put(url)
        print("PUT Status Code:", response_put.status_code)
        print("-----------------------------------------------------------------------")
    elif inp == '5':
        # Metodo DELETE -> Elimina una risorsa esistente
        print("\n-----------------------------------------------------------------------")
        response_delete = requests.delete(url)
        print("DELETE Status Code:", response_delete.status_code)
        print("-----------------------------------------------------------------------")
    elif inp == '6':
        # Metodo HEAD -> Recupera solo gli header di una risorsa esistente
        response_head = requests.head(url)
        print("\n-----------------------------------------------------------------------")
        print("HEAD Status Code:", response_head.status_code)
        print("Response Headers:", response_head.headers)
        print("-----------------------------------------------------------------------")
    elif inp == '7':
        response_trace = requests.request('TRACE', url)
        # Metodo TRACE -> Esegue un loopback della richiesta per scopi di debug
        print("\n-----------------------------------------------------------------------")
        print("TRACE Status Code:", response_head.status_code)
        print("Response Text:", response_trace.text)
        print("-----------------------------------------------------------------------")
    elif inp == '8':
        url = input("Inserire l'url interessato: ")
    elif inp == '9':
        print("\nUscita dal programma...")
        break    