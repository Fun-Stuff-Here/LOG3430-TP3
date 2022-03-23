from crud import CRUD
import unittest
from unittest.mock import patch

import datetime

class TestCRUD(unittest.TestCase):
    def setUp(self):
        # c'est un exemple de données "mock" à utiliser comme "return value" de read_users_file
        self.users_data = {
            "1": {
                "name": "alex@gmail.com",
                "Trust": 100,
                "SpamN": 0,
                "HamN": 20,
                "Date_of_first_seen_message": 1596844800.0,
                "Date_of_last_seen_message": 1596844800.0,
                "Groups": ["default"],
            },
            "2": {
                "name": "mark@mail.com",
                "Trust": 65.45454,
                "SpamN": 171,
                "HamN": 324,
                "Date_of_first_seen_message": 1596844800.0,
                "Date_of_last_seen_message": 1596844800.0,
                "Groups": ["default"],
            }
        }
        # c'est un exemple de données "mock" à utiliser comme "return value" de read_groups_file
        self.groups_data = {
            "1": {
                "name": "default",
                "Trust": 50,
                "List_of_members": ["alex@gmail.com", "mark@mail.com"],
            },
            "2": {
                "name": "friends",
                "Trust": 90,
                "List_of_members": ["alex@gmail.com"],
            },
        }

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_data_Returns_false_for_invalid_id(self, mock_read_groups_file):
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_groups_data(100, "name"), False)

    @patch("crud.CRUD.read_groups_file")
    @patch("crud.CRUD.read_users_file")
    def test_get_group_data_Returns_false_for_invalid_field(
            self, mock_read_groups_file, mock_read_users_file
    ):
        mock_read_users_file.return_value = self.users_data
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_groups_data(1, "FauxChamp"), False)


    @patch("crud.CRUD.read_groups_file")
    def test_innit_crud(
            self, mock_read_groups_file
    ):
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_groups_data(2, "name"), self.groups_data["2"]["name"])

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d1(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.update_groups(0, "Trust", 30)
        crud.remove_group_member(0, "alex@gmail.com")
        crud.remove_group(0)
        self.assertEqual(crud.get_groups_data(0, "name"), False)

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d2(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.update_groups(0, "Trust", 30)
        crud.remove_group(0)
        crud.remove_group_member(0, "alex@gmail.com")
        self.assertEqual(crud.get_groups_data(0, "name"), False)

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d3(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.remove_group(0)
        crud.update_groups(0, "Trust", 30)
        crud.remove_group_member(0, "alex@gmail.com")
        self.assertEqual(crud.get_groups_data(0, "name"), False)

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d4(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.remove_group(0)
        crud.remove_group_member(0, "alex@gmail.com")
        crud.update_groups(0, "Trust", 30)
        self.assertEqual(crud.get_groups_data(0, "name"), False)

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d5(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.remove_group_member(0, "alex@gmail.com")  
        crud.remove_group(0)
        crud.update_groups(0, "Trust", 30)
        self.assertEqual(crud.get_groups_data(0, "name"), False)
    
    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d6(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.remove_group_member(0, "alex@gmail.com")  
        crud.update_groups(0, "Trust", 30)        
        crud.remove_group(0)
        self.assertEqual(crud.get_groups_data(0, "name"), False)

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d7(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.remove_group_member(0, "alex@gmail.com")  
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.update_groups(0, "Trust", 30)        
        crud.remove_group(0)
        self.assertEqual(crud.get_groups_data(0, "name"), False)

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d8(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.remove_group_member(0, "alex@gmail.com")  
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.remove_group(0)
        crud.update_groups(0, "Trust", 30)        
        self.assertEqual(crud.get_groups_data(0, "name"), False)
  
    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d19(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_groups(0, "Trust", 30)
        crud.remove_group(0)
        crud.remove_group_member(0, "alex@gmail.com")
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        self.assertEqual(crud.get_groups_data(0, "name"), self.groups_data["0"]["name"])

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d20(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_groups(0, "Trust", 30)
        crud.remove_group(0)
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.remove_group_member(0, "alex@gmail.com")
        self.assertEqual(crud.get_groups_data(0, "name"), self.groups_data["0"]["name"])

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d21(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_groups(0, "Trust", 30)
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.remove_group_member(0, "alex@gmail.com")
        crud.remove_group(0)
        self.assertEqual(crud.get_groups_data(0, "name"), False)

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d22(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_groups(0, "Trust", 30)
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.remove_group(0)
        crud.remove_group_member(0, "alex@gmail.com")
        self.assertEqual(crud.get_groups_data(0, "name"), False)

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d23(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_groups(0, "Trust", 30)
        crud.remove_group_member(0, "alex@gmail.com")
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        crud.remove_group(0)
        self.assertEqual(crud.get_groups_data(0, "name"), False)

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d24(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_groups(0, "Trust", 30)
        crud.remove_group_member(0, "alex@gmail.com")
        crud.remove_group(0)
        crud.add_new_group("newGroups", 20, ["alex@gmail.com"])
        self.assertEqual(crud.get_groups_data(0, "name"), self.groups_data["0"]["name"])

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.read_groups_file")
    def test_d25(self, mock_read_groups_file, mock_read_users_file):
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertEqual(crud.get_new_group_id(), "0")