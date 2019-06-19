# Tether-Trade-Simulator

A fun little project to see if trading the crypto currency "Tether" over and over again on small changes would result in any profitable return. Tether is backed by the US dollar, so its price rarely changes that much. However there can be small changes due to minor fluctuations around the $1 US dollar mark.
  
Using the Bitfinex_api available here - https://github.com/akcarsten/bitfinex_api I was able to collect historical data on the coin. Simulating a crypto wallet, and taking into account trade fees of the exchange, the python script runs a small simulation on whether selling on slight increases, and buying on slight decreases might be profitable.

Of course, the simulation is very basic, and fails to take into account more complicated components of the exchanges like volume and the influence of other trades going on. However this is a simple fun exercise designed not to take itself too seriously. 

Run "getData.py" to start the simulation. You can tweak the parametres inside this script to simulate different historical data points, or different trading thresholds to see if there is any improvement
