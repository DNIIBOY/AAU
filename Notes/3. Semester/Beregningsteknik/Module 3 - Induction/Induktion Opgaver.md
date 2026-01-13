# Opg 3
![[Exercises_mm3a.pdf#page=1&rect=61,472,334,666|Exercises_mm3a, p.1]]

## a)
$$
P(1) = 1^2 = \frac{1(1+1)(2\cdot 1+1)}{6}
$$
## b)
$$
P(1) = 1^2 = \frac{1(1+1)(2\cdot 1+1)}{6} = \frac{6}{6} = 1
$$
## c)
Induktive hypotese er at det gælder for et vilkårligt positivt heltal:
$$
P(k) = 1^2 + 2^2 + \dots + k^2 = \frac{k(k+1)(2k+1)}{6}
$$
## d)
For at bevise det induktive step skal vi bruge hypotesen og et "target" (k+1)
## e)
$$
P(k+1) = 1^2 + 2^2 + \dots + k^2 + (k+1)^2 = \frac{(k+1)((k+1)+1)(2(k+1)+1)}{6}
$$
$$
= \frac{(k+1)(k+2)(2k+3)}{6}
$$

Vi kan substituere med den induktive hypotese:
$$
P(k+1) = \frac{k(k+1)(2k+1)}{6}+(k+1)^2 = \frac{k(k+1)(2k+1)+6(k+1)^2}{6}
$$
$$
P(k+1) = \frac{(k+1)(k(2k+1)+6(k+1))}{6} = \frac{(k+1)(2k^2+7k+6))}{6}
$$
$$
P(k+1) = \frac{(k+1)(2k^2+7k+6))}{6} = \frac{(k+1)(k+2)(2k+3)}{6}
$$
Her ses det at udtrykket er magen til det vi fik i det induktive step, hypotesen holder derfor

## f)
Da vi starter ved det mindste positive heltal, og beviser at hypotesen altid holder når man går opad med en, vises det at udtrykket holder for alle positive heltal

# Opg 9
![[Exercises_mm3a.pdf#page=1&rect=62,424,325,469|Exercises_mm3a, p.1]]

## a)
$$
P(n) = 2 + 4 + \dots + 2n = n(n+1)
$$

## b)
Base step:
$$
P(1) = 2 = 1(1+1) = 2
$$
The method works for the first positive integer
I.H:
The hypothesis is that it works for any given positive integer
$$
P(k) = 2 + 4 + \dots + 2k = k(k+1)
$$

Inductive step:
$$
P(k+1) = 2 + 4 + \dots + 2k + 2(k+1) = (k+1)((k+1)+1) = (k+1)(k+2)
$$
Now we use the inductive hypothesis:
$$
P(k+1) = k(k+1) + 2(k+1) = (k+1)(k +2)
$$
Which gives the same answer, thereby proving the formula.

# Opg 19
![[Exercises_mm3a.pdf#page=1&rect=60,236,345,418|Exercises_mm3a, p.1]]

## a)
$$
P(2) = 1 + \frac{1}{4} < 2 - \frac{1}{2}
$$
## b)
$$
P(2) = 1 + \frac{1}{4} < 2 - \frac{1}{2} \implies 1.25 < 1.5 = TRUE
$$
## c)
$$
P(k) = 1 + \frac{1}{4} + \frac{1}{9} \dots + \frac{1}{k^2} < 2 - \frac{1}{k}
$$
## e)
We want to prove that:
$$
P(k+1) = 1 + \frac{1}{4} + \frac{1}{9} + \dots + \frac{1}{k^2} + \frac{1}{(k+1)^2} < 2 - \frac{1}{k+1}
$$
Using the hypothesis, we can add $\frac{1}{(k+1)^2}$ to both sides, to get $P(k+1)$:
$$
P(k+1) = 1 + \frac{1}{4} + \frac{1}{9} \dots + \frac{1}{k^2} + \frac{1}{(k+1)^2} < 2 - \frac{1}{k} + \frac{1}{(k+1)^2}
$$
To complete the proof, the following must be true:
$$
2- \frac{1}{k} + \frac{1}{(k+1)^2} \leq 2 - \frac{1}{k+1}
$$
$$
\implies -\frac{1}{k} + \frac{1}{(k+1)^2} \leq -\frac{1}{k+1} \implies \frac{1}{(k+1)^2} \leq \frac{1}{k}-\frac{1}{k+1} \implies \frac{1}{(k+1)^2} \leq \frac{(k+1)-k}{k(k+1)}
$$
$$
\implies \frac{1}{(k+1)^2} \leq \frac{1}{k^2+k}
$$
Which is true if:
$$
(k+1)^2 \geq k^2 +k \implies k^2+1+2k \geq k^2+k \implies k+1 \geq 0 \implies k\geq-1
$$
Da hypotesen kun gælder for heltal større end 1, kan det siges at hypotesen holder, og 


# Chat opgave
$$
P(n): n! > 2^n, n\geq 4
$$
Base case:
$$
P(4): 4! > 2^4 = 24 > 16 = TRUE
$$
Hypothesis:
For an arbitrary $k \geq 4$ 
$$
P(k): k! > 2^k
$$
We want to prove:
$$
P(k+1): (k+1)! > 2^{k+1}
$$
Using the inductive hypothesis:
$$
k! > 2^k \implies (k+1)k! > (k+1)2^k \implies (k+1)! > (k+1)2^k
$$
If we prove $(k+1)2^k > 2^{k+1}, k\geq 4$, the proof works
We know that $2^{k+1} = 2\cdot2^k$, so for the proof to work, the following must be true:
$$
k+1>2 \implies k>1
$$
Which is always true for $k\geq4$

Since the base case $P(4)$ is true and the inductive step $P(k)⟹P(k+1)$ holds for $k\geq4$, by the Principle of Mathematical Induction, $n! > 2n$ is true for all integers $n\geq4$.


## Chat part 2
For all integers $n \geq 5$
$$
P(n): 2^n > n^2
$$
Base case:
$$
P(5): 2^5 > 5^2 = 32 > 25 = TRUE
$$
Hypothesis:
For an arbitrary $k\geq 5$ the following is true:
$$
P(k): 2^k > k^2
$$
We want to prove that:
$$
P(k+1): 2^{k+1} > (k+1)^2
$$
Using the inductive hypothesis, we can say that:
$$
2 \cdot 2^k > 2k^2 \implies 2^{k+1} > 2k^2
$$
Therefore, proving $2k^2 > (k+1)^2, k\geq 5$, would prove the statement.
$$
2k^2 > k^2 +1 +2k \implies k^2 > 1 +2k \implies k^2 -2k -1 > 0
$$
Which is true for all values $k \geq 1+\sqrt{2}$, which includes all values $k\geq 5$

Since the base case $P(5)$ is true and the inductive step $P(k)⟹P(k+1)$ holds for $k\geq 5$, by the Principle of Mathematical Induction, $2^n > n^2$ is true for all integers $n\geq5$.