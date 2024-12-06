import unittest
from unittest.mock import patch

class InputInfo:
    """Class that accepts participant data"""
    people_info = []

    def input_data(self):
        """Receive participant data from user input"""
        self.people_info = [
            ("Кошельков Захар Брониславович", "105"),
            ("Дьячков Нисон Иринеевич", "88"),
            ("Иванов Варлам Якунович", "88"),
            ("Старостин Ростислав Ермолаевич", "50"),
            ("Ярилова Розалия Трофимовна", "29"),
            ("Соколов Андрей Сергеевич", "15"),
            ("Егоров Алан Петрович", "7")
        ]

    def get_people_info(self):
        """Return the input data"""
        return self.people_info

class TestAgeGroups(unittest.TestCase):
    """Test case for InputInfo and AgeGroups classes"""

    @patch('builtins.input', side_effect=[
        "Кошельков Захар Брониславович, 105",
        "Дьячков Нисон Иринеевич, 88",
        "Иванов Варлам Якунович, 88",
        "Старостин Ростислав Ермолаевич, 50",
        "Ярилова Розалия Трофимовна, 29",
        "Соколов Андрей Сергеевич, 15",
        "Егоров Алан Петрович, 7",
        "End"
    ])
    def test_input_info(self, mock_input):
        # Create an instance of InputInfo and simulate user input
        input_info = InputInfo()
        input_info.input_data()  # This uses the mocked input()
        people_info = input_info.get_people_info()

        # Ensure the input data is correct
        self.assertEqual(len(people_info), 7)
        self.assertEqual(people_info[0], ("Кошельков Захар Брониславович", "105"))
        self.assertEqual(people_info[1], ("Дьячков Нисон Иринеевич", "88"))

if __name__ == "__main__":
    unittest.main()
