---
layout: post
title:  "Logistic Regression in Machine Learning"
date:   2016-02-20
categories: machine learning
---

This post is my note of Andrew Ng's Machine Learning course. It covers week 3. The code has considered oneVSall classification and can be appied to `ex2_reg.m` and `ex3.m`.

# Basic Ideas

## Basic Model

In the classification problem, the weight of every data is generally not linear. For example, the high price of a very big house is not surprising although this data can obviously change the parameter of linear regression. To slove the problem, we introduce the sigmoid function.

$$g(z) = \frac{1}{1+e^{-z}} \in (0,1)$$

For $z > 4$ or $z < -4$, the output value is nearly the same. Then, the extreme value won't hurt the parameters (weights now). The hypothesis now is:

$$h_\theta(x) = g(\theta^T X)$$

which is equivalent to

$$h_\theta(x) = \frac{1}{1+e^{-\theta^T X}} \in (0,1)$$

Here, $h$ defines a probability, which has a real meaning.

$$h_\theta(x) = p(y = 1|x;\theta)$$

According to probability,

$$p(y=1|x;\theta) + p(y=0|x;\theta) =1 $$

However, the hypothesis is not a convex function. However, we want the cost function can be convex, then we can apply gradient descent algorithm to find the minimum (like linear regression). Therefore, a few tricks here.


$$J(\theta) = \frac{1}{m} \sum_{i=1}^m \textrm{Cost}(h_\theta(x^{(i)}, y^{(i)}))$$

The Cost can be defined as follows.

$$\textrm{Cost}(h_\theta(x^{(i)}, y^{(i)})) = \begin{cases}
-\log(h_\theta(x)) & \textrm{if } y = 1\\
-\log(1 - h_\theta(x)) & \textrm{if } y = 0
\end{cases}
$$

which is equivalent to

$$\textrm{Cost}(h_\theta(x^{(i)}, y^{(i)})) = -y \log(h_\theta(x)) - (1-y) \log(1-h_\theta(x))$$

Thus,

$$J(\theta) = -\frac{1}{m}\left[ \sum_{i=1}^m(y^{(i)} \log(h_\theta(x^{(i)})) + (1-y^{(i)}) \log(1-h_\theta(x^{(i)}))) \right]$$

Similarly, we have

$$\theta := \theta - \alpha \frac{1}{m} [(h_\theta(x^{(i)})-y^{(i)}) \cdot x^{(i)} ]$$

## Regularization
There are overfit and underfit problems. Generally, regularization can be used to solve the overfit problem. Note that $\lambda$ can not be too big, or every parameter would be nearly zero.

### Linear
For $j = 0$,
$$J(\theta) = \frac{1}{2m} \sum_{i=1}^{m}(h_\theta(x) - y^{(i)})^2  $$

$$\theta_0 := \theta_0 - \alpha \frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)} ) x_0^{(i)}$$

For $j > 0$,

$$J(\theta) = \frac{1}{2m} \left[\sum_{i=1}^{m}(h_\theta(x) - y^{(i)})^2 +  \lambda\sum_{i=1}^{m}\theta_j^2\right] $$

$$\theta_j := \theta_j - \alpha \left[ \frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)} ) x_j^{(i)} + \frac{\lambda}{m}\theta_j \right]$$

### Logistic
For $j=0$,
$$J(\theta) = -\frac{1}{m}\left[ \sum_{i=1}^m(y^{(i)} \log(h_\theta(x^{(i)})) + (1-y^{(i)}) \log(1-h_\theta(x^{(i)}))) \right]$$

$$\theta_0 := \theta_0 - \alpha \frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)} ) x_j^{(0)}$$

For $j > 0$,

$$J(\theta) = -\frac{1}{m}\left[ \sum_{i=1}^m(y^{(i)} \log(h_\theta(x^{(i)})) + (1-y^{(i)}) \log(1-h_\theta(x^{(i)}))) \right] + \frac{\lambda}{2m} \sum_{i=1}^n \theta_j^2$$

$$\theta_j := \theta_j - \alpha \left[\frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)} ) x_j^{(i)} + \frac{\lambda}{m}\theta_j\right]$$

# Code
Just follow the instructions. Nothing too hard. However, since I cannot make sense how to use `fmincg`, I didn't vectorize it.

    #!matlab
    % Sigmoid function g(z)
    function g = sigmoid(z)
        g = 1.0 ./ (1.0 + exp(-z));
    end

    % Cost function J(\theta)
    function [J, grad] = CostFunction(theta, X, y, lambda)
        m = length(y);
        h = sigmoid(X * theta);
        J = 1/m * sum(-y .* log(h) -(1-y) .* log(1-h)) + lambda/(2*m) * (sum(theta.^2)-theta(1)^2);
        grad = 1/m * (X' * (h-y)) + (lambda * theta)/m;
        zero = 1/m * (X' * (h-y));
        grad(1) = zero(1);
        grad = grad(:);
    end

    % Train separately for every number
    function learn_theta = train(X, y, num_of_class, lambda)
        m = size(X, 1);
        n = size(X, 2);
        learn_theta = zeros(num_of_class, n + 1);
        X = [ones(m, 1), X];
        initial_theta = zeros(n + 1, 1);
        options = optimset('GradObj', 'on', 'MaxIter', 50);
        for i = 1:num_of_class
            theta = ...
                fmincg(@(t)(CostFunction(t, X, (y == i), lambda)), ...
                initial_theta, options);
            learn_theta(i, :) = theta';
        end
    end

    % Calculate the accuracy
    function accu = test(learn_theta, X, y)
        m = size(X, 1);
        X = [ones(m, 1) X];
        h = sigmoid(X * learn_theta);
        [~, p] = max(h, [], 2);
        accu = mean(double(p == y)) * 100; % percent
    end
