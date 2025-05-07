# Mindste kvadraters metode (Blok 4)

Når man har indsamlet eksperimentelle data, ønsker man ofte at opstille en model, der beskriver sammenhængene i dataene. Det vil sige, at vi har et antal baggrundsvariable (eller forklarende variable), som vi ønsker at bruge til at estimere en responsvariabel.

At opstille en model ud fra data indgår i Machine Learning. Man træner eksempelvis et kunstigt neuralt netværk ud fra data, hvor man kender både baggrundsvariable og respons. Netværket søger efter den model, der for de kendte datapunkter giver output/respons tæt på den kendte respons. Så kan man bruge modellen til at regne på tilfælde, hvor man ikke kender det korrekte svar.

Hvis vi for eksempel ønsker at undersøge brugernes tilfredshed med en brugergrænseflade (responsvariablen), kunne vi forsøge at forklare dette ud fra skriftstørrelse, ikonstrørrelse, antallet af farver eller lignende (baggrundsvariablene). Selvom hver bruger kan lægge vægt på forskellige ting, forventer vi, at der vil være generelle tendenser, og det er disse vi forsøger at fange med modellen.

Denne workshop handler om anvendelsen af mindste kvadraters metode og regressionsanalyse, til at approksimere en ukendt funktion af flere variable (responsvariablen) ud fra et antal datapunkter. Lad os først gå ud fra, at der er to baggrundsvariable samt responsvariablen. Vi har indsamlet datapunkter, så det $j$'te datapunkt er $(x^{(j)}_1, x^{(j)}_2, v_j)$.

Vi approksimerer nu responsvariablen med et andengradspolynomium i to variable:

$$
g(x_1, x_2) = u_1 + u_2x_1 + u_3x_2 + u_4x_1^2 + u_5x_1x_2 + u_6x_2^2
$$

![[Pasted image 20250428094302.png]]

Workshoppen går ud på at finde $u_1, ..., u_6$, så andengradspolynomiet tilnærmer datapunkterne bedst muligt. Altså at finde minimum for

$$
F(u_1, ..., u_6) = \sum_{j=1}^n \left( v_j - \left( u_1 + u_2x_1^{(j)} + u_3x_2^{(j)} + u_4(x_1^{(j)})^2 + u_5x_1^{(j)}x_2^{(j)} + u_6(x_2^{(j)})^2 \right) \right)^2
$$

Workshoppen består af tre delopgaver.

---

# Delopgave 1

## (i)

Lad $X$ være en $n \times 6$ matrix givet udfra data ved

$$
X = \begin{bmatrix}
1 & x^{(1)}_1 & x^{(1)}_2 & (x^{(1)}_1)^2 & x^{(1)}_1x^{(1)}_2 & (x^{(1)}_2)^2 \\
1 & x^{(2)}_1 & x^{(2)}_2 & (x^{(2)}_1)^2 & x^{(2)}_1x^{(2)}_2 & (x^{(2)}_2)^2 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
1 & x^{(n)}_1 & x^{(n)}_2 & (x^{(n)}_1)^2 & x^{(n)}_1x^{(n)}_2 & (x^{(n)}_2)^2
\end{bmatrix}
$$

Vis, at (1) kan omskrives som

$$
F(u) = \|v - Xu\|^2
$$

Et minimumspunkt for $F(u)$ er derfor en vektor $\hat{u}$, som opfylder, at $\|v - X\hat{u}\| \leq \|v - Xu\|$ for alle $u$.

$\hat{u}$ kaldes da en mindste kvadraters løsning til $Xu = v$.

I delopgave 2 vises, at $\hat{u}$ er en mindste kvadraters løsning til $Xu = v$ hvis og kun hvis $\hat{u}$ er løsning til normalligningen:

$$
X^TX\hat{u} = X^Tv
$$
## Svar

Vi har matricen $X$ og vektoren $u$:

