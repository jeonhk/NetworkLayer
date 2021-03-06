import physicalLayer
import standardSocket as socketLib

lanIP = 'T'

routerDict = {
    "E":("192.168.100.50",5080),
    "I":("192.168.100.73",5073),
    "T":("192.168.100.84",5084)
}




lowerLayer = physicalLayer.PhysicalLayer()

socket, AF_INET, SOCK_DGRAM, timeout = socketLib.socket, socketLib.AF_INET, socketLib.SOCK_DGRAM, socketLib.timeout

with socket(AF_INET, SOCK_DGRAM) as sock:
    print("'routing out' is now running........")
    while True:
        ret=None
        while ret==None:
            ret = lowerLayer.receiveResistor()
            
        print("router got: "+ret)
        dstIP = ret[0]
        if dstIP != lanIP:
            targetRouter = routerDict[dstIP]
            print("sending to router "+dstIP+": "+str(targetRouter))
            sock.sendto(bytearray(ret,encoding="UTF-8"), targetRouter)

