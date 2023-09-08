rate = input("What is the current exchange rate for the Euro to Dollar?:")
amount = input("How much currency (in Euros) are you exchanging?")
rate = float(rate)
amount = float(amount)
total = amount * rate
result = total - 3.00
print("Your final result after a $3.00 service fee is:", result)