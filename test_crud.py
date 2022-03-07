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

    def tearDown(self):
        pass

        # Partie James
    @patch("crud.CRUD.read_users_file")    
    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.modify_users_file")
    def test_add_new_user_Passes_correct_data_to_modify_users_file(
        self, mock_modify_users_file, mock_modify_groups_file, mock_read_users_file
    ):
        """Description: il faut utiliser les mocks des fonctions "read_users_file",
        "modify_users_file", "modify_groups_file" (ou selon votre realisation) pour tester que
        l'information a ajouter pour l'utilisateur a été formée correctement par la fonction, e.g.
        self.modify_users_file(data) -> "data" doit avoir un format et contenu expecte
        il faut utiliser ".assert_called_once_with(expected_data)"

        Note: Ce test a deja ete complete pour vous
        """        
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.modify_users_file(crud.read_users_file())
        mock_modify_users_file.assert_called_once_with(self.users_data)
          		

    @patch("crud.CRUD.read_groups_file")
    @patch("crud.CRUD.modify_groups_file")    
    def test_add_new_group_Passes_correct_data_to_modify_groups_file(
        self, mock_modify_groups_file, mock_read_groups_file
    ):
        """Description: il faut utiliser les mocks des fonctions "read_groups_file",
        "modify_groups_file" (ou selon votre realisation) pour tester que
        l'information a ajouter pour le groupe a été formée correctement par la fonction e.g.
        self.modify_groups_file(data) -> "data" doit avoir un format et contenu attendu
        il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_groups_file.return_value= self.groups_data
        crud = CRUD()
        crud.modify_groups_file(crud.read_groups_file())
        mock_modify_groups_file.assert_called_once_with(self.groups_data)       

    @patch("crud.CRUD.read_users_file")
    def test_get_user_data_Returns_false_for_invalid_id(self, mock_read_users_file):
        """Description: il faut utiliser le mock de fonction "read_users_file",
        (ou selon votre realisation) pour tester que false (ou bien une exception)
        est retourne par la fonction si ID non-existant est utilisé
        il faut utiliser ".assertEqual()" ou ".assertFalse()"
        """
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertEqual(crud.get_user_data(100,"name"),False)

        
# ?
    @patch("crud.CRUD.read_users_file")
    def test_get_user_data_Returns_false_for_invalid_field(self, mock_read_users_file):
        """Description: il faut utiliser le mock de fonction "read_groups_file",
        (ou selon votre realisation) pour tester que false (ou bien une exception)
        est retourne par la fonction si champ non-existant est utilisé
        il faut utiliser ".assertEqual()" ou ".assertFalse()"
        """
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertEqual(crud.get_user_data(1,"FauxChamp"),False)

    @patch("crud.CRUD.read_users_file")
    def test_get_user_data_Returns_correct_value_if_field_and_id_are_valid(
        self, mock_read_users_file
    ):
        """Description: il faut utiliser le mock de fonction "read_groups_file",
        (ou selon votre realisation) pour tester que une bonne valeur est fournie
        si champ et id valide sont utilises
        il faut utiliser ".assertEqual()""
        """
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertEqual(crud.get_user_data(2,"SpamN"),self.users_data["2"]["SpamN"])

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_data_Returns_false_for_invalid_id(self, mock_read_groups_file):
        """
        Similaire au test_get_user_data_Returns_false_for_invalid_id mais pour un groupe
        """
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_groups_data(100,"name"),False)
  # ?
    @patch("crud.CRUD.read_groups_file")
    def test_get_group_data_Returns_false_for_invalid_field(
        self, mock_read_groups_file
    ):
        """
        Similaire au test_get_user_data_Returns_false_for_invalid_field mais pour un groupe
        """
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_groups_data(1,"FauxChamp"),False)

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_data_Returns_correct_value_if_field_and_id_are_valid(
        self, mock_read_groups_file
    ):
        """
        Similaire au test_get_user_data_Returns_correct_value_if_field_and_id_are_valid mais pour un groupe
        """
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_groups_data(2,"name"),self.groups_data["2"]["name"])

    @patch("crud.CRUD.read_users_file")
    def test_get_user_id_Returns_false_for_invalid_user_name(
        self, mock_read_users_file
    ):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertEqual(crud.get_user_id("InvalidName"),False)

        
  # Partie Masabbir
    @patch("crud.CRUD.read_users_file")
    def test_get_user_id_Returns_id_for_valid_user_name(self, mock_read_users_file):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertEqual(crud.get_user_id('alex@gmail.com'), '1')

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_id_Returns_false_for_invalid_group_name(
        self, mock_read_groups_file
    ):
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertFalse(crud.get_group_id('enemies')) #Group qui n'existe pas

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_id_Returns_id_for_valid_group_name(self, mock_read_groups_file):
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertEqual(crud.get_group_id('friends'), '2')
        
    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    # Modify_user_file mock est inutile pour tester False pour update
    def test_update_users_Returns_false_for_invalid_id(
        self, mock_read_users_file, mock_modify_users_file
    ):
        """Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        (ou selon votre realisation)
        """
        mock_read_users_file.return_data = self.users_data
        crud = CRUD()
        self.assertFalse(crud.update_users(0, "Trust", 60)) #ID inexistant

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_update_users_Returns_false_for_invalid_field(
        self, mock_read_users_file, mock_modify_users_file
    ):
        """Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        (ou selon votre realisation)
        """
        mock_read_users_file.return_data = self.users_data
        crud = CRUD()
        self.assertFalse(crud.update_users(1, "banana", 60)) #Field inexistant

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_update_users_Passes_correct_data_to_modify_users_file(
        self, mock_read_users_file, mock_modify_users_file
    ):
        """Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        (ou selon votre realisation)
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_users(1, "Trust", 78)
        mock_modify_users_file.assert_called_once_with(self.users_data) # Si les données sont valides, la fonction est appelée 1 fois à la fin.

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")    
    def test_update_groups_Returns_false_for_invalid_id(
        self, mock_read_groups_file, mock_modify_groups_file
    ):
        """Il faut utiliser les mocks pour 'read_groups_file' et 'modify_groups_file'
        (ou selon votre realisation)
        """
        mock_read_groups_file.return_data = self.groups_data
        crud = CRUD()
        self.assertFalse(crud.update_groups(6, "Trust", 60)) # ID inexistant

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")    
    def test_update_groups_Returns_false_for_invalid_field(
        self, mock_read_groups_file, mock_modify_groups_file
    ):
        """Il faut utiliser les mocks pour 'read_groups_file' et 'modify_groups_file'
        (ou selon votre realisation)
        """
        mock_read_groups_file.return_data = self.groups_data
        crud = CRUD()
        self.assertFalse(crud.update_groups(0, "Tru", 60)) # Field inexistant

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")    
    def test_update_groups_Passes_correct_data_to_modify_groups_file(
        self, mock_read_groups_file, mock_modify_groups_file
    ):
        """Il faut utiliser les mocks pour 'read_groups_file' et 'modify_groups_file'
        (ou selon votre realisation)
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        crud.update_groups(1, "Trust", 78)
        mock_modify_groups_file.assert_called_once_with(self.groups_data) # Si les données sont valides, la fonction est appelée 1 fois à la fin.

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_remove_user_Returns_false_for_invalid_id(
        self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertFalse(crud.remove_user(3)) # ID inexistant

        # partie de Nicolas
    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_remove_user_Passes_correct_value_to_modify_users_file(
        self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.remove_user("1")
        mock_modify_users_file.assert_called_once_with({
            "2": {
                "name": "mark@mail.com",
                "Trust": 65.45454,
                "SpamN": 171,
                "HamN": 324,
                "Date_of_first_seen_message": 1596844800.0,
                "Date_of_last_seen_message": 1596844800.0,
                "Groups": ["default"],
            }
        })

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_remove_user_group_Returns_false_for_invalid_id(
        self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertFalse(crud.remove_user_group("69","friends"))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_remove_user_group_Returns_false_for_invalid_group(
        self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertFalse(crud.remove_user_group("1", "funTimes"))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")
    def test_remove_user_group_Passes_correct_value_to_modify_users_file(
        self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.remove_user_group("1", "default")
        mock_modify_users_file.assert_called_once_with({
            "1": {
                "name": "alex@gmail.com",
                "Trust": 100,
                "SpamN": 0,
                "HamN": 20,
                "Date_of_first_seen_message": 1596844800.0,
                "Date_of_last_seen_message": 1596844800.0,
                "Groups": [],
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
        })

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")    
    def test_remove_group_Returns_false_for_invalid_id(
        self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertFalse(crud.remove_group("69"))

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")    
    def test_remove_group_Passes_correct_value_to_modify_groups_file(
        self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        crud.remove_group("1")
        mock_modify_groups_file.assert_called_once_with({
            "2": {
                "name": "friends",
                "Trust": 90,
                "List_of_members": ["alex@gmail.com"],
            },
        })

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")    
    def test_remove_group_member_Returns_false_for_invalid_id(
        self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertFalse(crud.remove_group_member("69","alex@gmail.com"))

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")    
    def test_remove_group_member_Returns_false_for_invalid_group_member(
        self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertFalse(crud.remove_group_member("1", "randomStuff@yahoot.com"))

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")    
    def test_remove_group_member_Passes_correct_value_to_modify_groups_file(
        self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        crud.remove_group_member("1", "alex@gmail.com")
        mock_modify_groups_file.assert_called_once_with({
            "1": {
                "name": "default",
                "Trust": 50,
                "List_of_members": ["mark@mail.com"],
            },
            "2": {
                "name": "friends",
                "Trust": 90,
                "List_of_members": ["alex@gmail.com"],
            },
        })
    
    ###########################################
    #               CUSTOM TEST               #
    ###########################################

    @patch("crud.CRUD.read_users_file")    
    def test_add_new_user_returns_false_if_email_already_exist(
        self, mock_read_users_file
    ):
        """Description: On utilise le mock "read_users_file" pour tester que 
            la fonction add_new_user return False si l'email existe deja
        """        
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertFalse(crud.add_new_user("alex@gmail.com", "2022-01-01"))

    @patch("crud.CRUD.read_users_file")    
    def test_add_new_user_returns_false_if_email_has_wrong_format(
        self, mock_read_users_file
    ):
        """Description: On utilise le mock "read_users_file" pour tester que 
            la fonction add_new_user return False si l'email existe deja
        """        
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertFalse(crud.add_new_user("alexgmail.com", "2022-01-01"))

    @patch("crud.CRUD.read_users_file")    
    @patch("crud.CRUD.read_groups_file")    
    @patch("crud.CRUD.modify_users_file")    
    def test_add_new_user_should_call_modify_users_file_with_correct_data(
        self, mock_modify_users_file, mock_read_groups_file, mock_read_users_file
    ):
        """Description: On utilise le mock "read_users_file", "read_groups_file"
        et modify_users_file pour tester qu'on appelle la fonction modify_users_file
        apres qu'on ait respecter les conditions necessaire
        """        
        mock_read_users_file.return_value = self.users_data
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        crud.add_new_user("mario@gmail.com", "2022-01-01")
        mock_modify_users_file.assert_called_once_with(self.users_data)

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_update_users_spamN_Passes_correct_data_to_modify_users_file(
        self, mock_read_users_file, mock_modify_users_file
    ):
        """Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_users(1, "SpamN", 50)
        mock_modify_users_file.assert_called_once_with(self.users_data)

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_update_users_olderDate_Passes_correct_data_to_modify_users_file(
        self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_users(1, "Date_of_first_seen_message", "1999-03-31")
        mock_modify_users_file.assert_called_once_with(self.users_data)

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_update_users_newerDate_Fails_if_older_than_previous_one(
        self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertFalse(crud.update_users(1, "Date_of_last_seen_message", "1999-03-31"))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_update_users_spamN_Passes_correct_data_to_modify_users_file(
        self, mock_read_users_file, mock_modify_users_file
    ):
        """Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_users(1, "SpamN", 30)
        mock_modify_users_file.assert_called_once_with(self.users_data)

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_update_users_spamN_returns_false_if_data_smaller_than_zero(
        self, mock_read_users_file, mock_modify_users_file
    ):
        """Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertFalse(crud.update_users(1, "SpamN", -1))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_update_users_Trust_returns_false_if_data_out_of_limit(
        self, mock_read_users_file, mock_modify_users_file
    ):
        """Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertFalse(crud.update_users(1, "Trust", -1))
        self.assertFalse(crud.update_users(1, "Trust", 101))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    @patch("crud.CRUD.read_groups_file")    
    def test_update_users_Groups_Passes_correct_data(
        self, mock_read_groups_file, mock_read_users_file, mock_modify_users_file
    ):
        """Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_users_file.return_value = self.users_data
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        crud.update_users(1,"Groups", ["friends"])
        mock_modify_users_file.assert_called_once()

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    @patch("crud.CRUD.read_groups_file")    
    def test_update_users_Groups_returns_false_if_doesnt_exist(
        self, mock_read_groups_file, mock_read_users_file, mock_modify_users_file
    ):
        """Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_users_file.return_value = self.users_data
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        self.assertFalse(crud.update_users(1,"Groups", "enemies"))


    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")    
    def test_update_users_name_Passes_correct_data_to_modify_users_file(
        self, mock_read_users_file, mock_modify_users_file
    ):
        """ Il faut utiliser les mocks pour 'read_users_file' et 'modify_users_file'
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_users(1, "name", "alex@gmail.com")
        mock_modify_users_file.assert_called_once_with(self.users_data)

        
    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")    
    def test_update_groups_name_Passes_correct_data_to_modify_groups_file(
        self, mock_read_groups_file, mock_modify_groups_file
    ):
        """Il faut utiliser les mocks pour 'read_groups_file' et 'modify_groups_file'
        Il faut utiliser ".assert_called_once_with(expected_data)"
        """
        mock_read_groups_file.return_value = self.groups_data
        crud = CRUD()
        crud.update_groups(1, "name", "enemies")
        mock_modify_groups_file.assert_called_once_with(self.groups_data)

    @patch("crud.CRUD.read_groups_file") 
    @patch("crud.CRUD.read_users_file")    
    def test_update_groups_list_of_member_returns_false_if_email_not_existent(
        self, mock_read_users_file, mock_read_groups_file
    ):
        """Il faut utiliser les mocks pour 'read_groups_file' et 'read_users_file'
        pour tester qu'on ne peut pas update un groupe avec un email non-existant 
        dans la liste des users.
        """
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        self.assertFalse(crud.update_groups(1, "List_of_members", "mario@gmail.com"))

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file") 
    @patch("crud.CRUD.read_users_file")    
    def test_update_groups_List_of_member_Passes_correct_data_to_modify_groups_file(
        self, mock_read_users_file, mock_read_groups_file, mock_modify_groups_file
    ):
        """Il faut utiliser les mocks pour 'read_groups_file' et 'read_users_file'
        pour tester qu'on update correctememt un groupe avec la nouvelle liste des membres
        """
        mock_read_groups_file.return_value = self.groups_data
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        crud.update_groups(1, "List_of_members", ["alex@gmail.com"])
        mock_modify_groups_file.assert_called_once()
        
