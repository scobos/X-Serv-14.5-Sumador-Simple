# Me has dado un 2. Dame mas
# Me habias dado un 2. Ahora un 3. Suman 5
# Me has dado una a. Vete
#Me has dado un 2.45, Vete

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1235))

mySocket.listen(5)

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        peticion = recvSocket.recv(2048).decode("utf-8", "strict") #bytes! -> utf-8
        print(peticion)
        #recurso = peticion.split()[1][1:]
        if primera:
            sum1 = peticion.split()[1][1:]
            if recurso == "favicon.ico":
                    recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1> Not Found </h1></body></html>\r\n", 'utf-8'))
                    recvSocket.close()
                    continue
            #sum1, sum2 = recurso.split('+')
            #suma = int(sum1) + int(sum2)
            print('Answering back')
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>Me has dado un </h1>" +
                            "<p>" + str(sum1) +
                            "</p>.Dame mas" +
                            "</body></html>" +
                            "\r\n", 'utf-8'))
            recvSocket.close()
        else:


except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
