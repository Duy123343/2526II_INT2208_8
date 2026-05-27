import unittest

def loan_decision(age: int, income: float, credit_score: int, employment: str) -> str:
    if not isinstance(age, int) or not isinstance(credit_score, int):
        return "Invalid Input"
    if not isinstance(income, (int, float)):
        return "Invalid Input"

    if not (18 <= age <= 65):
        return "Invalid Input"
    if not (5.0 <= income <= 500.0):
        return "Invalid Input"
    if not (300 <= credit_score <= 850):
        return "Invalid Input"
    if employment not in ["C", "F"]:
        return "Invalid Input"

    if 300 <= credit_score <= 500:
        risk = "High"
    elif 501 <= credit_score <= 700:
        risk = "Medium"
    else:
        risk = "Low"

    if risk == "High":
        return "REJECT"

    if income < 15.0:
        if employment == "C" and risk == "Low":
            return "MANUAL REVIEW"
        else:
            return "REJECT"
    else:
        if employment == "C":
            return "APPROVE"
        else:
            return "MANUAL REVIEW"

class TestLoanDecisionSystem(unittest.TestCase):
    def test_tc01_age_below_bound(self):
        self.assertEqual(loan_decision(17, 50.0, 750, "C"), "Invalid Input")

    def test_tc02_age_above_bound(self):
        self.assertEqual(loan_decision(66, 50.0, 750, "C"), "Invalid Input")

    def test_tc03_income_below_bound(self):
        self.assertEqual(loan_decision(30, 4.9, 750, "C"), "Invalid Input")

    def test_tc04_income_above_bound(self):
        self.assertEqual(loan_decision(30, 500.1, 750, "C"), "Invalid Input")

    def test_tc05_credit_below_bound(self):
        self.assertEqual(loan_decision(30, 50.0, 299, "C"), "Invalid Input")

    def test_tc06_credit_above_bound(self):
        self.assertEqual(loan_decision(30, 50.0, 851, "C"), "Invalid Input")

    def test_tc07_employment_invalid_char(self):
        self.assertEqual(loan_decision(30, 50.0, 750, "X"), "Invalid Input")

    def test_tc08_r1_low_income_low_risk_contract(self):
        self.assertEqual(loan_decision(18, 14.9, 701, "C"), "MANUAL REVIEW")

    def test_tc09_r2_low_income_low_risk_freelance(self):
        self.assertEqual(loan_decision(65, 5.0, 850, "F"), "REJECT")

    def test_tc10_r3_low_income_med_risk_contract(self):
        self.assertEqual(loan_decision(30, 10.0, 501, "C"), "REJECT")

    def test_tc11_r4_low_income_med_risk_freelance(self):
        self.assertEqual(loan_decision(30, 10.0, 700, "F"), "REJECT")

    def test_tc12_r5_high_income_low_risk_contract(self):
        self.assertEqual(loan_decision(30, 15.0, 750, "C"), "APPROVE")

    def test_tc13_r6_high_income_med_risk_contract(self):
        self.assertEqual(loan_decision(30, 500.0, 600, "C"), "APPROVE")

    def test_tc14_r7_high_income_low_risk_freelance(self):
        self.assertEqual(loan_decision(30, 20.0, 800, "F"), "MANUAL REVIEW")

    def test_tc15_r8_high_income_med_risk_freelance(self):
        self.assertEqual(loan_decision(30, 20.0, 550, "F"), "MANUAL REVIEW")

    def test_tc16_r9_high_risk_always_reject(self):
        self.assertEqual(loan_decision(30, 400.0, 300, "C"), "REJECT")

if __name__ == "__main__":
    unittest.main()