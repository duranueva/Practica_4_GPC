import socket
import sys

def get_args(): 
    """
    Toma los parámetros enviados por el usuario y los convierte en una lista.

    Returns:
    --------
        La lista con los parámetros proporcionados.
    """
    host = sys.argv[1]
    method = sys.argv[2]
    url = sys.argv[3]
    user_agent = sys.argv[4]
    encoding = sys.argv[5]
    connection = sys.argv[6]
    return [host, method, url, user_agent, encoding, connection]

def get_agent(agent_name):
    """
    Función que recibe el nombre de algunos de los User Agents disponibles y regresa su valor específico.

    Parameters:
    -----------
    agent_name: str
        Nombre del user agent.

    Returns:
    --------
    agent: str.
        User-Agent necesario para realizar la petición.
    """
    user_agents = {
        "Xiaomi": "Mozilla/5.0 (Linux; Android 11; Redmi Note 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "LG": "Mozilla/5.0 (Linux; Android 10; LG G8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sony": "Mozilla/5.0 (Linux; Android 12; Sony Xperia 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Nokia": "Mozilla/5.0 (Linux; Android 11; Nokia 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "HTC": "Mozilla/5.0 (Linux; Android 10; HTC U12+) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Motorola": "Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Samsung": "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Apple": "Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",
        "Windows-Edge": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "MacOS-Safari": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
        "Roku-Ultra": "Roku4640X/DVP-7.70 (297.70E04154A)",
        "Ubuntu-Firefox": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    }
    
    if agent_name in user_agents:
        return user_agents[agent_name]
    else:
        raise ValueError(f"User Agent '{agent_name}' no está en la lista de User Agents disponibles.")

def constructHTTPRequest(args):
    """
    Función donde se crea la petición HTTP que se realizará al servidor

    Parameters:
    ----------
    args: list(str)
        Lista de los argumentos de la petición: host, http_method, url, user_agent, encoding, connection

    Returns:
    ---------
    request: str
        La petición creada
    """
    #Construcción de http request line
    http_method = args[1]
    url = args[2]
    version = "HTTP/1.1"
    request_line = http_method + " " + url +  " " + version + "\r\n"

    #Construcción de headers 
    host = "Host: " + args[0]
    user_agent = "User-Agent: " + get_agent(args[3])
    accept = "Accept: text/html;charset=US-ASCII, text/html;charset=UTF-8, text/plain;charset=US-ASCII,text/plain;charset=UTF-8"
    encoding = "Accept-Encoding: " + args[4]
    language = "Accept-Language: en-US"
    connection = "Connection: " + args[5]

    # Construir el request
    headers = host + "\r\n"+ \
                user_agent + "\r\n"+ \
                accept + "\r\n"+ \
                encoding + "\r\n"+ \
                language + "\r\n"+ \
                connection + "\r\n"
    end = "\r\n"

    request = request_line + \
                 headers + \
                 end

    return request

def TCPConnection(server,request):
    """
    Esta función se conecta con el servidor enviado como parámetro, envía la petición request y espera por una respuesta 

    Parameters:
    -----------
    server: str
        El servidor al que se mandará la petición
    request: str
        La petición bien formada
    """
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.connect((server,80))
    sckt.send(request.encode())

    response = sckt.recv(1024)
    if response == "":
        print("Sin respuesta del servidor")
    else:  
        print(response.decode())

    sckt.close()
    print("Conexión cerrada :)")

def help():
    """
    Imprime la documentación para usar el script.
    """
    print("Uso: python3 httpCliente.py <host> <url> [método] [User-Agent] [codificación] [conexión]")
    print()
    print("Parámetros:")
    print("  <host>          Nombre del host al que realizar la petición.")
    print("  <url>           URL del recurso a solicitar.")
    print("  [método]        Método HTTP a utilizar (GET, HEAD, POST, PUT, DELETE, etc.).")
    print("  [User-Agent]    User-Agent a utilizar (Motorola, Samsung, Apple, Windows-Edge, MacOS-Safari, Roku-Ultra, Ubuntu-Firefox, Xiaomi, LG, Sony, Nokia, HTC).")
    print("  [codificación]  Codificación a utilizar.")
    print("  [conexión]      Tipo de conexión (keep-alive, close).")
    print()
    print("Ejemplo: python3 httpCliente.py example.com /index.html GET Samsung utf-8 keep-alive")

try:
    if sys.argv[0] == '--h' or sys.argv[0] == '--help':
        help()
    else:
        args = get_args()
        request = constructHTTPRequest(args)
        TCPConnection(args[0], request)
except:
    help()
    sys.exit()