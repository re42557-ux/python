principle =float(input("principle amount: "))
years = int(input("years to maturity: "))
if principle > 100000 and years == 5:
    interest_rate =0.06
elif principle >= 50000 and principle <= 100000 and years == 10:
    interest_rate =0.05
elif principle >= 50000 and principle <= 100000 and years == 5:
    interest_rate =0.04
else:
    interest_rate =0.02
interest =principle*interest_rate
print()
print(f"Principle:${principle:10.2f}")
print(f"Interest rate:{interest_rate:10.2%}")
print(f"First-year interest: ${interest:8.2f}")
