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
        """
		Similaire au test_get_user_data_Returns_false_for_invalid_id mais pour un groupe
		"""
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_groups_data(100, "name"), False)

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_data_Returns_false_for_invalid_field(
            self, mock_read_groups_file
    ):
        """
		Similaire au test_get_user_data_Returns_false_for_invalid_field mais pour un groupe
		"""
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_groups_data(1, "FauxChamp"), False)


    @patch("crud.CRUD.read_groups_file")
    def test_innit_crud(
            self, mock_read_groups_file
    ):
        """
		Similaire au test_get_user_data_Returns_correct_value_if_field_and_id_are_valid mais pour un groupe
		"""
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_groups_data(2, "name"), self.groups_data["2"]["name"])