$$
Xu = 
\begin{bmatrix}
1 & x^{(1)}_1 & x^{(1)}_2 & (x^{(1)}_1)^2 & x^{(1)}_1x^{(1)}_2 & (x^{(1)}_2)^2 \\
1 & x^{(2)}_1 & x^{(2)}_2 & (x^{(2)}_1)^2 & x^{(2)}_1x^{(2)}_2 & (x^{(2)}_2)^2 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
1 & x^{(n)}_1 & x^{(n)}_2 & (x^{(n)}_1)^2 & x^{(n)}_1x^{(n)}_2 & (x^{(n)}_2)^2
\end{bmatrix}
\begin{bmatrix}
u_1 \\
u_2 \\
u_3 \\
u_4 \\
u_5 \\
u_6
\end{bmatrix}
$$

For datapunkt $j$ fås:

$$
(Xu)_j = u_1 + u_2x_1^{(j)} + u_3x_2^{(j)} + u_4(x_1^{(j)})^2 + u_5x_1^{(j)}x_2^{(j)} + u_6(x_2^{(j)})^2
$$

Fejlen på datapunkt $j$ er givet ved:

$$
(v - Xu)_j = v_j - (Xu)_j = v_j - \left( u_1 + u_2x_1^{(j)} + u_3x_2^{(j)} + u_4(x_1^{(j)})^2 + u_5x_1^{(j)}x_2^{(j)} + u_6(x_2^{(j)})^2 \right)
$$

Altså er $(v - Xu)_j$ en generel formel for fejlen mellem målingen $v_j$ og modellens forudsigelse.

---

For at finde den samlede fejl for alle datapunkter:

- Kvadrerer vi hver fejl for at sikre, at alle fejl er positive.
- Summerer vi de kvadrerede fejl for at få en samlet måling.(Mindste kvadraters løsning)

Så får vi:

$$
F(u)
=
\sum_{j=1}^n \left( v_j - \left( u_1 + u_2x_1^{(j)} + u_3x_2^{(j)} + u_4(x_1^{(j)})^2 + u_5x_1^{(j)}x_2^{(j)} + u_6(x_2^{(j)})^2 \right) \right)^2
=
\|v - Xu\|^2
$$

---

### Konklusion

Vi har dermed fundet en funktion $F(u)$, der måler den samlede fejl mellem:

- Datapunkterne $v_j$ (de målte værdier)
- Modellens forudsigelser $(Xu)_j$ baseret på de forklarende variable $x_1^{(j)}$ og $x_2^{(j)}$.

Når vi minimerer $F(u)$, finder vi de koefficienter $u_1, \dots, u_6$, der bedst tilnærmer datapunkterne med et andengradspolynomium.


## (ii)

Vi ser på det simplere problem: "Hvilket andengradspolynomium $u_1 + u_2x + u_3x^2$ tilnærmer fem givne datapunkter bedst," og undersøger dette ift. mindste kvadrater.

Opstil den $5 \times 3$ matrix, der svarer til matricen $X$, hvis de fem datapunkter er:

$$(x^{(1)}, v_1), (x^{(2)}, v_2), (x^{(3)}, v_3), (x^{(4)}, v_4), (x^{(5)}, v_5)$$
## Svar
$$
X=
\begin{bmatrix}
1 & x⁽¹⁾ & (x⁽¹⁾)²\\
1 & x⁽²⁾ & (x⁽²⁾)²\\
1 & x⁽³⁾ & (x⁽³⁾)²\\
1 & x⁽⁴⁾ & (x⁽⁴⁾)²\\ 
1 & x⁽⁵⁾ & (x⁽⁵⁾)²\\ 
\end{bmatrix}
$$
Hvis altså $u$ ganges på får vi at:
$$
Xu=
\begin{bmatrix}
1 & x⁽¹⁾ & (x⁽¹⁾)²\\
1 & x⁽²⁾ & (x⁽²⁾)²\\
1 & x⁽³⁾ & (x⁽³⁾)²\\
1 & x⁽⁴⁾ & (x⁽⁴⁾)²\\ 
1 & x⁽⁵⁾ & (x⁽⁵⁾)²\\ 
\end{bmatrix}
\begin{bmatrix}
u_1\\
u_2 \\
u_3 \\
\end{bmatrix}
$$
Som giver den bedst tilnærmelse af de givne datapunkter. (Hvis u vælges som mindste kvadraters løsning)
## (iii)

