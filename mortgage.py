#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import argparse
import decimal

MONTHS_IN_YEAR = 12
POUND_QUANTIZE = decimal.Decimal('.01')

def pound(f, round=decimal.ROUND_CEILING):
    """
    This function rounds the passed float to 2 decimal places.
    """
    if not isinstance(f, decimal.Decimal):
        f = decimal.Decimal(str(f))
    return f.quantize(POUND_QUANTIZE, rounding=round)

class Mortgage:
    def __init__(self, interest, months, amount, term_years=-1, arrangement=-1.):
        self._interest = float(interest)
        self._months = int(months)
        self._amount = pound(amount)
        self._term = int(term_years*MONTHS_IN_YEAR)
        self._arrangement = float(arrangement)

    def rate(self):
        return self._interest

    def month_growth(self):
        return 1. + self._interest / MONTHS_IN_YEAR

    def apy(self):
        return self.month_growth() ** MONTHS_IN_YEAR - 1

    def loan_years(self):
        return float(self._months) / MONTHS_IN_YEAR

    def loan_months(self):
        return self._months

    def amount(self):
        return self._amount

    def arrangement(self):
        return self._arrangement

    def term(self):
        return self._term

    def monthly_payment(self):
        pre_amt = float(self.amount()) * self.rate() / (float(MONTHS_IN_YEAR) * (1.-(1./self.month_growth()) ** self.loan_months()))
        return pound(pre_amt, round=decimal.ROUND_CEILING)

    def monthly_payment_incl_arr(self):
        if (self._arrangement>= 0. and self._term >= 0):
            pre_amt = float(self.amount()) * self.rate() / (float(MONTHS_IN_YEAR) * (1.-(1./self.month_growth()) ** self.loan_months()))
            arr = self._arrangement/self._term
            return self.monthly_payment() + pound(arr, round=decimal.ROUND_CEILING)
        else:
            return self.monthly_payment()

    def total_value(self, m_payment):
        return m_payment / self.rate() * (float(MONTHS_IN_YEAR) * (1.-(1./self.month_growth()) ** self.loan_months()))

    def annual_payment(self):
        return self.monthly_payment() * MONTHS_IN_YEAR

    def total_payout(self):
        return self.monthly_payment() * self.loan_months()

    def monthly_payment_schedule(self):
        monthly = self.monthly_payment()
        balance = pound(self.amount())
        rate = decimal.Decimal(str(self.rate())).quantize(decimal.Decimal('.000001'))
        while True:
            interest_unrounded = balance * rate * decimal.Decimal(1)/MONTHS_IN_YEAR
            interest = pound(interest_unrounded, round=decimal.ROUND_HALF_UP)
            if monthly >= balance + interest:
                yield balance, interest
                break
            principle = monthly - interest
            yield principle, interest
            balance -= principle

def print_summary(m):
    print('{0:>25s}:  {1:>12.6f}'.format('Rate', m.rate()))
    print('{0:>25s}:  {1:>12.6f}'.format('Month Growth', m.month_growth()))
    print('{0:>25s}:  {1:>12.6f}'.format('APY', m.apy()))
    print('{0:>25s}:  {1:>12.0f}'.format('Payoff Years', m.loan_years()))
    print('{0:>25s}:  {1:>12.0f}'.format('Payoff Months', m.loan_months()))
    print('{0:>25s}:  {1:>12.2f}'.format('Amount', m.amount()))
    if (m.arrangement() >= 0. and m.term() >= 0):
        print('{0:>25s}:  {1:>12.2f}'.format('Arrangement', m.arrangement()))
        print('{0:>25s}:  {1:>12.2f}'.format('Term [years]', int(m.term()/MONTHS_IN_YEAR) ))
        print('{0:>25s}:  {1:>12.2f}'.format('Monthly Payment incl arr ', m.monthly_payment_incl_arr()))
    else:
        print('{0:>25s}:  {1:>12.2f}'.format('Monthly Payment', m.monthly_payment()))

    print('{0:>25s}:  {1:>12.2f}'.format('Annual Payment', m.annual_payment()))
    print('{0:>25s}:  {1:>12.2f}'.format('Total Payout', m.total_payout()))

def main():
    parser = argparse.ArgumentParser(description='Mortgage Amortization Tools')
    parser.add_argument('-i', '--interest', default=6, dest='interest')
    parser.add_argument('-y', '--loan-years', default=30, dest='years')
    parser.add_argument('-m', '--loan-months', default=None, dest='months')
    parser.add_argument('-a', '--amount', default=100000, dest='amount')
    args = parser.parse_args()

    if args.months:
        m = Mortgage(float(args.interest) / 100, float(args.months), args.amount)
    else:
        m = Mortgage(float(args.interest) / 100, float(args.years) * MONTHS_IN_YEAR, args.amount)

    print_summary(m)

if __name__ == '__main__':
    main()
