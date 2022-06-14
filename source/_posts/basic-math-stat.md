---
title: Basic Concepts of Mathematical Statistics
date: 2022-06-06 23:11:58
tags:
- review
- time series
- probability
mathjax: true
---

Note on Mathematical Statistics

* A dry list of concepts as a personal review note
* The main references is Wooldridge's Introductory Econometrics, Appendix C (mostly). Also, wikis and googling.

Among all many concepts, probably the <span style="color:red">key</span> ones are
* An estimator is a random variable, thus has its sampling distribution. 
* A (test) statistic is *any* function of a random sample, so is a random variable itself. Defining the function is entirely up to us. 


<style>
  /* For the page */
  html, body, .markdown-body {
    font-size: 12px;
  }

  /* For the markdown content only */
  .markdown-body {
    font-size: 12px;
  }

  .center {
    margin-left: auto;
    margin-right: auto;
  }
  td {
    text-align: center;
  }
  th {
    text-align: center;
}
</style>


# Populations, Random Variable and Random Sample


<table class="center">
<tr>
  <th>concept</th>
  <th>description</th>
  <th>comment</th>
</tr>
<tr>
  <td>statistical inference</td>
  <td>learning something about a <em>population</em> from a <em>sample</em> from that population 
  <td style="text-align:left">
  typically
  <ul><li>estimation</li><li>hypothesis testing</li></ul>
  </td>
</tr>
<tr>
  <td>population</td>
  <td>a group of all subjects (e.g. all people in the world) </td>
  <td><em>modelled</em> using probability space $(\Omega, \mathcal B, P)$</td>
</tr>
<tr>
  <td>random variable</td>
  <td>a <em>numerical</em> model for the population relationship of *interest* (e.g. height)</td> 
  <td>assignment of a value (or a vector of values) <br>$Y: \Omega \to \mathcal R^N$</td>
</tr>
<tr>
  <td>parameters</td>
  <td>parameters for pdf of the random variable (e.g. mean and variance)</td> 
  <td>$\theta$ in $f(y; \theta)$</td>
</tr>
<tr>
  <td>random sample</td>
  <td>a random vector $(Y_1, \cdots, Y_n)$, consisting of independent random variables (not realisations) with the common pdf 
  $f(y;\theta)$ of $Y$</td> 
  <td>$Y_i$ are known to be <em>independent, identically distributed</em> (<em>i.i.d.</em>)</td>
</tr>
</table>

# Estimator and Estimate

## Setup: Random Sampling

From a given random variable, construct a random sample

<table class="center">
<tr>
  <th>notation</th>
  <th>description</th>
</tr>
<tr>
  <td>$Y$</td>
  <td>a <em>random variable</em> representing a poulation with pdf $f(y;\theta)$ </td>
</tr>
<tr>
  <td>$Y_1, \cdots, Y_n$</td>
  <td> a random vector of $Y$
  </td>
</tr>
<tr>
  <td>$\mu$</td>
  <td> the mean of $Y$
  </td>
</tr>
<tr>
  <td>$\sigma^2$</td>
  <td> the variance of $Y$
  </td>
</tr>
</table>


## Examples of Estimators

Some of the most commonly referenced estimators are
<table class="center" style="width:75%">
<tr>
    <th>estimator</th>
    <th>definition</th>
    <th>comments</th>
</tr>
<tr>
    <td>sample average</td>
    <td>$\bar{Y} = n^{-1} \sum_{i=1}^{n} Y_i$</td>
    <td style="text-align:left"><ul><li> unbiased estimator for $\mu$. <li>no assumption is required </ul></td>
</tr>
<tr>
    <td>sample variance with <em>unknown</em> $\mu$</td>
    <td>$$S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (Y_i - \bar Y)^2$$</td>
    <td style="text-align:left"><ul><li>unbiased estimator for $\sigma^2$.
        <li>If $1/n-1$ is replaced by $1/n$, it is consistent but not unbiased.</ul></td>
