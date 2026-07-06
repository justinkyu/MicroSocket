import socket
import time

def connect(host, port):

    print()
    print("MicroSocket")
    print("=" * 40)

    start = time.perf_counter()

    try:

        sock = socket.create_connection((host, int(port)), timeout=5)

        elapsed = (time.perf_counter() - start) * 1000

        print("Host      :", host)
        print("Port      :", port)
        print("Status    : CONNECTED")
        print(f"Latency   : {elapsed:.2f} ms")

        sock.close()

    except Exception as e:

        print("Host      :", host)
        print("Port      :", port)
        print("Status    : FAILED")
        print(e)
