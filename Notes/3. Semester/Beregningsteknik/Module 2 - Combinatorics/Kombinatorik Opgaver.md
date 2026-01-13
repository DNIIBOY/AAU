If $n$ is a positive integer and $r$ is an integer with $1\leq r\leq n$, the there are:
$$
P(n,r) = n(n-1)(n-2)\dots(n-r+1) = \frac{n!}{(n-r)!}
$$
$r$-permutations of a set with $n$ distinct elements

![[BIC_mm2.pdf#page=11&rect=30,326,684,423|BIC_mm2, p.11]]
$$
\frac{24!}{(24-3)!} = 24\cdot 23 \cdot 22 = 12144
$$
![[BIC_mm2.pdf#page=11&rect=33,220,673,306|BIC_mm2, p.11]]
Assuming no students are also faculty members, there are:
$$
250 + 50 = 300
$$
possible selections
![[BIC_mm2.pdf#page=11&rect=39,147,685,206|BIC_mm2, p.11]]

To find the number of bit strings of length 8 $(b_{7}b_{6}b_{5}​b_{4}​b_{3}​b_{2}​b_{1}​b_{0}​)$ that either start with 1 or end in 00, we use the **Principle of Inclusion-Exclusion**.

1. **Bit strings starting with 1 $(b_{7}=1)$:** The first bit is fixed as 1. The remaining 7 bits can be either 0 or 1.
$$
|A| = 2^7 = 128
$$
2. **Bit strings ending in 00 $(b_{1}=0,b_{0}​=0)$:** The last two bits are fixed as 0. The remaining 6 bits can be either 0 or 1.
$$
|B| = 2^6 = 64
$$
3. **Bit strings starting with 1 AND ending in 00 $(b7​=1,b1​=0,b0​=0)$:** Three bits are fixed $(b_{7}​,b_{1}​,b_{0}​)$. The remaining $8−3=5$ bits can be either 0 or 1.
$$
|A \cap B| = 2^5 = 32
$$
Using the Principle of Inclusion-Exclusion:
$$
|A \cup B| = |A|+|B| - |A \cap B| = 128 + 64 - 32 = 160
$$
There are **160** such bit strings.


![[exercises_mm2.pdf#page=1&rect=64,250,333,340|exercises_mm2, p.1]]
a) $4^{10} = 1.048.576$
b) $5^{10} = 9.765.625$

![[exercises_mm2.pdf#page=1&rect=65,221,330,243|exercises_mm2, p.1]]
Assuming capitalization doesn't matter, and using the english alfabet: 
$$
3^{26} = 2.541.865.828.329
$$
![[exercises_mm2.pdf#page=1&rect=64,187,326,217|exercises_mm2, p.1]]
A is locked, leaving all permutations of the remaining 6 values:
$$
P(6, 6) = 6! = 720
$$
![[exercises_mm2.pdf#page=1&rect=63,152,362,186|exercises_mm2, p.1]]
a)
$$
P(5,5)= 5! = 120
$$
b)
$$
a(n) = \sum_{k=1}^n k! \begin{Bmatrix} n\\k \end{Bmatrix}
$$
$$
a(n) = \sum_{i=1}^n \begin{pmatrix} n \\ i\end{pmatrix} a(n-i)
$$
$$
\begin{pmatrix}n\\k\end{pmatrix} = \frac{n!}{k!(n-k)!}
$$
$$
a(1) = \begin{pmatrix}1\\1\end{pmatrix} \cdot 1 = 1
$$
$$
a(2) = \begin{pmatrix}2\\1\end{pmatrix} \cdot a(1) + \begin{pmatrix}2\\2\end{pmatrix} \cdot a(0) = 2\cdot 1 + 1 \cdot 1 = 3
$$
$$
a(3) = \begin{pmatrix}3\\1\end{pmatrix} \cdot a(2) + \begin{pmatrix}3\\2\end{pmatrix} \cdot a(1) + \begin{pmatrix}3\\3\end{pmatrix}\cdot a(0) = 3\cdot 3 + 3 \cdot 1 + 1 \cdot 1 =9+3+1 = 13
$$
$$
a(4) = \begin{pmatrix}4\\1\end{pmatrix} \cdot a(3) + \begin{pmatrix}4\\2\end{pmatrix} \cdot a(2) + \begin{pmatrix}4\\3\end{pmatrix} \cdot a(1) + \begin{pmatrix}4\\4\end{pmatrix} \cdot a(0) = 4\cdot 13 + 6\cdot 3 + 4 \cdot 1 + 1 \cdot 1 = 75
$$
$$
a(5) = \begin{pmatrix}5\\1\end{pmatrix} \cdot a(4) + \begin{pmatrix}5\\2\end{pmatrix} \cdot a(3) + \begin{pmatrix}5\\3\end{pmatrix} \cdot a(2) + \begin{pmatrix}5\\4\end{pmatrix} \cdot a(1) + \begin{pmatrix}5\\5 \end{pmatrix} \cdot a(0)
$$
$$
a(5) = 5 \cdot 75 + 10 \cdot 13 + 10 \cdot 3 + 5 \cdot 1 + 1 \cdot 1 = \underline{\underline{541}}
$$

![[exercises_mm2.pdf#page=1&rect=55,73,270,148|exercises_mm2, p.1]]
a) Resten skal være 0, derfor er det antallet af kombinationer, hvor 4 værdier kan lægges i et sæt af 10:
$$
C(10, 4) = \begin{pmatrix}10\\4\end{pmatrix} = \frac{10!}{4!(10-4)!} = \frac{10\cdot 9 \cdot 8 \cdot 7 \cdot 6!}{4!\cdot 6!} = \frac{10\cdot 9 \cdot 8 \cdot 7}{4!} = \frac{5040}{24} = 210
$$
b)
$$
C(10,4) + C(10, 3) + C(10, 2) + C(10, 1) + C(10, 0) = 210 + 120 + 45 + 10 + 1 = 385
$$
c) 
$$
C(10,4) + C(10, 5) + C(10, 6) + C(10, 7) + C(10, 8) + C(10, 9) + C(10, 10)= 848
$$
d)
$$
C(10, 5) = 252
$$
![[exercises_mm2.pdf#page=2&rect=63,648,330,756|exercises_mm2, p.2]]
a) Hvis man betragter "BCD" som sit eget bogstav, kan man finde alle permutationer af $\{A, BCD, E, F, G\}$:
$$
P(5, 5) = 5! = 120
$$
b) Samme logik her, bare med mulighederne: $\{CFGA, B, D, E\}$
$$
P(4, 4) = 4! = 24
$$
c) Igen, vi betragter bare samlingerne som sine egne bogstaver: $\{BA, C, D, E, GF\}$
$$
P(5, 5) = 5! = 120
$$
d) Vi betragter permutationer af $\{ABCD, DE, F, G\}$
$$
P(4, 4) = 4! = 24
$$
d) For at både ABC og CDE kan eksistere på samme måde, skal det være på formen ABCDE, derfor bliver sættet: $\{ABCDE, F, G\}$, og der bliver:
$$
P(3,3) = 3! = 6
$$
f) CBA kan ikke stå på samme tid som BED, da der kun er ét B. Så der er 0 mulige permutationer


![[exercises_mm2.pdf#page=2&rect=63,581,334,635|exercises_mm2, p.2]]
Hvis M er en mand og X er en plads hvor der kan stå en kvinde, så er der disse muligheder:
XMXMXMXMXMXMXMXMX
Der er 9 x'er, og altså 9 pladser hvor der kan stå en kvinde. Det er derfor antallet af permutationer af 5 kvinder på 9 pladser, der er svaret:
$$
P(9, 5) = 9\cdot 8 \cdot 7\cdot 6 \cdot 5 = 15.120
$$
![[exercises_mm2.pdf#page=2&rect=59,514,335,574|exercises_mm2, p.2]]
$$
|A| = C(45, 3)
$$
$$
|B| = C(57, 4)
$$
$$
|C| = C(69, 5)
$$
$$
|A \cup B \cup C| = C(45, 3) + B(57, 4) + C(69, 5) = 11.647.713
$$
![[exercises_mm2.pdf#page=2&rect=60,482,218,505|exercises_mm2, p.2]]
$$
(x+y)^n = \sum_{k=0}^n \begin{pmatrix}n\\k\end{pmatrix}x^{n-k}y^k
$$
$$
\begin{pmatrix}6\\0\end{pmatrix}x^6y^0 + \begin{pmatrix}6\\1\end{pmatrix}x^5y^1 + \begin{pmatrix}6\\2\end{pmatrix}x^4y^2 + \begin{pmatrix}6\\3\end{pmatrix}x^3y^3 + \begin{pmatrix}6\\4\end{pmatrix}x^2y^4 + \begin{pmatrix}6\\5\end{pmatrix}x^1y^5 + \begin{pmatrix}6\\6\end{pmatrix}x^0y^6
$$
$$
= x^6 + 6x^5y + 15x^4y^2 + 20x^3y^3 + 15x^2y^4 + 6xy^5 + y^6
$$
![[exercises_mm2.pdf#page=2&rect=61,446,325,477|exercises_mm2, p.2]]
$$
P(26, 3) = 26 \cdot 25 \cdot 24 = 15.600
$$
![[exercises_mm2.pdf#page=2&rect=60,402,325,435|exercises_mm2, p.2]]
With exactly one repeated letter, two different letters must be chosen:
$$
P(26, 2) = 26\cdot 25 = 650
$$
Now we must choose which of the three positions in the initial that will have the unique letter:
$$
P(26,2)\cdot{3} = 1950
$$
![[exercises_mm2.pdf#page=2&rect=63,324,332,392|exercises_mm2, p.2]]
Hver stat har 3 muligheder, så der er $3^{50}$ muligheder.

![[exercises_mm2.pdf#page=2&rect=64,228,336,314|exercises_mm2, p.2]]
a) $2^{10}$
b) $C(10, 2) = 45$
c) $C(10, 3) + C(10, 2) + C(10, 1) + C(10, 0) = 176$
d) $C(10, 5) = 252$
