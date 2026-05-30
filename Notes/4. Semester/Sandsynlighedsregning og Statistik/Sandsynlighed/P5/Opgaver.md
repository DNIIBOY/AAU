## Problem 1: Parallel system
A system composed of n separate components is said to be a parallel system if it functions when at least one of the components functions. Independence of components is usually a key moment in designing a parallel system, e.g. to achieve independency of the components different operating systems or different types of processors can be chosen for different components.
Suppose that we have a parallel system with n independent components, each functions with probability $p_{i}, i = 1, \dots , n.$ What is the probability that the system work?
If $X$ is rv. describing how many components are working, the system will work if:
$$
P\{X\geq 1\} = 1 - (1-p_{1})(1-p_{2})\dots(1-p_{n})
$$