</tr>
<tr>
    <td>sample variance with <em>known</em> $\mu$</td>
    <td>$$S^2 = \frac{1}{n} \sum_{i=1}^{n} (Y_i - \mu)^2$$</td>
    <td>unbiased estimator for $\sigma^2$.</td>
</tr>
<tr>
    <td>sample standard deviation</td>
    <td>$$S = \sqrt{S^2}$$
    <td style="text-align:left"><ul><li>not an unbiased estimator of $\sigma$. <li>a consistent estimator of $\sigma$</ul></td>
</td>
<tr>
    <td>standard error of the mean</td>
    <td>
    $$\mathrm{se} = \frac{S}{\sqrt{n}}$$
    </td>
    <td style="text-align:left"><ul><li>An estimator of the standard deviation of the sampling distribution of $\bar{Y}$. 
    <li>Generally, the standard error of any statistic (usually parameter estimator) can be described (<a href="https://en.wikipedia.org/wiki/Standard_error">wiki</a>)</ul></td>
</tr>
</table>


## Concepts

Tabularizing some of the key concepts: 
<table>
<tr>
    <th style="width:20%">concept</th>
    <th style="width:30%">description</th>
    <th style="width:50%">comments</th>
</tr>
<tr>
    <td>estimator of $\theta$</td>
    <td><span style="color: #990000">a function of a random sample</span> as a rule to assign <br> each outcome of the sample $\to$ a value of $\theta$<br>
    $W = h(Y_1, \cdots, Y_n)$</td>
    <td style="text-align:left">
    <ul><li>Being a *random variable*, the standard convention is to use a capital letter (e.g. $\bar {Y}$ for $\mu$)
      <li>The <em>practical convention</em>, however, is to denote it by $\hat{\theta}$, which is the same practical convention for the estimate (e.g. $\hat{\mu}$)
      </ul></td> 
</tr>
<tr>
    <td>estimate</td>
    <td>The specific value of $h$ with a particular outcome <br> $w = h(y_1, \cdots, y_n)$</td>
    <td style="text-align:left">
    <ul><li>Being a value (not a random variable), the standard convention is to use the lower case of the estimator (e.g. $\bar{y}$)
    <li>The <em>practical</em> convention is, however, to denote it by $\hat{\theta}$, which is the same practical convention for the estimator (e.g. $\hat{\mu}$)
    </ul></td>
</tr>
<tr>
  <td><span style="color: #aa0000">sampling distribution</span></td>
  <td>The distribution of an estimator</td>
  <td>
    <ul>
    <li>{% asset_img sampling-dist.png 200%}
    <li>In short, the statistical inference is to study the sampling distribution.
    </ul>
  </td>
</tr>
<tr>
  <td>sampling variance</td>
  <td>the variance of an estimator, and thus a constant and not a random variable.
    This should not be confused with the sample variance, which is an estimator (so a random variable) of $\sigma^2$. </td>
  <td>For example, the sampling variance of the sample average is given by (easy to show)
  $$
  \mathrm{Var}(\bar{Y}) = \sigma^2/n.
  $$
  </td>
</tr>
<tr>
    <td>unbiased Estimator</td>
    <td>An estimate $W$ of $\theta$ is *unbiased* if $E(W) = \theta$ for all possible values of $\theta$</td>
    <td style="text-align:left">
    <ul>
      <li> Notably, $\bar{Y}$ and $S^2$ are unbiased estimators for $\mu$ and $\sigma^2$, respectively.
      <li> Unbiasedness does <em>not</em> imply that the <em>estimate</em> is equal to $\theta$.
      <li> Unbiased estimator can be quite poor (e.g. $\hat{\mu} = Y_1)$.
    </ul>
    </td> 
</tr>
<tr>
  <td>Bias of Estimator</td>
  <td>Defined as $$\mathrm{Bias}(W) := E(W) - \theta.$$</td>
  <td></td>
