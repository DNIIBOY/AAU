![[linear-algebra-and-its-applications.pdf#page=399&rect=35,544,282,679|linear-algebra-and-its-applications, p.398]]
$$
\frac{x \cdot u_{1}}{u_{1} \cdot u_{1}} \cdot u_{1} = -\frac{16}{18} \cdot \begin{bmatrix}
0 \\
1 \\
-4 \\
-1
\end{bmatrix} = \begin{bmatrix}
0 \\
-\frac{8}{9} \\
\frac{36}{9} \\
\frac{8}{9}
\end{bmatrix} = \frac{1}{9} \begin{bmatrix}
0 \\
-8 \\
32 \\
8
\end{bmatrix}
$$

$$
\frac{x \cdot u_{2}}{u_{2} \cdot u_{2}} \cdot u_{2} = -\frac{2}{9} \cdot \begin{bmatrix}
3 \\
5 \\
1 \\
1
\end{bmatrix} = \begin{bmatrix}
-\frac{6}{9} \\
-\frac{10}{9} \\
-\frac{2}{9} \\
-\frac{2}{9}
\end{bmatrix} = \frac{1}{9} \cdot \begin{bmatrix}
-6 \\
-10 \\
-2 \\
-2
\end{bmatrix}
$$

$$
\frac{x \cdot u_{3}}{u_{3} \cdot u_{3}} \cdot u_{3} = \frac{6}{9} \cdot \begin{bmatrix}
1 \\
0 \\
1 \\
-4
\end{bmatrix} = \frac{1}{9} \begin{bmatrix}
6 \\
0 \\
6 \\
-24
\end{bmatrix}
$$


$$
\hat{x} = \frac{1}{9} \begin{bmatrix}
0 \\
-18 \\
36 \\
-18
\end{bmatrix} = \begin{bmatrix}
0 \\
-2 \\
4 \\
-2
\end{bmatrix}
$$

$$
\frac{x \cdot u_{4}}{u_{4} \cdot u_{4}} \cdot u_{4} = \frac{72}{36} \cdot u_{4} = 2 \cdot \begin{bmatrix}
5 \\
-3 \\
-1 \\
1
\end{bmatrix} = \begin{bmatrix}
10 \\
-6 \\
-2 \\
2
\end{bmatrix}
$$


![[linear-algebra-and-its-applications.pdf#page=399&rect=35,366,280,432|linear-algebra-and-its-applications, p.398]]
$$
u_{1} \cdot u_{2} = 0
$$
$$
\frac{y \cdot u_{1}}{u_{1} \cdot u_{1}} \cdot u_{1} = \frac{3}{2} \cdot u_{1} = \begin{bmatrix}
\frac{3}{2} \\
\frac{3}{2} \\
0
\end{bmatrix}
$$
$$
\frac{y \cdot u_{2}}{u_{2} \cdot u_{2}} \cdot u_{2} = \frac{5}{2} \cdot u_{2} = \begin{bmatrix}
-\frac{5}{2}  \\
\frac{5}{2} \\
0
\end{bmatrix}
$$
$$
\frac{3}{2}u_{1} + \frac{5}{2}u_{2} = \begin{bmatrix}
-1 \\
4 \\
0
\end{bmatrix}
$$

![[linear-algebra-and-its-applications.pdf#page=405&rect=36,161,378,200|linear-algebra-and-its-applications, p.404]]
$v_{1} = \begin{bmatrix}2 \\ -5 \\ 1\end{bmatrix}$
$$
v_{2} = b_{2} - \hat{b_{2}} = b_{2} - \frac{b_{2} \cdot v_{1}}{v_{1} \cdot v_{1}} \cdot v_{1} = b_{2} - \frac{15}{30} \cdot v_{1} = b_{2} - \frac{1}{2} \cdot v_{1}
$$
$$
v_{2} = \begin{bmatrix}
4 \\
-1 \\
2
\end{bmatrix} - \frac{1}{2} \begin{bmatrix}
2 \\
-5 \\
1
\end{bmatrix} = \begin{bmatrix}
3 \\
\frac{3}{2} \\
\frac{3}{2}
\end{bmatrix}
$$

$$
b = Span\{v_{1}, v_{2}\} = Span\left\{ \begin{bmatrix}
2 \\
-5 \\
1
\end{bmatrix}, \begin{bmatrix}
3 \\
\frac{3}{2} \\
\frac{3}{2}
\end{bmatrix} \right\}
$$
![[linear-algebra-and-its-applications.pdf#page=406&rect=85,671,324,703|linear-algebra-and-its-applications, p.405]]
$$
\frac{1}{||v_{1}||}v_{1} = \frac{1}{\sqrt{ 2^2 + (-5)^2 + 1^2 }} v_{1} = \frac{1}{\sqrt{ 30 }} \begin{bmatrix}
2 \\
-5 \\
1
\end{bmatrix} = \begin{bmatrix}
\frac{2}{\sqrt{ 30 }} \\
-\frac{5}{\sqrt{ 30 }} \\
\frac{1}{\sqrt{ 30 }}
\end{bmatrix}
$$

$$
\frac{1}{||v_{2}||}v_{2} = \frac{1}{\sqrt{3^2 + \left( \frac{3}{2} \right)^2 + \left( \frac{3}{2} \right)^2}} v_{2} = \frac{1}{\sqrt{ \frac{27}{2} }} \begin{bmatrix}
3 \\
\frac{3}{2} \\
\frac{3}{2}
\end{bmatrix}
$$

![[linear-algebra-and-its-applications.pdf#page=406&rect=83,568,324,643|linear-algebra-and-its-applications, p.405]]
$v_{1} = \begin{bmatrix}3  \\ 1 \\ -1 \\ 3\end{bmatrix}$
$$
v_{2} = b_{2} - \frac{b_{2} \cdot v_{1}}{v_{1}\cdot v_{1}}v_{1} = -\frac{40}{20}v_{1} = 2\begin{bmatrix}
3 \\
1 \\
-1 \\
3
\end{bmatrix} = \begin{bmatrix}
6 \\
2 \\
-2 \\
6
\end{bmatrix}
$$
$$
v_{3} = b_{3} - \frac{b_{3}\cdot v_{1}}{v_{1}\cdot v_{1}}v_{1} - \frac{b_{3}\cdot v_{2}}{v_{2}\cdot v_{2}}v_{2} = b_{3} - \frac{30}{20}v_{1} - \frac{60}{50}v_{2}
$$

$$
v_{3} = \begin{bmatrix}
1 \\
1 \\
-2 \\
8
\end{bmatrix} - \frac{3}{2} \begin{bmatrix}
3 \\
1 \\
-1 \\
3
\end{bmatrix} - \frac{6}{5} \begin{bmatrix}
6 \\
2 \\
-2 \\
6
\end{bmatrix} = \begin{bmatrix}
1 \\
1 \\
-2 \\
8
\end{bmatrix} - \begin{bmatrix}
\frac{9}{2} \\
\frac{3}{2} \\
-\frac{3}{2} \\
\frac{9}{2}
\end{bmatrix} - \begin{bmatrix}
\frac{36}{5} \\
\frac{12}{5} \\
-\frac{12}{5} \\
\frac{36}{5}
\end{bmatrix}
$$

$$
v_{3} = \begin{bmatrix}
1 \\
1 \\
-2 \\
8
\end{bmatrix} - \begin{bmatrix}
\frac{45}{10} \\
\frac{15}{10} \\
-\frac{15}{10} \\
\frac{45}{10}
\end{bmatrix} - \begin{bmatrix}
\frac{72}{10} \\
\frac{24}{10} \\
-\frac{24}{10} \\
\frac{72}{10}
\end{bmatrix}
$$

$$
v_{3} = \begin{bmatrix}
1 + \frac{27}{10} \\
1 + \frac{9}{10} \\
-2 + \frac{9}{10} \\
8 + \frac{27}{10}
\end{bmatrix}
$$


