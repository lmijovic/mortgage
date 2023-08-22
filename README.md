# Mortgage rate calculator and UK data analysis

## Install 

```
git clone https://github.com/lmijovic/mortgage.git
cd mortgage
conda create --name mortgage --file requirements.txt 
conda activate mortgage
pip install -e .

```

## Run 

### Mortgage summary:

```
cd scripts

python get_mtg_into.py --amount=300000.0 --rate=0.05 --years=30

```

Produces this summary: 


```
                     Rate:      0.050000
             Month Growth:      1.004167
                      APY:      0.051162
             Payoff Years:            30
            Payoff Months:           360
                   Amount:     300000.00
          Monthly Payment:       1610.47
           Annual Payment:      19325.64
             Total Payout:     579769.20

```

### UK data analysis 

Data from Office of National Statistics: https://www.ons.gov.uk

```
cd scripts

python plot_rate_profile.py --start=01-01-2000

```

Produces this figure:

![Bank of England interest rate, UK consumer price index inflation](figures/uk_monetary.png)

## TODO

* unit tests

* scripts doc 

* unclutter 

* rename 


## Resources
* Office of national statistics  https://www.ons.gov.uk/economy/inflationandpriceindices , and specifically: https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/consumerpriceinflation/july2023
* Bank of England https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate


