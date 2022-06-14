---
title: Linear Projection & Conditional Expectation
date: 2022-05-17 21:09:44
tags:
- review
- time series
- probability
mathjax: true
---

Conditional Expectation, Linear Projection, Regression, Normal Distibution and Matrix Decomposition are all connected.

The purpose of this page is to review (mostly to remind myself of) topics related to conditional expectations and linear projections of random variables. Before we begin, a few key notations:
* $'$ is used to represent the transpose operator. 
* $\vec { } \ $ is used to represent a vector. Unless stated otherwise, we assume a *column* vector.





# Illustration of Conditional Expectation and Linear Projection

The content of this section can be summarised using the illustrated plots below. 

|special case of normal distribution|general case|
| :--: | :--: |
|{% asset_img ce_lp_linear.png 400 %}|{% asset_img ce_lp_nonlinear.png 400 %}|
|$Y=1+X+\epsilon$|$Y=1+X+X^2+\epsilon$|

[codes](https://github.com/xyise/xyise/blob/main/notebook/conditional_expectation/nb_conditional_expectation.ipynb)

* left: For normal distributions, the conditional expectation and the linear projection with a constant term are the same. 
* right: In general, it is not the case. 


*** 

# On Conditional Expectation

following [this](https://www.ee.nthu.edu.tw/cschang/Talk01142008.pdf)...

## Probability Density Functions

First, recall the probability density function... 

*Note*: For discrete random variables, it is more appropriate to use term *probability mass function*...

* Consider two discrete random variables $X$ and $Y$. 
* **joint** pdf (or pmf with m = mass): $p(x,y) = P(X=x, Y=y)$
* **marginal** pdf: 
    * $p_X(x) = P(X=x) = \sum_{y} p(x,y)$
    * $p_Y(y) = P(Y=y) = \sum_{x} p(x,y)$
* **conditional** pdf: 
$$p_{Y|X}(y|x) = P(Y=y|X=x) = \displaystyle \frac{p(x,y)}{p_X(x)}$$


## Definition

The conditional expectation of $Y$ given $X=x$ is defined as
$$ E[Y|X=x] = \sum_{y} y p_{Y|X}(y|x).$$
So, $E[Y|X]$ is a *function* of $X$. 


## Properties

Straightforward to prove the following properties
* tower rule: 
    $$E[E[Y|X,Z]|X] = E[Y|X]$$
* special cases: 
    * expectation of conditional expectation = expectation
    $$E[E[Y|X]] = E[Y]$$
    * conditional expectation of conditional expectation = conditional expectation
    $$E[E[Y|X]|X] = E[Y|X]$$
* conditioning is to freeze the conditioning variable. so, for a 1D function $h$:
$$E[h(X)Y|X] = h(X)E[Y|X].$$


## Mean Squared Error and Best Predictor

The conditional expectation $E(Y|X)$ is the minimizing function of the mean squared error
\begin{equation}
E[(Y-f(X))^2].
\nonumber
\end{equation}
over 1D functions $f$. Thus, the conditional expectation is the *best predictor* of $Y$ given $X$. 

To prove it is surprisingly easy. Denoting $h(X) = E(Y|X) - f(X)$, 
we have
\begin{eqnarray}
E[(Y - f(X))^2] & = & E\left[ \left((Y-E[Y|X]) + h(X)\right)^2 \right] \nonumber \\\\
& = & E\left[(Y-E[Y|X])^2\right] + E[h(X)^2] + 2 E[ (Y-E[Y|X])h(X)] \nonumber \\\\
& \ge & E\left[(Y-E[Y|X])^2\right], \nonumber
\end{eqnarray}
since the last term is zero:
\begin{equation}
E[ (Y-E[Y|X])h(X)] = E[E[(Y-E[Y|X])h(X)|X]] = E[h(X)E[Y-E[Y|X]|X]] = 0
\nonumber
\end{equation}
due to the tower rule. 


## Extension to Random Vector $X$

It is straightforward to extend to the case where $X$ is a multivariate random variable or random vector:
\begin{equation}
\vec X = (X_1, \dots, X_K).
\nonumber
\end{equation}

***

# On Linear Projection

Following Chapter 4, Time Series Analysis by Hamilton....

*Settings*: 
* $X$ and $Y$ are as before except $X$ is assumed to be a random vector, represented as $\vec X$. 
* Often, one of its entries is a constant $1$. 

## Definition 

Given $\vec X$, the prediction function for $Y$ is restricted to a linear function in $X$:
\begin{equation}
Y = \vec \alpha' \vec X
\nonumber
\end{equation}
where $\alpha$ is a vector parameter.

The linear projection of $Y$ on $\vec X$ is defined as
\begin{equation}
\hat{P}(Y|\vec X) = \vec \alpha' \vec X
\nonumber
\end{equation}
such that
\begin{equation}
E[(Y - \vec \alpha'\vec X)\vec X'] = \vec 0'
\label{E:linear-projection}
\end{equation}

For an illustration how the linear projection compares to the conditional expectation, go to the top of this page. 

**Solution**: From the definition, the solution of the linear projection is
\begin{equation}
\vec \alpha' =  E(Y \vec X') \left[E(\vec X \vec X')\right]^{-1}.
\label{E:sol-linear-projection}
\end{equation}


**Notation**: Hamilton uses the hat notation ($\hat{ }$) to differentiate it from the conditional expectation.
* $\hat{P}(Y|\vec X)$: linear projection of $Y$ into $\vec X$. 
* $\hat{E}(Y|\vec X)$: linear projection of $Y$ into $\vec X$ with a constant term, i.e. 
$$\hat{E}(Y|\vec X) := \hat{P}(Y|\vec X, 1)$$


## Properties

* Mean Squared Error (MSE) and Best Prediction: The linear projection produces the smallest mean squared error among all linear predictions. The proof, resembling that for conditional expectation, is simple. 

* Gaussian and Conditional Expectation: If the random vectors $\vec X$ and $\vec Y$ are Gaussian, the conditional probability is also a Gaussian with the mean and the covariance equal to the linear projection and MSE. 

* Linear Regression: Consider an ordinary least square regression:
\begin{equation}
\vec\beta = \left[ \sum_{i=1}^{N} \vec x_{i} \vec x_{i}' \right\]^{-1} \left[ \sum_{i=1}^{N} \vec x_{i} y_{i}\right]
\nonumber
\end{equation}
where $'\vec x_i$ is the $i$-th observation. 
The linear projection solution in (\ref{E:sol-linear-projection}) paralles the solution 
\begin{equation}
y_i = \vec\beta' \vec x_i + u_{i}
\nonumber
\end{equation}

## Updating Linear Projection

Let $\vec Y = (\vec Y_1, \vec Y_2, \cdots, \vec Y_N)$ be a set of $N$ random vectors, and let $\Omega$ be its second-moment matrix
\begin{equation}
\Omega = E[\vec Y \vec Y'],
\nonumber
\end{equation}
whose the sub-block at $(i,j)$ is
\begin{equation}
\Omega_{ij} = E[\vec Y_i \vec Y_j']
\nonumber
\end{equation}

Below, for notational simplicity, we drop $\ \vec{}\ $.


One can construct a sequence of linear projections and mean-square errors (MSE):
| $n$  | projection   |  MSE  |
| :--: | :--: | :--: |
| 2 | $\hat P(Y_2 \vert {\color{blue} Y_1}) = \Omega_{21} \Omega_{11}^{-1} {\color{blue} Y_1}$ | $\Omega_{22} - \Omega_{21}\Omega_{11}^{-1}\Omega_{12}$ |
| 3 | $\hat P(Y_3 \vert {\color{red} Y_2}, {\color{blue} Y_1}) = \hat P( Y_3 \vert {\color{blue}  Y_1}) + H_{32}H_{22}^{-1}({\color{red}  Y_2} - \hat P({\color{red}  Y_2} \vert {\color{blue}  Y_1}))$ | $H_{33}-H_{32}H_{22}^{-1}H_{23}$| 
|...|...|...|

where $H_{ij}$ is the second-moment matrix after taking the projection on $Y_1$ out:
\begin{equation}
H_{ij} = E[(Y_i - \hat P(Y_i|{\color{blue} Y_1}))(Y_j - \hat P(Y_j|{\color{blue} Y_1}))'] \quad i,j=2,3.
\nonumber
\end{equation}

Observe that the coefficients in the projection formula have a 'covariance/variance'-like form (as the correct means are not taken out):
\begin{equation}
\Omega_{21}\Omega_{11}^{-1} = \frac{E[{\color{red} Y_2} {\color{blue} Y_1}']}{E[{\color{blue} Y_1 Y_1'}]}
\quad\textrm{and}\quad
H_{32}H_{22}^{-1} = \frac{E[({\color{green} Y_3} - \hat P({\color{green} Y_3}|{Y_1}))({\color{red} Y_2} - \hat P({\color{red} Y_2}|{Y_1}))']}{E[({\color{red} Y_2} - \hat P({\color{red} Y_2}|{Y_1}))({\color{red} Y_2} - \hat P({\color{red} Y_2}|{Y_1}))']}
\nonumber
\end{equation}


### Derivation via Triangular Factorisation

{% asset_img triangular_factorisation.png 500 %}

To illustrate how one can derive the formula for updating linear projections, consider a simple case where each of $Y_n$ is a scalar and apply the triangular factorisation of $\Omega$:
\begin{equation}
\Omega = A D A',
\nonumber
\end{equation}
where
* $A$ is a lower triangular matrix with *1s* along the diagonal. 
* $D$ is a diagonal matrix with postive diagonal entries. 



For additional information, refer to the section on this subject later in this post, and of course, [wiki](https://en.wikipedia.org/wiki/LU_decomposition#Lower-diagonal-upper_(LDU)_decomposition).

Set $U = A^{-1} Y$ and observe
* The second-moment matrix of $U$ is diagonal:
\begin{equation}
E[U U'] = E[A^{-1} Y Y' (A')^{-1}] = A^{-1} \Omega (A')^{-1} = D.
\nonumber
\end{equation}
Thus, the components of $U$ are uncorrelated.
* Since $A$ is a lower triangular matrix, we have
\begin{eqnarray\*}
U_1 & = & Y_1 \\\\
a_{21} U_1 + U_2 & = & Y_2  \\\\
a_{31} U_1 + a_{32} U_2 + U_3 & = & Y_3 \\\\
& ... & \\\\
\end{eqnarray\*}

Now, we update the linear projections:

| projection | in terms of $U_n$ | in terms of $Y_n$ | MSE |
| :--: | :--: | :--: |  :--: |
| $\hat P(Y_2\vert Y_1)$ | $a_{21} U_1$ | $a_{21} Y_1$ | $E(U_2^2) = d_{22}$ |
| $\hat P(Y_3\vert Y_2, Y_1)$ | $a_{31} U_1 + a_{32} U_2$ | $a_{31} Y_1 + a_{32} (Y_2 - a_{21} Y_1)$ | $E(U_3^2) = d_{33}$ |
| ... | ... | ... |  ... |

Complete the derivation by taking the expressions in (\ref{E:A-three}) and (\ref{E:D-three}) for $a_{ij}$ and $d_{ii}$. 

### Projection with Constant Term

One can show that including a constant term is equivalent to working with the *de-meaned* variables $X = Y - E[Y]$ 
\begin{equation}
\hat E(Y_n|Y_{n-1}, \cdots, Y_1) = E[Y_n] + \hat P(X_n|X_{n-1}, \cdots, X_{1}).
\nonumber
\end{equation}
Let $\mu$ and $\Sigma$ be the mean and the covariance matrix of $Y$ (thus, the second-moment matrix of $X$):
\begin{eqnarray}
\mu & = & E[Y] = (\mu_1, \cdots, \mu_n) \nonumber \\\\
\Sigma & = & E[(Y-\mu)(Y-\mu)'] = E[(XX')]. \nonumber
\end{eqnarray}

Examples:
* $n=2$: 
\begin{eqnarray}
\hat{E}(Y_2|{\color{blue} Y_1}) & = & \mu_2 + \hat{P}(X_2|{\color{blue} X_1}) \nonumber \\\\
& = & \mu_{2} + \Sigma_{21}\Sigma_{11}^{-1} {\color{blue} X_1} \nonumber \\\\
& = & \mu_{2} + \Sigma_{21}\Sigma_{11}^{-1} ({\color{blue} Y_1} - \mu_1) \nonumber \\\\
\nonumber \\\\
\mathrm{MSE}(Y_2 - \hat{E}(Y_2|{\color{blue} Y_1})) & = & \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12} \nonumber \\\\
\end{eqnarray}


* $n=3$: It is a matter of writing things down to show
\begin{eqnarray}
\hat{E}(Y_3|{\color{red} Y_2}, {\color{blue} Y_1}) & = & \hat{E}(Y_3| {\color{blue} Y_1}) + G_{21}G_{11}^{-1} ({\color{red} Y_2} - \hat E({\color{red} Y_2}|{\color{blue} Y_1}))
\nonumber \\\\
\mathrm{MSE}(Y_3 - \hat{E}(Y_3|{\color{red} Y_2}, {\color{blue} Y_1})) & = & G_{33} - G_{32}G_{22}^{-1}G_{23} \nonumber \\\\
\end{eqnarray}
where 
\begin{equation}
G_{ij} = E\left[(Y_i - \hat E(Y_i|{\color{blue} Y_1}))(Y_j - \hat E(Y_j|{\color{blue} Y_1}))'\right] \quad \textrm{where} \quad i,j > 1.
\nonumber
\end{equation}


***
## Other Transformation toward Uncorrelated Variables

Through the triangular factorisation, $A^{-1} \vec{Z}$ has a diagonal second moment matrix, i.e. its components are uncorrelation. In this section, we consider two other transformations to map $\vec{Z}$ into a vector with a diagonal second moment matrix. 

### Transformations

**Cholesky factorisation**: From the triangular factorisation, we can easily derive
\begin{equation}
\Omega = P P' \quad \textrm{where} \quad P = AD^{1/2}.
\nonumber
\end{equation}
Then, $P^{-1} \vec{Z}$ has the identity matrix as its second moment matrix. 

**Diagonalisation**: Since $\Omega$ is a non-negative-definite symmetric matrix, it is diagonisable
\begin{equation}
\Omega = V \Lambda V^{-1}. 
\nonumber
\end{equation}
where $\Lambda$ is a diagonal matrix and $V$ is orthonormal: $V V' = V' V = I$ (thus $V^{-1} = V'$). Thus, $V^{-1} \vec{Z}$ has $\Lambda$ as its second moment matrix. (of course, the diagonal of $\Lambda$ is made up with eigenvalues and the columns of $V$ are eigenvectors.)

Note: This is nothing but the **principal component analysis (PCA)**!

### Mapping Illustration

Each transformation (which is nothing but a matrix multiplication) can be understood as a mapping of two basis vectors into the standard unit vectors:
\begin{equation}
\vec{Z}_1 \to \left[ \begin{array}{c}1 \\\\ 0\end{array}\right] \quad\textrm{and}\quad \vec{Z}_2 \to \left[ \begin{array}{c}0 \\\\ 1\end{array}\right]
\nonumber
\end{equation}
The plot below is an illustration of this mapping. 

{% asset_img mapping.png 800 %}

* The scatter data are generated from a bivariate normal vector with zero mean and
\begin{equation}
\Omega = \left[ \begin{array}{cc} 2 & 1.25 \\\\ 1.25 & 1 \end{array} \right]
\nonumber
\end{equation}
* For each plot: 
    
    * the blue and red lines correspond to $\vec{Z}_1$ and $\vec{Z}_2$, respectively. 
    * A unit circle and an inscribing square are shown to guage the length of the basis vectors. 
* Observations:
    * triangular: The $k$-th element of the $k$-th basis vector is 1 (as they touch the square). The second basis vector is the second unit vector. 
    * Cholesky: The lenghth of each basis vector indicates the dispersion of the data along its direction. 
    * diagonalisation: The basis vectors have a unit length and are orthogonal to each other. 


***

## Gaussian Random

Following Section 4.6 of Time Series Analysis by Hamilton....

For Gaussian (normal) random variables, the conditional expectation (optimal unrestricted predictor) is given by the linear projection with a constant term. Specifically, let $\vec Y_k$ be an $(n_k \times 1)$ vector with mean $\vec \mu_k$ for $k = 1, 2$, and let 

\begin{equation}
\left[ 
\begin{array}{cc}
    \Sigma_{11} & \Sigma_{12} \\\\
    \Sigma_{21} & \Sigma_{22}
\end{array}    
\right] = E \left[ \begin{array}{cc}
(\vec Y_1 - \vec \mu_1)(\vec Y_1 - \vec \mu_1)' & (\vec Y_1 - \vec \mu_1)(\vec Y_2 - \vec \mu_2)' \\\\
(\vec Y_2 - \vec \mu_1)(\vec Y_2 - \vec \mu_1)' & (\vec Y_2 - \vec \mu_2)(\vec Y_2 - \vec \mu_2)'.    \end{array}    
\right]
\nonumber
\end{equation}

We have seen that the linear projection of $\vec Y_2$ on $\vec Y_1$ with a constant term is given by
\begin{equation}
\hat{E}(\vec Y_2| \vec Y_1) = \vec \mu_2 + \Sigma_{21}\Sigma_{11}^{-11}(\vec Y_1 - \vec \mu_1)
\label{E:linear_projection_gauss}
\end{equation}
with 
\begin{equation}
\mathrm{MSE}=\Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}
\label{E:linear_projection_gauss_mse}
\end{equation}

So, the proof is to show $E(\vec Y_2 | \vec Y_1)$ is the same. This is just a matter of performing patient calculations. In particular, once we write down the following pdf functions: 
\begin{equation}
f_{\vec Y_1, \vec Y_2}(\vec y_1, \vec y_2) \quad\textrm{and}\quad f_{\vec Y_1}(\vec y_1), 
\nonumber
\end{equation}
we can derive the conditional pdf:
\begin{equation}
f_{\vec Y_2 | \vec Y_1}(\vec y_2| \vec y_1) = \frac{f_{\vec Y_1, \vec Y_2}(\vec y_1, \vec y_2) }{f_{\vec Y_1}(\vec y_1)}.
\nonumber
\end{equation}
After applying the triangular factorisation to $\Sigma$, one can show that $\vec Y_2 | \vec Y_1$ is Gaussian
\begin{equation}
\vec Y_2 | \vec Y_1 \sim N(\vec m, V)
\nonumber
\end{equation}
where $\vec m$ is equal to (\ref{E:linear_projection_gauss}) and $V$ is equal to (\ref{E:linear_projection_gauss_mse}), thus proving the claim. Note that the conditional covariance matrix $V$ is not a function of $Y_1$ but a *constant* matrix. 

As a reminder, the pdf of a Gaussian randon vector of length $n$ has the following form:
\begin{equation}
f_{\vec X}(\vec x) = \frac{1}{(2\pi)^{n/2}}  |\Sigma|^{-1/2} \exp \left(-\frac{1}{2} (\vec x - \vec \mu)' \Sigma^{-1} (\vec x - \vec \mu)\right)
\nonumber
\end{equation}

***

# Examples: Triangular Factorisation

The triangular factorisation is nothing but a series of Guassian eliminations in both rows and columns. 

## 2x2 matrix

As the simplest illustration, suppose that $\Omega$ in a $2 \times 2$ matrix:
\begin{equation}
\Omega = \left[
    \begin{array}{cc}
        \Omega_{11} & \Omega_{12} \\\\
        \Omega_{21} & \Omega_{22}
    \end{array}
    \right]. 
\nonumber
\end{equation}


To factorise this matrix, 
* Eliminate $\Omega_{21}$ by multiplying the first row by $-\Omega_{21}/\Omega_{11}$ and adding to the second row. 
* Similarly, eliminate $\Omega_{12}$ by multiplying the the first column by $-\Omega_{12}/\Omega_{11}$ and adding to the second column. 

Then, we obtain
\begin{equation}
\left[
\begin{array}{cc}
1 & 0 \\\\
-\Omega_{21}\Omega_{11}^{-1}  & 1
\end{array}
\right]
\left[
\begin{array}{cc}
    \Omega_{11} & \Omega_{12} \\\\
    \Omega_{21} & \Omega_{22}
\end{array}
\right]
\left[
\begin{array}{cc}
1 & -\Omega_{12}\Omega_{11}^{-1} \\\\
0 & 1
\end{array}
\right]=
\left[
\begin{array}{cc}
    \Omega_{11} & 0 \\\\
    0 & \Omega_{22} - \Omega_{12}\Omega_{11}^{-1}\Omega_{21}
\end{array}
\right]
\nonumber
\end{equation}
Invert the matrices surrounding $\Omega$ to obtain

\begin{equation}
\left[
\begin{array}{cc}
    \Omega_{11} & \Omega_{12} \\\\
    \Omega_{21} & \Omega_{22}
\end{array}
\right] =
\left[
\begin{array}{cc}
1 & 0 \\\\
\Omega_{21}\Omega_{11}^{-1}  & 1
\end{array}
\right]
\left[
\begin{array}{cc}
    \Omega_{11} & 0 \\\\
    0 & \Omega_{22} - \Omega_{12}\Omega_{11}^{-1}\Omega_{21}
\end{array}
\right]
\left[
\begin{array}{cc}
1 & \Omega_{12}\Omega_{11}^{-1} \\\\
0 & 1
\end{array}
\right]
\nonumber
\end{equation}
Since $\Omega$ is symmetric, this can be written as $A D A'$ where 
\begin{equation}
A = \left[
\begin{array}{cc}
1 & 0 \\\\
\Omega_{21}\Omega_{11}^{-1}  & 1
\end{array}
\right]
\nonumber
\end{equation}

## 2x2 block matrix

The above calculation with a 2x2 matrix extends to a 2x2 *block* matrix as well. To this end, suppose that $\Omega$ is an $(n+m)\times (n+m)$ matrix of 2x2 blocks. Then, we have 

\begin{equation}
\Omega = 
\left[
\begin{array}{cc}
    \Omega_{11} & \Omega_{12} \\\\
    \Omega_{21} & \Omega_{22}
\end{array}
\right] =
A D A'
\nonumber
\end{equation}
where 
\begin{equation}
A = \left[
\begin{array}{cc}
1_{n\times n} & 0_{n\times m} \\\\
\Omega_{21}\Omega_{11}^{-1}  & 1_{m\times m}
\end{array}
\right]
\quad\textrm{and}\quad
D = \left[
\begin{array}{cc}
    \Omega_{11} & 0_{n\times m}  \\\\
    0_{m\times n}  & \Omega_{22} - \Omega_{12}\Omega_{11}^{-1}\Omega_{21}
\end{array}
\right]
\nonumber
\end{equation}

## 3x3 matrix

Consider a 3x3 matrix: 

\begin{equation}
\left[
\begin{array}{ccc}
    \Omega_{11} & \Omega_{12} & \Omega_{13} \\\\
    \Omega_{21} & \Omega_{22} & \Omega_{23} \\\\
    \Omega_{31} & \Omega_{32} & \Omega_{33} \\\\
\end{array}
\right]
\nonumber
\end{equation}

As before, perform a series of Gauassian row and column elimations (expressed using $E_1$ and $E_1'$ below) with $\Omega_{11}$ as the pivot to get
\begin{equation}
E_1
\Omega
E_1' = 
\left[
\begin{array}{ccc}
    \Omega_{11} & 0 & 0 \\\\
    0 & H_{22} & H_{23} \\\\
    0 & H_{32} & H_{33} \\\\
\end{array}
\right]
\nonumber
\end{equation}
where
\begin{equation}
E_1 = 
\left[
\begin{array}{ccc}
    \Omega_{11} & 0 & 0 \\\\
    -\Omega_{21}\Omega_{11}^{-1} & 1 & 0 \\\\
    -\Omega_{31}\Omega_{11}^{-1} & 0 & 1 \\\\
\end{array}
\right]
\nonumber
\end{equation}
and
* $H_{22} = \Omega_{22} - \Omega_{21}\Omega_{11}^{-1}\Omega_{12}$
* $H_{23} = H_{32} = \Omega_{23} - \Omega_{21} \Omega_{11}^{-1}\Omega_{13}$
* $H_{33} = \Omega_{31}\Omega_{11}^{-1}\Omega_{13}$

Now, perform the Gauassian elimations using $H_{22}$ as the pivot to get
\begin{equation}
E_2 E_1
\Omega
E_1' E_2' = 
\left[
\begin{array}{ccc}
    \Omega_{11} & 0 & 0 \\\\
    0 & H_{22} & 0 \\\\
    0 & 0 & H_{33} - H_{32}H_{22}^{-1}H_{23} \\\\
\end{array}
\right]
:= D
\label{E:D-three}
\end{equation}
where
\begin{equation}
E_2 = 
\left[
\begin{array}{ccc}
    1 & 0 & 0 \\\\
    0 & 1 & 0 \\\\
    0 & -H_{32}H_{22}^{-1} & 1 \\\\
\end{array}
\right].
\nonumber
\end{equation}
Set $A = (E_2 E_1)^{-1}$ 
\begin{equation}
A = \left[
\begin{array}{ccc}
    1 & 0 & 0 \\\\
    \Omega_{21}\Omega_{11}^{-1} & 1 & 0 \\\\
    \Omega_{31}\Omega_{11}^{-1} & -H_{32}H_{22}^{-1} & 1
\end{array}
\right]
\label{E:A-three}
\end{equation}
and get
\begin{equation}
\Omega = A D A'
\nonumber
\end{equation}

## 3x3 block matrix

Again, the above calculations for a 3x3 matrix extends to a 3x3 block matrix.

