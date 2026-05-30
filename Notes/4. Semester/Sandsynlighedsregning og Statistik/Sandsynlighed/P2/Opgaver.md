
## Problem 1
The distribution function of the random variable $X$ is given
$$
F(x)= \begin{cases}
0 & x<0 \\
\frac{x}{2} & 0 \leq x \lt 1 \\
\frac{2}{3} & 1\leq x < 2 \\
\frac{11}{12} & 2 \leq x < 3 \\
1 & 3\leq x
\end{cases}
$$
This is a Cumulative Distribution Function (CDF)
### (a) Plot this distribution function:
Geogebra:
`F(x) = If(x < 0, 0, If(x < 1, x/2, If(x < 2, 2/3, If(x < 3, 11/12, 1))))`

### (b) What is $P\{X>1/2\}$?
$$P\{X > 1/2\} = 1-F(1/2) = 1- \frac{1}{4} = \frac{3}{4}$$

### (c) What is $P\{2 < X \leq 4\}$?
Since it stops at 3, this is the same as $P\{X>2\}$:
$$
P\{2<x\leq 4\} = P\{X>2\} = 1- F(2) = 1-\frac{11}{12} = \frac{1}{12}
$$

### (d) What is $P\{X < 3\}$?
$$
P\{X<3\} = F(3) = \frac{11}{12}
$$

### (e) What is $P\{X=1\}$?
$$
P\{X=c\}= F(c) - \lim_{ x \to c^- } F(x)
$$
$$
P\{X=1\}= F(1) - \lim_{ x \to 1^- }  F(x) = \frac{2}{3} - \frac{1}{2} = \frac{1}{6}
$$

## Problem 2
The amount of time, in hours, that a computer functions before breaking down is a continuous random variable with probability density function given by
$$
f(x) = \begin{cases}
\lambda e^{-x/100} & x\geq 0 \\
0 & x < 0
\end{cases}
$$
What is the probability that a computer will function between 50 and 150 hours before breaking down? What is the probability that it will function less than 100 hours?

To define the PDF, we need to know the value of $\lambda$. By definition of PDF we know:
$$
\int_{-\infty}^\infty f(x) dx = 1
$$
Since $f(0) = 0$, we can simplify:
$$
\int_{0}^\infty \lambda e^{-x/100} dx = 1 \implies 100\lambda = 1 \implies \lambda = \frac{1}{100}
$$
PDF becomes:
$$
f(x) = \begin{cases}
\frac{1}{100} e^{-x/100} & x\geq 0 \\
0 & x < 0
\end{cases}
$$
So CDF:
$$
F(x) = \int_{0}^x \frac{1}{100}e^{-x/100} dx = 1-e^{-x/100}
$$

Probability that it breaks down between 50 and 150 hours:
$$
P(50 \leq X \leq 150) = \int_{50}^{150} \frac{1}{100}e^{-x/100}dx = F(150) - F(50) = 1-e^{-3/2} - 1 - e^{-1/2} \approx 38.3\%
$$
Less that 100 hours:
$$
P(X < 100) = \int_{0}^{100} f(x) dx = F(100) = 1-e^{-1} \approx 63.2\%
$$
## Problem 3
Let X be the number of the cars being repaired at a repair shop. We have the following information

* (a) At any time, there are at most 3 cars being repaired.
* (b) The probability of having 2 cars at the shop is the same as the probability of having one car.
 * (c) The probability of having no car at the shop is the same as the probability of having 3 cars.
* (d) The probability of having 1 or 2 cars is half of the probability of having 0 or 3 cars.

Find the PMF of X.

$$
P(X=x) = \begin{cases}
\frac{1}{3}, & x=0,3 \\
\frac{1}{6}, & x=1,2 \\
0, & \text{otherwise}
\end{cases}
$$
## Problem 4
The joint probability density function of X and Y is
$$
f(x) = \begin{cases}
xe^{-(x+y)} & x>0, y>0 \\
0 & \text{otherwise}
\end{cases}
$$
### (a) Compute the density of x

$$
f_{x}(x) = \int_{-\infty}^\infty f(x, y)dy = \int_{0}^\infty xe^{-(x+y)} dy = xe^{-x}
$$
$$
f_{x}(x) = \begin{cases}
xe^{-x} & x>0 \\
0 & \text{otherwise}
\end{cases}
$$

### (b) Compute the density of Y

$$
f_{y}(x) = \int_{-\infty}^\infty f(x, y)dx = \int_{0}^\infty xe^{-(x+y)} dx = e^{-y}
$$
$$
f_{y}(x) = \begin{cases}
e^{-y} & y>0 \\
0 & \text{otherwise}
\end{cases}
$$
### Are X and Y independent?
$$
f_{x}(x) \cdot f_{y}(x) = xe^{-x} \cdot e^{-y} = xe^{-(x+y)}
$$
Which is the same as $f(x, y)$, so the random variables X and Y are independent


## Problem 5
If the probability density function of X equals
$$
f(x) = \begin{cases}
ce^{-2x} & x\geq 0 \\
0 & x<0
\end{cases}
$$
### Find c
The total of all values in the density (area under the curve; integral), must be equal to 1:
$$
\implies \int_{-\infty}^\infty f(x) dx = 1 \implies \int_{0}^\infty ce^{-2x} dx = 1 \implies \frac{c}{2} = 1 \implies c=2
$$

### What is $P\{X>2\}$?
Plugging in $c=2$ and solving the integral we get:
$$
P\{X > 2\} = \int_{2}^\infty 2e^{-2x} dx = e^{-4} \approx 1.8\%
$$


## Problem 6
A message is transmitted from A to B. Probability to receive a message is 0.8. A message is retransmitted until it is successfully received. Let X be a random variable represented a number of times it took to send the message until it is successfully received. Find pmf of X.

$$
P(X=x) = 0.8 \cdot 0.2^{x-1}, x \geq 1
$$
As it is a discrete case, the integral does not have to equal 1.

## Problem 7
Let X represent the difference between the number of heads and tails obtained when a coin is tossed n times. What are the possible values of X?

This is a fucking stupid question wtf

## Problem 8
We roll two dice and observe two numbers X and Y
### (a) Find marginal and joint pmfs of X and Y
What are these fucking notation questions???
$$
P(X=k, Y=j) = P(X=k)P(Y=j) = \frac{1}{36}
$$

### (b) Find $P(X=2, Y=6)$
$\frac{1}{36}$

### (c) Find $P(X>3|Y=2)$
They are independent, so its just $P(X>3) = \frac{1}{2}$
