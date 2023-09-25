  ## Motivation
Estimation of momoents is not possible for incompleted observed survival data.        
Likelihood, with good properties(e.g. consistent), is well-defined to capture the partial information contained in partial observations.    
There's also simple way to combine different types of likelihood(full/partial observed information).

## Likelihood Definition
### Discrete case
Given observation data $X=x$(x fixed), the likelihood function for $\theta$ is :
$$L(\theta) = P(x|\theta)$$
### Continuous case
Given $X\in(x-\epsilon/2, x+\epsilon/2)$ ,
$$ L(\theta) = P[{X\in(x-\epsilon/2, x+\epsilon/2)}|\theta]$$
$$L(\theta) = \int^{x+\epsilon/2}_{x-\epsilon/2}f(u|\theta)du$$
For $\epsilon\rightarrow0$,
$$L(\theta) = \epsilon f(x|\theta)$$
As $\epsilon$ is arbitrary multipicative constant, it can be ignored since we want to maximize $L(\theta)$ by $\theta$.    
The likelihood function is :
$$L(\theta) = f(x|\theta)$$

The actual value of $L$ is not meaningful, but the relative quantity is meaningful.

## Combining Likelihood
We consider each subject as independent individuals, 
$$L(\theta) = P(x_1,x_2,...,x_n|\theta)$$
$$L(\theta) = \Pi_{i} P(x_i|\theta)\ \ or\ \ L(\theta)=\Pi_i f(x_i|\theta)$$

Example:    
The probability model is $T_i =Exp(\lambda)$
## Likelihood for fully-observed data
$$L(\lambda) = \Pi_i f(t_i|\lambda)$$
In this case
$$L(\lambda) = \lambda^ne^{-\lambda\sum_{i=1}^nt_i}$$
$$\hat\lambda = \frac{1}{\bar t}$$
## Likelihood for censored data
### Right censoring    
For some observations, we only know $T>t$  
Their likelihood contributions can be expressed by:
$$L_j(\lambda) = P(T>t|\lambda) = S(t|\lambda)$$
Combining full-observed and censored data, the likelihood function is:
$$ L(\lambda) = \Pi_if(t_i|\theta)\Pi_jS(t|\lambda)$$
### Left censoring
For some observations, we only know $T<t$  
Their likelihood contributions can be expressed by:
$$L_j(\lambda) = P(T<t|\lambda) = F(t|\lambda)$$
Combining full-observed and censored data, the likelihood function is:
$$ L(\lambda) = \Pi_if(t_i|\theta)\Pi_jF(t|\lambda)$$
- The estimations are still consistent, but due to lack of information their efficiency decreases(variance increased) compared with fully-observed estimation. 
### Interval censoring
For some observations, we only know $L<t<U$
Their likelihood contributions can be expressed by:
$$L_j(\lambda) = P(L<T<U|\lambda) = F(U|\lambda)-F(L|\lambda)$$
### Double censoring
For all observations, we only know whether $T<t$ or not.
For obs that we know $T_i<t$, their likelihood contribution is 
$$ L_i(\lambda) = F(t|\lambda)$$
else,
$$L_j(\lambda) = S(t|\lambda)$$

## Likelihood for truncated data
### Left truncation
There is a case that we can not observe an event if $T<u$ , the subjects enrolled are actually biased sample, some additional subjects were unable to be oberved.    
In this case, the likelihood contribution by the fully-observed information should be corrected:
$$ L_i(\lambda) = f(t_i|T>u; \lambda)$$
$$L_i(\lambda) = \frac{f(t_i|\lambda)}{S(u|\lambda)}$$
- Note $S \in (0,1)$ , $L$ actually get inflated.

### Right truncation
A case that we can not observe an event if $T>u$
$$ L_i(\lambda) = f(t_i|T<u; \lambda)$$
$$L_i(\lambda) = \frac{f(t_i|\lambda)}{F(u|\lambda)}$$
To realistically account for the randomness of censoring and its effect, we consider the censoring as random variable. (We must consider the distributions of 2 random variable: time to event & time to cens
oring) 

### Random Censorship model
Let r.v. $\tilde T$ denote the true survival time and $C$ denote the random censoring time
$$\tilde T|X \sim S(t|\theta,x)$$
$$ C|X \sim G(t|\eta,x) = P(C>t|\eta,x)$$
$$\tilde T \perp C|X $$
We observe $\{ t_i, \delta_i, x_i\}_{i=1}^n$,
$$t_i = min(\tilde t_i, c_i)$$
$$\delta_i = I\{\tilde t_i\le c_i\}$$
Under the assumption of *random cencoring*(above), each observation is ind. and thus makes an ind. contribution $L_i(\theta)$ to the likelihood:
for $t_i = t, \delta_i = 1: L_i(\theta) = f(t|x_i, \theta)G(t|x_i,\eta)$
for $t_i = t, \delta_i = 0: L_i(\theta) = S(t|x_i,\theta)g(t|x_i,\eta)$
Thus,
$$
\begin{split}
L(\theta) &= \prod_i L_i(\theta)\\
&\propto \prod_if(t_i|x_i,\theta)^{\delta_i}S(t_i|x_i,\theta)^{1-\delta_i}
\end{split}
$$ 
proof:
![[5b0a8dfe2d1abd72dfd1a4ee64eccf3.jpg]]
We get the same likelihood as in the fixed censoring, making much convenience since we needn't model the censoring mechanism.

#### Speacial case: Random Entry
Random entry with a fixed censoring date
Entry date: $A_i \sim G'(\eta)$
Censoring date: $C_i' = c$
True Censoring time: $C_i = c - A_i$
Then under the assumption $A_i \perp \tilde T_i$:
$$ \tilde T_i \sim S(\theta)$$
$$ C_i \sim G(\eta)$$
$$ C_i \perp \tilde T_i$$
	We must consider the dependence or independence between $\tilde T_i$ and $C_i$, or our estimation may be biased, since the computation of likelihood is under the assumption of (conditional) independence.

### Independent Censoring 
Censoring mechanisms for which the 
$$L(\theta) = \prod_i f(t_i|x_i,\theta)S(t_i|x_i,\theta)$$
is correct are called *independent censoring*. Random censoring is a special case. 

### Non-informative Censoring
In the assumption of the random censorship, $C_i \sim G(\eta, x_i)$. We are assuming the distribution of the censoring time does not depend on the parameter of interest $\theta$. 
This assumption is referred to as non-informative censoring.

If the assumption is violated, with other assumptions holding, the main consequence is a loss of efficiency instead of  bias.

