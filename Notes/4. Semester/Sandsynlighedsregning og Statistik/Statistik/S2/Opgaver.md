# Exercise 1
Repeat the last exercise of the lecture with different parameters: There’s a bag with 3 balls. Each ball is either orange or green. The number of green balls is $\theta \in \{0, 1, 2, 3\}$. Estimate $\theta$ by grabbing and putting back a ball 5 times for the cases:

## a) 4 out of the 5 of the balls are green. Calculate the likelihood for each possible value of $\theta \in \mathbb{N}$
$$
\prod_{i=1}^5P(X_i=x_i;\theta)
$$
$$
P(\theta=0) = 0 \cdot 0\cdot 0\cdot 0\cdot 1 = 0
$$
$$
P(\theta=1) = \frac{1}{3} \cdot \frac{1}{3}\cdot \frac{1}{3}\cdot \frac{1}{3}\cdot \frac{2}{3} = \frac{2}{243}
$$
$$
P(\theta=2) = \frac{2}{3} \cdot \frac{2}{3}\cdot \frac{2}{3}\cdot \frac{2}{3}\cdot \frac{1}{3} = \frac{16}{243}
$$
$$
P(\theta=3) = 1 \cdot 1\cdot 1\cdot 1\cdot 0 = 0
$$

## b) 4 out of the 5 of the balls are green. Calculate the likelihood and maximise the likelihood function for $\theta \in \mathbb{R}$ and then choose the best valid integer.
Probability of picking a green ball:
$$
p = \frac{\theta}{3}
$$
Where $\theta$ is the number of green balls in the bag

Likelihood function:
$$
\mathcal{L}_{5}(\theta) = 5\left( \frac{\theta}{3} \right)^4\left( 1-\frac{\theta}{3} \right) = 5 \frac{\theta^4}{81}\cdot \frac{3-\theta}{3} = \frac{5\theta^4(3-\theta)}{243} = \frac{15\theta^4 - 5\theta^5}{243}
$$
To maximise, we set the derivative to 0:
$$
\frac{d\mathcal{L}_{5}}{d\theta} = \frac{60\theta^3 - 25\theta^4}{243} = 0
$$
Solving for $\theta$, we find:
$$
\theta = 0 \lor \theta= \frac{12}{5}
$$
Since $\mathcal{L}_{n}(0) = 0$, the first solution is the minimum, and the maximum must be $\theta=\frac{12}{5} = 2.4$.
There cannot be $0.4$ of a ball in the bag, so we must find the best of the two integers:
$$
\mathcal{L}_{5}(2) = \frac{80}{243} \approx 0.3292
$$
$$
\mathcal{L}_{5}(3) = 0
$$
#### Using log-likelihood:
$$
\ell_{5}(\theta) = \ln(\mathcal{L_{5}}) = \ln\left( \frac{5\theta^4(3-\theta)}{243} \right) = \ln\left( \frac{5}{243}\theta^4(3-\theta) \right) = \ln(5) - \ln(243) + 4\ln(\theta) + \ln(3-\theta) 
$$
$$
\frac{d\ell_{5}}{d\theta} = 0 - 0 + \frac{4}{\theta} + \frac{1}{3-\theta}(-1) = \frac{4}{\theta} - \frac{1}{3-\theta}
$$
Set to 0 for maximum:
$$
\frac{4}{\theta} - \frac{1}{3-\theta} = 0 \implies \frac{4}{\theta} = \frac{1}{3-\theta} \implies 4 =  \frac{\theta}{3-\theta} \implies 12-4\theta = \theta \implies 12=5\theta \implies \theta=\frac{12}{5}
$$

## c) 3 out of the 5 of the balls are green. Calculate the likelihood for each possible value of $\theta \in \mathbb{N}$
$$
P(\theta=0) = 0 \cdot 0\cdot 0\cdot 1\cdot 1 = 0
$$
$$
P(\theta=1) = \frac{1}{3} \cdot \frac{1}{3}\cdot \frac{1}{3}\cdot \frac{2}{3}\cdot \frac{2}{3} = \frac{13}{27}
$$
$$
P(\theta=2) = \frac{2}{3} \cdot \frac{2}{3}\cdot \frac{2}{3}\cdot \frac{1}{3}\cdot \frac{1}{3} = \frac{11}{27}
$$
$$
P(\theta=3) = 1 \cdot 1\cdot 1\cdot 0\cdot 0 = 0
$$
## d) 3 out of the 5 of the balls are green. Calculate the likelihood and maximise the likelihood function for $\theta \in \mathbb{R}$ and then choose the best valid integer.
Probability:
$$
p = \frac{\theta}{3}
$$
Likelihood function:
$$
\mathcal{L}_{5}(\theta) = \begin{pmatrix}5\\3\end{pmatrix}p^3(1-p)^2 = 10\left( \frac{\theta}{3} \right)^3\left( 1-\frac{\theta}{3} \right)^2 = 10 \frac{\theta^3}{27} \frac{(3-\theta)^2}{9}
$$
$$
\ell_{5}(\theta)=\ln(\mathcal{L}_{5}(\theta)) = \ln\left( \frac{10}{27}\theta^3 (3-\theta)^2 \frac{1}{9}\right) = \ln(10) - \ln(27) + 3\ln(\theta)+2\ln(3-\theta)-\ln(9)
$$
$$
\frac{d\ell_{5}}{d\theta} = 0 -0 +\frac{3}{\theta} + \frac{2}{3-\theta} (-1) - 0 = \frac{3}{\theta} - \frac{2}{3-\theta}
$$
Setting to 0:
$$
\frac{3}{\theta} - \frac{2}{3-\theta}  = 0 \implies \frac{3}{\theta} = \frac{2}{3-\theta} \implies 9-3\theta = 2\theta \implies 9 = 5\theta \implies \theta = \frac{9}{5} = 1.8
$$
Picking the best integer value:
$$
\mathcal{L_{n}}(1) = \frac{40}{243}
$$
$$
\mathcal{L_{n}}(2) = \frac{80}{243}
$$
So there is highest likelihood of 2 green balls in the bag.

# Exercise 2
The room temperature during a PhD course was recorded using a Raspberry Pi and a temperature sensor.
## a) Calculate the sample mean $\bar{X}_{n}$ and variance $S_{n}^2$ of the temperature with all the $n = 253$ measurements
$$
\bar{X}_{n} = \frac{6760.07}{253} = 26.72
$$
$$
S_{n}^2 = \frac{28.325}{253-1} = 0.1124
$$
## b) Assume that $\bar{X}_{n}$ is the true temperature $\mu$ and that $S_{n}^2$ is the real variance of the Gaussian noise that affects each measurement of the sensor, denoted by $\sigma^2$. Consequently, assume that the temperature measurements have a distribution $X_{i} \sim N(\mu, \sigma^2)$. Plot the likelihood or log-likelihood function for the first 10 and with the first 100 measurements.

$$
\mu_{10} = 26.655
$$
$$
\sigma_{10}^2 = 0.001094
$$
$$
\sigma_{10} = \sqrt{0.001094} = 0.03308
$$
$$
\mathcal{L_{10}}(x) = \frac{1}{\sqrt{ 2\pi }\cdot0.03308} e^{-\frac{(x-26.655)^2}{2\cdot 0.001094}}
$$