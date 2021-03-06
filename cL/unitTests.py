import unittest
import sys
from  models import UsersModel

#Error codes
SUCCESS = 1
ERR_BAD_CREDENTIALS = -1
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3 
ERR_BAD_PASSWORD = -4

class TestUsers(unittest.TestCase):
    """
    Unittests for the Users model class (a sample, incomplete)
    """
    def setUp(self):
        self.users = UsersModel()
        UsersModel.UsersModelManager.reset ()

        
    def testAdd1(self):
        """
        Tests that adding a user works
        """
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user1", "password"))

    def testAddExists(self):
        """
        Tests that adding a duplicate user name fails
        """
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user1", "password"))
        self.assertEquals(ERR_USER_EXISTS, UsersModel.UsersModelManager.add("user1", "password"))

    def testAdd2(self):
        """
        Tests that adding two users works
        """
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user1", "password"))
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user2", "password"))

    def testLogin1(self):
        """
        Tests login count
        """
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user1", "password"))
        self.assertEquals(2, UsersModel.UsersModelManager.login("user1", "password"))

    def testLogin2(self):
        """
        Tests logins with multiple users
        """
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user1", "password"))
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user2", "password2"))
        self.assertEquals(2, UsersModel.UsersModelManager.login("user1", "password"))
        self.assertEquals(3, UsersModel.UsersModelManager.login("user1", "password"))
        self.assertEquals(2, UsersModel.UsersModelManager.login("user2", "password2"))
        

    def testLoginFail(self):
        """
        Tests that adding an user with empty username fails
        """
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user1", "password"))
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user2", "password2"))
        self.assertEquals(ERR_BAD_CREDENTIALS, UsersModel.UsersModelManager.login("user1", "password2"))
        self.assertEquals(ERR_BAD_CREDENTIALS, UsersModel.UsersModelManager.login("user2", "password"))

    def testAddLongUsername(self):
        """
        Tests that adding an user with empty username fails
        """
        self.assertEquals(ERR_BAD_USERNAME, UsersModel.UsersModelManager.add("u"*129, "password"))

    def testAddLongPassword(self):
        """
        Tests that adding an user with empty username fails
        """
        self.assertEquals(ERR_BAD_PASSWORD, UsersModel.UsersModelManager.add("user1", "p"*129))

    def testAddEmptyUsername(self):
        """
        Tests that adding an user with empty username fails
        """
        self.assertEquals(ERR_BAD_USERNAME, UsersModel.UsersModelManager.add("", "password"))

    def testAddEmptyPassword(self):
        """
        Tests that adding an user with empty username fails
        """
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.add("user1", ""))

    def testresetFixture(self):
        self.assertEquals(SUCCESS, UsersModel.UsersModelManager.reset())


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
