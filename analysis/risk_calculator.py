class RiskCalculator:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def calculate_risk(self):
        if self.income == 0:
            return "Infinite risk: No income."
        risk_ratio = self.expenses / self.income
        if risk_ratio < 0.5:
            return "Low financial risk"
        elif 0.5 <= risk_ratio < 0.8:
            return "Moderate financial risk"
        else:
            return "High financial risk"

    def __str__(self):
        return f"RiskCalculator(income={self.income}, expenses={self.expenses})"