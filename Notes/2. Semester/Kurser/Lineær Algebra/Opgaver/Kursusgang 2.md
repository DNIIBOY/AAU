![[linear-algebra-and-its-applications.pdf#page=59&rect=38,303,280,372|linear-algebra-and-its-applications, p.58]]
$$
\begin{matrix}
4x_{1}-8x_{2}=9 \\
-3x_{1}+7x_{2}=-6 \\
2x_{1}=-5
\end{matrix}
$$

![[linear-algebra-and-its-applications.pdf#page=59&rect=290,433,531,515|linear-algebra-and-its-applications, p.58]]

$$
x_{1} \begin{bmatrix}
0 \\
4 \\
-1
\end{bmatrix}+ x_{2} \begin{bmatrix}
1 \\
6 \\
3 \\
\end{bmatrix}
+ x_{3} \begin{bmatrix}
5 \\
-1 \\
-8
\end{bmatrix}
= \begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$
![[linear-algebra-and-its-applications.pdf#page=59&rect=290,247,529,312|linear-algebra-and-its-applications, p.58]]
$$
x_{1} \begin{bmatrix}
1 \\
0 \\
-2
\end{bmatrix}
+ x_{2} \begin{bmatrix}
-4 \\
3 \\
8
\end{bmatrix}
+ x_{3} \begin{bmatrix}
2 \\
5 \\
-4
\end{bmatrix} = \begin{bmatrix}
3 \\
-7 \\
-3
\end{bmatrix}
$$
$$
\begin{bmatrix}
x_{1} \\
0 \\
-2x_{1}
\end{bmatrix}
+ \begin{bmatrix}
-4x_{2} \\
3x_{2} \\
8x_{2}
\end{bmatrix}
+ \begin{bmatrix}
2x_{3} \\
5x_{3} \\
-4x_{3}
\end{bmatrix}
= \begin{bmatrix}
3 \\
-7 \\
-3
\end{bmatrix}
$$
$$
\begin{bmatrix}
1 & -4 & 2 & 3 \\
0 & 3 & 5 & -7 \\
-2 & 8 & -4 & -3
\end{bmatrix}
\tilde{}
\begin{bmatrix}
1 & -4 & 2 & 3 \\
0 & 3 & 5 & -7 \\
0 & 0 & 0 & 3
\end{bmatrix}
$$
Svaret det nej


![[linear-algebra-and-its-applications.pdf#page=60&rect=330,590,577,701|linear-algebra-and-its-applications, p.59]]

$$
\begin{bmatrix}
1 & 0 & -4 & 4 \\
0  & 3 & -2 & 1 \\
-2 & 6 & 3 & -4
\end{bmatrix}
\begin{bmatrix}
1 & 0 & -4 & 4 \\
0  & 3 & -2 & 1 \\
0 & 6 & -5 & 4
\end{bmatrix}
\begin{bmatrix}
1 & 0 & -4 & 4 \\
0  & 3 & -2 & 1 \\
0 & 0 & -1 & 2
\end{bmatrix}
\begin{bmatrix}
1 & 0 & -4 & 4 \\
0  & 3 & -2 & 1 \\
0 & 0 & 1 & -2
\end{bmatrix}
\begin{bmatrix}
1 & 0 & -4 & 4 \\
0  & 1 & -\frac{2}{3} & \frac{1}{3} \\
0 & 0 & 1 & -2
\end{bmatrix}
$$
A. nej, 3
b. ja, $\infty$
c. fordi det står der, eller man kan gange med $\begin{bmatrix}1 \\ 0 \\ 0\end{bmatrix}$

![[linear-algebra-and-its-applications.pdf#page=68&rect=84,544,324,620|linear-algebra-and-its-applications, p.67]]

$$
x_{1} \begin{bmatrix}
4 \\
0
\end{bmatrix}
+ x_{2} \begin{bmatrix}
1 \\
1 \\
\end{bmatrix}
+ x_{3} \begin{bmatrix}
-7 \\
6
\end{bmatrix}
= \begin{bmatrix}
8 \\
0
\end{bmatrix}
$$
$$
\begin{bmatrix}
4 & 1 & -7 & 8 \\
0 & 1 & 6 & 0 \\
\end{bmatrix}
$$
![[linear-algebra-and-its-applications.pdf#page=76&rect=81,305,325,395|linear-algebra-and-its-applications, p.75]]

$$
\begin{bmatrix}
1 & 3 & 1 & 0 \\
-4 & 9 & 2 & 0 \\
0 & -3 & -6 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 3 & 1 & 0 \\
0 & 21 & 6 & 0 \\
0 & -3 & -6 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 3 & 1 & 0 \\
0 & -3 & -6 & 0 \\
0 & 0 & 36 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 3 & 1 & 0 \\
0 & 1 & 2 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$
$$
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3}
\end{bmatrix} = \begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$

![[linear-algebra-and-its-applications.pdf#page=76&rect=82,167,322,304|linear-algebra-and-its-applications, p.75]]

$$
\begin{bmatrix}
1 & -4 & -2 & 0 & 3 & -5 \\
0 & 0 & 1 & 0 & 0 & -1 \\
0 & 0 & 0 & 0 & 1 & -4 \\
0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
1 & -4 & -2 & 0 & 0 & 7 \\
0 & 0 & 1 & 0 & 0 & -1 \\
0 & 0 & 0 & 0 & 1 & -4 \\
0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
1 & -4 & 0 & 0 & 0 & 5 \\
0 & 0 & 1 & 0 & 0 & -1 \\
0 & 0 & 0 & 0 & 1 & -4 \\
0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
\begin{cases}
x_{1}-4x_{2} = 5 \\
x_{2} \text{ er fri} \\
x_{3} = -1 \\
x_{4} \text{ er fri} \\
x_{5} = -4 \\
\end{cases}
\implies
\begin{cases}
x_{1} = 5 + 4x_{2} \\
x_{3} = -1 \\
x_{5} = -4 \\
\end{cases}
$$

$$
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4} \\
x_{5}
\end{bmatrix}
= 
\begin{bmatrix}
5 \\
0 \\
-1 \\
0 \\
-4
\end{bmatrix} + 
s * \begin{bmatrix}
4 \\
0 \\
0 \\
0 \\
0 \\
\end{bmatrix} +
t * \begin{bmatrix}
0 \\
0 \\
0 \\
1 \\
0
\end{bmatrix}
$$

![[linear-algebra-and-its-applications.pdf#page=77&rect=31,150,280,441|linear-algebra-and-its-applications, p.76]]
27: T
28: F
29: 
30: T
31: F
32: T
33: F
34: T/F idk man
35: T
36: T
