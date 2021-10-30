---
title: Bayesian Inference
date: 2021-10-30 12:03:53
tags:
- review
- bayes
mathjax: true
---


|{% asset_img bayes1_guardian.png 300 %}|{% asset_img bayes2_guardian.png 500 %}|
| :--: | :--: |
|[source](https://www.theguardian.com/law/2011/oct/02/formula-justice-bayes-theorem-miscarriage)|[source](https://www.theguardian.com/world/2021/apr/18/obscure-maths-bayes-theorem-reliability-covid-lateral-flow-tests-probability)|

This post is a personal review post on the Bayesian Inference.

# Prior and Posterial Probabilities

## pictorial illustration

A tree diagram would be the simplest way to illustrate the approach. 

{% asset_img bayesian_inference.png 1000 %}

The left and right sides show prior and posterial probabilities, respectively. Given the prior probabilities $P(A)$ and $P(B)$ (which is $1-P(A)$ by definition), the posterial probabilities $P(A|C)$, $P(B|C)$, $P(A|D)$ and $P(B|D)$ are the updated probabilities after taking into account the events $C$ and $D$ (which is the complement of $C$). 

## formal derivation

The formal derivation is simple
\begin{eqnarray\*}
P(A|C) & = & \frac{P(C|A)P(A)}{P(C)} \\\\
& = & \frac{P(C|A)P(A)}{P(C|A)P(A) + P(C|B)P(B)}
\end{eqnarray\*}

# Examples

## Covid (or any medical) test

Notation:
* $Y$ and $N$ are the events of being infected or not infected from Covid, respectively. 
* $+$ and $-$ indicates the test results, positive and negative, respectively. 

***Prior probabilities***: The test kit should disclose
* sensitivity (true positive rate): $P(+|Y)$
* specificity (true negative rate): $P(-|N)$

Table with all prior probabilities:

|test \ covid|Y|N|
| :--: | :--: | :--: |
|+|$P(+\|Y)$: sensitivity, true positive|$P(+\|N)$: false positive|
|-|$P(-\|Y)$: false negative|$P(-\|N)$: specificity, true negative|
|sum| 1 | 1 |

***Posterior probabilities***: When we perform a test, we would like to know
* $P(Y|+)$: correct test result
* $P(Y|-)$: incorrect test result

Table with all posterial probabilities: 

|test \ covid|Y|N|sum|
| :--: | :--: | :--: | :--: |
|+|$P(Y\|+)$: correct |$P(N\|+)$: incorrect | 1 |
|-|$P(Y\|-)$: incorrect |$P(N\|-)$: correct | 1 |

Now, let's consider the [RLF](https://www.nhs.uk/conditions/coronavirus-covid-19/testing/regular-rapid-coronavirus-tests-if-you-do-not-have-symptoms/) test kit, which has 99.9% sensitivity, or
$$ P(+|Y) = P(-|N) = 0.999$$
Then, we have
$$
P(Y|+) = \frac{P(+|Y)P(Y)}{P(+|Y)P(Y) + P(+|N)P(N)}
$$
and
$$
P(Y|-) = \frac{P(-|Y)P(Y)}{P(-|Y)P(Y) + P(-|N)P(N)}
$$

The prior infection probability $P(Y) = 1-P(N)$ is varied between 0 and 0.001 (0.1%), and an alternative sensitivity assumption $0.99$ (rubbish kit) is also considered:

{% asset_img bayes_covid.png 800 %}

Suppose that the prevailing infection probabilty is at 1/1000. If the test kit shows a positive result, I have about 50% chance to have a Covid. In comparison, a positive result from a rubbish kit means about 10% chance. In both cases, if negative test result means that there is almost no chance to have a Covid (so, you can go out).