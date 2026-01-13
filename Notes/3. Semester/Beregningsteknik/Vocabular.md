
| Begreb (Engelsk)      | Begreb (Dansk)     | Forklaring                                                                                                                 |
| --------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Proposition           | Udsagn             | Proposition is a declarative statement – something that declares a fact - which can be either true or false, but not both. |
| Compound propositions | Sammensatte udsagn | Sammensætning af flere udsagn, sammensat af operationer som AND og OR                                                      |
| Negation              |                    | "Det modsatte" (NOT)                                                                                                       |
| Conjunction           |                    | AND                                                                                                                        |
| Disjunction           |                    | OR                                                                                                                         |
| Exclusive Disjunction |                    | XOR                                                                                                                        |
| Implication<br>       | Implikation        | p -> q, "if p then q"                                                                                                      |
|                       |                    |                                                                                                                            |

## Logiske definitioner

| Operator      | Notation              | Primitive definition                     |
| ------------- | --------------------- | ---------------------------------------- |
| Implication   | $p \to q$             | $\neg p \lor q$                          |
| Biconditional | $p \leftrightarrow q$ | $(p \land q) \lor (\neg p \land \neg q)$ |
| XOR           | $p \oplus q$          | $(p \land \neg q) \lor (\neg p \land q)$ |
| NAND          | $p \uparrow q$        | $\neg(p \land q)$                        |
| NOR           | $p \downarrow q$      | $\neg (p \lor q)$                        |


# Gode gæt til 2nd order DE

| Right-hand f(x)                      | Trial $y_p$                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------- |
| $e^{rx}$                             | $Ae^{rx}$                                                                       |
| $\sin(\omega x)$ OR $\cos(\omega x)$ | $A\cos(\omega x)+B\sin(\omega x)$                                               |
| $x^n$                                | $A_n x^n + A_{n-1} x^{n-1} + \dots + A_{1}x + A_{0}$                            |
| $e^{rx} \sin(\omega x)$              | $e^{rx}(A \cos(\omega x) + B \sin(\omega x))$                                   |
| $x^n e^{rx}$                         | $(A_n x^n + \dots + A_{0})e^{rx}$                                               |
| $x^n \sin(\omega x)$                 | $(A_n x^n + ... + A_{0})\cos(\omega x) + (B_n x^n + ... + B_{0})\sin(\omega x)$ |
| $n\cdot x$                           | $Ax + B$                                                                        |
|                                      |                                                                                 |
###  Special Case - Resonance!

CRITICAL: If your trial solution overlaps with the complementary solution y_c, you must multiply by x (or x² if needed).
Check for your problem:

    y_c = e^(-x)[C₁cos(x) + C₂sin(x)] (has e^(-x))
    y_p trial = e^x[A cos(x) + B sin(x)] (has e^x)

Different exponents (-x vs x), so NO overlap ✓

Your original guess is correct as-is!
Example of Resonance:

If the equation were y'' + 2y' + 2y = sin(x)e^(-x), then:

    The trial would normally be e^(-x)[A cos(x) + B sin(x)]
    But this IS in y_c!
    So multiply by x: y_p = x·e^(-x)[A cos(x) + B sin(x)]


# Standard Maclaurin serier:

| Function        | Maclaurin                                   | General n-th term                                  |
| --------------- | ------------------------------------------- | -------------------------------------------------- |
| $e^z$           | $1+z+\frac{z^2}{2!}+\frac{z^3}{3!} +\dots$  | $\sum_{n=0}^\infty \frac{z^n}{n!}$                 |
| $\sin(z)$       | $z-\frac{z^3}{3!} + \frac{z^5}{5!} - \dots$ | $\sum_{n=0}^\infty \frac{(-1)^nz^{2n+1}}{(2n+1)!}$ |
| $\cos(z)$       | $1-\frac{z^2}{2!}+\frac{z^4}{4!}-\dots$     | $\sum_{n=0}^\infty \frac{(-1)^nz^{2n}}{(2n)!}$     |
| $\frac{1}{1-z}$ | $1+z+z^2+z^3+\dots$                         | $\sum_{n=0}^\infty z^n$                            |
