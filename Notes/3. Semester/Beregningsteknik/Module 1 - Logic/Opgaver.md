![[exercises_mm1.pdf#page=1&rect=60,544,280,637|exercises_mm1, p.1]]
a) True
b) True
c) True
d) False

e) Nope
f) Nope

![[exercises_mm1.pdf#page=1&rect=63,440,285,530|exercises_mm1, p.1]]
a) If you have the flu, you miss the final examination
b) If you don't miss the final examination, you pass the course, and if you do miss the final examination you do not pass the course
c) If you miss the final examination, you do not pass the course

![[exercises_mm1.pdf#page=1&rect=60,246,281,439|exercises_mm1, p.1]]
a) ~p
b) p ^ ~q
c) p -> q
d) ~p -> ~q
e) p -> q
f) q ^ ~p
g) q -> p

![[exercises_mm1.pdf#page=1&rect=62,176,284,242|exercises_mm1, p.1]]
a) True
b) True
c) False
d) True

![[exercises_mm1.pdf#page=1&rect=62,105,282,176|exercises_mm1, p.1]]
a)

| p   | p ^ ~p |
| --- | ------ |
| 0   | 0      |
| 1   | 0      |
b)

| p   | p v ~p |
| --- | ------ |
| 0   | 1      |
| 1   | 1      |
c)

| p   | q   | p v ~q | (p v ~q) -> q |
| --- | --- | ------ | ------------- |
| 1   | 1   | 1      | 1             |
| 1   | 0   | 1      | 0             |
| 0   | 1   | 0      | 1             |
| 0   | 0   | 1      | 0             |
d)

| p   | q   | p v q | p ^ q | (p v q) -> (p ^ q) |
| --- | --- | ----- | ----- | ------------------ |
| 1   | 1   | 1     | 1     | 1                  |
| 1   | 0   | 1     | 0     | 0                  |
| 0   | 1   | 1     | 0     | 0                  |
| 0   | 0   | 0     | 0     | 1                  |
e)

| p   | q   | p -> q | ~q -> ~p | (p -> q) <-> (~q -> ~p) |
| --- | --- | ------ | -------- | ----------------------- |
| 1   | 1   | 1      | 1        | 1                       |
| 1   | 0   | 0      | 0        | 1                       |
| 0   | 1   | 1      | 1        | 1                       |
| 0   | 0   | 1      | 1        | 1                       |
f)

| p   | q   | p -> q | q -> p | (p->q) -> (q -> p) |
| --- | --- | ------ | ------ | ------------------ |
| 1   | 1   | 1      | 1      | 1                  |
| 1   | 0   | 0      | 1      | 1                  |
| 0   | 1   | 1      | 0      | 0                  |
| 0   | 0   | 1      | 1      | 1                  |


![[exercises_mm1.pdf#page=2&rect=59,725,282,755|exercises_mm1, p.2]]
$$
(p \lor \neg q) \land (q \lor \neg r) \land (r \lor \neg p)
$$
$$
\neg (\neg p \land q) \land \neg (\neg q \land r) \land \neg (\neg r \land p)
$$

![[exercises_mm1.pdf#page=2&rect=64,668,238,723|exercises_mm1, p.2]]

a)11000
b)01101
c)11001
d)11011

![[exercises_mm1.pdf#page=2&rect=62,528,281,667|exercises_mm1, p.2]]
a) q -> p
b) q ^ ~p
c) q -> p
d) ~q -> ~p

![[exercises_mm1.pdf#page=2&rect=59,484,274,528|exercises_mm1, p.2]]
a)

| p   | q   | p ^ q | (p ^ q) -> p |
| --- | --- | ----- | ------------ |
| 1   | 1   | 1     | 1            |
| 1   | 0   | 0     | 1            |
| 0   | 1   | 0     | 1            |
| 0   | 0   | 0     | 1            |

b)

