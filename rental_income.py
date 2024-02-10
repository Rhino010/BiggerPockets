class InvestmentCalculator():

    def __init__ (self):
        self.income = 0
        self.expenses = 0
        self.cashflow = 0
        self.roi = 0

    def monthInc(self):
        rentinc = int(input('Input monthly rent: '))
        laundryinc = int(input('Input estimated monthly laundry income: '))
        storage = int(input('Input monthly storage income: '))
        misc = int(input('Input total of miscellaneous monthly income items: '))

        self.income = rentinc + laundryinc + storage + misc
        print(f'Your monthyl income is {self.income}.')

    def monthExp(self):
        tax = int(input('Input monthly expense from taxes. '))
        insurance= int(input('Input monthly expense from insurance. '))
        utilities= int(input('Input monthly expense from utilities. '))
        hoa= int(input('Input monthly expense from Home Owners Association. '))
        lawn= int(input('Input monthly expense from lawn care or snow removal. '))
        vacancy= int(input('What is the monthly allowance set aside for vacancy months? '))
        repairs= int(input('Input monthly expense from repairs. '))
        capx= int(input('Input monthly expense from capital expenditures. '))
        propmanage= int(input('Input monthly expense from property management costs. '))
        mortgage= int(input('Input monthly expense from the mortgage payment. '))

        self.expenses = tax + insurance + utilities + hoa + lawn + vacancy + repairs + capx + propmanage + mortgage
        
        print(f'Your total monthly expenses are {self.expenses}')

    def monthlyCFlow(self):
        self.cashflow = self.income - self.expenses
        print(f'Your monthly cashflow minus expenses is {self.cashflow}.')


    def yearROI(self):
        downpayment = int(input('How much was your downpayment? '))
        closecosts = int(input('How much were your closing costs? '))
        rehabbudg = int(input('How much do you expect to put into the property for rehab projects? '))
        misc = int(input('How much do you aniticipate for miscellaneous funds not otherwise accounted for? '))
        totalinvest = downpayment + closecosts + rehabbudg + misc
        yearlyincome = (self.cashflow * 12)
        self.roi = ((yearlyincome / totalinvest) * 100)
        print(f'Your yearly cash on cash return on investment is %{self.roi}.')

calculator = InvestmentCalculator()

while True:
    selection = input('Please select from the following options: 1 = Income input, 2 = Expenses input, 3 = Calculate monthly cashflow, 4 = Calculate yearly ROI. ')
    if selection == '1':
        calculator.monthInc()
    elif selection == '2':
        calculator.monthExp()
    elif selection == '3':
        calculator.monthlyCFlow()
    elif selection == '4':
        calculator.yearROI()
    else:
        print('Input not recognized, please try again.')