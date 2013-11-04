Stock Price Decline Checker
===========================

Checks a list of stocks to see if the price has declined a certain percentage
from its maximum price over a specified number of days.

The goal is to identify primarily index ETFs that have declined substantially
in price from their maximum values over the past few weeks or months, which
could potentially signal a buying opportunity.

## Author

<a href="http://www.nicholaskuechler.com/">Nicholas Kuechler</a>

## Requirements

* argparse
* matplotlib - to pull the stock quote data from Yahoo! Finance

You can install them with pip:

    pip install argparse
    pip install matplotlib

Or you can install them using pip and the requirements.txt file:

    pip install -r requirements.txt

## Example

Show help menu:

    python stock-price-decline-checker.py -h

Run the decline checker against some index ETFs:

    python stock-price-decline-checker.py -s QQQ,SPY,DIA -d 50 -p 5 -v

Example output:

<pre>
Symbols: ['QQQ', 'SPY', 'DIA']
Percent: 5.0
Days: 50
Verbose: True

Checking for a 5.0% decline over the past 50 days

Index stock: QQQ
- max value over 50 days: 83.06
- most recent close: 82.81
- percent change: -0.3%

Index stock: SPY
- max value over 50 days: 177.17
- most recent close: 176.21
- percent change: -0.54%

Index stock: DIA
- max value over 50 days: 156.5
- most recent close: 155.86
- percent change: -0.41%
</pre>

The stock price decline checker will display an alert if the stock has dropped
in price greater than the percentage specified:

    python stock-price-decline-checker.py -s GOOG,FB -d 50 -p 7.5

Note how FB now has triggered an alert since it has fallen over 7.5%:

<pre>
Checking for a 7.5% decline over the past 50 days

Index stock: GOOG
- max value over 50 days: 1036.24
- most recent close: 1027.04
- percent change: -0.89%

Index stock: FB
- max value over 50 days: 54.22
- most recent close: 49.75
- percent change: -8.24%

ALERT! FB has dropped -8.24% over the last 50 days
</pre>