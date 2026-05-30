## Problem 1.1  
Let $S = 1, 2, 3, 4, 5, 6, 7$, $E = 1, 3, 5, 7$, $F = 7, 4, 6$, $G = 1, 4.$ Find
### (a) $EF$
$\{7\}$
### (b) $E \cup FG$
$FG = \{4\}$
$E \cup FG = \{1, 3, 4, 5, 7\}$
### (c) $EG^c$
$\{3, 5, 7\}$
### (d) $EF^c \cup G$
$EF^c = \{1, 3, 5\}$
$EF^c \cup G = \{1, 3, 4, 5\}$
### (e) $E^c(F \cup G)$
$F \cup G = \{1, 4, 6, 7\}$
$E^c(F \cup G) = \{4, 6\}$
### (f ) $EG \cup FG$
$EG = \{1\}$
$FG = \{4\}$
$EG \cup FG = \{1, 4\}$

## Problem 1.2
10 books are randomly placed on a shelf. 
### (a) How many distinct sequences of books are possible?
$10!$
### (b) How many distinct sequences of books are possible, if we know that two particular books of those ten books are placed next to each other?
$9! \cdot 2$


## Problem 1.3

### Show that the probability that exactly one of the events E or F occurs is equal to $P(E) + P(F ) − 2P(EF)$.

$P(\text{One or the other, not both}) = P((E \cup F)\backslash(E\cap F))$
$= (P(E) + P(F) - P(E\cap F)) - P(E\cap F)$
$= P(E) + P(F) - 2P(EF) QED$


## Problem 1.4
A transmitter can send two messages A and B. Message A is sent with probability 0.84 and message B is sent with probability 0.16. Due to transmission errors, 1/6 of all sent messages of type A are received as message of type B. 1/8 of all sent messages of type B are received as message of type A.
### (a) Find the probability that message A is received
$P(A_{r}) = P(A_{r}|A_{t}) \cdot P(A_{t}) + P(A_{r}|B_{t}) * P(B_{t}) = 0.84 \cdot \frac{5}{6} + 0.16 \cdot \frac{1}{8} = 0.72$
### (b) Find the probability that message B is received
$P(B_{r}) = P(B_{r}|A_{t}) \cdot P(A_{t}) + P(B_{r}|B_{t}) * P(B_{t}) = 0.84 \cdot \frac{1}{6} + 0.16 \cdot \frac{7}{8} = 0.28$
### (C) Message A is received. Find the probability that message A was sent.
Using Bayes' Law:
$$P(A_{t}|A_{r}) = \frac{P(A_{t}|A_{r})}{P(A_{r})} = \frac{P(A_{r}|A_{t})P(A_{t})}{P(A_{r}|A_{t})P(A_{t})+P(A_{r}|B_{t})P(B_{t})}=$$
$$
\frac{\frac{5}{6}\cdot0.84}{\frac{5}{6}\cdot 0.84+\frac{1}{8}*0.16} = \frac{0.7}{0.72} = 0.972 = 97.2\%
$$

## Problem 1.5
Show that 
$$
\begin{pmatrix}n\\r\end{pmatrix} = 
\begin{pmatrix}n \\ n-r\end{pmatrix}
$$
Now present a combinatorial argument for the foregoing by explaining why a choice of r items from a set of n is equivalent to a choice of n − r items from the set.

Picking r items out of n, leaves n-r items leftover, and picking r items has the same probability as not picking r items.



## Problem 1.6
A basket contains 40 transistors: 5 of them are defective (= immediately fail when put in use); 10 are partially defective (fail after a couple of hours of use) and 25 are well functioning transistors. A transistor is chosen at random and put in use. If it does not fail immediately, what is the probability that it is acceptable?

$$
\frac{25}{35} = \frac{5}{7} \approx 71.4\%
$$

## Problem 1.10
A patient in a hospital is suspected to have one of two diseases: disease H1 or disease H2. From statistical observations we know that the probability that he has the first disease is P (H1) = 0.6 and the probability that he has the second disease is P (H2) = 0.4. A blood test can be taken that can show either positive or negative reaction. In case of the first disease the probability of positive reaction is 0.9 and the probability of negative reaction is 0.1. In case of the second disease the test will show equally likely positive and negative reaction. The test was conducted twice and in both cases the reaction was positive. Find the probability that the patient has disease H1 and the probability that he has disease H2 using the knowledge about the test results.

$$
\begin{matrix}
P(+|H_{1}) = 0.9 \\
P(++|H_{1}) = 0.9^2 = 0.81
\end{matrix}
$$
$$
\begin{matrix}
P(+|H_{2}) = 0.5 \\
P(++|H_{2}) = 0.25
\end{matrix}
$$
Total probability of $P(++)$:
$$
P(++) = P(++|H_{1})(P(H_{1}))+P(++|H_{2})P(H_{2}) = 0.81\cdot 0.6 + 0.25 \cdot 0.4 = 0.586
$$

$$
P(H_{1}|++) = \frac{P(++|H_{1})P(H_{1})}{0.586} = \frac{0.81\cdot0.6}{0.586} \approx 82.9\%
$$

$$
P(H_{2}|++) = \frac{P(++|H_{2})P(H_{2})}{0.586} = \frac{0.25\cdot0.4}{0.586} \approx 17.1\% 
$$
## Problem 1.11
A student is doing a multiple choice test and answers a question with n choices. If he knows the answers, he gives a correct answer; if he does not know the answer, he chooses of the option at random. Let assume that p is the probability that the student knows the answer.

A is student knows answer, C is correct
### (a) What is probability that the question is answered correctly?
$$
P(C) = P(A) + P(C|A^c)P(A^c) = p+ \frac{1}{n} \cdot (1-p) = p + \frac{1-p}{n}
$$
### (b) Given the provided answer is correct, what is the probability that the student was guessing?
$$
P(A|C) = \frac{P(C|A)P(A)}{P(C)} = \frac{p}{p+\frac{1-p}{n}} = \frac{np}{np+1-p}
$$
$$
P(A^c|C) = \frac{P(C|A^c)P(A^c)}{P(C)} = \frac{\frac{1-p}{n}}{p+\frac{1-p}{n}} = \frac{1-p}{np+1-p}
$$