| p   | q   | p v q | p -> (p v q) |
| --- | --- | ----- | ------------ |
| 1   | 1   | 1     | 1            |
| 1   | 0   | 1     | 1            |
| 0   | 1   | 1     | 1            |
| 0   | 0   | 0     | 1            |

d)

| p   | q   | p ^ q | p -> q | (p ^ q) -> (p -> q) |
| --- | --- | ----- | ------ | ------------------- |
| 1   | 1   | 1     | 1      | 1                   |
| 1   | 0   | 0     | 0      | 1                   |
| 0   | 1   | 0     | 1      | 1                   |
| 0   | 1   | 0     | 1      | 1                   |


![[exercises_mm1.pdf#page=2&rect=62,461,282,484|exercises_mm1, p.2]]
This checks that they are either both 1 (p ^ q) or both 0 (~p ^ ~q). Which are the requirements for p<->q

![[exercises_mm1.pdf#page=2&rect=62,448,282,459|exercises_mm1, p.2]]
XOR is 1 when the values are different. Negating it means it is 1 when the values are the same, which is the same as p<->q

![[exercises_mm1.pdf#page=2&rect=58,294,280,447|exercises_mm1, p.2]]
a) p ^ q
b) p ^ ~q
c) ~p ^ ~q
d) p v q
e) p -> q
f) p XOR q
g) p <-> q

![[exercises_mm1.pdf#page=2&rect=62,197,283,293|exercises_mm1, p.2]]
a)

| p   | q   | r   | ~q v r | p -> (~q v r) |
| --- | --- | --- | ------ | ------------- |
| 1   | 1   | 1   | 1      | 1             |
| 1   | 1   | 0   | 0      | 0             |
| 1   | 0   | 1   | 1      | 1             |
| 1   | 0   | 0   | 1      | 1             |
| 0   | 1   | 1   | 1      | 1             |
| 0   | 1   | 0   | 0      | 1             |
| 0   | 0   | 1   | 1      | 1             |
| 0   | 0   | 0   | 1      | 1             |
b)

| p   | q   | r   | ~p  | (q -> r) | ~p -> (q -> r) |
| --- | --- | --- | --- | -------- | -------------- |
| 1   | 1   | 1   | 0   | 1        | 1              |
| 1   | 1   | 0   | 0   | 0        | 1              |
| 1   | 0   | 1   | 0   | 1        | 1              |
| 1   | 0   | 0   | 0   | 1        | 1              |
| 0   | 1   | 1   | 1   | 1        | 1              |
| 0   | 1   | 0   | 1   | 0        | 0              |
| 0   | 0   | 1   | 1   | 1        | 1              |
| 0   | 0   | 0   | 1   | 1        | 1              |
c) 

| p   | q   | r   | p -> q | ~p -> r | (p -> q) v (~p -> r) |
| --- | --- | --- | ------ | ------- | -------------------- |
| 1   | 1   | 1   | 0      | 1       | 1                    |
| 1   | 1   | 0   | 0      | 1       | 1                    |
| 1   | 0   | 1   | 0      | 1       | 1                    |
| 1   | 0   | 0   | 0      | 1       | 1                    |
| 0   | 1   | 1   | 1      | 1       | 1                    |
| 0   | 1   | 0   | 1      | 0       | 0                    |
| 0   | 0   | 1   | 1      | 1       | 1                    |
| 0   | 0   | 0   | 1      | 0       | 0                    |


![[exercises_mm1.pdf#page=2&rect=61,93,280,179|exercises_mm1, p.2]]

a)
$$
p \to (p \lor q)
$$
$$
\neg p \lor p \lor q \implies T \lor q
$$
b)
$$
(p \land q) \to (p \to q)
$$
$$
(p \land q) \to (\neg p \lor q)
$$
$$
\neg (p \land q) \lor (\neg p \lor q)
$$
$$
\neg p \lor \neg q \lor \neg p \lor q \implies \neg p \lor \neg p \lor T
$$
