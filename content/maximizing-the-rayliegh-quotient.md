Title: Maximizing the Rayleigh Quotient
Date: 2021-01-30
Category: Math
Tags: Optimization, Proofs
mathjax: True
Summary: The rayleigh quotient maximization problem naturally occurs in many disciplines---machine learning, statistics, quantum mechanics, and portfolio optimization just to name a few. Although the solution of this problem is widely known, many texts state the solution without offering any proof. In this post, I will present proof of the rayleigh quotient maximization problem solution that will hopefully satisfy the most inquisitive of readers!

The rayleigh quotient maximization problem naturally occurs in many disciplines---machine learning, statistics, quantum mechanics, and portfolio optimization just to name a few. Although the solution of this problem is widely known, many texts state the solution without offering any proof. In this post, I will present proof of the rayleigh quotient maximization problem solution that will hopefully satisfy the most inquisitive of readers!

We will begin by stating the rayleigh quotient maximization problem.

Let $A,B\in\mathbb{R}^{d\times d}$ be two symmetric positive semi-definite matrices and $x\in\mathbb{R}^{d}$ be a column vector. Additionally, we will require $B$ to be invertible. We will show that the rayleigh quotient problem in $(\ref{problem-statement})$ is maximized whenever $x$ is collinear to the eigenvector of $B^{-1}A$ that corresponds to the largest eigenvalue.

\begin{equation}
    \label{problem-statement}
    \mathop{\arg\max}\limits_{x}\frac{x^TAx}{x^TBx}
\end{equation}

Since $B$ is symmetric, we know that there exists an orthonormal matrix $P\in\mathbb{R}^{d\times d}$ and a diagonal matrix $D\in\mathbb{R}^{d\times d}$ such that $B=PDP^T$. Furthermore, since $B$ is also invertible and positive semi-definite, we know that the diagonal entries of $D$, i.e., the eigenvalues of $B$, are positive and non-zero. Consequently, the matrix $B^{-\frac{1}{2}}$ exists, and we can use the invertible substitution in $(\ref{sub})$ to transform our optimization problem in $(\ref{problem-statement})$ to the equivalent optimization problem shown in $(\ref{sub-problem})$.

\begin{equation}
    \label{sub}
    x=B^{-\frac{1}{2}}w
\end{equation}

\begin{equation}
    \label{sub-problem}
    \mathop{\arg\max}\limits_{w}\frac{w^TB^{-\frac{1}{2}}AB^{-\frac{1}{2}}w}{w^Tw}
\end{equation}

Considering the fact that $w=\lVert w\rVert\frac{w}{\lVert w\rVert}$, we notice that $(\ref{sub-problem})$ is invariant to the norm of $w$. So the optimization problem in $(\ref{sub-sub-problem})$ is equivalent to the optimization problem in $(\ref{sub-problem})$. In order to see this, suppose that $w^*$ is a solution to $(\ref{sub-sub-problem})$, then any $cw^*$ with $c\in\mathbb{R}$ is a solution to $(\ref{sub-problem})$.

\begin{equation}
    \label{sub-sub-problem}
    \mathop{\arg\max}\limits_{w,\lVert w \rVert=1}\frac{w^TB^{-\frac{1}{2}}AB^{-\frac{1}{2}}w}{w^Tw}=\mathop{\arg\max}\limits_{w,\lVert w\rVert=1}w^TB^{-\frac{1}{2}}AB^{-\frac{1}{2}}w
\end{equation}

Since the matrices $B^{-\frac{1}{2}}$ and $A$ are symmetric, the product $B^{-\frac{1}{2}}AB^{-\frac{1}{2}}$ is also clearly symmetric. Hence, $B^{-\frac{1}{2}}AB^{-\frac{1}{2}}$ can be orthogonally diagonalized by an orthonormal matrix $V$ and a diagonal matrix $\Sigma$ such that $B^{-\frac{1}{2}}AB^{-\frac{1}{2}}=V\Sigma V^T$. 

