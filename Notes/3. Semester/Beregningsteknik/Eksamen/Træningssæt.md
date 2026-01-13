
# Opg 1

Let set S consists of the first three letters of the English alphabet: $S = \{A, B, C\}$

### (a) What is the cardinality of the set $S$?
3

### (b) How many different subsets can we construct from the set S? List the possible subsets.
$2^3 = 8$

1. $\{\}$
2. $\{A\}$
3. $\{B\}$
4. $\{C\}$
5. $\{A,B\}$
6. $\{A,C\}$
7. $\{B,C\}$
8. $\{A,B,C\}$

### Now, let set $S_2$ consists of all letters in the English alphabet. Answer the same questions for the set $S_2$, except for listing the possible subsets.
#### (a): 26
#### (b): $2^{26} = 67108864$


# Opg 2

Bestem sandshedstabellen for det betingede udsagn $(p \vee q) \to (p \land \neg q)$. Er der tale om en tautologi, en modstrid (contradiction), eller en kontingens (contingency)?

| p   | q   | $p \vee q$ | $p \land \neg q$ | $(p \vee q) \to (p \land \neg q)$ |
| --- | --- | ---------- | ---------------- | --------------------------------- |
| 0   | 0   | 0          | 0                | 1                                 |
| 0   | 1   | 1          | 0                | 0                                 |
| 1   | 0   | 1          | 1                | 1                                 |
| 1   | 1   | 1          | 0                | 0                                 |
Det ses fra sandhedstabellen at udtrykket er en kontingens

# Opg 3
Benyt matematisk induktion til at bevise at $2^n > n^2 + n$, hvor n er et heltal større end 4; angiv de relevante hypoteser og step i proceduren.

$$

$$

# Opg 5
Betragt følgende logiske udsagn: $p \vee \neg q$, $\neg p \vee q$, $q \vee r$, $q \vee \neg r$, $\neg q \vee \neg r$
Bestem det maksimale antal udsagn der samtidigt kan gøres sande ved at tildele sandhedsværdier til p, q, og r; begrund dit svar.

| p   | q   | r   | $p \vee \neg q$ | $\neg p \vee q$ | $q \vee r$ | $q \vee \neg r$ | $\neg q \vee \neg r$ |
| --- | --- | --- | --------------- | --------------- | ---------- | --------------- | -------------------- |
| 0   | 0   | 0   | 1               | 1               | 0          | 1               | 1                    |
| 0   | 0   | 1   | 1               | 1               | 1          | 0               | 1                    |
| 0   | 1   | 0   | 0               | 1               | 1          | 1               | 1                    |
| 0   | 1   | 1   | 0               | 1               | 1          | 1               | 0                    |
| 1   | 0   | 0   | 1               | 0               | 0          | 1               | 1                    |
| 1   | 0   | 1   | 1               | 0               | 1          | 0               | 1                    |
| 1   | 1   | 0   | 1               | 1               | 1          | 1               | 1                    |
| 1   | 1   | 1   | 1               | 1               | 1          | 1               | 0                    |
Fuld plade ved p=1, q=1 og r=0, betyder at alle udsagn er sande ved dette input

# Opg 6
We are given a sequence defined by:
$$
a_{n+1} = (a_{n}-2), a_{1} = 5
$$
And must show that the series is decreasing for $n \in N$

This can also be written as:
$$
P(n): a_{n} > a_{n+1}
$$
The base case:
$$
P(1): a_{1} > a_{2}: 5 > 3 = TRUE
$$
Hypothosis:
$$
P(k): a_{k} > a_{k+1}
$$
We want to prove:
$$
P(k+1): a_{k+1} > a_{k+2}
$$
We can do this by using the hypothesis and subtracting 2 from both sides:
$$
a_{k} -2 > a_{k+1} -2
$$
Which by the definition $a_{n+1} = a_{n} -2$ becomes:
$$
a_{k+1} > a_{k+1+1}
$$
And proves:
$$
a_{k+1} > a_{k+2}
$$

