
![[Pasted image 20250313143701.png]]

![[linear-algebra-and-its-applications.pdf#page=191&rect=36,77,278,102|linear-algebra-and-its-applications, p.190]]
![[linear-algebra-and-its-applications.pdf#page=191&rect=293,197,454,226|linear-algebra-and-its-applications, p.190]]
$$
\begin{bmatrix}
1 & -2 & -3 \\
-4 & 7 & 7
\end{bmatrix}
\begin{bmatrix}
1 & -2 & -3 \\
0 & -1 & -5
\end{bmatrix}
\begin{bmatrix}
1 & -2 & -3 \\
0 & 1 & 5
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 7 \\
0 & 1 & 5
\end{bmatrix}
$$
$[x]_{B} = \begin{bmatrix}7\\5\end{bmatrix}$

![[linear-algebra-and-its-applications.pdf#page=192&rect=82,184,325,271|linear-algebra-and-its-applications, p.191]]

$$
\begin{bmatrix}
1 & -3 & 2 & -4 \\
0 & 0 & 5 & -7 \\
0 & 0 & 0 & 5 \\
0 & 0 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix}
1 & -3 & 2 & -4 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix}
1 & -3 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
\end{bmatrix}
$$

$$
\begin{cases}
x_{1} -3x_{2} = 0 \\
x_{2} \text{ er fri} \\
x_{3} = 0 \\
x_{4} = 0 \\
0 = 0 \\
\end{cases}
\implies
\begin{cases}
x_{1} = 3x_{2} \\
x_{2} \text{ er fri} \\
x_{3} = 0 \\
x_{4} = 0 \\
\end{cases}
$$

$$
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{bmatrix} = s \cdot \begin{bmatrix}
3 \\
0 \\
0 \\
0 \\
\end{bmatrix}
$$
$$
Nul(A) = \{\begin{bmatrix}
3 \\ 0 \\ 0 \\ 0
\end{bmatrix}\}
$$
1 Dimension

$$
Col(A) = \{\begin{bmatrix}
1 \\ -3 \\ 2 \\ 4 \\
\end{bmatrix}, \begin{bmatrix}
2 \\ -1 \\ 4 \\ 2 \\
\end{bmatrix}, \begin{bmatrix}
-4 \\ 5 \\ -3 \\ 7 \\
\end{bmatrix}
\}
$$
3 Dimensioner


![[linear-algebra-and-its-applications.pdf#page=202&rect=77,603,326,680|linear-algebra-and-its-applications, p.201]]
$$
\begin{vmatrix}
3 & 0 & 4 \\
2 & 3 & 2 \\
0 & 5 & -1 \\
\end{vmatrix} = 
3 \cdot \begin{vmatrix}
3 & 2 \\
5 & -1
\end{vmatrix} - 0 \cdot \begin{vmatrix}
\text{lort}
\end{vmatrix} + 4 \cdot \begin{vmatrix}
2 & 3  \\
0 & 5
\end{vmatrix} =
3 \cdot (-13) + 4 \cdot 10 = 1
$$

$$
\begin{vmatrix}
3 & 0 & 4 \\
2 & 3 & 2 \\
0 & 5 & -1
\end{vmatrix} = 
-0 \cdot \begin{vmatrix}
\text{lort}
\end{vmatrix} + 3 \cdot \begin{vmatrix}
3 & 4 \\
0 & -1
\end{vmatrix} - 5 \cdot \begin{vmatrix}
3 & 4 \\
2 & 2
\end{vmatrix} = 3 \cdot (-3) -5 \cdot (-2) = 1
$$

![[linear-algebra-and-its-applications.pdf#page=202&rect=78,343,326,482|linear-algebra-and-its-applications, p.201]]
$$
\begin{vmatrix}
2 & -3 & 4 & 5 \\
0 & 5 & 3 & -1 \\
0 & 0 & -2 & 7 \\
0 & 0 & 0 & 4
\end{vmatrix} = 2 \cdot 5 \cdot (-2) \cdot 4 = -80
$$
![[linear-algebra-and-its-applications.pdf#page=210&rect=331,191,578,270|linear-algebra-and-its-applications, p.209]]
$$
\begin{vmatrix}
3 & 4 & -3 & -1 \\
3 & 0 & 1 & -3 \\
-6 & 0 & -4 & 3 \\
6 & 8 & -4 & -1
\end{vmatrix} = \begin{vmatrix}
3 & 4 & -3 & -1 \\
3 & 0 & 1 & -3 \\
-6 & 0 & -4 & 3 \\
0 & 0 & 2 & 1
\end{vmatrix} = -4 \cdot \begin{vmatrix}
3 & 1 & -3 \\
-6 & -4 & 3 \\
0 & 2 & 1
\end{vmatrix} = -4 \cdot \begin{vmatrix}
3 & 1 & -3 \\
0 & -2 & -3 \\
0 & 2 & 1
\end{vmatrix} 
$$

$$= -4 \cdot 3 \begin{vmatrix}
-2 & -3 &  \\
2 & 1 \\
\end{vmatrix} = -4 \cdot 3 \cdot 4 = -48
$$

![[linear-algebra-and-its-applications.pdf#page=211&rect=289,440,496,472|linear-algebra-and-its-applications, p.210]]

![[linear-algebra-and-its-applications.pdf#page=208&rect=229,502,488,537|linear-algebra-and-its-applications, p.207]]
$\det A \cdot A^{-1} = \det A \cdot \det A^{-1}$
$\implies \det I = \det A \cdot \det A^{-1}$
$\implies 1 = \det A \cdot \det A^{-1}$
$\implies \frac{1}{\det A^{-1}} = \det A$

![[linear-algebra-and-its-applications.pdf#page=211&rect=289,131,533,199|linear-algebra-and-its-applications, p.210]]
a: $\det AB = -2 * 3 = -6$
b: $\det 5A = -2 \cdot 5³ = -250$
c: $\det B^T = 3$
d: $\det A^{-1} = \frac{1}{-2} = -0.5$
e: $\det A³ = -8$
