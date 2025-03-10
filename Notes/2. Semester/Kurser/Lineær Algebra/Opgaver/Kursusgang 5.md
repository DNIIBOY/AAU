![[linear-algebra-and-its-applications.pdf#page=149&rect=34,561,280,681|linear-algebra-and-its-applications, p.148]]
1: Da 5 og syv ikke kan gå op i hindanen, er søjlerne lineært uafhængige, og derfor er matricen invertibel (sætning 5)
3: Da der er nuller rundt omkring, kan det ikke lade sig gøre at de bliver lineært afhængige. Derfor er denne matrix også invertibel (sætning 5)

![[linear-algebra-and-its-applications.pdf#page=149&rect=288,549,530,595|linear-algebra-and-its-applications, p.148]]
Sætning 3 kan bruges til at vise at alle diagonalerne skal have en ikke-nul værdi, for at matricen bliver invertibel

![[linear-algebra-and-its-applications.pdf#page=149&rect=288,470,531,494|linear-algebra-and-its-applications, p.148]]
Sætning 5 siger at kolonnerne skal være lineært uafhængige, det er de ikke hvis 2 af dem er ens. Derfor er den aldrig invertibel.

![[linear-algebra-and-its-applications.pdf#page=149&rect=288,289,530,316|linear-algebra-and-its-applications, p.148]]


![[linear-algebra-and-its-applications.pdf#page=185&rect=35,416,280,679|linear-algebra-and-its-applications, p.184]]

![[Pasted image 20250310144840.png]]
![[Pasted image 20250310145042.png]]

![[linear-algebra-and-its-applications.pdf#page=185&rect=287,381,534,452|linear-algebra-and-its-applications, p.184]]

p = 4
q = 3
![[linear-algebra-and-its-applications.pdf#page=185&rect=285,141,533,278|linear-algebra-and-its-applications, p.184]]

15: Hvis den opstilles som matrice, bliver determinanten -35, som ikke er 0, og derfor er den en basis.
19: Hvis den opstilles som matrice, kan der ikke komme pivot i alle rækker, det kan derfor ikke være en basis.
![[linear-algebra-and-its-applications.pdf#page=186&rect=79,279,309,327|linear-algebra-and-its-applications, p.185]]
Lort:
$$
\begin{bmatrix}
1 & 0 & -4 & 7 \\
0 & 1 & 5 & -6 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$
Da der er pivot i $a_1$ og $a_2$, er disse kolonner en del af basis:
Basis for Col(A)
$$
\{
\begin{bmatrix}
4 \\ 6 \\ 3 \\
\end{bmatrix},
\begin{bmatrix}
5 \\ 5 \\ 4
\end{bmatrix}
\}
$$

Basis for Nul(A):


$$
\begin{cases}
x_{1} -4x_{3} + 7x_{4} = 0 \\
x_{2} + 5x_{3} - 6x_{4} = 0 \\
x_{3} \text{ er fri} \\
x_{4} \text{ er fri} \\
\end{cases}
\implies
\begin{cases}
x_{1} = 4x_{3} - 7x_{4} \\
x_{2} = -5x_{3} + 6x_{4} \\
x_{3} \text{ er fri} \\
x_{4} \text{ er fri} \\
\end{cases}
$$

$$
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{bmatrix} = s \cdot \begin{bmatrix}
4 \\
-5 \\
0 \\
0 \\
\end{bmatrix} + t \cdot \begin{bmatrix}
-7 \\
6 \\
0 \\
0 \\
\end{bmatrix}
$$

Basis for Nul(A)
$$
\{
\begin{bmatrix}
4 \\
-5 \\
0 \\
0 \\
\end{bmatrix},
\begin{bmatrix}
-7 \\
6 \\
0 \\
0 \\
\end{bmatrix}
\}
$$

