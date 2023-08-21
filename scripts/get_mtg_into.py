import mortgage
m=mortgage.Mortgage(interest=0.0625, amount=300000, months=30*12, term_years = 2, arrangement=999.)
mortgage.print_summary(m)
