## Koefficientmatrix / Totalmatrix
Engelsk: Augmented matrix


$$
\begin{matrix}
2x_1 & - & x_2 & + & 5x_3 & - & x_4 & = & 6 \\
x_1 & & & - & x_3 & & & = & 4 \\
& & 3x_2 & + & 2x_3 & - & x_4 & = & 1 \\
-7x_1 & & & & & + & 2x_4 & = & -1 \\
\end{matrix}
$$
$\Downarrow$
$$
\begin{bmatrix}
2 & -1 & 5 & -1 & 6 \\
1 & 0 & -1 & 0 & 4 \\
0 & 3 & 2 & 0 & 1 \\
-7 & 0 & 0 & 2 & -1
\end{bmatrix}
$$

Totalmatrix inkluderer konstanten på højre side af lighedtegnet, koefficientmatrix gør ikke.


## Elementære rækkeoperationer
### Ombyt to rækker
$$
\begin{bmatrix}
2 & -1 & 5 & -1 & 6 \\
1 & 0 & -1 & 0 & 4 \\
0 & 3 & 2 & 0 & 1 \\
-7 & 0 & 0 & 2 & -1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & -1 & 0 & 4 \\
2 & -1 & 5 & -1 & 6 \\
0 & 3 & 2 & 0 & 1 \\
-7 & 0 & 0 & 2 & -1
\end{bmatrix}
$$

### Skalér en række med en konstant
Skal være forskellig fra 0
### Læg et multiplum af èn række til en anden række


## Trappeform
(El. række-echelonform)

$$
\begin{bmatrix}
\blacksquare & * & * & * & * & * & * \\
0 & 0 & \blacksquare & * & * & * & * \\
0 & 0 & 0 & \blacksquare & * & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & \blacksquare \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
$$
$\blacksquare$ er ikke-nul
$*$ er hvad som helst

### Ledende koefficient
(El. pivot-indgange)
Alle $\blacksquare$ i trappeformen, første koefficient efter 0


## Reduceret trappeform
$$
\begin{bmatrix}
1 & * & 0 & 0 & * & * & 0 \\
0 & 0 & 1 & 0 & * & * & 0 \\
0 & 0 & 0 & 1 & * & * & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
$$
Enhver matrix _A_ er rækkeækvivalent til én og kun én reduceret
trappematrix _R_.


### Frie variable
Værdierne markeret med $*$ i den reducerede trappeform
Dem i pivot (altså de ikke-frie) hedder basisvariable

## Inkonsistent
Betyder ingen løsninger. Forekommer altid hvis trappeformen har en pivot/ledenede koefficient i den sidste kolonne.

## Entydig løsning
Når der kun er én løsning. Forekommer hvis der ikke er nogle frie variable