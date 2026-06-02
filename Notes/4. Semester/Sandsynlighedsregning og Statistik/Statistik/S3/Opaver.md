# Exercise 1: Poll results

On October 14, 2003, the New York Times reported that a recent poll indicated that 52% of the population was in favor of the job performance of president Bush, with a margin of error (i.e., 95% confidence interval (CI)) of $\pm4\%$. 

## a) What does this mean?
It means that we are 95% confident that the true approval rating lies within the 4% interval, the boundaries of which can be calculated as follows:
$$
C_{0.95} = (52\% - 4\%, 52\% + 4\%) = (48\%, 56\%)
$$
So we are 95% confident that the true approval rating is between 48% and 56%

## b) How many people were questioned?
We start by calculating the standard deviation:
$$
\sigma = \sqrt{ \hat{p}_{n}(1-\hat{p}_n) }= \sqrt{ 0.52(1-0.52)} \approx 0.4996
$$
By definition of confidence interval in a normal distribution:
$$
C_{0.95} = \left( \hat{p}_{n} - Z_{0.05/2} \frac{\sigma}{\sqrt{ n }}, \hat{p}_{n} + Z_{0.05/2} \frac{\sigma}{\sqrt{ n }} \right)
$$
We can equate:
$$
Z_{0.05/2} \frac{\sigma}{\sqrt{ n }} = 0.04 \implies 1.96 \frac{\sigma}{\sqrt{ n }} = 0.04
$$
Substituting $\sigma$ and solving for $n$
$$
1.96 \frac{0.4996}{\sqrt{ n }} = 0.04 \implies 0.9792 = 0.04\sqrt{ n } \implies 0.9589 = 0.0016n \implies
$$
$$
n = 599.2896
$$
Rounding up to nearest whole person, we would need 600 people to answer the poll to set this confidence interval.

# Exercise 2
A device transmits a signal towards a receiver. The receiver measures the signal strength, which is affected by Gaussian noise and, hence, is normally distributed with mean $\mu$ and variance $\sigma^2=4$. The receiver has 9 receiving antennas and each one records the value of the signal strength, which are
$$
[5, 8.5, 12, 15, 7, 9, 7.5, 6.5, 10.5]
$$

## a) Calculate the 95% CI using $Z_{\alpha/2}$
We estimate population mean, to be sample mean:
$$
\hat{\mu}_{n} = \bar{X_{n}} = 9
$$
Now we use the standard deviation and mean to calculate confidence intervals:
$$
C_{0.95} = \left( \hat{\mu}_{n} - Z_{0.05/2} \frac{\sigma}{\sqrt{ n }}, \hat{\mu}_{n} + Z_{0.05/2} \frac{\sigma}{\sqrt{ n }} \right)
$$
$$
C_{0.95} = \left( 9 - 1.96 \frac{2}{\sqrt{9}}, \hat{\mu}_{n} + 1.96 \frac{2}{\sqrt{9}} \right) = (7.693, 10.307)
$$

## b) Calculate the 95% CI using $T_{\alpha/2, n-1}$ and without knowing the variance
We start by estimating variance and standard deviation using sample variance:
$$
\hat{\sigma}_{n}^2 = S_{n}^2 = \frac{1}{n-1} \sum_{i=1}^n(x_{i}-\bar{x}_{n})^2 = 9.5
$$
$$
\hat{\sigma}_n = \sqrt{\hat{\sigma_{n}^2}} = \sqrt{ 9.5 } \approx 3.082
$$
We use python to calculate t value:
```python
from scipy.stats import t
t.ppf(1-0.05/2, df=8)
```
And get
$$
T_{\frac{0.05}{2}, 8} = 2.306
$$
Plugging in to formula using t value:
$$
C_{1-\alpha} =  \left(\hat{\mu}_{n} - T_{\frac{\alpha}{2},n-1} \frac{\hat{\sigma}_{n}}{\sqrt{ n }}, \hat{\mu}_{n} + T_{\frac{\alpha}{2}, n-1} \frac{\hat{\sigma}_{n}}{\sqrt{ n }} \right)
$$

