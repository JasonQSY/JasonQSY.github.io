---
layout: post
title:  "Multivariate Linear Regression"
date:   2016-02-11
categories: machine learning
---

This post is my note of [Andrew Ng's Machine Learning course](https://www.coursera.org/learn/machine-learning/home/welcome). It concludes the contents of Week 1 & Week 2. Meanwhile, the whole post is a problem introduced in Assignment: Linear Regression.

Although the course teaches Octave, I have access to Matlab through Academic Licence of my intitute. Thus, I use Matlab instead of Octave.

# Problem Background
The problem is that we want to assess the price of a house. Thus, we collect information on recent house sold. (The data can be obtained on the course website)

Size(feet$^2$) | Number of bedrooms | Price
--- | ---- | ---
2104 | 3 | 399900
1600 | 3 | 329900
2400 | 3 |369000
... | ... | ...

which is called a training set. We decide to construct a model by multivariate linear regression to assess the price of the house.

# Basic Definition
The number of houses is 47. We represent 47 with m, i.e. number of the training examples. ($m=47$)

We use $x$ to represent a input value and $y$ to represent an output value. In this problem, $x_1$ is the size, $x_2$ is the number of bedrooms and $y$ is the price.

It can be seen that there are 2 types of input values, i.e. features. We represent feature with n. ($n=2$)

Examples:

$$x_1^{(3)} = 2400 $$
$$ x_2^{(2)} = 3 $$
$$ y^{(2)} = 399900 $$

With linear algebra, we use a matrix X to represent the input value and a m-dimensional vector y to represent the output value. However, we add 1 one the left as the feature of constant $\theta_0$.
Examples:

$$X = \left(\begin{matrix}
1 & 2104 & 3 \\
1 & 1600 & 3 \\
1 & 2400 & 3 \\
& \cdots \cdots &
\end{matrix}\right)$$

$$ y = \left(\begin{matrix}
399900 \\
329900 \\
369000 \\
\cdots
\end{matrix} \right) $$

The model is based on a hypothesis, which is multivariate linear regression:

$$ h_\theta = \theta_0 + \theta_1 x_1 + \theta_2 x_2 $$

Let

$$ \theta = ( \theta_0 \; \theta_1 \; \theta_2 ) $$

We have

$$h_\theta(x) = \theta^T X$$

However, the hypothesis is generally different from the realistic data and we need a method to assess if the hypothesis is good enough. The method is cost function $J(\theta)$.

$$ J(\theta_0, \theta_1, \theta_2) = \frac{1}{2m} \sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2$$

which is equivalent to

$$ J(\theta) = \frac{1}{2m} \sum_{i=1}^{m}(h_\theta(x) - y^{(i)})^2$$

(The equation need modifying according to linear algebra. I do not know how to modify currently. Maybe I'll modify it in the future.)

These are basic definitions on linear regression. And what we want to solve is the n-dimensional vector $\theta$ when $J(\theta)$ attains its minimum.

# Mathematical Method
It is possible for us to slove $\theta$ with calculus. Set $\frac{\partial}{\partial \theta}J(\theta) = 0$, we find that at this time,

$$\theta = (X^T X)^{-1} X^T y $$

Here is the matlab code which calculate $\theta$.

    #!matlab
    data = load('ex1data2.txt');
    sz = size(data);
    m = sz(1);
    n = sz(2) - 1;
    X = [ones(m,1) data(:, 1:2)];
    y = data(:, 3);
    theta = (X' * X)^(-1) * X' * y;
    disp(theta);

The result is that

$$ \theta = \left( \begin{matrix}
8.9598 \\
0.0139 \\
-0.8738 \end{matrix} \right)
$$

However, the main disadvantage of the method is that $X^T X$ is a n x n matrix. When n is very large, it is very complicated to calculate $(X^T X)^{-1}$. The time complexity is often $O(n^3)$, which is less efficient.

# Gradient Descent Algorithm
To slove the problem, there is a machine learning algorithm named gradient discent algorithm. The mathematical base can be seen as follows.
For any j,

$$\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j}J(\theta)$$

Solving the partial derivative, we have for all $\theta_j$

$$\theta_j = \theta_j - \alpha \frac{1}{m} \sum_{i=1}^m\big((h_\theta(x^{(i)})-y^{(i)} )x^{(i)}\big)$$

And the calculation will continue until convergence. It is also easy to code by Matlab.

    #!matlab
    function J = computeCost(X, y, theta)
        m = length(y);
        h = X * theta;
        J = 1/(2*m) * sum((h-y).^2);
    end

    function theta = gradientDescent(X, y, theta, alpha, num_iters)
        m = length(y);
        len_theta = length(theta);
        h = X * theta;

        for j = 1:len_theta
            for i = 1:num_iters
                theta(j) = theta(j) - alpha/m * sum((h-y) .* X(:,j));
            end
        end
    end

You should check manually if the iteration takes effect. I do not use "while" in this case because the loop will be endless if $\alpha$ is not set properly.

# Brief Conclusion
Multivariate linear regression can fit continuous data with certain form by computing parameters. It is also possible to fit polynomial function by considering high-order term as another feature.
