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
    def show_all_portfolios(self, portfolios):
        return [p._get_admin_view() for p in portfolios]  # admin sees all details


class InvestorApp:
    def show_my_portfolio(self, portfolio):
        return portfolio.get_customer_view()  # investor sees only own details


# Example: Multiple investors
portfolio1 = MutualFundPortfolio("Veera", ["Equity Fund", "Debt Fund"], 500000, 15000)
portfolio2 = MutualFundPortfolio("Ezhil", ["Balanced Fund"], 300000, 10000)
portfolio3 = MutualFundPortfolio("Aadhi", ["Index Fund", "Liquid Fund"], 200000, 5000)

all_portfolios = [portfolio1, portfolio2, portfolio3]

admin = AdminDashboard()
investor = InvestorApp()

print("---- Admin View ----")
for p in admin.show_all_portfolios(all_portfolios):
    print(p)

print("\n---- Investor View (Ezhil) ----")
print(investor.show_my_portfolio(portfolio2))
