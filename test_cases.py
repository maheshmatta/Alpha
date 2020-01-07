import unittest
from server_functions import *


class TestSum(unittest.TestCase):
    def test_register(self):
        input_values = [
            [["register","sushma","123","user"],('127.0.0.1', 56683)],
            [["register","asri","123","admin"],('127.0.0.1', 56683)],
            [["register","bcd","123","adymin"],('127.0.0.1', 56683)]
        ]
        Expected_outputs = [
            ' Personal folder created ',
            ' Username already exists ',
            ' Invalid privilege entered '
        ]
        result = []
        for i in input_values:
            result.append(register(i[0],i[1]))
            print(i[0])
        self.assertListEqual(result, Expected_outputs)
    def test_login(self):
        input_values = [
            [["login","asri","153"],('127.0.0.1', 56683)],
            [["login","asri","123"],('127.0.0.1', 56683)],
            [["login","kdufg","123"],('127.0.0.1', 56683)],
            [["login","asri","123"],('127.0.0.1', 56684)]
        ]
        Expected_outputs = [
           'Login Unsuccesful - Wrong Password',
           'Login succesful - Admin',
           'Username does not exist',
           " User already logged in "
        ]
        result = []
        for i in input_values:
            result.append(login(i[0],i[1]))
        self.assertListEqual(result, Expected_outputs)

    def test_create_folder(self):
        input_values = [
           [["create_folder","asri1"],('127.0.0.1', 56683)],
           [["create_folder","asri"],('127.0.0.1', 56683)],
           [["create_folder","asri1"],('127.0.0.1', 56683)]   
        ]
        Expected_outputs = [
           ' folder created ',
           ' folder cannot be created in ROOT folder'
           " folder name already exists "
        ]
        result = []
        for i in input_values:
            if i == input_values[1]:
                result.append(create_folder(i[0],i[1]))
            else:
                login(["login","asri","123"],('127.0.0.1', 56683))
                result.append(create_folder(i[0],i[1]))

        self.assertListEqual(result, Expected_outputs)


    def test_write_file(self):
        login(["login","asri","123"],('127.0.0.1', 56683))
        input_values = [
           [["write_file", "tex.txt"]],
           [["write_file", "tex.txt", "Asritha is a good girl"]]  
        ]
        Expected_outputs = [
            ' File created ',
            ' FIle writing complete '   
        ]
        result = []
        for i in input_values:
            result.append(write_file(i[0]))
        self.assertListEqual(result, Expected_outputs)

    def test_read_file(self):
        login(["login","asri","123"],('127.0.0.1', 56683))
        input_values = [
           [["read_file", "yfguw.txt"],('127.0.0.1', 56683)],
           [["read_file","text.txt"],('127.0.0.1', 56683)]
        ]
        Expected_outputs = [
            'File doesn´t exist',
            'Hi hello how are u'
        ]
        result = []
        for i in input_values:
            result.append(read_file(i[0],i[1]))
        self.assertListEqual(result, Expected_outputs)


    def test_change_folder(self):
        input_values = [
           [["change_folder", "qwertyu"],('127.0.0.1', 56683)],
           [["change_folder","newfolder"]],
           [["change_folder",'..']],
           [["change_folder",'..']]
        ]
        Expected_outputs = [
            ' folder not found ',
            " Current working DIREctory changed ",
            " Current working DIREctory moved back to previous. ",
            " Cant move back from ROOT folder "
        ]
        result = []
        for i in input_values:
            if i == input_values[3]:
                result.append(change_folder(i[0],i[1]))
            else:
                login(["login","asri","123"],('127.0.0.1', 56683))
                result.append(change_folder(i[0],i[1]))
        self.assertListEqual(result, Expected_outputs)

    def test_delete(self):
        input_values = [
           [["delete", "sushma", '345'],('127.0.0.1', 56683)],
           [["delete", "lasya", '153'],('127.0.0.1', 56683)],
           [["delete", "lasya", '123'],('127.0.0.1', 56683)],
           [["delete", "qwerty", '123'],('127.0.0.1', 56683)]
        ]
        Expected_outputs = [
            "Command cannot be processed due to privilege issues.",
            "Entered password wrong"
            " User deleted ",
            " User name not found ",
        ]
        result = []
        for i in input_values:
            if i == input_values[0]:
                login(["login","lasya","123"],('127.0.0.1', 56685))
                result.append(delete(i[0],i[1]))
            else:
                login(["login","asri","123"],('127.0.0.1', 56683))
                result.append(delete(i[0],i[1]))

        self.assertListEqual(result, Expected_outputs)
    


if __name__ == '__main__':
    unittest.main()