# Opg 7
Fibonacci numbers are defined like this:
$$
F(0) = 1, F(1) = 1, F(n) = F(n-1) + F(n-2); n \geq 2
$$
## a) Explain how you calculate $F(7)$
To calculate $F(7)$, all previous Fibonacci numbers must be calculated, as it is a recursive definition, the first two steps can be described like this:
$$
F(7)=F(6) + F(5) = F(5) + F(4) + F(4) + F(3) = \dots
$$
A simpler approach may be to start at $F(0)$ and calculate all following numbers like so:
* $F(0) = 1$
* $F(1) = 1$
* $F(2) = 2$
* $F(3) = 3$
* $F(4) = 5$
* $F(5) = 8$
* $F(6) = 13$
* $F(7) = 21$
## b) Using principles of mathematical induction, show that $F (n) \leq 2n, n \geq 1$

$$
P(n): F(n) \leq 2^n, n\geq 2
$$

Base case:
$$
P(1): F(1) \leq 2^1 = 1 \leq 2 = TRUE
$$
$$
P(2): F(2) \leq 2^2 = 2 \leq 4 = TRUE
$$
Since we need multiple values for $F(j)$ to prove the statement, the hypothesis must include all values from 1 through k:
$$
P(j): F(j) \leq 2^j, 1 \leq j \leq k
$$
We want to show that:
$$
P(k+1): F(k+1) \leq 2^{k+1}
$$
Using the hypothesis and the definition of $F(k+1)$, we know that:
$$
F(k) + F(k-1) \leq 2^k + 2^{k-1}
$$
$$
\implies F(k+1) \leq 2^k+2^{k-1}
$$
We know that for all values $k\geq 1$, $2^k > 2^{k-1}$, therefore:
$$
2^k + 2^{k-1} < 2^k + 2^k
$$
Which means that:
$$
2^k + 2^{k-1} < 2(2^k) \implies 2^k + 2^{k-1} < 2^{k+1}
$$
Proving that:
$$
\implies F(k+1) \leq 2^k+2^{k-1} < 2^{k+1} \implies F(k+1) \leq 2^{k+1} Q.E.D
$$




# Opg 8
Derive all roots of $z^8 = -i2$ where $i=\sqrt{-1}$ and sketch them in an Argand diagram; state the answer in polar form, using rational numbers and arguments within the interval $[0; 2\pi)$.

Polar form:
$$
z = r(\cos(\theta) +i \sin(\theta))
$$
Where r is the modulus ($|z|$ (length of the "vector")) and $\theta$ is the argument (angle relative to x-axis). The n roots are then given by:
$r = 2$
$\theta = 270^o = \frac{3\pi}{2}$
$n=8$
$$
w_{k} = \sqrt[n]{r}\left( \cos\left( \frac{\theta+2\pi k}{n} \right) + i\sin\left( \frac{\theta + 2\pi k}{n} \right) \right)
$$
For $k=0, 1, 2, \dots, n-1$

$R=\sqrt[n]{ r } = \sqrt[8]{2} \approx 1.09$

$$
\phi_{0} = \frac{\frac{3\pi}{2} + 2\pi\cdot 0}{8} = \frac{3\pi}{16}
$$
$$
w_{0} = \sqrt[8]{ 2 }\left( \cos\left( \frac{3\pi}{16} \right) + i \sin\left( \frac{3\pi}{16} \right) \right)
$$
$$
\phi_{1} = \frac{\frac{3\pi}{2} + 2\pi\cdot 1}{8} = \frac{7\pi}{16}
$$
$$
w_{1} = \sqrt[8]{ 2 }\left( \cos\left( \frac{7\pi}{16} \right) + i \sin\left( \frac{7\pi}{16} \right) \right)
$$
$$
\phi_{2} = \frac{\frac{3\pi}{2} + 2\pi\cdot 2}{8} = \frac{11\pi}{16}
$$
$$
w_{2} = \sqrt[8]{ 2 }\left( \cos\left( \frac{11\pi}{16} \right) + i \sin\left( \frac{11\pi}{16} \right) \right)
$$
...

Vi kan se at 8 rødder med radius $\approx 1.09$ fordeler sig med $\frac{\pi}{4}$ afstand, og starter i $\frac{3\pi}{16}$
Plot med: `roots = Sequence[(2^(1/8)*cos((k * 2pi + 3pi/2)/ 8), 2^(1/8)*sin((k * 2pi + 3pi/2)/ 8)), k, 0, 7]`

# Opg 9
Find center and radius for convergence of the following series
$$
\sum_{n=0}^\infty \frac{n}{e^{1-n}}(z-i)^n
$$
$z_0 = i$ (center at i)

