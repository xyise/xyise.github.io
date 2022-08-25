---
layout: post
title:  "On Volatility Surfaces - Currencies"
categories: fx, crypto
---

<div style="display:none">
$
\newcommand\atm{\mathrm{ATM}}
\newcommand\xC[1]{#1\mathrm{C}}
\newcommand\xP[1]{#1\mathrm{P}}
\newcommand\xRR[1]{#1\mathrm{RR}}
\newcommand\xFLY[1]{#1\mathrm{FLY}}
$
</div>

<style>
    /* The . with the boxed represents that it is a class */
    .boxed {
    background: #eeeeee;
    color: black;
    border: 3px solid black;
    margin: 0px auto;
    width: 650px;
    padding: 10px;
    border-radius: 10px;
    }
</style>


<hr/>

**warnings**:
* this is incomplete (very far).
* probably nothing new to those who worked on fx options in trading/quant space. 

<hr/>

Here, I describe some basic concepts on FX (and crypto) volatility surfaces with the followings in mind: 
* No new concepts here. A great tutorial including detailed derivations is here: [FX volatility smile construction](https://core.ac.uk/download/pdf/6671945.pdf). 
* I focus on being precise in specifying the arguments in the volatility surfaces in order to *indicate* dependencies across different variables and parameters. Understanding the dependencies is useful for modelling volatility moves for risk management purposes - which is of my primary interest.  


# Black Scholes Implied Volatility 
Standard options such as European calls and puts trade by strikes and one can use the Black-Scholes (BS) pricing formula to convert a market value $V$ into a BS implied volatility $\sigma$:

\begin{equation}
V = V^{S}(S, \sigma, r_d, r_f; \kappa, \tau,  \phi) = 
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
\sigma = \sigma(\kappa, \tau, \phi; S, r_f, r_f)
\nonumber
\end{equation}

Deriving the volatilities across all strikes and expiries, and noting that the volatility is supposed to be independent of the option type (due to parity relationship), we construct a volatility *surface* in terms of strike $\kappa$ and time to maturity $\tau$:

<div class="boxed">
$$
\begin{equation}
\sigma^\kappa(\kappa, \tau; S, r_f, r_f)
\label{E:BS-vol}
\end{equation}
$$
</div>

Here, the super-script $\kappa$ is to indicate the surface is expressed in terms of strikes. 


# Forward Rate and Forward Value

The underlying contract of an option is a forward contract, its value $F$ (referred to as *Forward Value*) is given as

\begin{equation}
F = F(S, r_d, r_f; \kappa, \tau) = e^{-r_d\tau}(f(\tau) - \kappa) = 
Se^{-r_f \tau} - \kappa e^{-r_d\tau}.
\end{equation}

Observations: 
* Trivially, $F = 0$ if $\kappa = f(\tau)$. With the put-call parity, it is the strike level where the call and put values coincide. 
* Solving for $S$:

  $$ S = e^{r_f \tau} (F + \kappa e^{-r_d \tau}),$$
  
  the BS formula (\ref{E:BS}) can be written as 
  
  \begin{equation}
  V = V^F(F, \sigma, r_d, r_f; \kappa, \tau, \phi).
  \label{E:BS-F}  
  \end{equation}
  
  In fact, this formulation is used to calculate the delta sensitivity. 

# Delta and Moneyness

For FX options, the delta sensitivity is (typically) measured with respect to the underlying *forward value* $F$:

\begin{equation}
\Delta(\kappa, \tau, \phi) = 
\frac{\partial V^F}{\partial F} = 
\frac{\partial V^S}{\partial S}
\frac{\partial S}{\partial F} = \phi N(\phi d_+).
\end{equation}

With this delta definition, the put-call delta parity is 

$$ \Delta(\kappa, \tau, +1) - \Delta(\kappa, \tau, -1) = 1.0 $$

With this parity, the at-the-money (ATM) strike $K^\atm(\tau)$ for expiry $\tau$ is *defined* as 

$$ \Delta(K^\atm(\tau), \tau, +1) = 0.5 = -\Delta(K^\atm(\tau), \tau, -1). $$

For smiles (in-the-money or out-of-money), $K^{\xC{x}}(\tau)$ and $K^{\xP{x}}(\tau)$ (read as $x$-delta call and $x$-delta put, respectively) are defined as the strikes based on the corresponding delta values: 

$$
\begin{equation}
\left\{
\begin{array}{rcl}
\Delta(K^{\xC{x}}(\tau), \tau, +1) & = & x/100 \\
\\
\Delta(K^{\xP{x}}(\tau), \tau, -1) &=& x/100-1
\end{array}
\right.
\end{equation}
$$
where $0 < x < 100$. 

By definition, 

$$
K^{\xC{x}} = K^{\xP{(100-x)}}
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

For notational simplicity, let's combine the three expressions in (\ref{E:sigma-delta}) into a single function in negative put delta $y \in (0, 1)$:

$$
\sigma(y, \tau) := \left\{
\begin{array}{cc}
\sigma^{\xP{100y}}(\tau), & \text{if } 0 < y < 0.5 \\ \\
\sigma^{\atm}(\tau), & \text{if } y = 0.5 \\ \\
\sigma^{\xC{100(1-y)}}(\tau), & \text{if } 0.5 < y < 1
\end{array}
\right.
$$

or, equivalently and simply,

$$ \sigma(y, \tau) := \sigma^{\xP{100y}}(\tau) \quad\text{where}\quad 0 < y < 1$$

Adding all other parameters, we have a volatility surface in terms of $y$ and $\tau$

<div class="boxed">
$$
\begin{equation}
\sigma^y(y, \tau; S, r_d, r_f)
\label{E:BS-vol-delta}
\end{equation}
$$
</div>

The superscript $y$ is to indicate that the surface is expressed in terms of $y$, contrasting to the expression (\ref{E:BS-vol}), 


# Risk Factor Representation and Modelling

From the quantitative perspective, the core building block of any measurement models for risk management purposes is to specify how to perturb risk factors. Of course, the first step and the most important step is to define the risk factor representations. The rest of step is to specify perturbations in terms of the risk factors, and re-value the portfolio to the perturbed risk factors.  By the way, since the representation affect all the remaining steps, the act of choosing a specific risk factor representation is part of *modelling choices*. 

When it comes to currency options, we have at least two modelling choices based on the discussed above:

| choice | known as | spot | interest rates | volatility surface |
| :--: | :--: | :--: | :--: | :--: |
|1| Sticky Strike | $S$ | $r_d$, $r_f$ | $\sigma^\kappa$ by strike per (\ref{E:BS-vol}) |
|2| Sticky Delta | $S$ | $r_d$, $r_f$ | $\sigma^y$ by delta per (\ref{E:BS-vol-delta})|


To illustrate how each choice affects how risk factors are perturbed, let's focus how the volatility $\sigma_{K}$ at strike $K$ for a given expiry $\tau$ (which is omitted for notational simplicity).

For the first choice known as *Sticky Strike* approach, it is easy since we specify perturbation amounts $\delta \sigma_{K}$ *directly* in terms of strike $\kappa$. So, the volatility at $K$ is perturbed simply as

$$ \sigma_{K} \to \sigma_{K} + \delta \sigma_{K} $$

Here, perturbations on other risk factors $S$, $r_d$ and $r_f$ are not relevant here. 


For the second choice known as *Sticky Delta*, the situation is more complex. 

**TO BE CONTINUED**



{% comment %}
 For example, 
* sensitivities: perturb each risk factor by a tiny amount. 
* stress testing: perturb risk factors by significant amounts that reflect stresses. 
* market risk VaR: perturb risk factors by amounts equivalent to changes over a specific horizon (e.g. 1-day or 10-days)
* counterparty credit risk: simulate a series of perturbations and accumulate to generate scenarios at future time steps. 
{% endcomment %}