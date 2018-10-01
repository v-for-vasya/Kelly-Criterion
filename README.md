# Kelly-Criterion Application in Finance

<code>kelly_max.py</code> solves for the maximum betting amount to ensure best longterm compounding as visualised in the blue point in the graph below. Current example is given for a 50/50 coin with a 200% gain on heads and a 100% loss on tails giving us a Kelly bet of 25%.

![Kelly_maximum](https://github.com/v-for-vasya/Kelly-Criterion/blob/master/img/kellygraph.png)

Overbetting beyond the Kelly criterion increases volatility, increases the chance for bankruptcy, and in the long run further drifts apart our median and averages.

![Kelly_overbet](https://github.com/v-for-vasya/Kelly-Criterion/blob/master/img/kellybet_over_stats.jpg)

By betting the Kelly criterion amount we ensure that the median and average drift upwards in the long run.

![Kelly_bet](https://github.com/v-for-vasya/Kelly-Criterion/blob/master/img/kellybet_stats.jpg)

<code> your_time_series.csv </code> is the .csv data file one can use for percentage outcomes. In our 50/50 coin with 200% gains and 100% losses it would simply be <code> 2, -1 </code> within the .csv file. One can populate the file with thousands of data points, including returns for assets.

For more information see: http://wduwant.com/kelly/
