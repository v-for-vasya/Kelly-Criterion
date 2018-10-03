# Kelly-Criterion Application in Finance

<code>kelly_max.py</code> solves for the maximum betting amount to ensure best long-term compounding as visualised in the blue point in the graph below. Current example is given for a 50/50 coin with a 200% gain on heads and a 100% loss on tails giving us a Kelly bet of 25%.

![Kelly_maximum](https://github.com/v-for-vasya/Kelly-Criterion/blob/master/img/kellygraph.png)

Overbetting beyond the Kelly criterion increases volatility, increases the chance for bankruptcy, and in the long run further drifts apart our median and averages.

![Kelly_overbet](https://github.com/v-for-vasya/Kelly-Criterion/blob/master/img/kellybet_over_stats.jpg)

By betting the Kelly criterion amount we ensure that the median and average drift upwards in the long run.

![Kelly_bet](https://github.com/v-for-vasya/Kelly-Criterion/blob/master/img/kellybet_stats.jpg)

<code> your_time_series.csv </code> is the .csv data file one can use for the evolution of one's stochastic process. In our 50/50 coin with 200% gains and 100% losses it would simply be <code> 2, -1 </code> within the .csv file. One can populate the file with thousands of data points.

<h3> Kelly Portfolio </h3>

Construction of a Kelly portfolio involves maximizing the geometric mean and minimizing the geometric standard deviation of returns while Markowitz focuses on maximizing the arithmetic mean and minimizing the arithmetic standard deviation of returns. Due to this phenomenon Kelly may allocate too much to one particular asset in a portfolio, but at the benefit of long-term compounding.

<code>kelly_portfolio_weights.py</code> calculates the weights of a Kelly portfolio with three assets given as a default example by solving for the maximum of geometric compounding for the portfolio using sequential quadratic programming. The weights of each portfolio asset are bound to -100% to 100% and the sum of all asset weights is bound to 100%.

The bounds <code>b</code> for the maximum allocation weight for each asset can be decreased as the number of assets increases if one wishes to focus on removing idiosyncratic risk.
  
  
For more information see: http://wduwant.com/kelly/
