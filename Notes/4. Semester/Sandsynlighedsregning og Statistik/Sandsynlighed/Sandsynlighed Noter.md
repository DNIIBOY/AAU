# Sampling
![[Probability_theory_session1_with_notes.pdf#page=41&rect=4,4,781,554|Probability_theory_session1_with_notes, p.41]]

# Conditional Probability
$$
P(A|B) = \frac{P(AB)}{P(B)}, P(B) > 0
$$
## Formula of total probability

$P(A) = P(AB) + P(AB^c) =$

$P(A|B)P(B) + P(A|B^c)P(B^c)$

## Bayes' formula
Used if A has occurred, and we want to determine if B has also occurred:
$$P(B|A) = \frac{P(BA)}{P(A)} = \frac{P(A|B)P(B)}{P(A|B)P(B)+P(A|B^c)P(B^c)}$$


# Expectation
Expected value in discrete case:
$$
E[X] = \sum_{i} x_{i}p(x_{i})
$$
In continuous case, for pdf:
$$
E[X] = \int_{-\infty}^\infty x f(x) dx
$$
For cdf:
$$
E[X] = \int_{0}^\infty(1-F(x)) dx
$$
OR
Convert cdf to pdf:
$$
f(x) = \frac{dF(x)}{dx}
$$
To convert from pdf to cdf:
$$
F(X) = P(X\leq x) = \int_{\infty}^x f(t) dt
$$

When X and Y are independent:
$$
E[X+Y] = E[X] + E[Y]
$$
$$
E[XY] = E[X]E[Y]
$$

# Variance
Definition:
$$
Var(X) = E[(X-E(X))^2]
$$
Simplified:
$$
Var(X) = E[X^2] - E[X]^2
$$
![[Probability_Session2_Part2_with_notes-1.pdf#page=29&rect=68,130,638,420|Probability_Session2_Part2_with_notes-1, p.29]]

Standard Deviation (STD):
$$
Std(X) = \sqrt{Var(X)}
$$

### Covariance
Definition:
$$
Cov(X, Y) = E[(X- E[X])(Y-E[Y])]
$$
Simplified:
$$
Cov(X, Y) = E[XY] - E[X]E[Y]
$$
![[Probability_Session2_Part2_with_notes-1.pdf#page=37&rect=47,29,750,544|Probability_Session2_Part2_with_notes-1, p.37]]


# Moments
$$
E[X] \to \text{1st moment}
$$
$$
E[X^2] \to \text{2nd moment, etc..}
$$
![[Probability_Session2_Part2_with_notes-1.pdf#page=49&rect=265,56,587,341|Probability_Session2_Part2_with_notes-1, p.49]]

Moment generating function
![[Probability_Session2_Part2_with_notes-1.pdf#page=50&rect=53,34,741,536|Probability_Session2_Part2_with_notes-1, p.50]]


# Discrete special probability distributions
## Bernoulli
Two possible outcomes, like tossing a biased coin
Expected value is just the probability of success
$$
E[I] = p
$$
Therefore, variance can also be simplified:
$$
Var(I) = p-p^2 = p(1-p)
$$

## Binomial
If a random variable represents number of successes in n trials. P is probability of success, n is number of trials:
$$
X \sim b(n, p)
$$
$$
E[X] = np
$$
$$
Var(X) = np(1-p)
$$
PMF:
$$
P\{X=i\} = \begin{pmatrix}n\\i\end{pmatrix} p^i(1-p)^{n-i}, n=0, 1, \dots, n
$$
Probability of next value:
$$
P\{X=k+1\}=\frac{p}{1-p}\frac{n-k}{k+1}P\{X=k\}
$$

**If n is large and p is small, poisson can be used as estimator with $\lambda=np$**

## Geometric
Number of Bernoulli trials until the first occurrence of a success. So if a coin shows heads every 5 times, it is geometric, with p=0.2 if heads is a success. We call the rv M.

$$
P\{M=k\} = (1-p)^{k-1}p
$$
$$
E[M] = \frac{1}{p}
$$
$$
Var(M) = \frac{1-p}{p^2}
$$

## Poisson
Models number of times some independent event happens within a fixed interval.
Number of events per time (rate $\lambda$) must be constant.
$$
E[X] = \lambda
$$
$$
Var(X) = \lambda
$$
PMF:
$$
P\{X=i\} = e^{-\lambda} \frac{\lambda^i}{i!}
$$
If a binomial has large enough n and small enough p, poisson can be used as approximation with $\lambda=np$


## Hypergeometric
Objects of 2 types. With N "success" type objects and M "failure" type objects.
n objects are randomly selected _without_ replacement.
A random variable X represents number of "success" objects, with parameters (N, M, n)
$$
E[X] = \frac{nN}{N+M}
$$
$$
Var(X)=np(1-p)\left( 1-\frac{n-1}{N+M-1} \right)
$$
PMF:
$$
P\{X=i\} = \frac{\begin{pmatrix} N\\i\end{pmatrix} \begin{pmatrix}M\\n-i\end{pmatrix}}{\begin{pmatrix}N+M\\n\end{pmatrix}}
$$

## Negative Binomial (Pascal)

![[mm4_2026-1.pdf#page=19&rect=46,29,812,580|mm4_2026-1, p.19]]

# Continuous special probability distributions
## Uniform r.v.
A random variable with pdf as a constant $c$. Defined on the interval $[a, b]$
$$
E[X] = \frac{a+b}{2}
$$
$$
Var(X) = \frac{(b-a)^2}{12}
$$
## Exponential r.v
X is an exponential r.v. with parameter $\lambda$, if its pdf is:
$$
f(x) = \lambda e^{-\lambda x}, x\geq 0
$$
Has the memoryless property:
$$
P(X>s+t|X>t) = P(X>s)
$$
$$
E[X] = \frac{1}{\lambda}
$$
$$
Var(X) = \frac{1}{\lambda^2}
$$
## Normal r.v. (Gaussian r.v.)
A r.v. is said to be normally distributed if its pdf is
$$
f(x) = \frac{1}{\sqrt{ 2\pi }\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$
$$
X \sim N(\mu, \sigma^2)
$$
$$
E[X] = \mu
$$
$$
Std(X) = \sigma
$$
$$
Var(X) = \sigma^2
$$
Z-score:
$$
Z = \frac{X-\mu}{\sigma}
$$
