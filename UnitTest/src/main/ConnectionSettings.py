

class ConnectionSettings:
    def __init__(self):
        self.__username = ""
        self.__password = ""
        self.__hostname = ""
        self.__portnumber = 0
        self.__dbms = ""

    def username(self):
        return self.__username

    def setusername(self,a_username):
        self.__username = a_username

    def password(self):
        return self.__password

    def setpassword(self, a_password):
        self.__password = a_password

    def hostname(self):
        return self.__hostname

    def sethostname(self, a_hostname):
        self.__hostname = a_hostname

    def portnumber(self):
        return self.__portnumber

    def setportnumber(self, a_portnumber):
        self.__portnumber = a_portnumber

    def dbms(self):
        return self.__dbms

    def setdbms(self, a_dbms):
        self.__dbms = a_dbms

    def tostring(self):
        tostr = self.__username + ":" + \
            self.__password + ":" + \
            self.__hostname + ":" + \
            str(self.__portnumber) + ":" + \
            self.__dbms
        return tostr
