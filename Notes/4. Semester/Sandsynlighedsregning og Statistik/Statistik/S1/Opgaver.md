# Exercise 3
Consider the case of flipping a fair coin n times and let Hn be the random variable (RV) of the number of heads. Also recall that the sum of n Bernoulli RVs is a Binomial random variable with mean $np$ and variance $np(1−p)$. Calculate and compare the probability of observing $H_{10} = 7$ and $H_{100} = 70$ using each of the following methods.
## a) Using the formula for the probability mass funcion (pmf) of Binomial RVs
$$
P(H_{10} = 7) = \begin{pmatrix}10 \\ 7\end{pmatrix}0.5^7(1-0.5)^3 \approx 11.72\%
$$
$$
P(H_{100} = 70) = \begin{pmatrix}100 \\ 70\end{pmatrix}0.5^{70}(1-0.5)^{30} \approx 0.00232\%
$$
## b) Using the central limit theorem
Calculate mean and variance:
$$
\mu_{10} = 10 \cdot 0.5 = 5\land \sigma^2_{10} = 10\cdot 0.5(1-0.5) = 2.5
$$
$$
\mu_{100} = 100 \cdot 0.5 \land \sigma^2_{100} = 100\cdot 0.5(1-0.5) = 25
$$
Define normal distribution according to central limit theorem:
$$
H_{10} \sim N(10, 2.5)
$$
Since the normal distribution is continuous, the probability of a discrete outcome is 0.
$$
P(H_{10} = 7) = 0
$$
$$
P(H_{100} = 7) = 0
$$
#### Fuck it we try anyway using $\pm 0.5$
$$
Z_{1} = \frac{x-\mu}{\sigma} = \frac{6.5-5}{\sqrt{2.5}} \approx 0.9486
$$
$$
Z_{2} = \frac{x-\mu}{\sigma} = \frac{7.5-5}{\sqrt{2.5}} \approx 1.5811
$$
$$
P(H_{10} = 7) = P(6.5 \leq X \leq 7.5) = P(0.9486 \leq Z \leq 1.5811) = \Phi(1.5811) - \Phi(0.9486)
$$
$$
\approx 0.943 - 0.8286 \approx 11.45\%
$$
And for $H_{100} = 70$
$$
Z_{1} = \frac{x-\mu}{\sigma} = \frac{69.5-50}{\sqrt{25}} = 3.9
$$
$$
Z_{2} = \frac{x-\mu}{\sigma} = \frac{70.5-50}{\sqrt{25}} = 4.1
$$
$$
P(H_{100} = 70) = P(69.5 \leq X \leq 70.5) = P(3.9 \leq Z \leq 4.1) = \Phi(4.1) - \Phi(3.9)
$$
$$
\approx 0.999979 - 0.999952 \approx 0.00274\%
$$
Very close, so we say it good:)
### Now calculate and compare the probability of observing $H_{10} \geq 7$ and $H_{100} \geq 70$ with the following methods.
## c) Summing over the formula for the pmf of Binomial RVs
$$
P(H_{10}\geq 7) = \sum_{i=7}^{10} \begin{pmatrix}10\\i\end{pmatrix} 0.5^i (1-0.5)^{10-i}
$$
Using sagemath:
```python
P(n, p, x) = binomial(n, x)*p**x*(1-p)**(n-x)
sum(P(10, 0.5, i) for i in range(7, 11))
0.171875000000000
```
So 
$$
P(H_{10} \geq 7) = 0.171875 = 17.1875\%
$$
$$
P(H_{100}\geq 70) = \sum_{i=70}^{100} \begin{pmatrix}100\\i\end{pmatrix} 0.5^i (1-0.5)^{100-i}
$$
```python
P(n, p, x) = binomial(n, x)*p**x*(1-p)**(n-x)
sum(P(100, 0.5, i) for i in range(70, 101))
0.0000392506982279683
```
$$
P(H_{100} \geq 70) \approx 0.00003925 = 0.003925\%
$$
## d) Using the central limit theorem
We already calculated:
$$
\mu_{10} = 5\land \sigma^2_{10} = 2.5
$$
$$
\mu_{100} = \land \sigma^2_{100} = 25
$$
We calculate Z-score for $P(H_{10} \geq 7)$:
$$
Z = \frac{x-\mu}{\sigma} = \frac{7-5}{\sqrt{ 2.5 }} \approx 1.2649
$$
Using Z-score to calculate probability:
$$
P(H_{10} \geq 7) = 1-P(Z\leq 1.2649) = 1-\Phi(1.2649) \approx 1- 0.897 \approx 10.29\%
$$
Also for $P(H_{100} \geq 70)$:
$$
Z = \frac{70-50}{\sqrt{ 25 }} = 4
$$
$$
P(H_{100} \geq 70) = 1-P(Z\leq 4) = 1-\Phi(4) = 1- 0.99996832 \approx 0.00316\%
$$
# Exercise 4
A football team will play 60 games this year. Thirty-two of these games are against teams playing the champions league, denoted as class A teams, and 28 are against other teams, denoted as class B teams. The outcomes of the games are independent. The team will win each game against a class A team with probability 0.5, and it will win each game against a class B team with probability 0.7. Let X denote its total number of victories in the year.

## a) Is $X$ a binomial RV?
No, its the sum of two binomials, since $p_A$ and $p_B$ are different.

## b) Let $X_A$ and $X_B$ denote, respectively, the number of victories against class A and class B teams. What are their distributions?
Binomials:
$$
X_{A} \sim b(32, 0.5) \land X_{B} \sim b(28, 0.7)
$$
## c) What is the relationship between $X$ $X_A$ and $X_B$?
$$
X = X_{A} + X_{B}
$$
## d) Approximate the probability that the teams wins 40 or more games this year
Total mean:
$$
\mu_{X} = \mu_{A} + \mu_{B} = 32\cdot 0.5 + 28 \cdot 0.7 = 35.6 
$$
Total variance:
$$
\sigma^2_{X} = \sigma^2_{A} + \sigma^2_{B} = 32 \cdot 0.5(1-0.5) + 28 \cdot 0.7(1-0.7) = 13.88
$$
Total std:
$$
\sigma_{X} = \sqrt{\sigma^2_{X}} = \sqrt{ 13.88 } \approx 3.73
$$
Using the central limit theorem, we can assume $X$ is normally distributed:
$$
X \sim N(35.6, 13.88)
$$
$$
P(X\geq 40) = \int_{40}^\infty \frac{1}{\sqrt{ 2\pi }\cdot 3.73}e^{-\frac{(x-35.6)^2}{2\cdot 13.88}} \approx 0.1188
$$
OR, using Z-score:
$$
Z = \frac{x-\mu}{\sigma} = \frac{40-35.6}{3.73} \approx 1.1796
$$
$$
P(Z\geq 1.1796) = 1- \Phi(1.1796) \approx 0.119
$$
