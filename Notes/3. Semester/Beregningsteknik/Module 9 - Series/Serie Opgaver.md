# 1.
$$
\sin(2z^2)
$$
$$
\sin(\omega) = \sum_{n=0}^\infty \frac{(-1)^n\omega^{2n+1}}{(2n+1)!}
$$
$$
\omega=2z^2
$$
$$
\sin(2z^2) = \sum_{n=0}^\infty \frac{(-1)^n(2z^2)^{2n+1}}{(2n+1)!} = \sum_{n=0}^\infty \frac{(-1)^n2^{2n+1}(z^2)^{2n+1}}{(2n+1)!} = \sum_{n=0}^\infty \frac{(-1)^n2^{2n+1}z^{4n+2}}{(2n+1)!}
$$
$$
2z^2 - \frac{8z^{6}}{6} + \frac{32z^{10}}{120} - \frac{128z^{14}}{5040} + \dots
$$
# 2.
Maclaurin series for:
$$
\frac{1}{2+z^4}
$$
Start with defined series for:
$$
\frac{1}{1-\omega} = \sum_{n=0}^\infty = \omega^n
$$
Rewrite the express to be in the geometric form:
$$
\frac{1}{2\left( 1+\frac{z^4}{2} \right)} = \frac{1}{2} \cdot \frac{1}{1-\left( -\frac{z^4}{2} \right)}
$$
Place the new term in the geometric series:
$$
\frac{1}{2+z^4} = \frac{1}{2}\sum_{n=0}^\infty \left(-\frac{z^4}{2}\right)^n = \frac{1}{2}\sum_{n=0}^\infty \frac{(-1)^nz^{4n}}{2^n} = \sum_{n=0}^\infty \frac{(-1)^nz^{4n}}{2^{n+1}}
$$
$$
\frac{1}{2} - \frac{z^4}{4} + \frac{z^{8}}{8} - \frac{z^{12}}{16} + \dots
$$
With the constraint:
$$
\left|-\frac{z^4}{2}\right| < 1 \implies -z^4 < 2 \implies |z| < \sqrt[4]{2}
$$

# 3.
$$
\frac{1}{1+5iz}
$$
Rewritten is a geometric series:
$$
\frac{1}{1-(-5iz)}
$$
Placed in the geometric maclaurin series:
$$
\frac{1}{1+5iz} = \sum_{n=0}^\infty (-5iz)^n
$$
The first 4 terms:
$$
1 - 5iz - 25z^2 + 125iz^3 + \dots
$$
With the constraint:
$$
|-5iz| < 1 \implies |-5||i||z| < 1 \implies |z| < \frac{1}{5}
$$

# 4.
$$
\cos^2\left( \frac{z}{2} \right)
$$
Fucking freaky regel:
$$
\cos^2(\theta) = \frac{1+\cos(2\theta)}{2}
$$
$$
\sin^2(\theta) = \frac{1-\cos(2\theta)}{2}
$$
Hvis vi sætter $\frac{z}{2} = \theta$, får vi:
$$
\cos^2\left( \frac{z}{2} \right) = \frac{1}{2} + \frac{1}{2} \cos(z)
$$
$$
\cos^2\left( \frac{z}{2} \right) = \frac{1}{2} + \frac{1}{2} \sum_{n=0}^\infty \frac{(-1)^nz^{2n}}{(2n)!} = \frac{1}{2} + \sum_{n=0}^\infty \frac{(-1)^nz^{2n}}{2(2n!)}
$$
Første 4 værdier:
$$
1 - \frac{z^{2}}{4} + \frac{z^{4}}{48} - \frac{z^{6}}{1440} + \dots
$$
# 5. 
$$
\sin^2(z)
$$
Vi kender definitionen:
$$
\sin^2(\theta) = \frac{1-\cos(2\theta)}{2}
$$
Så vi kan opstille dette udtryk for $\sin^2(z)$
$$
\sin^2(z) = \frac{1}{2} - \frac{1}{2}\cos(2z)
$$
Hvis vi sætter $\omega = 2z$, kan det generelle udtryk for $\cos(\omega)$ bruges:
$$
\cos(\omega) = \sum_{n=0}^\infty \frac{(-1)^n\omega^{2n}}{(2n)!}
$$
$$
\cos(2z) = \sum_{n=0}^\infty \frac{(-1)^n(2z)^{2n}}{(2n)!}
$$
Dette udtryk kan indsættes i det tidligere udtryk for $\sin^2(z)$:
$$
\sin^2(z) = \frac{1}{2} - \frac{1}{2}\sum_{n=0}^\infty \frac{(-1)^n(2z)^{2n}}{(2n)!} = \frac{1}{2} + \sum_{n=0}^\infty \frac{(-1)^{n+1}(2z)^{2n}}{2((2n)!)}
$$
De første værdier findes:
$$
z^2 - \frac{z^4}{3} + \frac{2z^6}{45} - \dots
$$