Ratio test:
$a_{n} = \frac{n}{e^{1-n}} = ne^{n-1}$
$$
L = \lim_{ n \to \infty } |\frac{a_{n+1}}{a_{n}}| = \lim_{ n \to \infty } \frac{(n+1)e^n}{ne^{n-1}}
$$
$$
= \lim_{ n \to \infty } \frac{n+1}{n}\cdot e = e
$$
Radius for ratio test is
$$
R = \frac{1}{L} = \frac{1}{e}
$$

## Part 2
$$
\sum_{n=1}^\infty \frac{3^n}{n^2}(5z-6)^n
$$
Ønsket form for en power series:
$$
\sum_{n=0}^\infty a_{n}(z-z_{0})^n
$$
Omskrevet til den form:
Center for $5z-6$ findes ved at omskrive til $z-z_0$:
$\frac{5z-6}{5} = z-\frac{6}{5}$
$z_{0}$ (center) må derfor være $\frac{6}{5}$
$a_{n}=\frac{3^n}{n^2}$

Serien sker ikke direkte i $z$, men i $\omega=5z-6$, vi udregner derfor først radius i $\omega$:
$$
R_{\omega} = \frac{1}{L} = \lim_{ n \to \infty } |\frac{a_{n}}{a_{n+1}}| = \lim_{ n \to \infty }  \frac{\frac{3^n}{n^2}}{\frac{3^{n+1}}{(n+1)^2}} = \lim_{ n \to \infty } \frac{3^n}{n^2} \cdot \frac{(n+1)^2}{3^{n+1}}
$$
$$
\implies R_{\omega} = \lim_{ n \to \infty } \frac{1}{3} \cdot \frac{(n+1)^2}{n^2} = \frac{1}{3}
$$

Radius i $z$ findes ved at gange med forholdet mellem $\omega$ og $z$, som er 5:
$$
R = \frac{R_{\omega}}{5} = \frac{1}{15}
$$

# Opg 11
Calculate the Taylor series with center $z_{0}$ of the following functions:
Taylor serier er defineret:
$$
\frac{f^{(n)}(z_{0})}{n!}(z-z_{0})^n
$$
## 1
$f(z) = e^{z-1}, z_{0}=1$
Maclaurin for $e^\omega$ is defined as:
$$
e^\omega = \sum_{n=0}^\infty \frac{\omega^n}{n!}
$$
If we substitute $\omega = z-1$, we can find the Taylor series with $z_{0}=1$:
$$
e^{z-1} = \sum_{n=0}^\infty \frac{(z-1)^n}{n!}
$$
### Den "rigtige" måde
$$
f(1) = e^0 = 1
$$
$$
f'(1) = e^0 = 1
$$
$$
\dots = 1
$$
$$
e^{z-1} = \sum_{n=0}^\infty \frac{(z-1)^n}{n!}
$$
## 2
$$
f(z) = \cos(z), z_{0}=\frac{\pi}{2}
$$
$$
f\left( \frac{\pi}{2} \right) = \cos\left( \frac{\pi}{2} \right) = 0
$$
$$
f'\left( \frac{\pi}{2} \right) = -\sin\left( \frac{\pi}{2} \right) = -1
$$
$$
f''\left( \frac{\pi}{2} \right) = -\cos\left( \frac{\pi}{2} \right) = 0
$$
$$
f'''\left( \frac{\pi}{2} \right) = \sin\left( \frac{\pi}{2} \right) = 1
$$
$$
-z+\frac{\pi}{2} + \frac{\left( z+\frac{\pi}{2} \right)^3}{6}
$$
$$
f(z) = \sum_{n=0}^\infty \frac{(-1)^{n+1}(z-\frac{\pi}{2})^{2n+1}}{(2n+1)!}
$$
### Den nemme
$$
\cos(\omega) = \sum_{n=0}^\infty \frac{(-1)^n(\omega)^{2n}}{(2n)!}
$$
Vi vil have formen $z-\frac{\pi}{2}$, så vi definere 
$$
\omega=z-\frac{\pi}{2} \implies z=\omega+\frac{\pi}{2}
$$
$$
\cos(z) \implies \cos\left( \omega+\frac{\pi}{2} \right)
$$
Aimbot hack:
$$
\cos\left( \omega+\frac{\pi}{2} \right) = -\sin(\omega)
$$
Vi kan bruge den kendte Maclaurin for $\sin$:
$$
-\sin(\omega) = -\sum_{n=0}^\infty \frac{(-1)^n\omega^{2n+1}}{(2n+1)!} =\sum_{n=0}^\infty \frac{(-1)^{n+1}\omega^{2n+1}}{(2n+1)!}
$$
Så indsætter vi definitionen for $\omega$:
$$
f(z)=\cos\left( z-\frac{\pi}{2} \right) = \sum_{n=0}^\infty \frac{(-1)^{n+1}\left( z-\frac{\pi}{2} \right)^{2n+1}}{(2n+1)!}
$$
## 3
$$
f(z) = \sin(5z), z_{0}=0
$$
### Den nemme
Da centrum er $z_{0}=0$, er det er Maclaurin serie, som er kendt for $\sin(\omega)$:
$$
\sin(\omega) = \sum_{n=0}^\infty \frac{(-1)^n\omega^{2n+1}}{(2n+1)!}
$$
Vi kan definere $\omega=5z$, og sætte det ind i udtrykket:
$$
f(z) = \sin(5z) = \sum_{n=0}^\infty \frac{(-1)^n(5z)^{2n+1}}{(2n+1)!}
$$
### Den svære
Maclaurin defintion:
$$
\frac{f^{(n)}(0)z^n}{n!}
$$
$$
f(0) = \sin(5\cdot 0) = 0
$$
$$
f'(0) = 5 \cos(5\cdot 0) = 5
$$
$$
f''(0) = -25 \cdot \sin(5\cdot 0) = 0
$$
$$
f'''(0) = -125 \cdot \cos(5\cdot 0) = -125
$$
$$
f(z) = 5z - \frac{125z^3}{6} + \dots
$$



