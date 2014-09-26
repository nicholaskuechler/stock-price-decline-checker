#!/usr/bin/env python

import datetime
import argparse

from matplotlib.finance import quotes_historical_yahoo_ochl


def rate_of_return(start, end):
    rate = ((end - start) / start) * 100.0
    return rate


def symbol_list(symbols):
    return map(str, symbols.split(","))


def main(symbols, percent, days, verbose):
    if verbose:
        print "Symbols: %s" % symbols
        print "Percent: %s" % percent
        print "Days: %d" % days
        print "Verbose: %s" % verbose

    print

    if days > 0:
        days = -days

    print "Checking for a %s%% decline over the past " \
          "%d days" % (percent, abs(days))
    print

    for ticker in symbols:
        ticker = ticker.upper()
        print "Stock: %s" % ticker

        start_date = datetime.datetime.now() + datetime.timedelta(days)
        end_date = datetime.datetime.now()

        quotes_objects = quotes_historical_yahoo_ochl(ticker,
                                                      start_date,
                                                      end_date,
                                                      asobject=True)

        max_value = round(float(max(quotes_objects.close)), 5)
        print "- max value over %d days: %s" % (abs(days), max_value)

        most_recent_close = round(float(quotes_objects.close[-1]), 5)
        print "- most recent close: %s" % most_recent_close

        percent_change = round(float(
                               rate_of_return(max_value, most_recent_close)
                               ), 2)
        print "- percent change: %s%%" % percent_change

        if percent_change < -percent:
            print
            print "ALERT! %s has dropped %s%% " \
                  "over the last %s days" % (ticker,
                                             percent_change,
                                             abs(days))

        print


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--symbols", type=symbol_list,
                        default="SPY,QQQ,DIA",
                        help="Comma separate list of symbols. "
                             "Example: SPY,QQQ")
    parser.add_argument("-p", "--percent", type=float,
                        default=5.0,
                        help="Percent change. Example: 5")
    parser.add_argument("-d", "--days", type=int,
                        default=50,
                        help="Number of days. Example: 50")
    parser.add_argument("-v", "--verbose", action="store_true",
                        default=False,
                        help="Increase output verbosity")

    args = parser.parse_args()
    main(args.symbols, args.percent, args.days, args.verbose)