</tr>
<tr>
  <td>Efficiency</td>
  <td>Let $W_1$ and $W_2$ be two <em>unbiased</em> estimators of $\theta$. $W_1$ is <em>efficient</em> relative to $W_2$ if <br>$\mathrm{Var}(W_1) \le \mathrm{Var}(W_2)$ <br> for <em>all</em> $\theta$, with strict inequality for at least one value of $\theta$</td>
  <td style="text-align:left">
  <ul>
    <li>$\bar{Y}$ is the <em>most efficient</em> (has the smallest variance) among all <em>unbiased</em> estimators that are <em>linear</em> combinations of the random sample (not difficult to show)
    <li>In general, it is possible to have two unbiased estimationrs where one has smaller variances for some values of $\theta$ while the other has smaller variance for other values of $\theta$. 
  </ul>
  </td>
</tr>
<tr>
  <td>mean squared error (MSE)</td>
  <td>$\mathrm{MSE}(W) = E[(W-\theta)^2]$ <br>
  Unlike efficieny, MSE can be used whether the estimators are unbiased or biased. </td>
  <td>can show <br> $\mathrm{MSE}(W) = \mathrm{Var}(W) + [\mathrm{Bias}(W)]^2$</td>
</tr>
<tr>
  <td>consistency</td>
  <td>Let $W_n$ be an estimator of $\theta$ based on a random sample of size $n$. $W_n$ is a consistent estimator of $\theta$ if $W_n \to \theta$.</td>
  <td style="text-align:left">
  <ul><li>More precisely, for every $\epsilon > 0$, <br> $P(|W_n-\theta| > \epsilon) \to 0 \ \textrm{as}\ n \to \infty$ 
  <li> Here, $\theta$ is said to be the <em>probability limit</em> of $W_n$, denoted as <br> $\plim(W_n)=\theta$
  </ul>
  </td>
</tr>
</table>


## Law of Large Numbers and Central Limit Theorem: Classical results on sample average

<table>
<tr>
    <th style="width:20%">concept</th>
    <th style="width:30%">description</th>
    <th style="width:50%">comments</th>