# Opg 12
$$
\frac{d^2y}{dx^2} + \frac{dy}{dx} -6y = \sin(x)
$$
Corresponding homogeneous:
$$
y'' + y' - 6y = 0
$$
$$
y_{h} = Ae^{-3x} + Be^{2x}
$$
Specific guess:
$$
y_{p} = A\cos(x) + B\sin(x)
$$
$$
y_{p}'= - A\sin(x) + B\cos(x) 
$$
$$
y_{p}'' = -A\cos(x) - B\sin(x)
$$
In the original equation:
$$
-A\cos(x)-B\sin(x)-A\sin(x)+B\cos(x)-6(A\cos(x)+B\sin(x)) = \sin(x)
$$
$$
-A\sin(x) + B\cos(x)-7A\cos(x)-7B\sin(x) = \sin(x)
$$
$$
B-7A = 0, -A-7B = 1
$$
$$
A = -\frac{1}{50} \land B=-\frac{7}{50}
$$
$$
y_{p} = -\frac{1}{50}\cos(x) -\frac{7}{50}\sin(x)
$$

$$
y = y_{h} +y_{p} = Ae^{-3x} + Be^{2x} - \frac{1}{50}\cos(x) - \frac{7}{50}\sin(x)
$$

# Opg 13

Solve the following differential equations:

### $\frac{dy}{dx} - 1 + 2\cos(x) = 0, y(0) = 3$

$$
1 - 2\cos(x) = \frac{dy}{dx}
$$
$$
\implies \int 1 - 2\cos(x) dx = \int\frac{dy}{dx}dx
$$
$$
\implies x - 2\cdot \sin(x) +C = y
$$
$$
0 -2\cdot \sin(0) +C = 3
\implies C = 3
$$
$$
y = x-2\cdot \sin(x) +3
$$

### $\frac{dy}{dx} + 2x + y = 0,y(0) = 4$

$$
\mu(x) = \int 1dx = x +C
$$
$$
y(x) = e^{-x} \int -2xe^x dx
$$
$$
y = e^{-x} \cdot (-2xe^x+2e^x + C) = -2x +2 +Ce^{-x}
$$
$$
-2\cdot 0 + 2 + C = 4 \implies C=2
$$
$$
y = -2x + 2 +2e^{-x}
$$


### $\frac{d^2y}{dx^2} - \frac{dy}{dx} -2x = 0, y(0)=1,y'(0)=-1$

