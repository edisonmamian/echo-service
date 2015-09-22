Realizado por: Edison Felipe Mamian Ceron 1224279

El archivo echo-server.py tiene el proposito de escuchar por clientes,
cuando recibe un mensaje se encarga de devolver el mismo mensaje al 
cliente que lo envio.

El archivo echo-client.py se encarga de iniciar una coneccion con el 
servidor, una vez establecida la coneccion envia un mensaje el cual es 
ingresado por el usuario, y vuelve a recibir el mismo mensaje pero en 
paquetes de 16 bytes.

Para ejecutar echo-server.py y echo-client.py debe ejecutar las siguientes
lineas de comando en diferentes terminales('numeroPUERTO' hace referencia
al puerto por el cual se van a comunicar el cliente y el servidor).

python echo-server.py --port 'numeroPUERTO'

python echo-client.py --port 'numeroPUERTO'


