
# Importing required libraries
import license

class ComplianceLicensing:
    def __init__(self):
        self.license = license.License()

    def check_compliance(self):
        """
        Function to check compliance
        """
        compliance_status = self.license.check_compliance()
        return compliance_status

    def get_license_details(self):
        """
        Function to get license details
        """
        license_details = self.license.get_details()
        return license_details

if __name__ == "__main__":
    cl = ComplianceLicensing()
    print(cl.check_compliance())
    print(cl.get_license_details())
