
# Opg 1
$$
y'' + 7y' + 10y = 0, y(0) = 4, y'(0) = 7
$$
a = 1, b = 7, c = 10

$$
\frac{-7\pm \sqrt{7^2-4*1*10}}{2*1}
$$

$D=9$
$r_{1} = -5$
$r_{2} = -2$

$$
y(x) = A \cdot e^{-5x} + B \cdot e^{-2x}
$$
$$
y'(x) = -5x \cdot A \cdot e^{-5x} -2 \cdot B \cdot e^{-2x}
$$
$$
y(0) = A \cdot e^{0} + B \cdot e^{0} = 4
$$
$$
A + B = 4
$$

$$
y'(0) = -5 \cdot A \cdot e^{0} -2 \cdot B \cdot e^{0} = 7
$$
$$
-5 A -2 B  = 7
$$

$$
-5 (4-B) -2 B  = 7 \implies -20 + 5B -2B =7 \implies 3B = 27 \implies B=9
$$


$$
y(x) = -5 \cdot e^{-5x} + 9 \cdot e^{-2x}
$$


# Opg 2

$$
y'' + 6y' + 10y = 0, y(0)=2, y'(0) = 2
$$
$a = 1, b = 6, c = 10$
$D=-4$
$$
r = -3 \pm i
$$
$$
y(x) = A\cdot e^{-3x} \cos(x) + B \cdot e^{-3x} \sin(x)
$$
$$
y'(x) = -3A e^{-3x}\cos(x) -A\cdot e^{-3x} \sin(x) + B \cdot e^{-3x} \cos(x) - 3Be^{-3x}\sin(x)
$$
$$
y(0) = A\cdot e^{0} \cos(0) + B \cdot e^{0} \sin(0) = 2
$$
$$
\implies A = 2
$$

$$
y'(0) = -3A e^{-3x}\cos(x) -A\cdot e^{-3x} \sin(x) + B \cdot e^{-3x} \cos(x) - 3Be^{-3x}\sin(x) = 2
$$
$$
\implies -3A + B = 2 \implies -6 + B =2 \implies B=8
$$

$$
2\cos(x)\cdot e^{-3x} + 8\sin(x)\cdot e^{-3x}
$$


# Opg 3
$$
y''+y'-2y = 1
$$
Først løser man den tilsvarende homogene:

$$
y''+y'-2y = 0
$$
$r_{1} =1 \land r_{2} =-2$
$$
y = Ae^{x} + Be^{2x}
$$
Da højre side er en konstant, sætter vi $y_p = A$, og får:
$$
0+0-2A=1 \implies A= -\frac{1}{2}
$$
Dermed er den partikulære løsning: $y_{p} = -\frac{1}{2}$
Den generelle løsning er summen af den homogene og den partikulære:
$$
y = Ae^{x}+Be^{2x} -\frac{1}{2}
$$

# Opg 4
$$
y'' + 2y' +2y = e^x\sin(x)
$$
Først løses den tilsvarende homogene:
$r = -1 \pm i$
$$
y = Ae^{-x}\cos(x)+Be^{-x}\sin(x)
$$
Baseret på tabellen gætter vi:

$$
y_{p} = e^{x}(A \cos(x) + B \sin(x))
$$
$$
y_{p}' = A\cos(x)e^x+B\sin(x)e^x + B\cos(x)e^x-A\sin(x)e^x
$$
$$
= Ae^x(\cos(x) - \sin(x)) + Be^x(\cos(x)+\sin(x))
$$
$$
y_{p}'' = 2B\cos(x)e^x-2A\sin(x)e^x
$$
Indsat i det originale udtryk:
$$
2B\cos(x)e^x-2A\sin(x)e^x + 2(A\cos(x)e^x+B\sin(x)e^x + B\cos(x)e^x-A\sin(x)e^x)
$$
$$
 + 2(Ae^{-x}\cos(x)+Be^{-x}\sin(x)) = e^x\sin(x)
$$
$$
= e^x(4A + 4B)\cos(x) + e^x(4B-4A)\sin(x)
$$
$$
\implies(4A + 4B)\cos(x) + (4B-4A)\sin(x) = \sin(x)
$$
$$
4A + 4B = 0, 4B-4A = 1 \implies A=-\frac{1}{8} \land B=\frac{1}{8}
$$
Specifik løsning:
$$
y_{p} = -\frac{1}{8}\cos(x) + \frac{1}{8}\sin(x)
$$
General løsning:
$$
y = Ae^{-x}\cos(x)+Be^{-x}\sin(x) - \frac{1}{8} e^x\cos(x) + \frac{1}{8}e^x\sin(x)
$$