Title: Vv186 RC Notes on Integration
Date: 2015-12-3
Category: Mathematics
Modified: 2016-2-10
Tags: Single Variable Calculus

## Step function

$$P=\{a_0,a_1,...,a_n\} $$

The integration is the area under the functions.

$$\int_a^b \phi =I_p(\phi)=\sum_{i=1}^n(a_i-a_{i-1})$$

Bounded: 

$$ \sup_{x\in Domain}|f(x)|<\infty $$

Prove a function is regulated: Find a step function uniformly converges to it.

$$ C([a,b])\subset Reg([a,b]) $$

## Darboux Intergral
Find two step function.

$$ v < f < u $$ 
$$ \sup \int_a^bv=\inf \int_a^bu :=\int_a^b f $$
$$ f \subset Reg([a,b]) \Rightarrow Darboux $$

Darboux Integral is more general.

## Riemann Integral 

Only one step function.

$$P=\{a_0,a_1,...,a_n\} $$
$$ \Xi=\{\xi_1,\xi_2,...,\xi_n\} $$
$$ \int_a^b\phi = \sum_{k=1}^n f(\xi_k)(x_k-x_{k-1}) $$

We have proved that

$$ Darboux \Leftrightarrow Riemann $$

## Calculation

With $F'=f$,
$$ \int_a^b f(t)\;\mathrm{dt}=F(b)-F(a) $$
Substitution rule
eg1. With $y=3+2x$ and $dy=2dx$

$$ \int_1^3 \frac{dx}{3+2x}=\int_5^9\frac{dy}{2y}=\frac{1}{2}\int_5^9\frac{dy}{y} =\cdots$$
$$ f=\frac{x+5}{x^2-2x-3}=\frac{A}{x-3}+\frac{B}{x+1} $$
$$ f=\frac{x^2+6x+4}{(x-1)^2(x+2)}=\frac{A}{x-1}+\frac{B}{x+2}+\frac{C}{(x-1)^2}$$

Integration By Parts
...

## Exercise 

$$\int \; x \arctan{x} \;\mathrm{dx} $$
$$=\frac{x^2}{2} \arctan{x} - \frac{1}{2} \int \frac{x^2}{1+x^2} dx $$
$$\int \frac{x^2}{1+x^2}dx=\int dx - \int \frac{1}{1+x^2}dx $$ 

Remember $\int arctanx$

$$\int \sqrt{a^2-x^2}dx \; \textrm{Let } x=a\cos{\theta} $$
$$\int \sqrt{a^2+x^2}dx \; \textrm{Let } x=a\tan{\theta} $$

$$\lim_{n\to\infty}\int_a^n=\int_a^\infty f $$
$$\int_{-\infty}^{\infty}f=\int_{\infty}^cf+\int_{c}^{\infty}f $$

## Euler-Gamma Function

$$\Gamma(t)=\int_0^\infty z^{t-1}e^{-z} dz $$
$$\Gamma(n+1)=n \cdot \Gamma(n) $$

Define factorial.

$$\Gamma(\frac{1}{2}+n)=\frac{(2n)!}{4^nn!}\sqrt{\pi} $$
$$\Gamma(\frac{1}{2}-n)=\frac{(-4)^n n!}{(2n)!}\sqrt{\pi} $$

Keep in mind

$$\int_a^bf(x)dx=(b-a)\sup_{x\in[a,b]}|f(x)| $$

## Exercise 

$$f,g\in C([a,b]),\forall x\in[a,b],g\ge 0$$

Prove:

$$ \exists S\in[a,b], \int_a^bf(x)g(x) dx=f(s)\int_a^bg(x)dx $$
__Proof__: $f$ is a continuous function defined on a closed inteval. Thus, it must attain its maximum and minimum. Let
$$ m:=\min_{x\in[a,b]}f(x), M:=\max_{x\in[a,b]}f(x)$$

Thus,

$$ m\cdot\int_a^bg(x)dx \le \int_a^b f(x)g(x) dx \le M\cdot \int_a^b g(x)dx $$

Let $k\cdot \int_a^bg(x)dx=\int_a^b f(x)g(x) dx$, then $m\le k \le M$.

It means that

$$ \exists s\in[a,b], \; f(s)=k $$

## Exercise

Calculate:

$$ \int_0^\infty \frac{v^2}{v^4+1}dv $$

Solution:

Set $w=1/v$ such that $dw=-\frac{dv}{v^2}$, thus
$$\int_0^\infty \frac{v^2}{1+v^4}dv=\int_\infty^0 \frac{-dw}{w^4+1}=\int^\infty_0 \frac{dw}{w^4+1} $$
Thus,
$$\int_0^\infty \frac{v^2}{1+v^4}dv=\int_0^\infty \frac{dv}{1+v^4} $$
Thus,
$$ 2\cdot \int_0^\infty \frac{v^2}{1+v^4}dv=\int_0^\infty \frac{v^2+1}{1+v^4}dv=\int_0^\infty \frac{1+1/v^2}{v^2+1/v^2}dv $$
Let $t=v-1/v$ such that $dt=(1+1/v^2)dv, then
$$\int_{-\infty}^{\infty}\frac{dt}{t^2+2}$$
$$=\frac{1}{2}\int_{-\infty}^{\infty}\frac{dt}{(t/\sqrt{2})^2+1}$$
$$=\frac{\sqrt{2}}{2} \int_{-\infty}^{\infty}\frac{dk}{k^2+1}$$
$$=\frac{\sqrt{2}}{2} \pi $$
Hence, the result is $\frac{\sqrt{2}}{4}$

Meet $v^4+1$, try change $v^2+1/v^2$ and substitute $v\pm 1/v$

##Exercise

If $f$ is an odd function,
$$0=\int_{-a}^a f(x)dx$$
