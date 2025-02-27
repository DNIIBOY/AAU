![[linear-algebra-and-its-applications.pdf#page=133&rect=38,251,281,347|linear-algebra-and-its-applications, p.132]]
-2A:
$$
\begin{bmatrix}
-4 & 0 & 2 \\
-8 & 6 & -4
\end{bmatrix}
$$
B-2A:
$$
\begin{bmatrix}
3 & -5 & 3 \\
-7 & 2 & -7
\end{bmatrix}
$$

AC: Kan ikke lade sig gøre fordi A har 3 kolonner, men C har kun 2 rækker

CD:
$$
\begin{bmatrix}
1 \cdot 3 + 2 \cdot -1  & 1 \cdot 5 + 2 \cdot 4 \\
-2 \cdot 3 + 1 \cdot -1  & -2 \cdot 5 + 1 \cdot 4 \\ 
\end{bmatrix} = 
\begin{bmatrix}
1 & 13 \\
-7 & -6
\end{bmatrix}
$$

![[linear-algebra-and-its-applications.pdf#page=133&rect=294,242,528,268|linear-algebra-and-its-applications, p.132]]
![[Kursusgang4KmbComTekUdfyldt.pdf#page=14&rect=22,20,311,117|Kursusgang4KmbComTekUdfyldt, p.14]]
$3 \times 7$ 


![[linear-algebra-and-its-applications.pdf#page=133&rect=285,69,540,154|linear-algebra-and-its-applications, p.132]]
$$
AD = \begin{bmatrix}
2 & 3  & 5 \\
2 & 6  & 15\\
2 & 12  & 25
\end{bmatrix}
DA = \begin{bmatrix}
2 & 2 & 2 \\
3 & 6  & 9\\
5 & 20  & 25\\
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 1 & 1 & 1 & 0 & 0 \\
1 & 2 & 3 & 0 & 1 & 0 \\
1 & 4 & 5 & 0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 1 & 2 & -1 & 1 & 0 \\
0 & 3 & 4 & -1 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 1 & 2 & -1 & 1 & 0 \\
0 & 0 & -2 & 2 & -3 & 1 \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 1 & 2 & -1 & 1 & 0 \\
0 & 0 & 1 & -1 & \frac{3}{2} & -\frac{1}{2} \\
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 1 & 0 & 1 & -2 & 1 \\
0 & 0 & 1 & -1 & \frac{3}{2} & -\frac{1}{2} \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 1 & 0 & 2 & -1 \\
0 & 1 & 0 & 1 & -2 & 1 \\
0 & 0 & 1 & -1 & \frac{3}{2} & -\frac{1}{2} \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 0 & 0 & 1 & \frac{1}{2} & -\frac{1}{2} \\
0 & 1 & 0 & 1 & -2 & 1 \\
0 & 0 & 1 & -1 & \frac{3}{2} & -\frac{1}{2} \\
\end{bmatrix}
A^{-1} = B = \begin{bmatrix}
1 & \frac{1}{2} & -\frac{1}{2} \\
1 & -2 & 1 \\
-1 & \frac{3}{2} & -\frac{1}{2} \\
\end{bmatrix}
$$

![[linear-algebra-and-its-applications.pdf#page=134&rect=83,614,324,650|linear-algebra-and-its-applications, p.133]]
$$
Q \cdot [r_{1}\dots r_{p}]
$$


![[linear-algebra-and-its-applications.pdf#page=143&rect=34,377,229,453|linear-algebra-and-its-applications, p.142]]

1.
$$
A =\begin{bmatrix}
8 & 3 \\
5 & 2
\end{bmatrix}
$$
$$
\text{detA} = 8*2-5*3 = 1
$$

$$
A^{-1} = \frac{1}{detA} \begin{bmatrix}
2 & -3 \\
-5 & 8
\end{bmatrix}
=
\begin{bmatrix}
2 & -3 \\
-5 & 8 \\
\end{bmatrix}
$$

![[linear-algebra-and-its-applications.pdf#page=143&rect=38,102,281,239|linear-algebra-and-its-applications, p.142]]

$$
detA = 1 \cdot 12 - 5 \cdot 2 = 2
$$
$$
\frac{1}{detA} = \frac{1}{2}
$$
$$
A^{-1} = \frac{1}{2} \begin{bmatrix}
12 & -2 \\
-5 & 1 \\
-\frac{5}{2} & \frac{1}{2}
\end{bmatrix}
$$

$Ax = b_{1}$:
$$
\begin{bmatrix}
6 & -1 \\
-\frac{5}{2} & \frac{1}{2}
\end{bmatrix} \cdot \begin{bmatrix}
-1 \\
3
\end{bmatrix} =
\begin{bmatrix}
-6  - 3 \\
\frac{5}{2} + \frac{3}{2}
\end{bmatrix} = 
\begin{bmatrix}
-9 \\
4
\end{bmatrix}
$$

$Ax = b_{2}$:

$$
\begin{bmatrix}
6 & -1 \\
-\frac{5}{2} & \frac{1}{2}
\end{bmatrix} \cdot \begin{bmatrix}
1 \\
-5
\end{bmatrix} =
\begin{bmatrix}
11 \\
-5
\end{bmatrix}
$$

$Ax = b_{3}$:

$$
\begin{bmatrix}
6 & -1 \\
-\frac{5}{2} & \frac{1}{2}
\end{bmatrix} \cdot \begin{bmatrix}
2 \\
6
\end{bmatrix} =
\begin{bmatrix}
6 \\
-2
\end{bmatrix}
$$

$Ax = b_{4}$:

$$
\begin{bmatrix}
6 & -1 \\
-\frac{5}{2} & \frac{1}{2}
\end{bmatrix} \cdot \begin{bmatrix}
3 \\
5
\end{bmatrix} =
\begin{bmatrix}
13 \\
-5
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 2 & -1 & 1 & 2 & 3 \\
5 & 12 & 3 & -5 & 6 & 5
\end{bmatrix}
\begin{bmatrix}
1 & 2 & -1 & 1 & 2 & 3 \\
0 & 2 & 8 & -10 & -4 & -10
\end{bmatrix}
\begin{bmatrix}
1 & 2 & -1 & 1 & 2 & 3 \\
0 & 1 & 4 & -5 & -2 & -5
\end{bmatrix}
$$


$$
\begin{bmatrix}
1 & 0 & -9 & 11 & 6 & 13 \\
0 & 1 & 4 & -5 & -2 & -5
\end{bmatrix}
$$

![[linear-algebra-and-its-applications.pdf#page=144&rect=330,383,575,486|linear-algebra-and-its-applications, p.143]]
41:
$$
A =\begin{bmatrix}
1 & 0 & -2 \\
-3 & 1 & 4 \\
2 & -3 & 4
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 0 & -2  & 1 & 0 & 0 \\
-3 & 1 & 4  & 0 & 1 & 0 \\
2 & -3 & 4  & 0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & -2  & 1 & 0 & 0 \\
0 & 1 & -2  & 3 & 1 & 0 \\
0 & -3 & 8  & -2 & 0 & 1 \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 0 & -2  & 1 & 0 & 0 \\
0 & 1 & -2  & 3 & 1 & 0 \\
0 & 0 & 2  & 7 & 3 & 1 \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0  & 8 & 3 & 1 \\
0 & 1 & 0  & 10 & 4 & 1 \\
0 & 0 & 2  & 7 & 3 & 1 \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0  & 8 & 3 & 1 \\
0 & 1 & 0  & 10 & 4 & 1 \\
0 & 0 & 1  & \frac{7}{2} & \frac{3}{2} & \frac{1}{2} \\
\end{bmatrix}
$$
$$
A^{-1} = 
\begin{bmatrix}
8 & 3 & 1 \\
10 & 4 & 1 \\
\frac{7}{2} & \frac{3}{2} & \frac{1}{2} \\
\end{bmatrix}
$$

![[linear-algebra-and-its-applications.pdf#page=144&rect=81,581,329,622|linear-algebra-and-its-applications, p.143]]
If a is invertible:
$$
A^{-1}AB = A^{-1}AC \implies B = C
$$
This does not work if $A^{-1}$ doesn't exist (A is not invertible)

![[linear-algebra-and-its-applications.pdf#page=144&rect=81,516,325,555|linear-algebra-and-its-applications, p.143]]
When invertible they can be reduced to I, multiplying I by i still makes I, so all is good.

$D = C^{-1}B^{-1}A^{-1}$

![[linear-algebra-and-its-applications.pdf#page=134&rect=76,181,328,438|linear-algebra-and-its-applications, p.133]]
15: F
17: T
19: T
20: T
23: F, must be opposite order