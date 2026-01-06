
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
