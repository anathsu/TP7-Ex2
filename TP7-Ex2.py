from psutil import net_io_counters

def netInfo():
    info = net_io_counters()
    print("Bytes enviados: ", info[0])
    print("Bytes recebidos: ", info[1])
    print("Pacotes enviados: ", info[2])
    print("Pacotes recebidos: ", info[3])
    print("Erros durante recebimento:", info[4])
    print("Erros durante envio:", info[5])
    print("Pacotes recebidos descartados:", info[6])
    print("Pacotes enviados descartados:", info[7])
    
netInfo()