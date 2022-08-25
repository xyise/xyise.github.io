---
layout: post
title:  "On Volatility Surfaces - Currencies"
categories: fx, crypto
---

<div style="display:none">
$
\newcommand\strike{\mathrm{strk}}
\newcommand\mdelta{\mathrm{dlt}}
\newcommand\forward{\mathrm{fwd}}
\newcommand\spot{\mathrm{spt}}
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

**To-dos**:
* Examples why delta-based smiles make more sense. 
* How to interpolate across strikes / deltas and across expiries. Adopt the approach in [Castagna and Mercurio](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=873788)?

<hr/>

Here, I describe some basic concepts on FX (and crypto) volatility surfaces with the followings in mind: 
* No new concepts here. A great tutorial including detailed derivations is here: [FX volatility smile construction](https://core.ac.uk/download/pdf/6671945.pdf). 
* I focus on being precise in specifying the arguments in the volatility surfaces in order to *indicate* dependencies across different variables and parameters. Understanding the dependencies is useful for modelling volatility moves for risk management purposes - which is of my primary interest.  


# Black Scholes Implied Volatility 
Standard options such as European calls and puts trade by strikes and one can use the Black-Scholes (BS) pricing formula to convert a market value $V$ into a BS implied volatility $\sigma$:

\begin{equation}
V = V^{\spot}(S, \sigma, r_d, r_f; \kappa, \tau,  \phi) = 
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
\sigma = \sigma^\strike(\kappa, \tau; S, r_f, r_f)
\label{E:BS-vol}
\end{equation}
$$
</div>

Here, the super-script `$\strike$' is to indicate the surface is expressed in terms of strikes. 


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
  V = V^\forward(F, \sigma, r_d, r_f; \kappa, \tau, \phi).
  \label{E:BS-F}  
  \end{equation}
  
  In fact, this formulation is used to calculate the delta sensitivity. 

# Delta and Moneyness

## Delta, ATM, Smiles

For FX options, the delta sensitivity is (typically) measured with respect to the underlying *forward value* $F$:

\begin{equation}
\Delta(\kappa, \tau, \phi) = 
\frac{\partial V^\forward}{\partial F} = 
\frac{\partial V^\spot}{\partial S}
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
where $0 < x < 100$. By definition, 

$$
K^{\xC{x}} = K^{\xP{(100-x)}}
$$


Typically, practitioners consider $x = 25$ or $10$, or both. 

From the option market, *search* for the BS volatilities at $K^{\xP{x}}(\tau)$, $K^{\atm}(\tau)$, $K^{\xC{x}}(\tau)$ and obtain volatilities in terms of deltas-based moneyness:

$$
\begin{equation}
\sigma^{\xP{x}}(\tau), \quad  \sigma^{\atm}(\tau), \quad \sigma^{\xC{x}}(\tau).
\label{E:sigma-delta}  
\end{equation}
$$

Here, the search is effectively solving equation (\ref{E:strike-to-putdelta}) below.

The risk-reversal (RR) and butterfly (FLY) volatilities are defined as

$$
\begin{eqnarray*}
\sigma^{\xRR{x}}(\tau)  & := &  \sigma^{\xC{x}}(\tau) - \sigma^{\xP{x}}(\tau)\\
\\
\sigma^{\xFLY{x}}(\tau)  & := &  \frac{\sigma^{\xC{x}}(\tau) + \sigma^{\xP{x}}(\tau)}{2} - \sigma^{\atm}(\tau)\\
\end{eqnarray*}
$$

## Delta-based Volatility Surface

To make mathematical treatments easier, let's combine the three expressions in (\ref{E:sigma-delta}) into a single function in terms of $y$, the negative of the put delta. 

$$ 
\begin{equation}
{\color{blue} y} = - \Delta(S, \sigma^\strike( {\color{red} \kappa}), r_d, r_f; {\color{red} \kappa}, \tau, -1), 
\label{E:strike-to-putdelta}
\end{equation}
$$

For each $\color{blue} y$, solve for $\color{red} \kappa$ to define a mapping $\zeta: {\color{blue} y} \mapsto {\color{red} \kappa}$

$$
{\color{red} \kappa} = \zeta({\color{blue} y}; S, r_d, r_f, \tau)
$$

Plugging this into $\sigma^\strike(\kappa, \tau)$, we have a volatility surface in terms of $y$ and $\tau$

<div class="boxed">
$$
\begin{equation}
\sigma = \sigma^\mdelta(y, \tau; S, r_d, r_f)
\quad \text{where} \quad 0 < y < 1.
\label{E:BS-vol-delta}
\end{equation}
$$
</div>

The superscript $\mdelta$ is to indicate that the surface is expressed in terms of $y$, contrasting to the expression (\ref{E:BS-vol}). 

With respect to this volatility surface $\sigma^\mdelta(y)$, $\kappa$ and $y$ satisfy

$$ 
\begin{equation}
{\color{blue} y} = - \Delta(S, \sigma^\mdelta( {\color{blue} y}), r_d, r_f; {\color{red} \kappa}, \tau, -1), 
\label{E:putdelta-to-strike}
\end{equation}
$$

which is the same as (\ref{E:strike-to-putdelta}) except $\sigma^\strike( {\color{red} \kappa})$ is replaced by $\sigma^\mdelta( {\color{blue} y})$



Expressing $\sigma^\mdelta$ in terms of $\xP{x}$, $\atm$ and $\xC{x}$, we have

$$
\sigma^\mdelta(y, \tau) = \left\{
\begin{array}{cc}
\sigma^{\xP{100y}}(\tau), & \text{if } 0 < y < 0.5 \\ \\
\sigma^{\atm}(\tau), & \text{if } y = 0.5 \\ \\
\sigma^{\xC{100(1-y)}}(\tau), & \text{if } 0.5 < y < 1
\end{array}
\right.
$$

or, equivalently and simply,

$$ \sigma^\mdelta(y, \tau) := \sigma^{\xP{100y}}(\tau) \quad\text{where}\quad 0 < y < 1$$




# Risk Factor Representation and Modelling

From the quantitative perspective, the core building block of any measurement models for risk management purposes is to specify how to perturb risk factors. Of course, the first step and the most important step is to define the risk factor representations. The rest of step is to specify perturbations in terms of the risk factors, and re-value the portfolio to the perturbed risk factors.  By the way, since the representation affect all the remaining steps, the act of choosing a specific risk factor representation is part of *modelling choices*. 

When it comes to currency options, we have at least two choices of risk factor representations based on the discussed above:

| choice | known as | spot | interest rates | volatility surface |
| :--: | :--: | :--: | :--: | :--: |
|1| Sticky Strike | $S$ | $r_d$, $r_f$ | $\sigma^\strike(\kappa, \tau)$ |
|2| Sticky Delta | $S$ | $r_d$, $r_f$ | $\sigma^\mdelta(y, \tau)$ |

Let's first agree on notations. For variable $x$,

| notation | description | comments |
| :--:     | :--: | :--: |
| $x_0$ | unperturbed value, referred to as *base* value | typically, current market data |
| $\delta x$ | perturbation | specified by risk models (stress shocks, simulated risk factor moves, etc) |
| $\tilde x$ | perturbed value, i.e. $\tilde x = x_0 + \delta_0$ | this is by definition |

Suppose that we have a single option position with strike $K$, and we would like to calculate how perturbations in risk factors affect its valuation. In order to value the position using the BS formula (\ref{E:BS}) before and after the perturbations, we need
* $S_0$, $r_{d,0}$, $r_{f,0}$, $\sigma_{0}(K)$ for base valuation
* $\tilde S$, $\tilde r_d$, $\tilde r_f$, $\tilde \sigma(K)$ for perturbed valuation

For spot ($S$) and interest rates ($r_d$, $r_f$), it is trivial because they are risk factors in both representations. So, the risk model under consideration specifies $\delta S$, $\delta r_d$ and $\delta r_f$. 

How about $\sigma(K)$ and $\tilde \sigma(K)$, the base and perturbed volatility for strike $K$? 

## Sticky Strike Approach


For the first choice known as the *Sticky Strike* approach, it is also trivial: 
* $\sigma_0(K)$ is obtained by reading off $\sigma_0^\strike(\kappa)$ volatility surface at $\kappa = K$. 
* The risk model specifies perturbation amount $\delta \sigma^\strike(\kappa)$ for each $\kappa$. So, the perturbed volatility at $K$ is trivially

  $$ \tilde\sigma(K) = \sigma_0(K) + \delta \sigma^\strike(K) $$

Note that perturbations on other risk factors $S$, $r_d$ and $r_f$ have no impact on $\tilde\sigma_K$. 

## Sticky Delta Approach


For the second choice known as the *Sticky Delta* approach, the situation is more complex. The risk model specifies perturbation amount $\delta \sigma^\mdelta(y)$ for each $y$, and we have the perturbed volatilities in terms of $y$:

$$ \tilde{\sigma}^\mdelta(y) = \sigma_0^{\mdelta}(y) + \delta \sigma(y)$$

For the base volatility $\sigma_0(K)$, we solve equation (\ref{E:putdelta-to-strike}) for ${\color{blue} y_0}$ with $\kappa = K$:

$$
{\color{blue} y_0} = - \Delta(S_0, \sigma^\mdelta_0( {\color{blue} y_0}), r_{d,0}, r_{f,0}; K, \tau, -1).
$$

Then, $\sigma_0(K) = \sigma^\mdelta({\color{blue} y_0})$. 

For the perturbed volatility $\tilde\sigma(K)$, solve the same equation for perturbed delta {\color{blue} \tilde y}, but with other risk factors perturbed as well: 

$$
{\color{blue} \tilde y} = - \Delta(\tilde S, \sigma^\mdelta( {\color{blue} \tilde y}), \tilde r_d, \tilde r_f; K, \tau, -1).
$$

Then, $\tilde \sigma(K) = \tilde \sigma^\mdelta({\color{blue} \tilde y})$. 




{% comment %}
 For example, 
* sensitivities: perturb each risk factor by a tiny amount. 
* stress testing: perturb risk factors by significant amounts that reflect stresses. 
* market risk VaR: perturb risk factors by amounts equivalent to changes over a specific horizon (e.g. 1-day or 10-days)
* counterparty credit risk: simulate a series of perturbations and accumulate to generate scenarios at future time steps. 
{% endcomment %}