Datapunkterne

$$(x^{(1)}, v_1) = (-1, 1), (x^{(2)}, v_2) = (1, 1), (x^{(3)}, v_3) = (0, 0), (x^{(4)}, v_4) = (2, 1)$$

ønskes tilnærmet med et andengradspolynomium.

Opstil $4 \times 3$ matricen $X$ og vis, at

$$
X^TX = \begin{bmatrix}
4 & 2 & 6 \\
2 & 6 & 8 \\
6 & 8 & 18
\end{bmatrix}
$$

og at $X^TX$ er invertibel.

## Svar
Vi kan se på data punkterne at,
$$
X=
\begin{bmatrix}
1 & x⁽¹⁾ & (x⁽¹⁾)²\\
1 & x⁽²⁾ & (x⁽²⁾)²\\
1 & x⁽³⁾ & (x⁽³⁾)²\\
1 & x⁽⁴⁾ & (x⁽⁴⁾)²\\ 
1 & x⁽⁵⁾ & (x⁽⁵⁾)²\\ 
\end{bmatrix}
, \quad X=
\begin{bmatrix}
1 & -1 & 1 \\
1 & 1 & 1 \\
1 & 0 & 0 \\
1 & 2 & 4 \\
\end{bmatrix}
$$
Og derfor må den transponeret være:
$$
X^T=
\begin{bmatrix}
1 & 1 & 1 & 1 \\
-1 & 1 & 0 & 2 \\
1 & 1 & 0 & 4 \\
\end{bmatrix}
$$
$$
X^TX=

\begin{bmatrix}
1 & 1 & 1 & 1 \\
-1 & 1 & 0 & 2 \\
1 & 1 & 0 & 4 \\
\end{bmatrix}
\begin{bmatrix}
1 & -1 & 1 \\
1 & 1 & 1 \\
1 & 0 & 0 \\
1 & 2 & 4 \\
\end{bmatrix}
=
\begin{bmatrix}
4 & 2 & 6 \\
2 & 6 & 8 \\
6 & 8 & 18 \\
\end{bmatrix}
$$
Da $X$ er lineært uafhængig må $X^TX$ være invertible

## (iv)

Løs normalligningen $X^TX\hat{u} = X^Tv$, hvor

$$
v = \begin{bmatrix} 1 \\ 1 \\ 0 \\ 1 \end{bmatrix}
$$

Opstil det andengradspolynomium, der bedst tilnærmer de fire datapunkter og tegn det og punkterne i et plant koordinatsystem.

## Svar
$$
X^Tv=
\begin{bmatrix}
1 & 1 & 1 & 1 \\
-1 & 1 & 0 & 2 \\
1 & 1 & 0 & 4 \\
\end{bmatrix}
\begin{bmatrix}
1 \\
1 \\
0 \\
1 \\
\end{bmatrix}
=
\begin{bmatrix}
3 \\
2 \\
6
\end{bmatrix}
$$

$$
(X^TX)⁻¹X^TXû=(X^TX)⁻¹X^Tv
$$
$$
û=(X^TX)⁻¹X^Tv
$$

$$
û=
(X^TX)⁻¹
\begin{bmatrix}
3 \\
2 \\
6 \\
\end{bmatrix}
$$
$$
(X^TX)⁻¹=

\left[ \begin{array}{ccc|ccc}
4 & 2 & 6 & 1 & 0 & 0 \\
2 & 6 & 8 & 0 & 1 & 0 \\
6 & 8 & 18 & 0 & 0 & 1 \\
\end{array} \right] 
=
\begin{bmatrix}
\frac{1}{20} & \frac{3}{20} & -\frac{1}{4} \\
-\frac{7}{20} & \frac{9}{20} & -\frac{1}{4} \\
\frac{1}{4} & -\frac{1}{4} & \frac{1}{4}
\end{bmatrix}
$$

