---
layout: post
title:  "Catalan Triangle - Alternative Proof"
date:   2022-07-18
categories: maths
---

## Random Walk and Back to Origin

Consider a random walk with 50/50 chance to go up/down by a unit. Let $$X_n$$ be the location after $n$-th step with $X_0 = 0$. How many ways are there to come back to the original location at the $2n$-th step with

\begin{equation}
X_j > 0 \text{ for }j = 1, \cdots, 2n-1
\label{E:condition}
\end{equation}
in other words, while staying positive? The answer to this question is known to be the $\color{red}{(n-1)}$-the Catalan number. 

Whilst there are many ways to prove this, I would like to present my way as an alternative. 

Let's consider Pascal's triangle where the $k$-th element of the $n$-th row is given by
\begin{equation}
P(n,k) = \left( \begin{array}{c} n \\\\ k \end{array} \right) 
\nonumber
\end{equation}
where $n = 0, 1, \cdots, $ and $k = 0, 1, \cdots, n$.  

The triangle can be depicted as below

![pascal triangle](/assets/catalan/pascal.png)

where $n = 0$ corresponds to the top row and $k=0$ corresponds to the far left circle in each row. 

The triangle is thought to be constructed by 
1. fill the space with zeros: $P(n,k) = 0$ for $n$ and $k$ all integers (negative integers as well)
2. drop one at the yellow circle: $P(0,0) = 1$
3. let it cascade down through
\begin{equation}
P(n,k) = P(n-1, k-1) + P(n-1, k)
\nonumber
\end{equation}
4. update $n \leftarrow n+1$ and go back to step 3. 

The triangle tracks the number of possible paths to each circle from the starting yellow circle with

| left half | center line | right half |
| :--: | :--: | :--: |
| $\color{blue}{X_n} > 0$ | $X_n=0$ | $\color{red}{X_n} < 0$ |



## Catalan's Triangle

The condition (\ref{E:condition}) can be incorporated by adding the step between step 3 and 4: 
(step 3.5): If $n$ is even, overwrite the value (red circles below) at the center to zero
\begin{equation}
P(n, n/2) \leftarrow 0
\end{equation}


![pascal triangle](/assets/catalan/pascal_to_catalan.png)


The same result can be achieved if we reverse the sign of the values in the right half and perform the standard Pascal triangle operation *without* overwriting. 


![pascal triangle](/assets/catalan/catalan.png)


This triangle is the sum of the two Pascal's triangles starting from the yellow circles above, respectively. 

| | triangle 1 | triangle 2 |
| :--: | :--: | :--: |
| constructed by | dropping +1 at (1,0) at step 2 | dropping -1 at (1,1) at step 2 |
| value | $P_1(n,k) = \left( \begin{array}{c} n-1 \\\\ k \end{array} \right) $ | $P_2(n,k) = -\left( \begin{array}{c} n-1 \\\\ k-1 \end{array} \right)$ |



![pascal triangle](/assets/catalan/catalan_number.png)


Then, the number of possible paths to return to zero at $2n$ is the value at (2n-1, n-1) as highlighted in grey, i.e. 1, 1, 2, 5, 14, ...
\begin{equation}
P_1(2n-1, n-1) +  P_2(2n-1,1) = \left( \begin{array}{c} 2(n-1) \\\\ (n-1) \end{array} \right)- \left( \begin{array}{c} 2(n-1) \\\\ (n-1)-1 \end{array} \right) = C(n-1)
\end{equation}


<!-- You’ll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated.

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/ -->
