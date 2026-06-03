# Exercise 1
It is claimed that a certain type of bipolar transistor has a mean value of current gain that is at least 210. A sample of these transistors is tested. If the sample mean value of the current gain is 200 and the standard deviation is unknown, but estimated from the sample standard deviation to be 35, would the claim be rejected at the 5 percent level of significance if
Hypothesis:
$$
H_{0}: \mu_{n} \geq 210, H_{1}: \mu_{n} < 210
$$
## a) The sample size is 25?
Test statistic:
$$
T = (200 - 210) \frac{\sqrt{ 25 }}{35} = - \frac{10}{7} \approx -1.4287
$$
Rejection region:
$$
R = \{T < -t_{0.05, 24}\} = \{-1.4287 < -1.7109\} =false
$$
So we fail to reject the hypothesis $H_{0}$
## b) The sample size is 64?
Test statistic:
$$
T = (200 - 210) \frac{\sqrt{ 64 }}{35} = - \frac{16}{7} \approx -2.2857 
$$
$$
R = \{T < -t_{0.05, 63}\} = \{-2.2857 < -1.6694\} = true
$$
In this case, we reject the hypothesis.

# Exercise
A question of medical importance is whether jogging leads to a reduction in one’s heart rate. To test this hypothesis, 8 nonjogging volunteers agreed to begin a 1-month jogging program. After the month, their pulse rates were determined and compared with their earlier values. If the data are as follows, can we conclude that jogging has an effect on the pulse rates with a 5 percent level of significance?

| Subject | 1    | 2    | 3    | 4     | 5    | 6    | 7    | 8    |
| ------- | ---- | ---- | ---- | ----- | ---- | ---- | ---- | ---- |
| Before  | $74$ | $86$ | $98$ | $102$ | $78$ | $84$ | $79$ | $70$ |
| After   | $70$ | $85$ | $90$ | $110$ | $71$ | $80$ | $69$ | $74$ |
Null hypothesis:
$$
H_{0}: \mu_{X} = \mu_{Y}
$$
Where $X$ is the pulse rate before and $Y$ is the pulse rate after.
We use sample means as estimator for population mean:
$$
\hat{\mu_{X}} = \bar{X} = \frac{671}{8} = 83.875
$$
$$
\hat{\mu_{Y}} = \bar{Y} = \frac{649}{8} = 81.125 = 81.125 
$$

Since we do not know the variance, we use the estimator:
$$
S_{\bar{X}-\bar{Y}}^2 = \frac{\sum_{i=1}^{n_{X}}(X_{i}-\bar{X})^2 + \sum_{i=1}^{n_{Y}}(Y_{i}-\bar{Y})^2}{n_{X} + n_{Y} - 2} = \frac{880.875+1352.875}{8+8-2} = \frac{2233.75}{14} \approx 159.5536
$$
So the standard error is:
$$
S_{\bar{X}-\bar{Y}} = \sqrt{ S_{\bar{X}-\bar{Y}}^2 } = \sqrt{ 159.5536 } = 12.6315
$$
We use this value in the test statistic:
$$
T = \frac{|\hat{\mu}_{X} - \hat{\mu}_{Y}|}{S_{\bar{X}-\bar{Y}}\sqrt{\frac{1}{n_{X}}+\frac{1}{n_{Y}}}} = \frac{|83.875-81.125|}{12.6315\sqrt{ \frac{1}{8} + \frac{1}{8} }} = 0.4354
$$
Which we compare to the rejection region:
$$
R = \{T > T_{0.05/2, 14}\} = \{0.4354 > 2.1448\} = false
$$
So we cannot reject the hypothesis that the two population means are the same, with $5\%$ confidence.

P value:
```python
sage: 2 * (1 - t.cdf(0.4354, df=14))
np.float64(0.6699097013963753)
```

# Exercise 3
Two different types of cable insulation have been tested. We need to determine the voltage level at which failures occur. The tests revealed that the individual cables failed at the following voltage levels.

With these data, can you reject the hypothesis $H_{0}: \mu_A = \mu_B$ with
## a) 5 percent level of significance?
We use sample mean as estimator for population mean of both populations:
$$
\hat{\mu_{A}} = \bar{A} = \frac{600}{14} \approx 42.8571
$$
$$
\hat{\mu_{B}} = \bar{B} = \frac{670}{12} \approx 55.8333
$$
Then we use the following test statistic:
$$
T = \frac{|\hat{\mu}_{X} - \hat{\mu}_{Y}|}{\sqrt{\frac{\sigma_{X}^2}{n_{X}}+\frac{\sigma_{Y}^2}{n_{Y}}}} = \frac{|42.8571-55.8333|}{\sqrt{\frac{40}{14} + \frac{100}{12}}} \approx 3.879
$$
With following rejection region:
$$
R = \{T > Z_{0.05/2}\} = \{3.879 > 1.96\} = true
$$
We reject the hypothesis that the two cables have the same mean failure voltage at $5\%$ significance
## b) 10 percent level of significance?
$$
R = \{T > Z_{0.1/2}\} = \{3.879 > 1.64\} = true
$$
We reject the hypothesis that the two cables have the same mean failure voltage at $10\%$ significance
## b) 1 percent level of significance?
$$
R = \{T > Z_{0.01/2}\} = \{3.879 > 2.5758\} = true
$$
We reject the hypothesis that the two cables have the same mean failure voltage at $1\%$ significance