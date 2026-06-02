# Exercise 1
It is claimed that a certain type of bipolar transistor has a mean value of current gain that is at least 210. A sample of these transistors is tested. If the sample mean value of the current gain is 200 and it is known that the standard deviation is 35, would the claim be rejected at the 5 percent level of significance if

Hypotheses:
$$
H_{0}: \mu \geq 210, H_{1}: \mu < 210
$$
One-sided since we are dealing with anything below 210 being rejected
Test statistic:
$$
T = (\hat{\mu}_{n} - \mu_{0}) \frac{\sqrt{ n }}{\sigma}
$$
Rejection region:
$$
R = \{x: T < c\}
$$
We compare test statistic T to the threshold c, which in this case is $c= -Z_{0.05} = -1.6449$

## a) The sample size is 25?
$$
T = (200 - 210) \frac{\sqrt{ 25 }}{35} = -10 \cdot \frac{5}{35} \approx -1.4286
$$
The hypothesis is accepted as the T value is outside of the rejection region:
$$
-1.4286 < -1.6449: False \to H_{0}: True
$$
## b) The sample size is 64?
$$
T = (200 - 210) \frac{\sqrt{ 64 }}{35} = -10 \cdot \frac{8}{35} \approx -2.2857
$$
Now, the hypothesis is rejected, as the T value lies within the rejection region:
$$
-2.2857 < -1.6449: True \to H_{0}: False
$$

# Exercise 2
According to the U.S. Bureau of Census, 25.5 percent of the population of those age 18 or over smoked in 1990. A scientist has recently claimed that this percentage has since increased, and to prove her claim she randomly sampled 500 individuals from this population. If 138 of them were smokers, is her claim proved? Use the 5 percent level of significance.

This is a Bernoulli RV, as all outcomes only have two options: smoker or non-smoker.
This follows a binomial distribution, but as $n=500$ is large, we can estimate it using a normal distribution:
$$
T = \frac{k-np_{0}}{\sqrt{ np_{0}(1-p_{0}) }}
$$
As the scientist want to reject the hypothesis, that the number of smokers has stayed the same, we define the null hypothesis as:  $H_{0}: p\leq p_{0}$. We test using the test statistic $T$:
$$
T = \frac{138-500(0.255)}{\sqrt{500 \cdot 0.255(1-0.255) }} = 1.0773
$$
Which i compared to the rejection region, for the one-sided Z value for the 5 percent level of significance:
$$
1.0773>1.64485: False, H_{0}: True
$$
So we fail to reject the hypothesis that the percentage of the population that smokes has not gone up, and reject the claim of the scientist.

# Exercise 3
The students from last year were asked to choose between the following two options for the rest of the course using an online poll.
To make a decision that is fair, Israel decided to conduct a test. First, he defined $X_{i} \sim Bernoulli(p)$, where $X_{i} = 0$ if a student selects 1) and $X_{i} = 1$ the students selects 2). With this, he set $p_{0} = 0.5$, defined the null hypothesis H0: “the students prefer option 2)”, which can be formulated as $p \geq p_{0}$. Then, he estimated
$$
\hat{p}_{32} = \frac{1}{32}\sum_{i=1}^nX_{i} = 0.469
$$
## a) Perform a one-sided test with $\alpha=0.05$ using the null hypothesis $H_{0}$ and calculating the p-value for the Binomial distribution $v=P(X\leq x;n,p_{0})$ where $k=15$ is the number of student that chose option 2. Can you reject Israel's hypothesis?

$$
v = P(X\leq 15) = \sum_{i=0}^{15} \begin{pmatrix}32\\i\end{pmatrix}p_{0}^i(1-p_{0})^{32-i} = 0.43
$$
Using sagemath:
```python
sage: sum(binomial(32, i)*0.5**i * 0.5**(32-i) for i in range(1, 16))
0.430025032721460
```
Since $v < \alpha \implies 0.43 < 0.05$ is false, we cannot reject Israel's hypothesis.

## b) Change the null hypothesis to be $H'0$: “the students prefer option 1)”. What is the mathematical formulation of this? Can you reject this hypothesis with the collected evidence?
The new $H'_{0}$ is described: $H'_{0}: p\leq p_{0}$.
The math is very similar, we just take the other half of the pmf:
$$
v = P(X \geq 15) = \sum_{i=15}^{32} \begin{pmatrix}32\\i\end{pmatrix}p_{0}^i(1-p_{0})^{32-i} = 0.7
$$
Using sagemath:
```python
sage: sum(binomial(32, i)*0.5**i * 0.5**(32-i) for i in range(15, 33))
0.701692552072927
```
Since $v<\alpha \implies 0.7 <0.05$ is also false, we also cannot reject this hypothesis.

## c) Assume that the result of the poll is now $k = 11$, meaning that only eleven students preferred option 2). Can the original null hypothesis $H_{0}$ be rejected?
$$
v = P(X\leq 11) = \sum_{i=0}^{11} \begin{pmatrix}32\\i\end{pmatrix}p_{0}^i(1-p_{0})^{32-i} = 0.055
$$
Using sagemath:
```python
sage: sum(binomial(32, i)*0.5**i * 0.5**(32-i) for i in range(1, 12))
0.0550920823588967
```
Again $v< \alpha \implies 0.055 < 0.05$ is still false, but this time they are very close, indicating that if k is just slightly smaller, the hypothesis will become true.

