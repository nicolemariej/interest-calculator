investmentAmount = float(input("What is the investment amount in $?"))
years = int(input("Enter the number of years"))
rate = float(input("What is the percentage rate?"))

print("Year\tStarting balance\tInterest\t\tEnding Balance")

startBalance = investmentAmount
totalInterest = 0.0
i = 1

while i <= years:
    interest = startBalance * rate / 100
    endBalance = startBalance + interest
    print(i, "\t\t", round(startBalance, 2), "\t\t\t", round(endBalance, 2))
    totalInterest += interest
    startBalance = endBalance
    i += 1

print("Ending balance: $", round(endBalance, 2))
print("Total interest earned: $", round(totalInterest, 2))