$$
C_{0.95} =  \left(9 - 2.306 \frac{3.082}{\sqrt{ 9 }}, 9 + 2.306 \frac{3.082}{\sqrt{ 9 }} \right) = (6.6308, 11.3691)
$$
# Exercise 3
We measured the execution time of an image processing algorithm and obtained an average execution time of $\mu = 12.995$  Assume that our measurements are subject to Gaussian noise with zero mean and variance $\sigma^2 = 1.997$

## a) Get the maximum likelihood estimates for $\mu$, denoted as $\hat{\mu}_{n}$ after taking a sample with $n = 10$ and $n = 1000$

```python
X10 = np.random.normal(12.995, np.sqrt(1.997), 10)
np.average(X10)
```
$$
\hat{\mu}_{10} = 11.8751
$$

```python
X1000 = np.random.normal(12.995, np.sqrt(1.997), 1000)
np.average(X1000)
```
$$
\hat{\mu}_{1000} = 13.0027
$$
## b) Plot
I dont want to

## c) Calculate the 95% CI for both values of $n$ assuming that the variance $\sigma^2$ is known
$$
\sigma = \sqrt{ \sigma^2 } = \sqrt{ 1.997 } = 1.4132
$$
$$
CI_{10} = \left( 11.8751 - 1.96 \frac{1.4132}{\sqrt{ 10 }}, 11.8751 + 1.96 \frac{1.4132}{\sqrt{ 10 }} \right) = (10.9992, 12.7511)
$$
$$
CI_{1000} = \left( 13.0027 - 1.96 \frac{1.4132}{\sqrt{ 1000 }}, 13.0027 + 1.96 \frac{1.4132}{\sqrt{ 1000 }} \right) = (12.9151, 13.0903)
$$

## d) Calculate the 95% CI for both values of $n$ assuming that the variance is not known using $Z_{\alpha/2}$
In this case, we will use the sample variance as an estimator for the true variance:
$$
\hat{\sigma}^2_{10} = S^2_{10} = 0.8979
$$
$$
\hat{\sigma}^2_{1000} = S^2_{1000} = 1.961
$$

$$
CI_{10} = \left( 11.8751 - 1.96 \frac{\sqrt{ 0.8979 }}{\sqrt{ 10 }}, 11.8751 + 1.96 \frac{\sqrt{ 0.8979 }}{\sqrt{ 10 }} \right) = (11.2878, 12.4625)
$$
$$
CI_{1000} = \left( 13.0027 - 1.96 \frac{\sqrt{1.961}}{\sqrt{ 1000 }}, 13.0027 + 1.96 \frac{\sqrt{1.961}}{\sqrt{ 1000 }} \right) = (12.9189, 13.0895)
$$

## e) Calculate the 95% CI for both values of $n$ assuming that the variance is not known using $T_{\alpha/2, n-1}$
We can keep the variances we calculated in d), but this time, we use the formula using the t-distribution:
$$
C_{1-\alpha} =  \left(\hat{\mu}_{n} - T_{\frac{\alpha}{2},n-1} \frac{\hat{\sigma}_{n}}{\sqrt{ n }}, \hat{\mu}_{n} + T_{\frac{\alpha}{2}, n-1} \frac{\hat{\sigma}_{n}}{\sqrt{ n }} \right)
$$
$$
CI_{10} = \left( 11.8751 - 2.2622 \frac{\sqrt{ 0.8979}}{\sqrt{ 10 }}, 11.8751 + 2.2622 \frac{\sqrt{ 0.8979 }}{\sqrt{ 10 }} \right) = ()
$$
$$
CI_{1000} = \left( 13.0027 - 1.9623 \frac{\sqrt{ 1.961 }}{\sqrt{ 1000 }}, 13.0027 + 1.9623 \frac{\sqrt{ 1.961 }}{\sqrt{ 1000 }} \right) = ()
$$

## f) Which if these CIs is wider?
The t-distribution gives a larger CI. All CIs with n=10 are also wider, as there is less data, so it is harder to be confident about the CI. In this case the n=10 sample is a bit of an outlier, as none of the $C_{0.95}$ intervals cover the true value for $\mu$.
