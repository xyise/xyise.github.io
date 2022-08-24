---
layout: post
title:  "On Volatility Surfaces - Currencies"
categories: fx, crypto
---

<div style="display:none">
$
\newcommand\bsvol{\sigma^{\mathrm{BS}}}
\newcommand\bsdelta{\delta^{\mathrm{BS}}}
\newcommand\bsvega{\nu^{\mathrm{BS}}}
\newcommand\bsrho{\rho^{\mathrm{BS}}}
\newcommand\atm{\mathrm{ATM}}
\newcommand\xC[1]{#1\mathrm{C}}
\newcommand\xP[1]{#1\mathrm{P}}
\newcommand\xRR[1]{#1\mathrm{RR}}
\newcommand\xFLY[1]{#1\mathrm{FLY}}
$
</div>

<hr/>

**Todos**:
* this is incomplete (very far).
* probably nothing new to those who worked on fx options in trading/quant space. 
* this [old article](https://core.ac.uk/download/pdf/6671945.pdf) is great.

<hr/>

The purpose of this article is to lay out basic concepts that could be helpful to model FX (and crypto) volatility surfaces for risk measurement purposes. 


# Black Scholes Implied Volatility 
Standard options such as European calls and puts trade by strikes and one can use the Black-Scholes (BS) pricing formula to convert a market value $V$ into a BS implied volatility $\sigma$:

\begin{equation}
V(S, \sigma, r_d, r_f; \kappa, \tau,  \phi) = 
\phi e^{-r_d\tau} \left[f(\tau) N(\phi d_{+}) - \kappa N(\phi d_{-}) \right]
\label{E:BS}
\end{equation}

where 
* $S$: spot price
* $\sigma$: BS implied volatility
* $r_d$ and $r_f$: domestic and foreign interest risks
* $\kappa$: contractual option price
* $\tau$: time to option expiration date
* $\phi = +1$ for call, $\phi=-1$ for put
* $N(x)$: cdf of normal distribution
* $f(\tau) = f(S, r_d, r_f; \tau) = Se^{(r_d-r_f)\tau}$: forward rate for $\tau$
* $d_{\pm}$ is given as

  $$ d_{\pm} = \frac{\ln \frac{f(\tau)}{\kappa} \pm \frac{1}{2} \sigma^2 \tau}{\sigma \sqrt{\tau}} $$

Notes:
* $S$, $\sigma$, $r_d$, $r_f$ are market data
* $\kappa$, $\tau$, $\phi$ are contractual parameters

Fix a contract, observe market data $S$, $r_d$, $r_f$ through other contracts (e.g. spot contracts, domestic and foreign debt contracts, etc), and solve (\ref{E:BS}) for $\sigma$ to match the market value of the contract. This BS volatility is thus written as a function of contractual parameters, given current values of market parameters:

\begin{equation}
\sigma = \bsvol(\kappa, \tau, \phi; S, r_f, r_f)
\nonumber
\end{equation}

Deriving the volatilities across all strikes and expiries, and noting that the volatility is supposed to be independent of the option type (due to parity relationship), we construct a volatility surface in terms of strike $K$ and time to maturity $T$:

$$
\begin{equation}
\bsvol(K, T; S, r_f, r_f)
\label{E:BS-vol}
\end{equation}
$$

Here, $K$ and $T$ are considered *dummy* variables. 


# Forward Rate and Forward Value

The underlying contract of an option is a forward contract, its value $F$ (referred to as *Forward Value*) is given as

\begin{equation}
F(S, r_d, r_f; \kappa, \tau) = e^{-r_d\tau}(f(\tau) - \tau) = 
Se^{-r_f \tau} - \tau e^{-r_d\tau}.
\end{equation}

Observations: 
* Trivially, $F$ is zero if $\tau = f(\tau)$. Due to the put-call parity, it is the strike level where the call and put values coincide. 
* Solving for $S$:

  $$ S = e^{r_f\tau} (F + \tau e^{-r_d \tau}),$$
  
  the BS formula (\ref{E:BS}) can be written as 
  
  \begin{equation}
  V(F, \sigma, r_d, r_f; \kappa, \tau, \phi).
  \label{E:BS-F}  
  \end{equation}
  
  In fact, this formulation is used to calculate the delta sensitivity. 

# Delta and Moneyness

For FX options, the delta sensitivity is (typically) measured with respect to the underlying *forward value* $F$:

\begin{equation}
\bsdelta(\kappa, \tau, \phi) = \frac{\partial V}{\partial F} = \frac{\partial V}{\partial S}
\frac{\partial S}{\partial F} = \phi N(\phi d_+)
\end{equation}

where $\partial V/\partial F$ is of (\ref{E:BS-F}) and $\partial V/\partial S$ is of (\ref{E:BS}). 

With this delta definition, the put-call delta parity is 

$$ \bsdelta(\kappa, \tau, +1) - \bsdelta(\kappa, \tau, -1) = 1.0 $$

With this parity, the at-the-money (ATM) strike $K^\atm(\tau)$ for expiry $\tau$ is *defined* as 

$$ \bsdelta(K^\atm(\tau), \tau, +1) = 0.5 = -\bsdelta(K^\atm(\tau), \tau, -1). $$

For smiles (in-the-money or out-of-money), $K^{\xC{x}}(\tau)$ and $K^{\xP{x}}(\tau)$ (read as $x$-delta call and $x$-delta put, respectively) are defined as the strikes based on the corresponding delta values: 

$$
\begin{eqnarray*}
\bsdelta(K^{\xC{x}}(\tau), \tau, +1) & = & x/100 \\
\\
\bsdelta(K^{\xP{x}}(\tau), \tau, -1) &=& x/100-1.
\end{eqnarray*}
$$

By definition, 

$$
K^{\xC{x}} = K^{\xP{(x-100)}}
$$


Typically, practitioners consider $x = 25$ or $10$, or both. 

From the option market, *interpolate* the BS volatilities at $K^{\xP{x}}(\tau)$, $K^{\atm}(\tau)$, $K^{\xC{x}}(\tau)$ and obtain volatilities in terms of deltas-based moneyness:

$$
\begin{equation}
\sigma^{\xP{x}}(\tau), \quad  \sigma^{\atm}(\tau), \quad \sigma^{\xC{x}}(\tau)
\label{E:sigma-delta}  
\end{equation}
$$

Then, the risk-reversal (RR) and butterfly (FLY) volatilities are defined as

$$
\begin{eqnarray*}
\sigma^{\xRR{x}}(\tau)  & := &  \sigma^{\xC{x}}(\tau) - \sigma^{\xP{x}}(\tau)\\
\\
\sigma^{\xFLY{x}}(\tau)  & := &  \frac{\sigma^{\xC{x}}(\tau) + \sigma^{\xP{x}}(\tau)}{2} - \sigma^{\atm}(\tau)\\
\end{eqnarray*}
$$



**TO BE CONTINUED**