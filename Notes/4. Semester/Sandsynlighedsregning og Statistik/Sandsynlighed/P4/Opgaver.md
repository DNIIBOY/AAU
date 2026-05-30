# Slides
## Problem 1
Suppose that an average number of accidents on a busy crossing occuring during a month is 3. Calculate probability that there is at least one accident per month.

Poisson with $\lambda=3$
$$
P\{X\geq1\} = 1- P\{X=0\}= 1- e^{-3}\frac{3^0}{0!} = e^{-3} \approx 95.02\%
$$
## Problem 2
Components produced at a factory are defective with probability 0.1. They are sold in package of 20 components and a return is accepted, if more than one component is defective in a package. What is a probability that a package is returned?
$$
X \sim b(20, 0.1)
$$
$$
P\{X>1\} = 1- P\{X=0\} - P\{X=1\} = 1 - \begin{pmatrix} 20 \\ 0\end{pmatrix}0.1^0(1-0.1)^{20} - \begin{pmatrix}20 \\ 1\end{pmatrix}0.1^1(1-0.1)^{19}
$$
$$
= 1-(1-0.1)^{20}-2(1-0.1)^{19} \approx 1-0.12-0.27 \approx 60.83\%
$$

## Problem 3
Deck of cards contains 20 cards: 6 red cards and 14 black cards. 5 cards are drawn randomly without replacement. What is the probability that exactly 4 red cards are drawn?
Hypergeometric with $N=6$, $M=14$ and $n=5$

$$
P\{X=4\} = \frac{\begin{pmatrix}6\\4\end{pmatrix} \begin{pmatrix}14\\1\end{pmatrix}}{\begin{pmatrix}20\\5\end{pmatrix}} = \frac{15\cdot 14}{15504}=\frac{14}{323} \approx 1.35\%
$$

## Problem 4
It is known that 20% of products on a production line are defective. Products are inspected until first defective is encountered. How many inspections will be done to obtain the first defective product?

Geometric series with p=0.2

$$
E[M] = \frac{1}{0.2} = 5
$$

# Problem Set

## Problem 4.1
A communication channel transmits the digits 0 and 1. However, due to static, the digit transmitted is incorrectly received with probability 0.2. Suppose that we want to transmit an important message consisting of one binary digit. To reduce chances of error, we transmit 00000 instead of 0 and 11111 instead of 1. If the receiver of the message uses ”majority” decoding, what is the probability that the message will be incorrectly decoded? What independence assumptions are you making?

Binomial:
$$
X \sim b(5, 0.2)
$$
Failure if $X>2$
$$
P\{X>2\} = 1-P\{X=0\} - P\{X=1\} - P\{X=2\} =
$$
$$
1- (1-0.2)^5-5\cdot 0.2(1-0.2)^4 - \begin{pmatrix}5\\2\end{pmatrix}0.2^2(1-0.2)^3 \approx
$$
$$
1-0.33-0.41-0.2 \approx 5.8\%
$$
## Problem 4.2
Suppose that a particular trait (such as eye color or left-handedness) of a person is classified on the basis of one pair of genes, and suppose that d represents a dominant gene and r represents a recessive gene. Thus, a person with dd genes is pure dominant, one with rr is pure recessive, and one with rd is hybrid. The pure dominance and the hybrid are alike in appearance. Children receive one gene from each parent. If, with respect to a Particular trait, 2 hybrid parents have a total of 4 children, what is the probability that 3 of the 4 children have the outward appearance of the dominant gene?

Each kid has a $0.5 \cdot 0.5 = 0.25$ chance of getting two recessive genes, so a 0.75 probability of having appearance of the dominant gene.
We can model this with a binomial rv $X\sim b(4, 0.75)$

$$
P\{X=3\} = \begin{pmatrix}4\\3\end{pmatrix}0.75^3(1-0.75)^1 \approx 42.19\%
$$

## Problem 4.3
If you buy a lottery ticket in 50 lotteries, in each of which your chance of winning a prize is 1/100, what is (approximate) probability that you will win a prize 

This is also binomial with $X \sim b(50, 0.01)$
### (a) at least once
$$
P\{X\geq 1\} = 1- P\{X=0\} = 1- (1-0.01)^{50} \approx 39.49\%
$$
### (b) exactly once
$$
P\{X = 1\} = \begin{pmatrix}50\\1\end{pmatrix}0.01(1-0.01)^{49} \approx 30.56\%
$$
### (c) at least twice?

$$
P\{X\geq 2\} = 1 - P\{X=0\} - P\{X=1\} = 1- (1-0.01)^{50}-\begin{pmatrix} 50\\ 1\end{pmatrix}0.01(1-0.01)^{49} \approx 8.94\%
$$

### (a) at least once (estimate)
Using poisson with $\lambda=np = 50\cdot 0.01 = 0.5$
$$
P\{X\geq 1\} = 1 - P\{X=0\} \approx 1- e^{-0.5} \frac{0.5^0}{0!} \approx 39.35\%
$$

## Problem 4.4
If X is a Poisson r.v. with mean $\lambda$, show that P {X = i} first increases and then decreases as i increases, reaching its maximum value when i is the largest integer less or equal to $\lambda$.


## Problem 4.7
I roll a fair die repeatedly until a number larger than 4 is observed. If N is the total number of times that I roll the die, find P (N = k) where k = 1, 2, 3, .... How many trials we will need on average?

Geometric series with parameter $p=\frac{1}{3}$
$$
E[X] = \frac{1}{p} = \frac{1}{\frac{1}{3}} = 3
$$

## Problem 4.8
The number of customers arriving at a grocery store is a Poisson random variable. On average 10 customers arrive per hour. Let X be the number of customers arriving from 10:00 to 11:30. Find P (10 < X ≤ 15)
This just becomes a Poisson for 1.5 times the span so parameter $\lambda=10 \cdot 1.5 = 15$

$$
P\{10<X\leq 15\} = \sum_{i=11}^{15}e^{-15} \frac{15^i}{i!} \approx 44.96\%
$$
