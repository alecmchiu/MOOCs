#!/usr/bin/env python3

def calculate(balance, annualInterestRate, monthlyPaymentRate, months=12):
	'''
	balance: initial balance
	annualInterestRate: annual interest rate
	monthlyPaymentRate: monthly payment rate
	months: months elapsed (default: 12)
	return: balance after n months
	'''
	UpdatedBalance = balance
	monthlyInterestRate = annualInterestRate/12.0
	for i in range(months):
		minimumMonthlyPayment = monthlyPaymentRate * UpdatedBalance
		monthlyUnpaidBalance = UpdatedBalance - minimumMonthlyPayment
		UpdatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
	print("Remaining balance: {:.2f}".format(UpdatedBalance))
	return UpdatedBalance

def fixedCalculate(balance, annualInterestRate):
	'''
	balance: initial amount
	annualInterestRate: annual interest rate
	returns: minimum monthly payment to pay off debt
	'''
	UpdatedBalance = balance
	monthlyInterestRate = annualInterestRate/12.0
	minimumMonthlyPayment = 0
	while UpdatedBalance >= 0:
		minimumMonthlyPayment += 10
		UpdatedBalance = balance
		for i in range(12):
			monthlyUnpaidBalance = UpdatedBalance - minimumMonthlyPayment
			UpdatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
	print("Lowest payment: {}".format(minimumMonthlyPayment))
	return minimumMonthlyPayment

def fixedBinaryCalculate(balance, annualInterestRate):
	'''
	balance: initial amount
	annualInterestRate: annual interest rate
	returns: minimum monthly payment to pay off debt
	'''
	UpdatedBalance = balance
	monthlyInterestRate = annualInterestRate/12.0
	lowerBound = balance/12.0
	upperBound = (balance * (1 + monthlyInterestRate)**12)/12.0
	minimumMonthlyPayment = 0
	while abs(UpdatedBalance) > 0.01:
		minimumMonthlyPayment = (upperBound + lowerBound) / 2
		UpdatedBalance = balance
		for i in range(12):
			monthlyUnpaidBalance = UpdatedBalance - minimumMonthlyPayment
			UpdatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
		if UpdatedBalance < 0:
			upperBound = minimumMonthlyPayment
		if UpdatedBalance > 0:
			lowerBound = minimumMonthlyPayment
	print("Lowest payment: {:.2f}".format(minimumMonthlyPayment))
	return minimumMonthlyPayment

if __name__=='__main__':
	#calculate(42, 0.2, 0.04)
	#calculate(484,0.2,0.04)
	#fixedCalculate(3329,0.2)
	#fixedCalculate(4773,0.2)
	#fixedCalculate(3926, 0.2)
	fixedBinaryCalculate(320000,0.2)
	fixedBinaryCalculate(999999,0.18)
