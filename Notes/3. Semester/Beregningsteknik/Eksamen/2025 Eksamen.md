# Opg 4
## a) Verify the convergence of the following series:

### $\sum_{n=1}^\infty \frac{n}{n!}$ 

$$
\left| \frac{z_{n+1}}{z_{n}}\right| \leq q < 1
$$
$$
L = \lim_{ n \to \infty } \frac{\frac{n+1}{(n+1)!}}{\frac{n}{n!}} = \lim_{ n \to \infty } \frac{n+1}{(n+1)!} \cdot \frac{n!}{n} = \lim_{ n \to \infty }  \frac{n+1}{n} \cdot \frac{n!}{(n+1)!} = 1 \cdot 0 = 0
$$
Since L is < 1, the series converges absolutely

Tech tip til næste gang:
$$(n+1)!=(n+1)n!$$

### $\sum_{n=0}^\infty \frac{n^2}{e^{n-1}}$

Ratio:
$$
\frac{\frac{(n+1)^2}{e^n}}{\frac{n^2}{e^{n-1}}} = \frac{(n+1)^2}{e^n}\cdot \frac{e^{n-1}}{n^2} = \frac{(n+1)^2}{n^2}\cdot \frac{e^{n-1}}{e^n}
$$
$$
L = \lim_{ n \to \infty }  \frac{(n+1)^2}{n^2}\cdot \frac{e^{n-1}}{e^n} = 1 \cdot \frac{1}{e} = \frac{1}{e}
$$

Since $L < 1$, the series converges absolutely

### $\sum_{n=1}^\infty \frac{5^{n+2}}{n^n}$

Ratio:
$$
\frac{\frac{5^{n+3}}{(n+1)^{n+1}}}{\frac{5^{n+2}}{n^n}} = \frac{5^{n+3}}{(n+1)^{n+1}}\cdot \frac{n^n}{5^{n+2}} = \frac{5^{n+3}}{5^{n+2}}\cdot \frac{n^n}{(n+1)^{n+1}}
$$
Ratio test:
$$
L = \lim_{ n \to \infty } \frac{5^{n+3}}{5^{n+2}}\cdot \frac{n^n}{(n+1)^{n+1}} = 5 \cdot 0 = 0
$$
Since $L<1$, the series is absolutely convergent

Root test:
$$
\sqrt[n]{\frac{5^{n+2}}{n^n}} = \left( \frac{5^{n+2}}{n^n} \right)^{1/n} = \frac{5^{(n+2)/n}}{n} = \frac{5^{1 + 2/n}}{n} = \frac{5\cdot 5^{2/n}}{n}
$$

$$
\lim_{ n \to \infty } 5^{2/n} = 5^0 = 1
$$
$$
L = \lim_{ n \to \infty } \frac{5\cdot 1}{n} = 0
$$

## b) Calculate for which values of $a$ the following series is absolutely convergent
$$
\sum_{n=0}^\infty n^2 \left( \frac{a}{5} \right)^n
$$
Ratio:
$$
\left| \frac{(n+1)^2 \left(\frac{a}{5}\right)^{n+1}}{n^2 \left(\frac{a}{5}\right)^n} \right| = \left| \frac{(n+1)^2}{n^2} \right| \cdot \left| \frac{a}{5} \right|
$$

Ratio test:
$$
L = \lim_{ n \to \infty } \frac{(n+1)^2}{n^2} \cdot \left|\frac{a}{5}\right| = \left|\frac{a}{5}\right|
$$
Series is absolutely  convergent when $L<1$, so, which implies:
$$
\left| \frac{a}{5} \right| <1 \implies |a| < 5
$$
or: $-5\lt a \lt 5$

The ratio test is not defined at the boundaries, so we must check for a=5 and a=-5:

$$
\sum_{n=0}^\infty n^2 \left( \frac{5}{5} \right)^n = n^2
$$
$$
\sum_{n=0}^\infty n^2 \left( \frac{-5}{5} \right)^n = (-1)^n\cdot n^2
$$

Both of these values are divergent, and thus the series is absolutely convergent for all values of a, that satisfy:
$$
-5 < a < 5
$$

# Opg 5
Solve the following differential equation:
$$
\frac{d^2y}{dx^2} + \frac{dy}{dx} - 6y=\sin(x)
$$
Solution to the corresponding homogeneous:
$$
\frac{d^2y}{dx^2} + \frac{dy}{dx} - 6y= 0
$$
$$
r_{1} = -3 \land r_{2}=2
$$
Solution for the homogeneous:
$$
y_{h} = Ae^{-3x}+Be^{2x}
$$
Guess for the particular solution:
$$
y_{p} = A\cos(x)+B\sin(x)
$$
$$
y_{p}' = -A\sin(x) + B\cos(x)
$$
$$
y_{p}'' = -A\cos(x) - B\sin(x)
$$
Which is placed in the original equation:
$$
-A\cos(x) - B\sin(x) -A\sin(x) + B\cos(x) - 6A\cos(x)-6B\sin(x) = \sin(x)
$$
$$
\implies -7A\cos(x) - A\sin(x) + B\cos(x) - 7B\sin(x)= \sin(x)
$$
Since there is no cosine on the right, cosine terms must equal 0:
$$
-7A + B = 0
$$
And sine terms must equal 1:
$$
-A -7B = 1
$$
$$
B = 7A \implies -A-49A=1 \implies -50A = 1 \implies A=-\frac{1}{50}
$$
$$
B = 7A \implies B=-\frac{7}{50}
$$
In the original specific guess:
$$
-\frac{1}{50} \cos(x) - \frac{7}{50}\sin(x)
$$


The general solution is the sum of the homogeneous and particular solutions:
$$
y = y_{h} + y_{p} = Ae^{-3x} + Be^{2x} - \frac{1}{50}\cos(x) - \frac{7}{50}\sin(x)
$$
