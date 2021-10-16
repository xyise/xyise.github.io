---
title: Illustration of Volatility Clustering using Garch
date: 2021-09-18 19:23:09
tags:
- time series
mathjax: true
---

Source Codes: 
* [Jupyter notebook](https://github.com/xyise/xyise/blob/main/notebook/garch11/nb_garch_11.ipynb)
* [folder](https://github.com/xyise/xyise/tree/main/notebook/garch11)

# Opening

In financial time series data, it is common to observe *volatility clusturing*, meanining large changes tend to be clustered. For example, the figure below shows daily returns (light blues) of the S&P500 index where one can observe clusters of larges changes during 2009 (financial crisis) and 2020 (Covid-19 stress). 

{% asset_img returns.png %}

In this document, we demonstrate how the volatility clustering phenomena can be analysed using Garch(1,1), one of the model simplest models featuring *heteroskedasticity* (a fancy word indicating that the volatility is varying over time as indicated by the red line in the above figure.)

## Garch(1,1) Model

The model describes the dynamics for return variable $r_t$ and volatility variable $\sigma_t$:
\begin{eqnarray}
r_t&=&\mu+\sigma_t\epsilon_t \label{E:garch-return}\\\\
\sigma_{t+1}^2 & = &\sigma_\infty^2(1 - \beta-\gamma) + \beta \sigma_{t}^2 + \gamma \sigma_{t}^2\epsilon_{t}^2 \label{E:garch-vol}\\\\
\end{eqnarray}
where 
* $\epsilon_t$ is the innovation variable, assumed to be Gaussian (for simplicity) and i.i.d. over time.
* $\mu$ is the drift parameter for $r_t$
* $\sigma_\infty$, $\beta$ and $\gamma$ are Garch(1,1) model parameters with 
$$ \sigma_\infty > 0,\quad \beta \ge 0, \quad \gamma \ge 0,\quad \beta + \gamma < 1. \nonumber $$

References: See [this wiki](https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity) page for the model general model Garch(p,q) as well as other Garch families. 

# Properties

The followings are some of notable properties of the model:
* Re-writing the second equation above, it is easy to see that the Garch volatility $\sigma_t$ is mean-reverting:
\begin{equation}
\sigma_{t+1}^2 - \sigma_{t}^2 = (1 -\beta - \gamma)(\sigma_{\infty}^2 - \sigma_{t}^2) + \gamma\sigma_{t}^2(\epsilon_{t}^2-1)
\end{equation}
where $\sigma_t$ is the mean-reverting level and $(1-\beta-\gamma)$ is the mean-reverting speed. 
* Given the information up to today $t$, the *expected forward* variance at $\tau > t$ is fully determined and calculated as 
\begin{eqnarray\*}
\bar{\sigma}^2_t(\tau) & := & E[\sigma_{t+\tau}^2| \mathcal F_t ]\\\\
& = & \sigma_{\infty}^2 + (\beta+\gamma)^{\tau-1}(\sigma_{t+1}^2 - \sigma_\infty^2)
\end{eqnarray\*}
* Then, the *expected spot* variance over tenor $\tau$ is given by
\begin{eqnarray\*}
\bar{\nu}^2_t(\tau) & := &\frac{1}{\tau} \sum_{n=1}^{\tau} \bar \sigma_t^2(n)\\\\
& = &\sigma_{\infty}^2 + \frac{1-(\beta+\gamma)^\tau}{1-(\beta+\gamma)} \frac{\sigma_{t+1}^2 - \sigma_\infty^2}{\tau}
\end{eqnarray\*}

# Garch Filtering

Denoting the index price time series as
$$ S_0, S_1, \cdots, S_t, \cdots, $$
the goal is to derive the Garch volatility time series (red line in the above figure)
$$ \sigma_0, \sigma_1, \cdots, \sigma_t, \cdots. $$

To this end, 
* Set $r_t$ is the log-change of $S_{t}$, i.e.
$$ r_t = \ln { S_t / S_{t-1}}.$$
* $\mu$ and $\sigma_\infty$ are set to the unconditional mean and standard deviation of $\{r_t\}$ over all available data, respectively. 
* For now, we set $\beta = 0.9$ and $\gamma = 0.09$, which would be within typical ranges (based on google search). The estimation method is discussed later this document. 

Then, $\sigma_t$ can be derived using the following simple recursive algorithm:
* Initialise: $\sigma^2_0 = \sigma^2_\infty$ (or other value that is defendable)
* Assume that we have the volatility $\sigma_t$ as of time $t$. Then, 
    1. Set the innovation term $\epsilon_t = (r_t - \mu) / \sigma_t$, which is from (\ref{E:garch-return}).
    1. Set the next volatility $\sigma_{t+1}$ using (\ref{E:garch-vol}).

The above algorithm produces the corresponding innovation time series (illustrated figure below)
$$ \epsilon_1, \cdots, \epsilon_t, \cdots, $$
which are daily returns with Garch volatilities removed. 

{% asset_img innovations.png %}

While one may run many statistical tests, it is *visually obvious* that the filtered returns ($\epsilon_t$) are more i.i.d. than the original returns ($r_t$). So, from the statistically perspective, the former samples are more meaningful to work with. 

# Simulation

To simulate a sample path using Garch(1,1), we generate samples for the innovation variable $\epsilon_t$. For illustration purposes, the standard normal random variable is used although other variables such as Student-t distributions can be used as well. The top/left figure below shows simulated returns (in light blue) using Garch(1,1) together with the corresponding Garch volatilities (in red). Volatility clustering pheonomena are clearly visible. To contrast, the bottom/left figure shows simulated returns when the geometric brownian motion (GBM) is applied (by setting $\beta=\gamma=0$) with constant volatility $\sigma_\infty$. 

|returns  |levels   |
| :-------: | :-------: |
|{% asset_img simulation.png %}  |{% asset_img simulation-level.png %}|

Finally, for simulated price paths, set an initial value, say 0, and sum the returns cumulatively, and take the exponential to obtain the paths in the right figure above. 

# Estimation: MLE

So far, we have postulated certain values for $\beta$ and $\gamma$ without justifications. In this section, we estimate them by applying the standard maximum likelihood estimation method. 

## Objective Function

To this end, noting that $\sigma_t$ is determined one time step in advance:
$$
r_t | \mathcal F_{t-1} \sim \mathcal N (\mu, \sigma_{t}^2),
$$
the **likelihood function** for time step $t$ is given as
\begin{equation}
l(r_t|\mathcal F_{t-1}) = \displaystyle \frac{1}{\sqrt{2\pi \sigma_t^2}}
\exp\left( - \frac{(r_t - \mu)^2}{2\sigma_t^2}\right).
\end{equation}
Thus, we can write the **objective function** to maximize as below after doing the *usual steps* (multiply over samples, take log to turn into sum, ignore constant factors)
\begin{equation}
L(\beta, \gamma) = -\sum_{t} \left[ \ln \sigma_t^2 + \frac{(r_t - \mu)^2}{\sigma_t^2}\right].
\end{equation}

## Optimisation

Before running the actual optimisation function, we calculate $L$ over a range of $\beta$ and $\gamma$ values with constraint $\beta + \gamma < 1$ and obtain the following contour plot which indicates where the maximum is roughly located. 

{%asset_img mle-contour.png %}

Running an optimisation routine (e.g. Nelder-Mead), the maximum is achieved at
$$ (\beta, \gamma) = (0.88035162, 0.10633708), $$
which is not too far from our postulated values (0.9, 0.09).

# In Closing

When $\beta+\gamma=1$, we have
$$
\sigma_{t+1}^2 = \beta \sigma_{t}^2 + (1-\beta) \left( r_t - \mu \right)^2
$$
which can be easily shown to be the EWMA volatility. For typical parametrisations (e.g. \beta = 0.9), EWMA volatilities are very close to Garch(1,1) volatilities. But, as a long-term forecasting model, EWMA is not suitable (try it out).