$$
û=
\begin{bmatrix}
\frac{1}{20} & \frac{3}{20} & -\frac{1}{4} \\
-\frac{7}{20} & \frac{9}{20} & -\frac{1}{4} \\
\frac{1}{4} & -\frac{1}{4} & \frac{1}{4}
\end{bmatrix}
\begin{bmatrix}
3 \\
2 \\
6 \\
\end{bmatrix}
=
\begin{bmatrix}
\frac{9}{20} \\
-\frac{3}{20} \\
\frac{1}{4}
\end{bmatrix}
$$


## (v)

Vis, at hvis $X^TX$ er invertibel og $X = QR$ er en QR-faktorisering, så er

$$
\hat{u} = R^{-1}Q^Tv
$$

(I behøver ikke vise, at $R$ er invertibel.)

## Svar
$$
Q^TQ=I
$$

$$
  ((QR)^TQR)^{-1}(QR)^Tv=
$$
		 $$ (R^TQ^TQR)^{-1}R^TQ^Tv=$$
  $$(R^TR)^{-1}R^TQ^Tv=$$
  $$R^{-1}(R^T)^{-1}R^TQ^Tv=$$
  $$R^{-1}Q^Tv$$

# Delopgave 2

I denne delopgave vises, at $\hat{u}$ er en mindste kvadraters løsning til $Xu = v$, hvis og kun hvis $\hat{u}$ er en løsning til normalligningen, og at denne ligning altid er konsistent.

## (i)

$Xu$ ligger i søjlerummet $\text{Col}(X)$, så $\|v - Xu\|$ er mindst, hvis $Xu$ er den vektor i søjlerummet, der ligger tættest på $v$. Indse, at $Xu$ skal være projektionen af $v$ på $\text{Col}(X)$. Projektionen kaldes nu $\hat{v}$. I skal ikke udregne $\hat{v}$.

Gør rede for, at ligningen $Xu = \hat{v}$ er konsistent, og konkluder, at der findes et minimum for $F(u)$.

## Svar
Vi ønsker at finde den tætteste vektor i $\text{Col}(X)$. For at finde den tætteste vektor i  $\text{Col}(X)$ bruger vi projektionen $\hat{v}$.
Altså $\hat{v}$ ligger i $\text{Col}(X)$ og $Xu$ spænder alle vektorer i $\text{Col}(X)$,
og der vil altså altid være mindst én $u$ sådan at,
$$
Xu=\hat{v}
$$
## (ii)

Gør rede for, at $v - \hat{v}$ ligger i $(\text{Col}(X))^\perp$ og derfor

$$
X^T(v - \hat{v}) = 0
$$

(Vink: Rækkerne i $X^T$ er søjlerne i $X$. Og disse er ortogonale på $v - \hat{v}$.)

## Svar
Da $\hat{v}$ er en ortogonalprojektion på planen vil foreskellen $v-\hat{v}$ (Den ortogonale vektor) altså ligge i ortogonalkomplementet $(\text{Col}(X))^\perp$

Da $X^T$'s søjler er rækkerne i $X$ vil vi, når vi ganger $v-\hat{v}$ på, få at ved matrix-vektor multiplikation at,
$$
X^T(v - \hat{v}) = 0
$$
(Da de er ortogonale og deres prikprodukt vil give 0-vektoren)

## (iii)

Lad $\hat{u}$ være et minimum for $F$ i (1). Konkludér fra (i), at $\hat{u}$ er en løsning til $Xu = \hat{v}$. Brug nu (ii) til at udlede

$$
X^T(v - X\hat{u}) = 0
$$

Konkludér derfor, at hvis $\hat{u}$ er mindste kvadraters løsning til (1), så er $\hat{u}$ løsning til (2). Konkludér desuden, at hvis $X^TX$ er invertibel, så er der en entydig løsning:

