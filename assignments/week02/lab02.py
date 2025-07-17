"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

Type = (input("1.THB to USD or 2.USD to THB :"))
Money = float(input("Amout : "))
if Type == "1" :
    USD = Money / 35.5
    print("THB to USD =" ,USD," Dollar")
if Type == "2" :
    THB = Money * 35.521
    print("USD to THB =" ,THB," Baht")
