class InputInfo:
    """Class to receive participant information"""
    people_info = []

    def input_data(self):
        """Receives participant data from user input"""
        print("Enter participant data in the format: Name,Age (no spaces). Type 'End' to finish.")
        while True:
            person_info = input("Enter data: ")
            if person_info.lower() != "end":
                self.people_info.append(person_info.split(","))
            else:
                break

    def input_people_info(self):
        """Calls the function to receive participant data"""
        self.input_data()

    def get_people_info(self):
        """Returns the data of participants that have been entered"""
        return self.people_info


class AgeGroups:
    """Class that groups participants by age"""
    # Age ranges where each group contains the upper limit of that range.
    ages = [18, 25, 35, 45, 60, 80, 100]
    age_groups: list
    people_info: list

    def __init__(self, people_info: list):
        # Initialize the range of age intervals
        # Lower and upper bounds for the age intervals
        self.ages = [-1] + self.ages + [123]
        # Empty list for each age group
        self.age_groups = [[] for _ in range(len(self.ages))]
        self.people_info = people_info

    def people_to_age_groups(self):
        """Groups participants by age into their respective age groups"""
        for person in self.people_info:
            name, age = person[0], int(person[1])
            for i in range(1, len(self.ages)):
                if self.ages[i-1] < age <= self.ages[i]:
                    self.age_groups[i-1].append((name, age))
                    break

    def sort_people_in_age_groups(self):
        """Sorts participants in each age group in descending order of their age"""
        for group in range(len(self.age_groups)):
            self.age_groups[group] = sorted(
                self.age_groups[group], key=lambda x: x[1], reverse=True)

    def format_group_output(self, group_index):
        """Formats the output for each age group"""
        group_output = []
        for person in self.age_groups[group_index]:
            group_output.append(f"{person[0]} ({person[1]})")
        return ", ".join(group_output)

    def get_people_ages_statistic(self):
        """Displays the result of grouping participants by age and sorting them"""
        self.people_to_age_groups()  # Group participants by age
        self.sort_people_in_age_groups()  # Sort participants within each group
        output = []
        for i in range(len(self.age_groups) - 1, -1, -1):
            if self.age_groups[i]:
                # Define the age range for the group
                age_range = f"{self.ages[i]}-{self.ages[i+1] - 1}"
                group_output = self.format_group_output(i)
                output.append(f"{age_range}: {group_output}")
        return "\n".join(output)


if __name__ == "__main__":
    # Creating an instance of InputInfo to collect participant data
    utils = InputInfo()
    utils.input_people_info()  # Collect input from the user
    people_info = utils.get_people_info()  # Retrieve the entered data
    # Create an instance of AgeGroups
    sort_to_age_groups = AgeGroups(people_info)
    # Get the grouped and sorted result
    result = sort_to_age_groups.get_people_ages_statistic()
    print(result)  # Display the result
