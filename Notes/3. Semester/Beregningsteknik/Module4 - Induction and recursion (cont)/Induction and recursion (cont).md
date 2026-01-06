
## Strong induction
### Example: Prime factorization
Show that if n is an integer greater than 1, then n can be written as the product of primes.

P(n): n, n >= 1 can be written as a product of primes

Basis step

$P(1): \text{1 is a prime}$
$P(2): 2 = 2*1$

Inductive Hypthosis
$P(j):  \text{j can be written as a product of primes}, 1 \leq j \leq k$

$p(k) \to p(k+1)$


$k +1 = a \cdot b$
$1 \leq a \leq b < k+1$
Per inductive hypothosis:
a and b have a prime factorization

## Recursive definitions
To define an object (function, sequence, set, algorithm, structure) in terms of itself.
May be easier to write in some instances


$f(n) = 2f(n-1) +1, f(0) = 0$

Closed form
$f(n) = 2^n -2$

Inductive proof
Basis step $f(0) = 0$

Inductive hypothosis: $f(k) = 2^k +1$
Inductive step:
$P(k) \to P(k+1)$

Prove $f(k+1) = 2^{k+1}-1$

$$
f(k+1) = 2f(k) + 1 = 2 \cdot (2^{k-1}) + 1
$$
$$
= 2 \cdot 2^k - 2 +1 = 2^{k+1} -1
$$
