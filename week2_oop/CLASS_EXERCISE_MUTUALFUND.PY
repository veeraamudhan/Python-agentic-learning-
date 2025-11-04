class MutualFundPortfolio:
    def __init__(self, investor_name, funds, total_investment, charges):
        self.investor_name = investor_name       # public
        self.funds = funds                       # public
        self.__total_investment = total_investment   # private
        self.__charges = charges                     # private

    def __calculate_net_value(self):  # private helper
        return self.__total_investment - self.__charges

    def _get_admin_view(self):  # protected method
        return {
            "Investor": self.investor_name,
            "Funds": self.funds,
            "Total Investment": f"₹{self.__total_investment}",
            "Charges Deducted": f"₹{self.__charges}",
            "Net Portfolio Value": f"₹{self.__calculate_net_value()}"
        }

    def get_customer_view(self):  # public method
        return {
            "Investor": self.investor_name,
            "Funds": self.funds,
            "Net Portfolio Value": f"₹{self.__calculate_net_value()}"
        }


class AdminDashboard:
    def show_portfolio(self, portfolio):
        return portfolio._get_admin_view()  # accessing protected method


class InvestorApp:
    def show_portfolio(self, portfolio):
        return portfolio.get_customer_view()  # accessing public method


# Example usage
portfolio = MutualFundPortfolio("Veera", ["Equity Fund", "Debt Fund"], 500000, 15000)

admin = AdminDashboard()
customer = InvestorApp()

print(admin.show_portfolio(portfolio))
# {'Investor': 'Veera', 'Funds': ['Equity Fund', 'Debt Fund'],
#  'Total Investment': '₹500000', 'Charges Deducted': '₹15000',
#  'Net Portfolio Value': '₹485000'}

print(customer.show_portfolio(portfolio))
# {'Investor': 'Veera', 'Funds': ['Equity Fund', 'Debt Fund'],
#  'Net Portfolio Value': '₹485000'}
