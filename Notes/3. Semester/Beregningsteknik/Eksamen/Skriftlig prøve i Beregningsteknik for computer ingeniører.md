# Exercise 1
$$
n 7^n < 5n!, n \in Z^+, n>b
$$
Udtrykket er tvetydigt, så jeg vælge at fortolke det som $n(7^n) < 5(n!)$
## 1. Determine the value of $b$ required for completing the basis step

$$
P(1) = 7 < 5 = FALSE
$$
$$
P(2) =  98 < 10 = FALSE
$$
$$
\dots = FALSE
$$
Ved brug af et simpelt python script kan alle muligheder afprøves indtil:
$$
P(17) = 17 \cdot 7^{17} < 5 \cdot 17! = FALSE
$$
$$
P(18) = 18 \cdot 7^{18} < 5 \cdot 18! = TRUE
$$
$$
\dots = TRUE
$$
Det gælder altså for et vilkårligt $n \in Z^+, n>17$

$P(18)$ er også basissteppet for det induktive bevis

## Prove that the inequality is true for all $n \in Z^+, n > b$
Induktive Hypotese:
$$
P(k) = k(7^k) < 5(k!), k\in Z^+, k > 17
$$
Vi vil vise at:
$$
P(k+1) = (k+1)(7^{k+1}) < 5((k+1)!), k \in Z^+, k > n
$$

Vi kan den induktive hypotese med $(k+1)$ på begge sider, for at få samme højre side som det vi vil bevise:
$$
(k+1)k(7^k) < 5(k!)(k+1) \implies (k+1)k(7^k) < 5((k+1)!)
$$
Vi ved nu at så længe denne venstre side er større end eller lig med venstresiden i det vi vil bevise, så er udtrykket sandt:
$$
(k+1)(7^{k+1}) \leq (k+1)k(7^k)
$$
Da vi antager $k>17$, må vi dele med $(k+1)$ på begge sider, uden at vende ligheden
$$
7^{k+1} \leq k(7^k)
$$
Det kan ses at dette udtryk er sandt for alle $k\geq 7$, da en forøgelse af k, vil gange venstresiden med 7, og højresiden med $k$.
$k\geq 7$ inkluderer alle værdier $k \gt 17$, og udsagnet holder


# Exercise 2
## Find the zeros of the complex function $f(z)$ defined in the complex number domain $z \in C$
$$
f(z) = 2\sin(z) + \sqrt{3}e^{iz}
$$
$$
z = \sin^{-1}\left(-\frac{\sqrt{ 3 }e^{iz}}{2}\right)
$$

Ved brug af et CAS værktøj, kan jeg se, at der ikke findes nogle løsninger til dette udtryk
```python
solve(arcsin(-(sqrt(3)*e**(I*z))/2) == 0, z)
[]
```

# Exercise 3
18 people need to go to an event, out of which four volunteer to drive using their own car. The drivers have a capacity to carry 4, 4, 3 and 3 people, respectively, i.e., totally 14 people, which, including the 4 drivers, makes up the total (18).

In how many ways is it possible to distribute the people to the four cars? What counting principle(s) did you apply?
---

Da hver fører allerede sidder i en specific bil, skal 14 mennesker distribueres. 
Der er forskellige måde at tænke på fordelingen af mennesker. Hvis hvert sæde er "unikt" (altså at det er en anden kombination, hvis passagerne i en given bytter pladser), så er der: $14!$ forskellige måder at fylde sæderne.

Hvis man istedet betragter hver bil som unik, men ikke de individuelle sæder, så er der:
$C(14, 4)$ måder at fylde den første bil
For hver af de måder, er der $C(10, 4)$ måder at fylde den anden bil
For hver af de måder, er der $C(6, 3)$ måder af fylde den tredje bil
For hver af de måder, er der $C(3, 3) = 1$ måde at fylde den sidste bil (resten sætter sig i den sidste bil)
Der er derfor:
$$
C(14, 4) \cdot C(10, 4) \cdot C(6, 3) \cdot C(3, 3) = 4.204.200
$$
Forskellige måder at fylde bilerne på.

# Exercise 4
## Find center and radius of convergence of the following series
### 1.
$$
\sum_{n=0}^\infty \frac{n^2}{(n+1)!}(z-1)^n
$$
Da series er en power series på formen:
$$
\sum_{n=0}^\infty a_{n}(z-z_{0})^n
$$
Kan centrum aflæses direkte af udtrykket til at være $z_{0}=1$
Radius kan findes ved Cauchy-Hadamard test af $a_n$:
$$
R = \frac{1}{L} = \lim_{ n \to \infty } \left| \frac{a_{n}}{a_{n+1}} \right| = \lim_{ n \to \infty } \left| \frac{\frac{n^2}{(n+1)!}}{\frac{(n+1)^2}{(n+2)!}} \right| = \lim_{ n \to \infty } \left| \frac{n^2}{(n+1)^2} \cdot \frac{(n+2)!}{(n+1)!} \right| = 1\cdot \infty
$$
Serien divergerer da Radius $\to \infty$

