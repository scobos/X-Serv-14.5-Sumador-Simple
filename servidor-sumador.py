# Me has dado un 2. Dame mas
# Me habias dado un 2. Ahora un 3. Suman 5
# Me has dado una a. Vete
#Me has dado un 2.45, Vete

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1235))

mySocket.listen(5)
primera = True;
try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        peticion = recvSocket.recv(2048).decode("utf-8", "strict") #bytes! -> utf-8
        print(peticion)
        recurso = peticion.split()[1][1:]
        if recurso == "favicon.ico":
                recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1> Not Found </h1></body></html>\r\n", 'utf-8'))
                recvSocket.close()
                continue
        try:
            entero = int(recurso)
        except ValueError:
            recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1> Me has dado un " + str(recurso) + ". Vete</h1></body></html>\r\n", 'utf-8'))
            recvSocket.close()
            continue


        print('Answering back')
        if primera:
            sum1 = entero
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><p>Me has dado un " +
                             str(sum1) + ".Dame mas</p></body></html>" +
                             "\r\n", 'utf-8'))
            primera = False
        else:
            sum2 = entero
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><p>Me habias dado un " +
                            str(sum1) + ".Ahora un " + str(sum2) +
                            ".Suman " + str(sum1+sum2) +
                            ".</p></body></html>" +
                            "\r\n", 'utf-8'))
            primera = True
        recvSocket.close()

except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
