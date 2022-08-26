# Selection Combining

## Channel model
Assuming flat slow fading channel, the received signal model is given by 
### $\begin{aligned} r = hs + n \end{aligned}$

where, $h$ is the channel impulse response, $r$ is the received signal, $s$ is the transmitted signal and $n$ is the additive Gaussian white noise $(AWGN)$.

Assuming small scale Rayleigh fading, the channel impulse response is modeled as complex Gaussian random variable with zero mean and variance $\sigma_h^2$
### $\begin{aligned} h \sim CN(0, \sigma_h^2) \end{aligned}$

Therefore, the instantaneous channel power is exponentially distributed
### $\begin{aligned} |h|^2 \sim \frac{1}{\sigma_h^2}e^{-|h|^2/ \sigma_h^2} \end{aligned}$
<!-- ### $|h|^2 \sim \frac{1}{\sigma_h^2}e^{-\frac{|h|^2}{\sigma_h^2}}$ -->

In the context of AWGN, the signal-to-noise ratio (SNR) for a given channel condition, is a constant. 
But in the case of fading channels, the signal-to-noise ratio is no longer a constant as the signal is fluctuating when passed through a fading channel. 
Therefore, for fading channel, the SNR has a random variable component built into it. Hence, we just don’t call it SNR, instead it is called ${\bf instantaneous \ SNR}$ which depends on the current conditions of the channel (or equivalently, the value of the random variable at that instant). 
Since the SNR is a random variable, we can also talk about its expected (average) value, which is called $\bf  average \ SNR$.

Denoting the average SNR as $\Gamma$ and for convenience, let’s assume that the average power of the channel is unity, $i.e. \sigma_h^2 = 1$
### $\begin{aligned} average \ SNR=E\{ {|h|^2} \} \cdot \frac{E\{ {|s|^2} \}}{\sigma_n^2} = \sigma_h^2 \cdot \Gamma = \Gamma \end{aligned}$

The instantaneous SNR $\gamma$ is given by
### $\begin{aligned} \gamma = |h|^2 \cdot \frac{E\{ {|s|^2} \}}{\sigma_n^2} = |h|^2\Gamma \end{aligned}$
Therefore, like the channel impulse response, the instantaneous SNR is also exponentially distributed
### $\begin{aligned} \gamma \sim \frac{1}{\Gamma}e^{-\gamma / \Gamma} \end{aligned}$


## Selection Combining
In selection combining, the received signal from the antenna that experiences the highest SNR (i.e, the strongest signal from N received signals) is chosen for processing at the receiver.

### $\begin{aligned} \omega_k = \left\{ \begin{array}{l} 1,  \ \gamma_k = arg \ \max\limits_{i=1, ..., N} \gamma_i \\ 0, \  \ otherwise \end{array} \right. \end{aligned}$

That is, the weight $\omega_k$ of path $i$ that has the highest $|h_i|$ is chosen.
### $\begin{aligned} \omega_k = 1 \ \ \ with \ \ k = arg \ \max\limits_{i=1, ..., N} |h_i| \end{aligned}$

Therefore, the output SNR (at the combiner output) is the maximum SNR of all the received signals
### $\begin{aligned} \gamma_{out} = arg \ \max\limits_{i=1, ..., N} \gamma_i \end{aligned}$

As we know, fading channels are characterized by fades, i.e, the period when the signal level falls below a certain threshold or certain noise level. 
During such fades, the user experiences signal outage. We would like to compute the probability, in certain fading channel, that a user will experience signal outage. 
This is called outage probability. Outage probability can be easily computed if we know the probability distribution characteristics of the fading.

For a selection combining scheme, for an user to experience outage, the SNR $\gamma_i$  of all the received branches should fall below the given threshold $\gamma_{t}$. 
In otherwords, the output SNR $\gamma_{out}$ at the combiner is below the threshold $\gamma_{t}$. The outage probability of selection combining receiver is given by 
### $\begin{aligned} P_{outage} &= P[\gamma_{out} < \gamma_{t}] \\ &= P[\gamma_{1}, \gamma_{2}, ..., \gamma_{n} < \gamma_{t}] \\ &= P[\gamma_{1} < \gamma_{t}]P[\gamma_{2} < \gamma_{t}]...P[\gamma_{n} < \gamma_{t}] \\ &= \prod_{i=1}^{n}P[\gamma_{i} < \gamma_{t}] \\ &= [1 - e^{-\gamma_{t} / \Gamma}]^N \end{aligned}$

For high average SNR conditions $\Gamma \rightarrow \infty$, the outage probability can be approximated as 
###  \begin{aligned} P_{outage} \propto \left( \frac{1}{\Gamma} \right)^N or \ \left( \frac{\gamma_{t}}{\Gamma} \right)^N \ ?? \end{aligned} 


## 





## References
:::info
Selection Combining – architecture simulation
December 10, 2019 by Mathuranathan
(https://www.gaussianwaves.com/2019/12/receiver-diversity---selection-combining/)
:::












