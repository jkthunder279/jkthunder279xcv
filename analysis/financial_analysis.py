# analysis/financial_analysis.py

class FinancialAnalyzer:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def calculate_savings(self):
        return self.income - self.expenses

    def savings_rate(self):
        return (self.calculate_savings() / self.income) * 100 if self.income else 0

    def is_financially_healthy(self):
        return self.calculate_savings() > 0