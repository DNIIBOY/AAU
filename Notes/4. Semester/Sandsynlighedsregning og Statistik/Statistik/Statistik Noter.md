# Samples
## Sample mean

$$
\bar{x}_{n} = \frac{1}{n} \sum_{i=1}^n x_{i}
$$
## Sample variance
$$
S_{n}^2 = \frac{1}{n-1} \sum_{i=1}^n(x_{i}-\bar{x}_{n})^2
$$
# Central limit theorem
Everything is a normal (Gaussian) distribution if we have enough samples:
$$
\sum_{i=1}^n X_{i} = X_{1} + X_{2} + \dots + X_{n} \approx N(n\mu, n\sigma^2)
$$
With mean at the sum mean/expectation of the variables, and variance ($\sigma^2$) the sum of variances.


# Estimators
## Metrics
### Bias
$$
bias(\theta_{n}) = E[\hat{\theta_{n}}] - \theta
$$
### Variance
$$
var(\hat{\theta_{n}}) = E[(\hat{\theta_{n}} - E[\hat{\theta_{n}}])^2]
$$
#### Standard error
$$
se(\hat{\theta_{n}}) = \sqrt{ var(\hat{\theta_{n}}) }
$$
But $se(\hat{\theta_{n}})$ depends on $F$ (the distribution),  and might be unknown.
Estimated standard error is called $\hat{se}(\hat{\theta_{n}})$
### Mean square error
$$
MSE = E[\theta_{n} - \theta]^2 = bias^2(\hat{\theta_{n}}) + var(\hat{\theta_{n}})
$$
