   

class passw:
    def encode(password):
        new = ""
        buffer = len(password)
        for char in password:
            x = str(ord(char)+buffer)
            new += x
        new+= '#'+str(buffer)
        return new
    def decode(pwd):
        x = pwd.find("#")
        buffer = int(pwd[x+1::])
        pwd = pwd[0:x]
        #add recursion here 
        new = ''
        while len(pwd) > 0:
            new, pwd = passw.keep(new, pwd, buffer)
        return new
    def keep(new,pwd,buffer):
        if 34+buffer<=int(pwd[0:2])<=122+buffer:
            n = int(pwd[0:2]) - buffer
            new += str(chr(n))
            pwd = pwd[2::]
            return new, pwd
        else:
            n = int(pwd[0:3]) - buffer
            new += str(chr(n))
            pwd = pwd[3::]
            return new, pwd