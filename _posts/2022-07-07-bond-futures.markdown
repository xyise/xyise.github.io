---
layout: post
title:  "Bond Futures and Cheapest-to-Deliver"
categories: math
---

The purpose of this article is to present the concept of cheapest-to-deliver bonds for bond futures in an *idealised* setting for illustration purposes. For practical backgrounds, see the [contract specification](https://www.cmegroup.com/markets/interest-rates/us-treasury/30-year-us-treasury-bond.contractSpecs.html) in CME and their [manual](https://www.cmegroup.com/education/files/understanding-treasury-futures.pdf).

# Bond Future Price and Conversion Factor

Bond futures are used to bet the direction of interest rate movement. Since the underlying deliverable assets are bonds, the rate would be closely linked to those bonds. Roughly speaking, the future price should reflect the value of a *hypothetical* bond paying 6% coupons (known as *notional coupon*) with time-to-maturity *comparable to* those of the deliverable bonds In the market where the bond trades with 6% yield, the hypothetical bond is at par, i.e. its present value is roughly 1. 

Now, the conversion factor $\mathrm{CF}_i$ for a bond $i$ is the clean price (to be precise, forward bond price) if the bond is assumed to be traded with 6% yield. The conversion factors of bonds with coupon rates less than the notional coupon would be less than 1 and vice versa.  

As an illustration, the bond PVs are shows by varying coupon rates and yields below in the left plot. PVs along the vertical center dotted line at 6% are conversion factors over coupons, also illustrated using a grey line in the right plot. Here, the time-to-maturity is assumed to be 10 year. 


|present values (PVs) of bonds|PVs at different yield rates|
| :--: | :--: |
|![pv-2d](/assets/bondfutures/pv-2d.png)|![pv-2d](/assets/bondfutures/pv-1d.png)|


# Settlement of Bond Futures

We assume:
* The notional amount of the bond future is set to one (1). This means the seller delivers a *single* bond from a set of the eligible bonds
* No lag between the date on which the futures price for the settlement is determined and the actual delivery date. 
* Accrual interests are ignored

On the settlement date $T$, 
* seller: select a bond $i$ from a basket of eligible bonds and delivers
* buyer: pays the conversion factor $\mathrm{CF}_{i}$ times the futures price $F_T$ at the settlement date. 

Observe that the market value of the delivered bond does not appear in the settlement, so there is no need to *fix* it (and thus not subject to potential rigging). 

Interestingly, the *size* of the settlement depends on which bond is delivered, which results in a *discontinuity* in the process: 
* Before the settlement, daily margins are based on the actual futures price; no conversion factor is (can not be) applied. But, the cash amount of the actual settlement reflects the conversion rate and can be larger or smaller than the future price on the settlement day
* I have seen people mistakenly think $1/\mathrm{CF}_{i}$ amount of bond needs to be delivered. Preparing a fractional amount of bonds is annoying.

# Cheapest-to-Deliver

The question is which bond the seller delivers, and of course, the cheapest one among the eligible bonds. The seller (who has the right to select which bond to deliver) wants to maximize the cash amount received over the value of the delivered bond $d$
\begin{equation}
d = \arg \max_{i} \frac{\mathrm{CF}_i F_T}{V_i} = \arg \min_i \frac{V_i}{\mathrm{CF}_i}
\nonumber
\end{equation}
where $V_i$ is the market clean value of the delivered bond, and the bond $d$ is the *cheapest-to-deliver* (CTD).

Under a *perfect* no-arbitrage condition, the net payout of the contract with the cheapest-to-deliver bond $d$ should be zero
\begin{equation}
0 = \mathrm{CF}_d F_T - V_d \quad \text{implying} \quad F_T = V_d / \mathrm{CF}_d.
\label{E:no-basis}
\end{equation}
For other deliverable bond $i$, the payout to the seller should be negative (i.e. a loss):
\begin{equation}
\mathrm{CF}_i F_T - V_i = V_i \left(\frac{\mathrm{CF}_i F_T}{V_i} - 1\right) \le V_i \left(\frac{\mathrm{CF}_d F_T}{V_d} - 1\right) = 0.
\nonumber
\end{equation}

Below, we show the present values $V_i/\mathrm{CF}_i$ after adjusting conversion factors are shown. 

|CF adjusted present values (PVs) of bonds|CF adjusted PVs at different yield rates|
| :--: | :--: |
|![pv-2d-adj](/assets/bondfutures/adj-pv-2d.png)|![pv-1d-adj](/assets/bondfutures/adj-pv-1d.png)|

Observe
* When the yield is larger than 6%, bonds with larger coupons (so, shorter durations) are cheaper to deliver. 
* When the yield is smaller than 6%, bonds with smaller coupons (so, longer durations) are cheaper to deliver

# Breaking Down, Basis and Optionality

So, when the bonds are trading at 6% yields, we have a problem since all bonds have the same present values after the conversion factor adjustment as illustrated below. And, one should model the optionality. Also, the net payout in (\ref{E:no-basis}) may not be zero, producing basis. 

![adj-pv-1d-y](/assets/bondfutures/adj-pv-1d-y.png)


# In Practice

The situation is more complex in practice since there are a finite number of eligible bonds and they are expected to have different maturities. But, the overall picture is the same. 
