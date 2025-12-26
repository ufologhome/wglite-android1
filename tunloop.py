import os, socket

udp_sock = None

def tun_loop(tun_fd, ip, port):
    global udp_sock
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = os.read(tun_fd, 2048)
        udp_sock.sendto(data, (ip, port))
