from unittest import TestCase
from src.main.ConnectionSettings import ConnectionSettings


class TestConnectionSettings(TestCase):
    expected_username = "TestUserName"
    expected_password = "ExpectedPassword"
    expected_hostname = "ExpectedHostName"
    expected_portnumber = 12345
    expected_dbms = "ExpectedDBMS"

    def test_defaultCreate(self):
        cd = ConnectionSettings()
        self.assertEqual(cd.username(), "", "Property username is not correctly set.")
        self.assertEqual(cd.password(), "", "Property password is not correctly set.")
        self.assertEqual(cd.hostname(), "", "Property hostname is not correctly set.")
        self.assertEqual(cd.portnumber(), 0, "Property portnumber is correctly set.")
        self.assertEqual(cd.dbms(), "", "Property dbms is not correctly set.")

    def test_tostring(self):

        expected_tostring = \
            TestConnectionSettings.expected_username + ":" + \
            TestConnectionSettings.expected_password + ":" + \
            TestConnectionSettings.expected_hostname + ":" + \
            str(TestConnectionSettings.expected_portnumber) + ":" + \
            TestConnectionSettings.expected_dbms

        cd = ConnectionSettings()
        cd.setusername(TestConnectionSettings.expected_username)
        cd.setpassword(TestConnectionSettings.expected_password)
        cd.sethostname(TestConnectionSettings.expected_hostname)
        cd.setportnumber(TestConnectionSettings.expected_portnumber)
        cd.setdbms(TestConnectionSettings.expected_dbms)
        test_tostring = cd.tostring()
        self.assertEqual(expected_tostring, test_tostring, "Method tostring returns incorrect values.")

    def test_username(self):
        cd = ConnectionSettings()
        cd.setusername(TestConnectionSettings.expected_username)
        test_username = cd.username()
        self.assertEqual(TestConnectionSettings.expected_username, test_username, "Property username is incorrect.")

    def test_password(self):
        cd = ConnectionSettings()
        cd.setpassword(TestConnectionSettings.expected_password)
        test_password = cd.password()
        self.assertEqual(TestConnectionSettings.expected_password, test_password, "Property password is incorrect.")

    def test_hostname(self):
        cd = ConnectionSettings()
        cd.sethostname(TestConnectionSettings.expected_hostname)
        test_hostname = cd.hostname()
        self.assertEqual(TestConnectionSettings.expected_hostname, test_hostname, "Property hostname is incorrect.")

    def test_portnumber(self):
        cd = ConnectionSettings()
        cd.setportnumber(TestConnectionSettings.expected_portnumber)
        test_portnumber = cd.portnumber()
        self.assertEqual(TestConnectionSettings.expected_portnumber, test_portnumber, \
                         "Property portnumber is incorrect.")

    def test_dbms(self):
        cd = ConnectionSettings()
        cd.setdbms(TestConnectionSettings.expected_dbms)
        test_dbms = cd.dbms()
        self.assertEqual(TestConnectionSettings.expected_dbms, test_dbms, "Property dbms is incorrect.")