\begin{equation}
    \mathop{\arg\max}\limits_{w,\lVert w\rVert=1}w^TB^{-\frac{1}{2}}AB^{-\frac{1}{2}}w=\mathop{\arg\max}\limits_{w,\lVert w\rVert=1}w^TV\Sigma V^Tw
\end{equation}

Let $\lambda_i\in\mathbb{R}$ and $v_i\in\mathbb{R^{d}}$ with $i\in\{1,2,\dots,d\}$ be the eigenvalues and eigenvectors of $B^{-\frac{1}{2}}AB^{-\frac{1}{2}}$ respectively. We note the following about the matrices $\Sigma$ and $V$.

\begin{align}
    V&=\begin{bmatrix}v_1 & v_2 & \dots & v_d\end{bmatrix}\\
    \Sigma&=\operatorname{diag}\{\lambda_1,\lambda_2,\dots,\lambda_d\}
\end{align}

Now we can rewrite $w^TV\Sigma V^Tw$ as a summation and rewrite the optimization problem in $(\ref{sub-sub-problem})$ as the one shown in $(\ref{summation})$.

\begin{align}
    \mathop{\arg\max}\limits_{w,\lVert w\rVert=1}w^TV\Sigma V^Tw&=\mathop{\arg\max}\limits_{w,\lVert w\rVert=1}\begin{bmatrix}w^Tv_1 & w^Tv_2 & \dots & w^Tv_d\end{bmatrix}\Sigma\begin{bmatrix}w^Tv_1\\w^Tv_2\\\vdots\\w^Tv_d\end{bmatrix}\\
    &=\mathop{\arg\max}\limits_{w,\lVert w\rVert=1}\sum_{i=1}^{d}\left(w^Tv_i\right)^2\lambda_i\label{summation}
\end{align}

Since $V$ is orthonormal, we have $w^TVV^Tw=1$, so the summation $\sum_{i=1}^{d}\left(w^Tv_i\right)^2=1$ for all $w$. Additionally, since $A$ and $B^{-\frac{1}{2}}$ are symmetric and positive semi-definite, $B^{-\frac{1}{2}}AB^{-\frac{1}{2}}$ is also symmetric and positive semi-definite, but not necessarily invertible. Thus, we conclude that all $\lambda_i\ge 0$. Now suppose that $\lambda^*=\lambda_d$ is the largest eigenvalue of $B^{-\frac{1}{2}}AB^{-\frac{1}{2}}$. So $(\ref{ortho})$ must be true.

\begin{equation}
    \label{ortho}
    \frac{\lambda_1}{\lambda^*}\left(w^Tv_1\right)^2+\frac{\lambda_2}{\lambda^*}\left(w^Tv_2\right)^2+\dots+\frac{\lambda_{d-1}}{\lambda^*}\left(w^Tv_{d-1}\right)^2+\left(w^Tv_d\right)\leq 1
\end{equation}

It follows from $(\ref{ortho})$ that $(\ref{almost-done})$ must also be true.
\begin{equation}
    \label{almost-done}
    \sum_{i=1}^d\left(w^Tv_i\right)^2\lambda_i\leq \lambda^*
\end{equation}

Clearly, $\sum_{i=1}^d\left(w^Tv_i\right)^2\lambda_i=\lambda^*$ if and only if $w$ is collinear to the eigenvector of $B^{-\frac{1}{2}}AB^{-\frac{1}{2}}$ that corresponds to the largest eigenvalue. Hence, under these conditions, we have maximized $(\ref{sub-problem})$. Using the substitution in $(\ref{sub})$, a solution to $(\ref{sub-problem})$ can be translated into a solution to $(\ref{problem-statement})$.

\begin{align}
    B^{-\frac{1}{2}}AB^{-\frac{1}{2}}w&=\lambda w\\
    B^{-\frac{1}{2}}AB^{-\frac{1}{2}}B^{\frac{1}{2}}x&=\lambda B^{\frac{1}{2}}x\\
    B^{-1}Ax&=\lambda x\\
\end{align}

Thus, $(\ref{problem-statement})$ is maximized when $x$ is collinear to the eigenvector of $B^{-1}A$ that corresponds to the largest eigenvector. This completes the proof!