$$
\hat{u} = (X^TX)^{-1}X^Tv
$$
## Svar
At minimere $F(u)$ er det samme som at finde den $u$ der gør at $Xu=\hat{v}$.
Denne specifikke $u$ kaldes $\hat{u}$.
Vi ved at:
$$
X^T(v - \hat{v}) = 0
$$
Da $\hat{v}$ altså må være vores specifikke $Xû$ vil vi få:
$$
X^T(v-X\hat{u})=0
$$
Dette kan omskrives:
$$
X^Tv-X^TX\hat{u}=0
$$
og derfor at:
$$
X^TX\hat{u}=X^Tv, \quad \hat{u}=(X^TX)⁻¹X^Tv
$$

## (iv)

Brug nedenstående trin til at vise det omvendte udsagn:

(a) Lad $w$ være en løsning til (2). Vis, at $v - Xw$ er i $(\text{Col}(X))^\perp$.

(b) Konkluder, at $Xw$ er den ortogonale projektion af $v$ ind på $\text{Col}(X)$.

(c) Konkluder, at $Xw = \hat{v}$.

Hvorfor er argumentet færdigt nu? (Vink: Se (i) og (ii))

## Svar
### (a)
Vi ved at $w$ er vores løsning ($\hat{u}$).
Vi opskriver normalligningen:
$$
X^TXw=X^Tv
$$
Vi omskriver:
$$
X^T(v-Xw)=0
$$
Dette betyder at $v-Xw$ ligger ortogonalt på alle kolonner i $X$.
Hvis en vektor er ortogonal på alle søjler i X så er den ortogonal på hele $Col(X)$ og derfor i $(\text{Col}(X))^\perp$
### (b)
(a) giver den præcise definition på en ortogonal projektion:
at $Xw$ ligger i $Col(X)$, og $(v-Xw)$ er ortogonal på $Col(X)$, så er $Xw$ projektionen af $v$ på $Col(X)$.
### (c)
Så $Xw=\hat{v}$

---

# Delopgave 3

I skal nu bruge MATLAB til at finde mindste kvadraters løsning for tre dataeksempler.

De tre eksempler er givet i filen `dataEksempler.m`. I filen kaldes funktionen `leastSquaresFit` fra den tilhørende fil `leastSquaresFit.m`, som I først skal have gemt på jeres computer. (I kan med fordel gemme den sammen med resten af filerne til denne workshop.)

For at MATLAB kan finde filen, skal I sikre jer, at arbejdsmappen i MATLAB er den mappe, hvor filerne ligger. Dette gør I ved at ændre "Current Folder" i venstre side af MATLAB.

## (i)

Udfyld det, der mangler, i linjerne 6 og 7 i `leastSquaresFit`. I kan antage, at $X^TX$ er inverterbar, så (iii) fra delopgave 2 kan benyttes.

```matlab
function [u,vHat] = leastSquaresFit(X,v)
% LEASTSQUARESFIT Mindste kvadraters metode
% 	Find mindste kvadraters løsning u
% 	til Xu=vHat, så ||v-vHat||^2 minimeres 
    
    u = (X'*X)\(X'*v);
    vHat = X*u;
    
    % Plot datapunkterne y sammen med modellen
    clf('reset');
    plot3(X(:,2),X(:,3),v,'o')
    hold on;
    
    [T1,T2] = meshgrid(-10:0.1:10, -10:0.1:10);
    Z = arrayfun(@(t1,t2) [1, t1, t2, t1^2, t1*t2, t2^2]*u, T1, T2);
    
    mesh(T1,T2,Z)
end
    
```

## (ii)

Brug `leastSquaresFit` på hvert af de tre eksempler ved at bruge `dataEksempler.m`. Undersøg plottet for at tjekke, at målepunkterne ligger tæt på det fittede andengradspolynomium.
![[eksempel1.jpg]]
![[eksempel2.jpg]]
![[eksempel3.jpg]]
## (iii)

Hvilket af tilfældene i figur 1 falder hvert af de tre eksempler ind under?
![[Pasted image 20250428134130.png]]
![[Pasted image 20250428134140.png]]
![[Pasted image 20250428134234.png]]
![[Pasted image 20250428134245.png]]
![[Pasted image 20250428134156.png]]
![[Pasted image 20250428134210.png]]