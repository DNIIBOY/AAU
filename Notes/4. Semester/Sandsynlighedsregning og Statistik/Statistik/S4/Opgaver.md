The following data indicate the relationship between $x$, the specific gravity of a wood sample, and $Y$ , its maximum crushing strength in compression parallel to the grain

| $x_{i}$ | $y_{i}$ | $x_{i}$ | $y_{i}$ |
| ------- | ------- | ------- | ------- |
| .41     | 1850    | .39     | 1760    |
| .46     | 2620    | .41     | 2500    |
| .44     | 2340    | .44     | 2750    |
| .47     | 2690    | .43     | 2730    |
| .42     | 2160    | .44     | 3120    |

## a) Plot a scatter diagram. Does a linear relationship seem reasonable?
Yes, very

## b) Estimate the regression coefficients
We start by calculating all relevant values:
Sum of $X$ and $Y$
$$
\sum_{i=1}^n X_{i} = 4.31
$$
$$
\sum_{i=1}^n Y_{i} = 24520
$$
Sum of squares for $X$:
$$
\sum_{i=i}^nX_{i}^2 = 1.8629
$$
Sum of products:
$$
\sum_{i=0}^n X_{i}Y_{i} = 10632.9
$$
Now, using the least squares estimate:
$$
\hat{\beta}_{1} = \frac{n\sum X_{i}Y_{i} - \left( \sum X_{i} \right)\left( \sum Y_{i} \right)}{n\sum X_{i}^2 - \left( \sum X_{i} \right)^2}
$$
$$
\hat{\beta}_{1} = \frac{10(10632.9) - (4.31)(24520)}{10(1.8629) - 4.31^2}
$$
$$
\hat{\beta}_{1} = \frac{647.8}{0.0529} = 12245.7467
$$
We can use slope and means to estimate y-intercept:
$$
\hat{\beta}_{0} = \bar{Y}_{n} - \hat{\beta}_{1}\bar{X}_{n} = \frac{24520}{10} - 12245.7467 \cdot \frac{4.31}{10} = -2825.9168
$$

## c) Predict the maximum crushing strength of a wood sample whose specific gravity is 0.43
We have estimated the function for $f(x)$:
$$
f(x) = \hat{\beta}_{1}x + \hat{\beta}_{0} = 12245.7567x - 2825.9168
$$
Plugging in 0.43, we get:
$$
f(0.43) = 12245.7567\cdot 0.43 - 2825.9168 = 2439.7586
$$
## d) Estimate the variance $\sigma^2$ of an individual response.
$$
\hat{\sigma^2} = \frac{1}{n-2} \sum_{i=1}^n \hat{\epsilon}_{i}^2 = \frac{1}{8}(845280.529) = 105660.066
$$

# Exercise 2
A measurement campaign involving two wireless devices was performed. One device (receiver) was kept on a fixed position, while the other (transmitter) was moved around and placed at several distances $d_i$ for $i = 1, 2, \dots$ from the receiver. The transmitter was configured to send a known signal toward the receiver in every position and the receiver calculated the received power for every transmission. The file `received_power.csv` contains the $n = 500$ data obtained, in which $P_i$ is the received power, measured in milliWatts, and $di \in [30, 300]$ (meters) is the distance between the transmitter and receiver.
