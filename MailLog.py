import sys
import os
import MailGui
def Print_Last_Lines():
    fname="MailLog.txt"
    lines=10
    num_lines = 0
    with open(fname) as f:
        for line in f:
            num_lines += 1
    if num_lines<=10:
        with open (fname) as f:
            MailGui.MailLog(f.read())
    else:
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        data = []
                        x=""
                        while True:
                                iter +=1
                                f.seek(fsize-bufsize*iter)
                                data.extend(f.readlines())
                                if len(data) >= lines or f.tell() == 0:
                                        x=x.join(data[-lines:])
                                        MailGui.MailLog(x)
                                        break

