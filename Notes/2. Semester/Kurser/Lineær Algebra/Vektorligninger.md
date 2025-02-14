## Søjlevektor/rækkevektor
* $n \times 1$ matrix hedder en søjlevektor
* $1 \times n$ matrix hedder en rækkevektor

### Søjlevektor:
$$
\begin{bmatrix}
a \\
b \\
c \\
\end{bmatrix}
$$
### Rækkevektor:
$$
\begin{bmatrix}
a & b & c \\
\end{bmatrix}
$$


## Rum af vektorer
Deadass det er bare længden

$\mathbb{R}²$: Plannet
$\mathbb{R}³$: Rummet

## Vektoraddition
$u + v$ er summen af hver ting
$$
\begin{bmatrix}
u_{1} + v_{1} \\
u_{2} + v_{2}
\end{bmatrix}
$$
## Skalar
$u * c$ hver ting i u ganges med c
$$
\begin{bmatrix}
u_{1} * c \\
u_{2} * c
\end{bmatrix}
$$


## Linearkombination
$y = c_{1}v_{1} + c_{2}v_{2}$ 

$$ 
u = \begin{bmatrix}
1 \\
2
\end{bmatrix},
v = \begin{bmatrix}
5 \\
4
\end{bmatrix}
$$

$$
5u + 2v =
\begin{bmatrix}
1*5 + 2*5 \\
5*2 + 2*4
\end{bmatrix}
$$

## Vektorspænd
Alle linearkombinationer man kan lave, altså ved at betragte alle værdier for $c_{1}, c_{2}$ osv.
Ofte hele planet, eller rummet, med mindre vektorerne er ens.

### Ligger en vektor i spændet?
$$
b = \begin{bmatrix}
9 \\
8
\end{bmatrix}
\in Span \begin{Bmatrix}
\begin{bmatrix}
1 \\
2 \\
\end{bmatrix},
 & \begin{bmatrix}
6 \\
7
\end{bmatrix}
\end{Bmatrix}?
$$
$1c_{1} + 6c_{2} = 9$
$2c_{1} + 7c_{2} = 8$

$$
\begin{bmatrix}
1 & 6 & 9 \\
2 & 7 & 8
\end{bmatrix}
$$
Bare opstil dem sådan her og lav 2 med 2 bekendte

### Hvilke vektorer ligger i spændet?
![[Pasted image 20250213131705.png]]

$$
\begin{bmatrix}
v_{1} & v_{2} & v_{3} & b \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 2 & 2 & b_{1} \\
4 & 8 & 3 & b_{2} \\
3 & 6 & 1 & b_{3}
\end{bmatrix}
\tilde{}
\begin{bmatrix}
1 & 2 & 2 & b_{1} \\
0 & 0 & 5 & 4b_{1}-b_{2} \\
0 & 0 & 0 & b_{1} -b_{2}+b_{3}
\end{bmatrix}
$$
B ligger i så i spændet, hvis der ikke er pivot i sidste, altså $b_{1}-b_{2}+b_{3} = 0$


## Matrix-vektor-produkt
Kun hvis v har lige så mange rækker som A har søjler

$Av=v_{1}a_{1}+v_{2}a_{2}+\dots+v_{n}a_{n}$

$$
\begin{bmatrix}
4 & 1 & -1 & 0 \\
7 & 0 & 3 & 2 &  \\
6 & -2 & -3 & 2
\end{bmatrix}
\begin{bmatrix}
1 \\
2 \\
0 \\
-1
\end{bmatrix}
= 1 \begin{bmatrix}
4 \\
7 \\
6
\end{bmatrix}
+ 2\begin{bmatrix}
1 \\
0 \\
-2
\end{bmatrix}
+ 0 \begin{bmatrix}
-1 \\
3 \\
-3
\end{bmatrix}
+ (-1) \begin{bmatrix}
0 \\
2 \\
2 \\
\end{bmatrix}
= \begin{bmatrix}
6 \\
5 \\
0
\end{bmatrix}
$$

### Identitetsmatricen
Kaldes I eller $I_n$ hvor i er længen og bredden
$$
\begin{bmatrix}
1 & 0 & 0 &\\
0 & 1 & 0\\
0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
a \\
b \\
c \\
\end{bmatrix}
= \begin{bmatrix}
a \\
b \\
c
\end{bmatrix}
$$
## Kanonisk basisvektor
Den 2. kanoniske basisvektor ($e_2$):
$$
\begin{bmatrix}
0 \\
1 \\
0
\end{bmatrix}
$$

## Egenskaber
![[Pasted image 20250213133329.png]]