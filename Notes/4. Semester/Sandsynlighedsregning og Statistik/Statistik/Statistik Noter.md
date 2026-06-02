# Samples
## Sample mean

$$
\bar{x}_{n} = \frac{1}{n} \sum_{i=1}^n x_{i}
$$
## Sample variance
$$
S_{n}^2 = \frac{1}{n-1} \sum_{i=1}^n(x_{i}-\bar{x}_{n})^2
$$
In sage (use ddof=1 for sample, and 0 for population):
```python 
np.var(data, ddof=1)
```
# Central limit theorem (CLT)
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


# Maximum likelihood estimator (MLE)
Likelihood function (function of $\theta$):
$$
\mathcal{L}_{n}(\theta) = \prod_{i=1}^nf(X_{i};\theta)
$$
log-likelihood function:
$$
\ell_{n}(\theta) = \log{\mathcal{L}_{n}(\theta)} = \sum_{i=1}^n \log{f(X_{i}; \theta)}
$$

Maximum likelihood estimator $\hat{\theta}_{n}$: value of $\theta$ that maximises $\mathcal{L}_{n}(\theta)$ or $\ell_{n}(\theta)$

## Discrete RVs
$$
\mathcal{L}_{n}(\theta) = \mathcal{L}(x_{1}, x_{2}, \dots, x_{n}; \theta)
$$
### Bernoulli
$$
\mathcal{L}_{n}(p) = p^X(1-p)^{n-X}
$$
$$
\ell_{n}(p) = \log(p^X(1-p)^{n-X})
$$
## Continuous RVs
$$
\mathcal{L}_{n}(\theta) = \mathcal{L}(x_{1}, x_{2}, \dots, x_{n}; \theta) = f_{x_{1},x_{2},\dots,x_{n}}(x_{1}, x_{2}, \dots, x_{n})
$$

# Confidence intervals
## Two-sided confidence intervals:
$$
C_{1-\alpha}= \left(\hat{\mu}_{n} - Z_{\alpha/2} \frac{\sigma}{\sqrt{ n }}, \hat{\mu}_{n} + Z_{\alpha/2} \frac{\sigma}{\sqrt{ n }} \right)
$$
For example, $95\%$ confidence interval:
$$
C_{0.95} = \left( \hat{\mu}_{n} - Z_{0.05/2} \frac{\sigma}{\sqrt{ n }}, \hat{\mu}_{n} + Z_{0.05/2} \frac{\sigma}{\sqrt{ n }} \right)
$$
Where $Z_{\alpha}$ is the the standard normal complementary quantile function $\Phi(\alpha)$

When we dont know the value of $\sigma$, we can either set it to the max (0.25), or if it is Bernoulli RV, we can estimate it using sample mean:
$$
\hat{\sigma}^2 = \hat{p}_{n}(1-\hat{p}_{n})
$$
Alternatively, the sample variance can be used as an estimator for the real variance: $S_{n}^2 = \sigma_{n}^2$

### Small sample size
If the sample is too small, we cannot assume normal distribution (CLT).
So we can use the t-distribution instead:
$$
C_{1-\alpha} =  \left(\hat{\mu}_{n} - T_{\frac{\alpha}{2},n-1} \frac{\hat{\sigma}_{n}}{\sqrt{ n }}, \hat{\mu}_{n} + T_{\frac{\alpha}{2}, n-1} \frac{\hat{\sigma}_{n}}{\sqrt{ n }} \right)
$$
Can be calculated in sage using:
```python
from scipy.stats import t
t.ppf(1-a/2, df=n-1)
```


# Regression
Slope (least squares linear regression):
$$
\hat{\beta}_{1} = \frac{\sum_{i=1}^n (X_{i} - \bar{X}_{n})( Y_{i} - \bar{Y}_{n})}{\sum_{i}^n(X_{i} - \bar{X}_{n})^2}
$$
Can be simplified to:
$$
\hat{\beta}_{1} = \frac{n\sum X_{i}Y_{i} - \left( \sum X_{i} \right)\left( \sum Y_{i} \right)}{n\sum X_{i}^2 - \left( \sum X_{i} \right)^2}
$$
Intercept:
$$
\hat{\beta}_{0} = \bar{Y}_{n} - \hat{\beta}_{1}\bar{X}_{n}
$$
Unbiased estimator for $\sigma^2$. We divide by $n-2$, because there are two degrees of freedom (dofs)
$$
\hat{\sigma^2} = \left( \frac{1}{n-2} \right)\sum_{i=1}^n \hat{\epsilon}_{i}^2
$$
$\epsilon_{i}$ is the difference between the true y-value in the dataset, and the output of the model

# Hypothesis testing
With Gaussian distribution and known variance:

| $H_{0}$            | $H_{1}$            | Test statistic $T$                             | Rejection region   | P-value        |
| ------------------ | ------------------ | ---------------------------------------------- | ------------------ | -------------- |
| $\mu=\mu_{0}$      | $\mu \neq \mu_{0}$ | $\|\hat{\mu_{n}} - \mu_{0}\|\sqrt{ n }/\sigma$ | $T > Z_{\alpha/2}$ | $2(1-\Phi(T))$ |
| $\mu \leq \mu_{0}$ | $\mu > \mu_{0}$    | $(\hat{\mu_{n}} - \mu_{0})\sqrt{ n }/\sigma$   | $T > Z_{\alpha}$   | $(1-\Phi(T))$  |
| $\mu \geq \mu_{0}$ | $\mu < \mu_{0}$    | $(\hat{\mu_{n}} - \mu_{0})\sqrt{ n }/\sigma$   | $T < -Z_{\alpha}$  | $\Phi(T)$      |
For Bernoulli RV:
$$
v = P(X\geq k) = \sum_{i=k}^n \begin{pmatrix}n\\i\end{pmatrix}p_{0}^i(1-p_{0})^{n-i}
$$
We reject $H_{0}$ if $v < \alpha$. $\alpha = 0.05$ at 5% test

We can also use Central Limit Theorem to approximate Normal, if n is large:
$$
T = \frac{k-np_{0}}{\sqrt{ np_{0}(1-p_{0}) }}
$$
And compare with normal rejection region.