Corresponding homogenous:
$$
y'' - y' = 0
$$
$r_{1} = 0 \land r_{2} = 1$
$$
y_{h} = A + Be^x
$$
Particular, we guess:
$$
y_{p} = Ax^2+Bx
$$
$$
y_{p}' = 2Ax + B
$$
$$
y_{p}'' = 2A
$$
Placed in the original equation:
$$
2A - 2Ax - B = 2x
$$
$$
-2Ax = 2x, 2A-B = 0
$$
$$
\implies A=-1 \land B=-2
$$
$$
y_{p} = -x^2 -2x
$$

$$
y = y_{h} + y_{p} = A + Be^x -x^2-2x
$$
$$
y(0) = A + B = 1
$$
$$
y'(0) = Be^0 - 2\cdot{0} - 2 = -1 \implies B -2 = -1 \implies B=1 \land A=0
$$
$$
y = e^x - x^2 - 2x
$$
# Opg 4 - Reeksamen
## $\sum_{n=0}^\infty \frac{e^n}{2^{n+1}}(z-2)^n$

Power series er defineret på denne form, hvor $z_{0}$ er center of convergence.
$$
\sum_{n=0}^\infty a_{n}(z-z_{0})^n
$$
Da udtrykker passer på denne form, er center givet ved $z_{0}=2$
Radius kan vindes ved cauchy-hadamard test af $a_n$ ledet:

$$
R = \frac{1}{L} = \lim_{ n \to \infty } \left| \frac{a_{n}}{a_{n+1}} \right| = \lim_{ n \to \infty } \left| \frac{\frac{e^n}{2^{n+1}}}{\frac{e^{n+1}}{2^{n+2}}} \right| = \lim_{ n \to \infty } \frac{e^n}{e^{n+1}} \cdot \frac{2^{n+2}}{2^{n+1}} = 2e^{-1} = \frac{2}{e}
$$
Radius er altså givet ved $\frac{2}{e} \approx 0.736$


# Opg 5 - Reeksamen
## $\frac{dy}{dx}-16x=y, y(0)=6$

Den ønskede form er:
$$
\frac{dy}{dx}+p(x)y=q(x)
$$
Ligningen opstilles på formen:
$$
\frac{dy}{dx} - y = 16x
$$
Ledene bestemmes til at være:
$$
p(x) = 1 \land q(x) = 16x
$$
$\mu(x)$ bestemmes:
$$
\mu(x) = \int p(x)dx = \int 1 dx = x + C
$$
$y(x)$ bestemmes:
$$
y(x) = e^{-\mu(x)} \int e^{\mu(x)}q(x)dx = e^{-x} \int e^x 16x dx = (16xe^x -16e^x + C)e^{-x}
$$
$$
y(x) = Ce^{-x} + 16x - 16
$$
Værdien for $y(0)$ indsættes for at bestemme konstanten:
$$
y(0) = Ce^0 + 16\cdot 0 - 16 = 6 \implies C - 16 = 6 \implies C = 22
$$
Den færdige løsning er derfor:
$$
y(x) = 22e^x - 16x -16
$$

## $\frac{dy}{dx}+\frac{y}{x^3}=0, y(1)=\sqrt{ e }$

Den ønskede form er:
$$
\frac{dy}{dx}+p(x)y=q(x)
$$
Ledene bestemmes til at være:
$$
p(x) = \frac{1}{x^3} \land q(x) = 0
$$
$\mu(x)$ bestemmes:
$$
\mu(x) = \int p(x)dx = \int \frac{1}{x^3} dx = -\frac{1}{2x^2} + C
$$
$y(x)$ bestemmes:
$$
y(x) = e^{-\mu(x)} \int e^{\mu(x)}q(x)dx = e^{1/2x^2} \int e^{-1/2x^2} 0 dx = e^{1/2x^2}(0 + C)
$$
$$
y(x) = Ce^{1/2x^2}
$$
Værdien for $y(1)$ indsættes for at bestemme konstanten:
$$
y(1) = Ce^{1/(2\cdot 1^2)} = \sqrt{ e }
$$
$$
Ce^{1/2} = C\sqrt{ e } = \sqrt{ e } \implies C=1
$$
Den endelige løsning er derfor:
$$
y(x) = e^{1/2x^2}
$$
