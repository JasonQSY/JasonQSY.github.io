---
layout: post
title:  "LaTeX Counters"
date:   2016-02-17
categories: latex
---

# Basic Command
Although there are some default counters accepted by LaTeX, you can also create your own counters.
Since I often use `\usepackage[a4paper]{article}`, there are some counters I often use.

- section
- subsection
- subsubsection
- page

Sometimes, I create my own counter.
```tex
\newcounter{exercise}
```
Initially, the counter `exercise` is equal to zero. `\setcounter{}{}` can be used to intialize it.
```tex
\setcounter{exercise}{1}
```
Actually, counter `exercise` is like a variable in a programming language. There are several ways to modify it (take C-family language for example).
```tex
\stepcounter{exercise} % exercise++
\addtocounter{exercise}{1} % exercise += 1
\setcounter{exercise}{1} % exercise = 1
```
The modification of deafault counters can take effect at once. For instance, if you `\stepcounter{page}` in page 7 of an article, the page number of this page will be 8, and that of the next page will be 9. The page number will change both on the specific page and table of contents. In other words, the count in the whole LaTeX document relies on the default counters.
In addition, there are several ways to have access to the counters. However, what I often use is:
```tex
\arabic{exercise} % print a (arabic) number
```
# An Actual Usage
One of my courses has a series of assignments and one assignment has various exercises. Instead of entering the specific index of exercise such as `Exercise 8.1`, I want that everything can be automatic. That means, I only need enter the index of assignment at first.
```tex
\newcounter{assigncount}
\newcommand{\newassignment}[1]
{
    \setcounter{assigncount}{#1}
    \begin{raggedright}
        \textbf{\large Cource Code Assignment #1} \\
        Instructor\\
        Name, Student ID\\
        \today
    \end{raggedright}
}
\newcounter{excount}
\setcounter{excount}{1} % Initialize
\newenvironment{exercise}
{
    \textbf{Exercise \arabic{assigncount}.\arabic{excount}}
    \stepcounter{excount}
    \begin{enumerate}[(i)]
}
{
    \end{enumerate}
}
```
Then, when I write the assignment, I can just write as follows.
```tex
\input head-document
\newassignment{2}
\begin{exercise}
	\item Proof: %...
    \item Solution: %...
    %...
\end{exercise}
%...
```
Nothing like `\begin{exercise}{2.1}` and `\item[(i)]` needs offering.

# Reference
[1] LaTeX Wiki. Retrieved from <https://en.wikibooks.org/wiki/LaTeX>
