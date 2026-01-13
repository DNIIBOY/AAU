
# Opg 1 - 2025 Eksamen
Show that the biconditional statement $p\leftrightarrow q$ is logically equivalent to the negation of the exclusive disjunction ("exclusive OR"), i.e. $p\leftrightarrow q \equiv \neg(p \oplus q)$:

We can also look at this through the lens of Boolean definitions:
1. XOR is defined as $p\oplus q \equiv (p\land \neg q) \lor (\neg p \land q)$
2. Negating it gets us: $\neg(p\oplus q) \equiv \neg((p\land \neg q) \lor (\neg p \land q))$ 
3. Using De Morgan: $\equiv \neg (p \land \neg q) \lor \neg(p \land q)$
4. Again: $\equiv (\neg p \lor q) \lor (p  \lor \neg q)$


	
5. Applying **De Morgan's Laws**: ≡¬(p∧¬q)∧¬(¬p∧q)
    
6. Applying De Morgan's again: ≡(¬p∨q)∧(p∨¬q)
    
7. This is the standard expansion for the **Biconditional** (p→q)∧(q→p), which is p↔q


# Opg 2
## $z^2 = -4z +2i -4, z \in C$

### a)
Først skrives den på standardform:

$$
z^2 +4z + (4 - 2i) = 0
$$
Diskriminant:
$$
D= \sqrt{ b^2 -4ac } = \sqrt{ 4^2-4\cdot 1 \cdot (4-2i) } = \sqrt{8i}
$$
Da $D\neq 0$ er der 2 unikke løsninger til ligningen.

### b)
$$
(x+yi)^2 = 8i \implies x^2 -y^2 + 2xyi = 8i
$$
Dette kan deles op i den imaginære og reele del:
$$
x^2+y^2=0
$$
$$
2xy = 8
$$
$$
\sqrt{ 8i } = \pm(2 + 2i)
$$
$$
z_{1} = \frac{-4+(2+2i)}{2} = \frac{-2+2i}{2} = -1+i
$$
$$
z_{2} = \frac{-4-(2+2i)}{2} = \frac{-6-2i}{2} = -3-i
$$
Polær form:
$$
r_{1} = |z_{1}| = \sqrt{ (-1)^2 + 1^2 } = \sqrt{2}
$$
$$
\theta_{1} = \arctan\left( \frac{1}{1} \right) + \frac{\pi}{2} = \frac{\pi}{4} + \frac{2\pi}{4} = \frac{3\pi}{4}
$$
$$
r_{2} = |z_{2}| = \sqrt{ (-3)^2 + (-1)^2 } = \sqrt{ 10 }
$$
$$
\theta_{2} = \arctan\left( \frac{1}{3} \right) + \pi \approx 3.46 rad
$$


### c)
Indtegnet er punkterne (-1, 1) og (-3, -1), som passer til de to løsninger $z_{1}$ og $z_{2}$
![[Pasted image 20260107185551.png]]
# Opg 3
### 1. Should we count combinations or permutations?

In this scenario, we should count **combinations**.

**The Motivation:** The problem specifies that from a client's perspective, the connections "look all the same." This implies that the clients themselves are **indistinguishable** for the purpose of this count. If Client 1 is on Server A and Client 2 is on Server B, it is considered the same "way" or state as Client 2 being on Server A and Client 1 on Server B.

Furthermore, since the question asks how we can connect the clients to the servers (rather than how the servers see the clients), we are looking for the number of unique distributions of "load" across the server set. In combinatorics, when the items being placed (clients) are identical, we use combinations.

#### Case 1: The clients are on different servers

We choose 2 servers out of the 5 available. Since the clients are identical, the order doesn't matter.

$$
\begin{pmatrix} 5\\2 \end{pmatrix} = \frac{5 \cdot 4}{2\cdot 1} = 10
$$
#### Case 2: Both clients are on the same server

The only server that can accommodate more than one client is **Server C**.

- There is only **1 way** to do this (both clients on C).

So there are 11 ways

### Recalculating with Distinguishable Clients (Unique Clients, Identical Ports)

If the clients are unique (Client 1 and Client 2) but Server C's internal slots are identical, we evaluate the possibilities like this:

#### 1. Clients on Different Servers

We pick 2 different servers from the 5 available.

- There are (25​)=10 pairs of servers.
    
- Since the clients are distinguishable, each pair (e.g., A and B) can happen in **2 ways** (C1 on A, C2 on B OR C2 on A, C1 on B).
    
- 10×2=20 ways
    

#### 2. Both Clients on Server C

Since Server C can handle two connections, both clients can be there at once.

- Because the "slots" on Server C are indistinguishable, there is only **1 way** for this to happen: both are simply "on Server C."
    
- Unlike the "different server" case, swapping them doesn't create a new state because they are both in the same place.
    
- Total = 1 way

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