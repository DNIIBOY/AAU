
| Begreb (Engelsk)      | Begreb (Dansk)     | Forklaring                                                                                                                 |
| --------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Proposition           | Udsagn             | Proposition is a declarative statement – something that declares a fact - which can be either true or false, but not both. |
| Compound propositions | Sammensatte udsagn | Sammensætning af flere udsagn, sammensat af operationer som AND og OR                                                      |
| Negation              |                    | "Det modsatte" (NOT)                                                                                                       |
| Conjunction           |                    | AND                                                                                                                        |
| Disjunction           |                    | OR                                                                                                                         |
| Exclusive Disjunction |                    | XOR                                                                                                                        |
| Implication           | Implikation        | p -> q, "if p then q"                                                                                                      |


| Right-hand f(x)                      | Trial $y_p$                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------- |
| $e^{rx}$                             | $Ae^{rx}$                                                                       |
| $\sin(\omega x)$ OR $\cos(\omega x)$ | $A\cos(\omega x)+B\sin(\omega x)$                                               |
| $x^n$                                | $A_n x^n + A_{n-1} x^{n-1} + \dots + A_{1}x + A_{0}$                            |
| $e^{rx} \sin(\omega x)$              | $e^{rx}(A \cos(\omega x) + B \sin(\omega x))$                                   |
| $x^n e^{rx}$                         | $(A_n x^n + \dots + A_{0})e^{rx}$                                               |
| $x^n \sin(\omega x)$                 | $(A_n x^n + ... + A_{0})\cos(\omega x) + (B_n x^n + ... + B_{0})\sin(\omega x)$ |
| $n\cdot x$                           | $Ax + B$                                                                        |
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