### 2.
$$
\sum_{n=1}^\infty \frac{e^{n-1}}{\sqrt{n}}(z-4)^{2n}
$$
Ved at tage kvadratroden, får vi den forventede form, og kan aflæse centrum $z_{0}=4$ samt $a_{n}$
$$
\sum_{n=1}^\infty \sqrt{\frac{e^{n-1}}{\sqrt{n}}}(z-4)^{n}
$$
$$
a_{n} = \sqrt{ \frac{e^{n-1}}{\sqrt{ n }} }
$$
Vi kan udføre Cauchy-Hadamard på det inderste udtryk først, så fremt vi tager kvadratroden til sidst:
$$
R^2 = \left(\frac{1}{L}\right)^2 = \lim_{ n \to \infty } \left| \frac{\frac{e^{n-1}}{\sqrt{n}}}{\frac{e^n}{\sqrt{ n+1 }}} \right| = \lim_{ n \to \infty } \left| \frac{e^{n-1}}{e^n} \cdot \frac{\sqrt{ n+1}}{\sqrt{n}} \right| = e^{-1} \cdot 1 = \frac{1}{e}
$$
Da hele $a_{n}$ skulle under en kvadratrod for at åbne den ønskede form, tages kvadratroden:
$$
R = \sqrt{ \frac{1}{e} } = \frac{1}{\sqrt{ e }}
$$
### 3.
$$
\sum_{n=0}^\infty \frac{(z+1)^n}{3^{n+1}}
$$
Denne series kan blot skrives på formen:
$$
\sum_{n=0}^\infty \frac{1}{3^{n+1}}(z+1)^n
$$
Hvor $z_{0}=-1$ og
$$
a_{n} = \frac{1}{3^{n+1}} = (3^{n+1})^{-1} = 3^{-n-1}
$$ 
Cauchy-Hadamard udføres på $a_{n}$:
$$
R = \frac{1}{L} = \lim_{ n \to \infty } \left| \frac{a_{n}}{a_{n+1}} \right| = \lim_{ n \to \infty } \left| \frac{3^{-n-1}}{3^{-(n+1)-1}} \right| = \lim_{ n \to \infty }  \left| \frac{3^{-n-1}}{3^{-n-2}} \right| = 3
$$
Serien har altså centrum i $z_{0}=-1$ og radius $R=3$


# Exercise 5
## Solve the following differential equations:
### 1.
$$
\frac{dy}{dx} -2x = xy, y(\sqrt{ 2 })=0
$$
Ligningen opstilles på formen:
$$
\frac{dy}{dx}+p(x)y=q(x)
$$
$$
\frac{dy}{dx} -xy = 2x
$$
Heraf får vi værdierne for $p(x)$ og $q(x)$:
$$
p(x) = -x \land q(x) = 2x
$$
$\mu(x)$ bestemmes, ved brug af formlen:
$$
\mu(x) = \int p(x)dx = \int -x dx = -\frac{1}{2}x^2 +C
$$
$y(x)$ kan nu bestemmes, ved hjælp af formlen:
$$
y(x) = e^{-\mu(x)} \int e^{\mu(x)}q(x)dx = e^{x^2/2} \int e^{-x^2/2}2x dx = e^{x^2/2}(-2e^{-1/2x^2} +C) = Ce^{x^2/2} -2
$$
Den ubestemte funktion for $y(x)$ er altså:
$$
y(x) = Ce^{x^2/2} - 2
$$
Den kendte værdi for $y(\sqrt{ 2 })$ indsættes:
$$
y(\sqrt{ 2 }) = Ce^{(\sqrt{ 2 })^2/2} - 2 = 0 \implies Ce - 2 = 0
$$
$$
\implies Ce = 2 \implies C=\frac{2}{e} = 2e^{-1}
$$
Indsættes værdien for $C$ i den ubestemte funktion, findes den bestemte funktion:
$$
y(x) = (2e^{-1})e^{x^2/2} - 2 =  2e^{(x^2/2) - 1} - 2
$$

### 2.
$$
\frac{d^2y}{dx^2} + \frac{dy}{dx} = 3, y(0) = 4, y'(0) = 1
$$
Først løses den tilsvarende homogene ligning:
$$
\frac{d^2y}{dx^2} + \frac{dy}{dx} = 0
$$
Her bruges diskriminantformlen:
$$
r = \frac{-b \pm \sqrt{b^2 -4ac}}{2a} = \frac{-1 \pm \sqrt{1^2 -4\cdot 1 \cdot 0}}{2 \cdot 1} = \frac{-1 \pm 1}{2}
$$
$$
r_{1} = 0 \land r_{2}=-1
$$
Disse værdier indsættes i udtrykket:
$$
y_{h}(x) = Ae^{r_{1}x} + Be^{r_{2}t} = Ae^0 + Be^{-x}
$$
Løsningen for den tilsvarende homogene ligning er altså:
$$
y_{h}(x) = A + Be^{-x}
$$
Nu kan vi lave et "gæt" på specifikke løsning. Da højresiden af ligningen er konstanten $3$, men der indgår en konstant i den homogene løsning gættes den simple lineære funktion:
$$
y_{p}(x) = Cx
$$
$$
y_{p}(x)' = C
$$
$$
y_{p}(x)'' = 0
$$
Indsættes dette i den originale ligning, finder vi:
$$
0 + C = 3
$$
Den specifikke løsning til ligningen er altså:
$$
y_{p}(x) = 3x
$$
Den generelle  ubestemte løsning på ligningen er altså:
$$
y(x) = y_{h}(x) + y_{p}(x) = A + Be^{-x} +3x
$$
For at finde den bestemte løsning, indsættes de kendte værdier for $y(0)$ og $y'(0)$:
$$
y(0) = A + B -3 = 4
$$
$$
y'(0) = -B +3 = 1
$$
Lignings systemet løses, og konstanterne bestemmes til:
$$
A= 5 \land B=2
$$
Disse værdier indsættes i den ubestemte løsning:
$$
y(x) = 5 + 2e^{-x} +3x = 2e^{-x} +3x + 5
$$
Den bestemte, generelle løsning til ligningen er altså:
$$
y(x) = 2e^{-x} +3x + 5
$$
Da der ikke indgår noget $y$ led i differentialligningen, bliver alle konstanter dog mistet når der differentieres, så $+5$ ledet kan være en arbitrær konstant, der ikke har noget indflydelse på, om ligningen går op:
$$
y(x) = 2e^{-x} +3x + C
$$
