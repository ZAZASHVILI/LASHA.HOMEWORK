principal = float(input())
interest_rate = float(input())
years = 2
interest_earned = principal * (1 + interest_rate) ** years - principal
total_amount = principal + interest_earned
print(total_amount)