</tr>
<tr>
    <td>law of large numbers (LLN)</td>
    <td>Let $\bar{Y}_n$ be the same average of $Y_1, \cdots, Y_n$. Then,
    $$ \plim_{n\to\infty} \bar{Y_n} = \mu$$</td>
    <td style="text-align:left">
    <ul>
      <li>Thus, the sample average is a consistent estimator.
      <li>This is the <em>weak</em> law of large numbers [wiki](https://en.wikipedia.org/wiki/Law_of_large_numbers). If $\sigma^2$ is assumed to be finite, this law is not only easy to prove but we have a more precise statement, the <em>central limit theorem</em>.  
      <li>For the strong law and related proof, see <a href="https://terrytao.wordpress.com/2008/06/18/the-strong-law-of-large-numbers/">Prof Tao's blog</a>.
    </ul>
    </td> 
</tr>
<tr>
    <td>central limit theorem</td>
    <td>Let $Z_n$ be the standardised version of $\bar{Y}_n$
    $$Z_n = \frac{\bar{Y}_n - \mu}{\sigma/n}$$
    Then, it converges <em>in distribution</em> to the standard normal:
    $$P(Z_n \le z) \to \Phi(z) \ \textrm{as}\ n \to \infty$$
    </td>
    <td style="text-align:left">
    <ul>
      <li>$\sigma^2$ is assumed to be finite (otherwise, $Z_n$ would not be defined).
      <li>Whilst the law of large numbers says the sample average converges to $\mu$, this class central limit theorem describes the distributional aspect around $\mu$. 
      <li>This is the classical central limit theorem.
      <li>One can replace <span style="color: #ff0000">$\sigma$</span> by <span style="color: #ff0000">$S_n$</span> (sample standard deviation).
    </ul>
    </td> 
</tr>
</table>


## Confidence Interval Estimator

<table>
<tr>
    <th style="width:20%">concept</th>
    <th style="width:30%">description</th>
    <th style="width:50%">comments</th>
</tr>
<tr>
    <td>confidence interval estimator</td>
    <td>Given a confidence level $\gamma$ (e.g. 95%), a confidence interval estimator for $\theta$ is an interval such that
    $$P(u(Y_1, \cdots, Y_n) < \theta < v(Y_1, \cdots, Y_n)) = \gamma$$
    </td>
    <td style="text-align:left">
    <ul>
      <li>The boundary values $u(Y_1, \cdots, Y_n)$ and $v(Y_1, \cdots, Y_n)$ are random variables. 
      <li>Interval estimate is the interval when a specific realisations of $Y_i$ are plugged into $u$ and $v$. 
    </ul>
    </td> 
</tr>
</table>


**Application to the mean of a normal**
Recall that, if $Y$ is normal, the standardised version of (the sampling distribution of) the sample average follows a $t$-distribution:
\begin{equation}
\frac{\bar{Y} - \mu}{S/\sqrt{n}} \sim t_{n-1}.
\nonumber
\end{equation}
The most common interval estimator with the confidence level $\gamma := (1-\alpha)$ is
\begin{equation}
\begin{array}{ccccc}
\displaystyle \bar{Y} - c_{\alpha/2} \frac{S}{\sqrt{n}} & < & \mu & < & \displaystyle  \bar{Y} + c_{\alpha/2} \frac{S}{\sqrt{n}}. \\\\
\shortparallel & & & & \shortparallel \\\\
u(Y_1, \cdots, Y_n) & & & & v(Y_1, \cdots, Y_n)
\end{array}
\nonumber
\end{equation}
where $c_{\alpha/2}$ is the $100(1-\alpha/2)$-th percentile in the $t_{n-1}$ sitribution. 

# Hypothesis Testing and Test Statistic

A hypothesis test is about rejecting or not rejecting a null hypothesis.

<table>
<tr>
    <th style="width:15%">concept</th>
    <th style="width:42.5%">description</th>
    <th style="width:42.5%">comments</th>
</tr>
<tr>
  <td>null hypothesis</td>
  <td>The statement being tested. 
  <br>A typical form is
  $$H_0:\theta = \theta_0$$
  where $\theta$ is the <em>true</em> parameter (or the collection of true parameters or the model itself) based on the <em>population</em>.
  </td>
  <td style="text-align:left">
    <ul>
      <li>The null hypothesis is <em>presumed to be true</em> until the data <em>strongly suggest otherwise</em>. Just as a defendent is presumed to be innocent util proven guilty. 
      <li>For example, the hypothetical testing on a null hypothesis $$H_0: \mu = 0$$ is <em>not</em> about proving the mean is  (this would be a very difficult task if the true value were 0.000001).
    </ul>
  </td> 
</tr>
<tr>
  <td>alternative hypothesis</td>
  <td>The statement being tested against the null hypothesis. <br> A typical form is either one-sided
    $$H_1: \theta < \theta_0 \ \textrm{or} \ H_1: \theta > \theta_0 $$
    or two-sided:
    $$H_1: \theta \text{ not equal } \theta_0$$.
  </td>
  <td style="text-align:left">
    <ul>
    <li>To conclude that $H_0$ is false and $H_1$ is true, there should be evidence "beyond reasonable doubt" against $H_0$, which is quantified with respect to the <em>significance level</em> (e.g. 5%). 
    <li>The one-sided alternative hypothesis, say $\theta < \theta_0$, is used when it is not of an interest to show the other side of relation $\theta > \theta_0$. Showing a defendent is more than innocent is not of the interest in proving guilty.  
    </ul>
  </td>
</tr>
<tr>
  <td>Type I error & significant level</td>
  <td style="text-align:left">
    <ul>
    <li>Type I error: Rejecting the null hypothesis when it is in fact true
    <li>significant level $\alpha$ of a test: the probability of a Type 1 error
    $$\alpha = P(\text{Type I}) = P(\text{Reject }H_0|H_0)$$
    or, equivalently
    $$\alpha = P(\text{Reject }H_0 ; \theta={\color{blue} \theta_0})$$
  </td>
  <td style="text-align:left">
  <ul>
  <li>Type I error is also known as <em>false negative</em>, which means that $H_0$ is <em>falsely</em> deemed to be <em>positive</em> (rejected).
  <li>The significant level is <em>set before</em> the test. Common values are 10%, 5% and 1% although there are no clear justifications for them. 
  <li>By the way, why am I using ';' instead of '|'? See <a href="https://gist.github.com/xyise/fdb078d6488a73061c62270b5644b012">here</a>
  </ul></td>
</tr>
<tr>
  <td>Type II error & power</td>
  <td style="text-align:left">
  <ul>
  <li>Type II error: Failing to reject the null hypothesis when it is in fact false. 
  <li>power of a test $\pi({\color{red} \theta_1})$ against a <em>relevant</em> and <em>specific</em> alternative $\theta = {\color{red} \theta_1}$:
  $$\pi({\color{red} \theta_1}) = P(\text{Reject }H_0 ; \theta={\color{red} \theta_1})$$
  or, equivalently
  $$\pi({\color{red} \theta_1}) = 1 - P(\text{Type II} ; \theta={\color{red} \theta_1})$$
  </ul>
  </td>
  <td style="text-align:left">
  <ul>
    <li>type II error is also known as <em>false positive</em>, which means that $H_0$ is <em>falsely</em> deemed to be <em>positive</em> (not rejected).
    <li>Notice that a test's power is against a <em>specific</em> alternative hypothesis, making it as a function $\pi({\color{red} \theta_1})$ of ${\color{red} \theta_1}$. 
    <li>Whilst a power is loosely referred as $P(\text{Reject }H_0 ; H_1 \text{ is true})$, it is difficult to calculate as $H_1$ is typically not an equality. 
    <li>For a binary classification, there is only one alternativate and the power is called <em>sensitivity</em>.
    <li>Factors that make a power larger: significant level, difference in $\theta_0$ and $\theta_1$, sample size
    <li>In practice, a power is denoted simply as $\pi(\theta) = P(\text{Reject }H_1|\theta)$. 
  </ul>
  </td>
</tr>
</table>

An examples in [wiki](https://en.wikipedia.org/wiki/Power_of_a_test#Example) is illustrating where the hypotheses are $H_0:\mu=0$ and $H_1:\mu=1$. The power for $\mu = \theta$ is given by 
\begin{equation}
\pi(\theta) \approx 1 - \Phi( c - \frac{\theta}{\hat{\sigma}/\sqrt{n}}) \text{ with } c = \Phi^{-1}(1-\alpha)
\nonumber
\end{equation}
where the central limit theorm is applied for approximation. Observe that the power increases if
* a larger confidence level $\alpha$ (though $c$) is taken, 
* $\theta$ is taken further from $0$, or
* $n$ increases. 

Back to describing concepts:

<table>
<tr>
    <th style="width:15%">concept</th>
    <th style="width:42.5%">description</th>
    <th style="width:42.5%">comments</th>
</tr>
<tr>
  <td>test statistic</td>
  <td style="text-align:center"><span style="color: #990000">a function of a random sample</span> used in (statistical) hypothesis testing<br>
  Denoted by $T$ below.</td>
  <td style="text-align:left">
  <ul>
    <li>Recall that a <span style="color: #990000">statistic</span> is any function of a random sample; it is called an <em>estimator</em> if used for estimating a parameters while called a <em>test statistic</em> if used for hypothesis testing. 
    <li>Almost always, a test statistic takes values in $\mathcal R$. 
    <li>For a list of test statistics, see <a href="https://en.wikipedia.org/wiki/Test_statistic">wiki</a>. 
  </ul>
  </td>
</tr>
<tr>
  <td>rejection region & critical value</td>
  <td style="text-align:left">
    <ul>
      <li>If $t$ (a realisation of $T$) is inside the <em>rejection region</em> $R_c$, $H_0$ is rejected in favor of $H_1$. 
      <li>The boundary of the rejection region are called a critical value $c$. 
    </ul>
  </td>
  <td style="text-align:left">
    <ul>
      <li>We have $P(T \in R_c ; H_0) = \alpha$
      <li>If $T$ is real-valued,
      <ul>
        <li>one-sided left-tail: $$R_c = \{ t < c \} \text{ and } P(T < c) = \alpha$$
        <li>one-sided right-tail: $$R_c = \{ t > c\} \text { and } P(T > c) = \alpha$$
        <li>two-sided: $$R_c = \{ t < c_1 \text{ or } t > c_1  \}$$ and $$P(T < c_1) = P(T > c_1) = \alpha/2$$ 
      </ul>
    </ul>
  </td>
  <tr>
    <td>p-value</td>
    <td style="text-align:left">
      Consider a random sample $Y_1, \cdots, Y_n$, and fix a test-statistic $T$ for a hypothesis testing.
      <ul>
        <li>The p-value is the largest significance level at which we fail to reject the null hypothesis.
        <li>For a given realisation $t$, the probability to observe at least as <em>extreme</em> as $t$ if $H_0$ is assumed to be true. Thus,
        <ul>
          <li>one-sided left-tail: $p = P(T < t; H_0)$ 
          <li>one-sided right-tail: $p = P(T > t; H_0)$
          <li>two-sided and symmetric $T$: $p = P(|T|>|t|; H_0)$
        </ul>
        For two-sided with asymmetric $T$, there seems to be debates. 
      </ul>
      {% asset_img p-value.png 200%}
      </td>
    <td style="text-align:left">
    <ul>
      <li>p-value is a <em>random variable</em>.
      <li>Debates on the p-value for a two-tail test with asymmetric $T$: 
      <a href="https://stats.stackexchange.com/questions/140107/p-value-in-a-two-tail-test-with-asymmetric-null-distribution">here.</a>
      <ul>
        <li>consistent with the definition with symmetric rejection regions:
        $$p = 2 \min\{ P(T < t; H_0), P(T > t; H_0) \}$$
        (proof: not reject if $P(T < t ) \ge \alpha/2)$ and $P(T > t) \le 1-\alpha/2$. The largest of such $\alpha$ is $p$.) 
        <li>use the likelihood function
        $$p = P(f(T) < f(t))$$
        (this is like a one-sided test with the test-statistic $f(T)$)
      </ul>
      In the end, the p-value depends on the choice of the test-statistic $T$. It is up to us which one is better one. 
    </ul>
    </td>
  </tr>
</tr>
</table>

**Application to multinomial distribution**

Definition:
* Non-standard definition: A multinomial random vector with $K$ categories with $N$ trial is a vector-valued test-statistic $(X_1, \cdots, X_K)$ from a random sample $Y_1, \cdots, Y_N$ of a categorical random variable $Y$ where 
  * $Y_n$ takes a value in $\{1, \cdots, K\}$ with an event probability $p_k$ satisfying $\sum_{k=1}^{K} p_k = 1$. 
  * $X_k$ is the count of $Y_n$ such that $Y_n = k$. 
By definition, $\sum_{k=1}^{K} X_k = n$. 
* Standard versions are in [wiki](https://en.wikipedia.org/wiki/Multinomial_distribution) and [here](https://arxiv.org/pdf/2008.12682.pdf)

Unlike the examples we have seen so far, the random sampling is already embedded within the multinomial distribution. Thus, for a given realisation $(x_1, \cdots, x_K)$ with $\sum_{k=1}^{K}x_k = n$, one can form a hypothesis testing whether it is from a multinomial distribution with event probabilities $p_k$.

See [here](https://arxiv.org/pdf/2008.12682.pdf) for several test-statistics used to this end. 