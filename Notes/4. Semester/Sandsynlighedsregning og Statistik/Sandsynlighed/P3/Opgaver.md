## Problem 3.1
The density function of X is given by
$$
f(x) = \begin{cases}
a + bx^2 & 0\leq x \leq 1 \\
0 & \text{otherwise}
\end{cases}
$$
If $E[X]=\frac{3}{5}$,  find a and b:

The whole thing must equal 1:
$$
\int_{0}^1 (a+bx^2) dx= 1 \implies a + \frac{b}{3} = 1
$$
By definition of expectation we get:
$$
\int_{0}^1 x(a+bx^2) dx= \frac{3}{5} \implies \frac{a}{2} + \frac{b}{4} = \frac{3}{5}
$$

$$
a + \frac{b}{2} = \frac{6}{5} \implies 1-\frac{b}{3} + \frac{b}{2} = \frac{6}{5} \implies \frac{6}{6} - \frac{2b}{6} + \frac{3b}{6} = \frac{6}{5}
$$
Multiply by 6:
$$
6+b = \frac{36}{5} \implies b = \frac{36}{5} - \frac{30}{5} = \frac{6}{5}
$$
Substitute for a: 
$$
a = 1- \frac{6}{5\cdot 3} \implies a = \frac{15}{15} - \frac{6}{15} = \frac{9}{15} = \frac{3}{5}
$$
So we have: $a=\frac{3}{5} \land b=\frac{6}{5}$

## Problem 3.2
If $E[X]=2$ and $E[X^2]=8$ calculate:
### (a) $E[(2+4X)^2]$
$$
E[(2+4X)^2] = E[4 + 16x+16X^2] = E[4] + E[16X] + E[16X^2] = 4 + 16 \cdot 2 + 16 \cdot 8 = 164
$$


### (b) $E[X^2+(X+1)^2]$
$$
E[X^2+(X+1)^2] = E[2X^2+2X+1] = 2E[X^2] + 2E[X] + 1 = 16 + 4 +1 = 21
$$

## Problem 3.3
A product is classified according to the number of defects it contains and the factory that produces it. Let X1 and X2 be the random variables that represent the number of defects per unit (taking the possible values of 0, 1, 2, or 3) and the factory number (taking on possible values 1 or 2), respectively. The entries in the table represent the joint probability mass function of a random chosen product: P (0, 1) = 1/8; P (0, 2) = 1/16; P (1, 1) = 1/16; P (1, 2) = 1/16; P (2, 1) = 3/16; P (2, 2) = 1/8; P (3, 1) = 1/8; P (3, 2) = 1/4

### (a) Find the marginal probability distributions of $X_{1}$ and $X_{2}$

| $X_{1}$\ $X_2$ | $X_{2}=1$      | $X_{2}=2$      | $P(X_{1})$     |
| -------------- | -------------- | -------------- | -------------- |
| $X_{1}=0$      | $\frac{2}{16}$ | $\frac{1}{16}$ | $\frac{3}{16}$ |
| $X_{1}=1$      | $\frac{1}{16}$ | $\frac{1}{16}$ | $\frac{2}{16}$ |
| $X_{1}=2$      | $\frac{3}{16}$ | $\frac{2}{16}$ | $\frac{5}{16}$ |
| $X_{1}=3$      | $\frac{2}{16}$ | $\frac{4}{16}$ | $\frac{6}{16}$ |
| $P(X_{2})$     | $\frac{8}{16}$ | $\frac{8}{16}$ |                |
So marginal probability distribution of $X_{1}$:
$$
P(X_{1}=0) = \frac{3}{16}, P(X_{1}=1)=\frac{1}{8}, P(X_{1}=2)=\frac{5}{16}, P(X_{1}=3)=\frac{6}{16}
$$
And marginal probability distribution of $X_{2}$:
$$
P(X_{2}=1)=\frac{1}{2}, P(X_{2}=2)=\frac{1}{2}
$$

### (b) Find $E[X_1]$
$$
E[X_{1}] = 0 \cdot \frac{3}{16} + 1 \cdot \frac{2}{16} + 2 \cdot \frac{5}{16} + 3 \cdot \frac{6}{16} = \frac{30}{16} = \frac{15}{8} = 1.875
$$
### (c) Find $E[X_2]$
$$
E[X_{2}] = 1 \cdot \frac{1}{2} + 2\cdot \frac{1}{2} = \frac{3}{2} = 1.5
$$
### (d) Find $Var[X_1]$
$$
E[X_{1}^2] = 0^2 \cdot \frac{3}{16} + 1^2 \cdot \frac{2}{16} + 2^2 \cdot \frac{5}{16} + 3^2 \cdot \frac{6}{16} = \frac{76}{16} = 4.75
$$
$$
Var(X_{1}) = E[X_{1}^2] - E[X_{ 1}]^2 = 4.75 - 1.875^2 \approx 1.234
$$
### (e) Find $Var[X_2]$

$$
E[X_{2}^2] = 1^2 \cdot \frac{1}{2} + 2^2\cdot \frac{1}{2} = \frac{5}{2} = 2.5
$$
$$
Var(X_{2}) = E[X_{2}^2] - E[X_{2}]^2 = 2.5 - 1.5^2  = 0.25
$$
### (f) Find $Cov[X_1, X_2]$

$$
E[X_{1}X_{2}] = 1\left( 1\cdot \frac{1}{16} + 2\cdot \frac{1}{16} \right) + 2 \left( 1 \cdot \frac{3}{16} + 2 \cdot \frac{2}{16} \right) + 3 \left( 1 \cdot \frac{2}{16} + 2 \cdot \frac{4}{16} \right) = \frac{47}{16}
$$
$$
Cov(X_{1}, X_{2}) = E[X_{1}X_{2}] - E[X_{1}]E[X_{2}] = \frac{47}{16}-\frac{15}{8} \cdot \frac{3}{2} = \frac{1}{8}
$$
## Problem 3.4
Suppose that X has density function
$$
f(x) = e^{-x}, x>0
$$

Compute the moment generating function of X and use your results to determine its means and variance.
Check your answer fir the mean by a direct calculation


## Problem 3.5
A cdf of a r.v. $X$ is
$$
F(x) = \begin{cases}
0 & x\leq 0 \\
\frac{x}{4} & 0<x\leq 4 \\
1 & x>4
\end{cases}
$$
Find $E[X]$
$$
E[X] = \int_{-\infty}^\infty 1-F(x) dx = \int_{0}^4 1-\frac{x}{4} dx = \left|x - \frac{x^2}{8}\right|_{0}^4 = 2
$$
OR
$$
f(x) = \frac{dF(x)}{dx} = \frac{1}{4}
$$
$$
E[X] = \int_{-\infty }^\infty xf(x) dx =  \int_{0}^4 \frac{x}{4} dx = \left|\frac{x^2}{8}\right|_{0}^4 = 2
$$
