from Common import utils
from Common.breach_checker import BreachChecker

# EmailReputationChecker class inherits methods from BreachChecker super class
class EmailReputationChecker(BreachChecker):
    def __init__(self, email):
        super().__init__(email)
        self.is_valid_email(email)

    def is_valid_email(self, email):
        if super().is_valid_email(email) == True:
            print("Input is a valid Email address.", email)
            try:
                # Call function to check Email reputation from Virus Total
                VT_results = self.checkEmailReputationVT(email)
                print("Virus Total results: ", VT_results)

                # TODO: Call function to check Email reputation from Cisco Talos
                
            except Exception as ex:
                print("Error checking Virus Total reputation: ", ex)
                utils.exit_message(f"Error checking Virus Total reputation:", ex)
        else:
            # print("Input is not a valid Email address.")
            return utils.exit_message("Input is not a valid Email address.")
