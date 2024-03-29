## 1. Generative effects

### 1.1
Find `f : Real -> Real` (not) preserving
- Order: `sign`; not: `\x -> x**2`.
- Distance: `\x -> -x+1`; not: `\x -> 2*x`.
- Addition: `\x -> -2*x+1`; not: `exp`.

### 1.4
Let  
`a = [("11", "12"), ("13",), ("21",), ("22", "23")]`  
and  
`b = [("11",), ("21",), ("12", "22"), ("13", "23")]`.  
Then  
`a v b = [("21",), ("11", "12", "13", "22", "23")]`.

### 1.6
1. $\{\{*\},\{\circ\}\} \leq \{*,\circ\}$
2. $\{\{1\},\{2\},\{3\},\{4\}\} \leq \{\{1,2\},\{3\},\{4\}\}$ etc - TODO: tikz
3. Let $A\leq C$ and $B\leq C$ such that there is no other $C'\leq C$ in the diagram satisfying both $A\leq C'$ and $B\leq C'$. Then $C=A\vee B$. This is the universal property of the coproduct (right?).
4. True.
5. The transitive closure of $A\vee B$.
6. True.

### 1.7
1. `true v false = true`
2. `false v true = true`
3. `true v true = true`
4. `false v false = false`

### 1.10
1. True.
2. False unless you're doing analysis.
3. True.

### 1.11
1. $\mathcal{P} B = \{\{\}, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}\}$
2. $\{1\} \cup \{2\} = \{1,2\}$, $B \cup \{\} = B$, $\{1\} \cup \{1,3\} = \{1,3\}$.
3. $A\times B = \{(h,1), (h,2), (h,3), (2,1), (2,2), (2,3)\}$.
4. $A \sqcup B = (A\times \{1\}) \sqcup (B\times \{2\}) =$  
$\{(h,1), (1,1)\} \cup \{(1,2), (2,2), (3,2)\} =$  
$\{(h,1), (1,1), (1,2), (2,2), (3,2)\}$.
5. $A\cup B = \{h,1\}\cup \{1,2,3\} = \{h,1,2,3\}$.

### 1.16
1. Let $A_{p} = A^{\prime}_{q} = A^{\prime}_{r}$. Then $ q = r $, since $ A^{\prime}_{q} \cap A^{\prime}_{r} = A^{\prime}_{q} = A^{\prime}_{r} \neq \{\} $ because $ \{A^{\prime}_{p\prime}\}_{p^{\prime}\in P^{\prime}} $ is a partition.
2. Let $i p = p^{\prime}$ iff $A_{p} = A^{\prime}_{p^{\prime}} $. We want to show that $\{A^{\prime}\}_{p^{\prime}\in i P}$ is a partition. We check that
    - $\cup_{i p\in i P} A' = \cup_{p\in P} A = S$.
    - $B_{i p} \cap B_{i p'} = A_{p} \cap A_{p'} = \delta_{p,p'} = \delta_{i p, i p'}$ since $i$ is injective.  
    
    Finally, show that no proper subset of a partition is a partition, so we must have $\{B_q\}_{q\in i P} = \{B_q\}_{q\in Q}$, i.e. $i$ is a bijection and $i P = Q$.

### 1.17
1. All the diagonal elements $(i,i)$ for $i\in S$ together with $(11,12)$, $(12,11)$, $(22,23)$, and $(23,22)$.

### 1.20
1. $\sim$ is reflexive, so for every $a\in A$, we always have $a\sim a$. Therefore, every part has at least one element.
2. Suppose there is an $a\in A_p \cap A_q$ with $p\neq q$. Then both $A_p$ and $A_q$ would be the ($\sim$)-closure of $\{a\}$, but since $\sim$ is transitive they'd have to be the same set. But we know this can't be because $p\neq q$, so it must be that their intersection is empty.
3. $\cup_{p\in P} A_p \subseteq A$ is obvious because the $A_p$ are subsets of $A$. Let's prove the converse. Observe that every $a\in A$ gets sent to some part $A_{p(a)}$. Now notice that $\cup_{p\in P} A_p = \cup_{a\in A} A_{p(a)}$ and it's done - we're not "losing" any element in between steps.

### 1.24
1. $A=B=\mathbb{R}$ and $f(x)=\tanh{x}$.
2. $A=B=\mathbb{R}$ and $f(x)=x\sin{x}$.
3. The first and fourth ones are functions. The second and third ones aren't.
4. Let's see:
    - Neither injective nor surjective.
    - Not a function because the first element in $A$ is mapped to two elements in $B$.
    - Not a function because the first element in $A$ has no image - but it is a _partial_ function.
    - Bijective function.

### 1.25
Let $a\in A$. What's $f a$. Can't be anything. Therefore, $A = \{\}$.

### 1.26
TODO Trivial but boring.

### 1.38
$s(c)=1$, $s(d)=2$, $s(e)=2$, $t(a)=1$, $t(c)=3$, $t(d)=2$, $t(e)=3$

### 1.40
$1 \leq 2$, $1 \leq 3$, $2\leq 2$, $2\leq 3$.

### 1.41
TODO There's no definition of Hasse diagram in the text, but I'm guessing they just have to be lattices? IDK

### 1.42
TODO 12? I see 7... If we label the partitions $\mathbf{0}=\{\{1\},\{2\},\{3\}\}$

### 1.44
Yup

### 1.46
Not a total order because some numbers are (relative) primes, e.g. $2$ and $5$ or $4$ and $9$.

### 1.48
Yes

### 1.51
- $P(\{\}) \simeq 1 $
- $P\{1\} \simeq 0 \to 1$
- $P\{1,2\} \simeq \{\} \to \{1\} \to \{1,2\} \leftarrow \{2\} \leftarrow \{\}$

### 1.53
- The coarsest partition corresponds to the (unique) function into the singleton set, $f \colon S \to \{*\}$.
- The finest partition corresponds to the identity function $f = \mathrm{id}_S$.

### 1.55
For discrete preorders there's no order structure to preserve, so every element in the powerset is an upper set and we just get the powerset ordered by inclusion.

### 1.57
- Product preorder: $(a,1)\leq (c,2)$, $(a,1)\leq (b,2)$.
- Upper set preorder: $\{\},\{b\}, \{c\}, \{a,c\}, \{a,b\}, \{b,c\}$ ordered by inclusion. The Hasse diagram has "levels" $\{\}$, $\{\{a\}, \{b\}\}$, $\{\{a,b\}, \{a,c\}, \{b,c\}\}$.

### 1.63
1. TODO boring but trivial
2. $0\to 1\to 2\to 3$.
3. TODO need tikz

### 1.65
Trivial - basically the identity function but there's an extra element $\{\mathrm{false}\}$ in the codomain with no pre-image.

### 1.66
1. This is the definition of an upper set with least element $p$.
2. Let $p, q\in P$ with $p\leq q$. Then $\uparrow q\subseteq \uparrow p$ by transitivity of $\leq$. Since the order in $U P$ is given by inclusion, $\uparrow$ is a monotone map from $P^{op}$.
3. $p\leq q$ implies $\uparrow q \subseteq \uparrow p$ by (2.). We now show the opposite direction. Any element $q'\in\uparrow q$ is in $\uparrow p$, so $q'\geq p$. This is true for $q'=q$ in particular.
4. $\uparrow a = P$, $\uparrow b = \{b\}$, $\uparrow c = \{c\}$.

### 1.67
For any $p\in P$ the only element $p'\in P$ with $p'\leq_P p$ is $p$ itself, and $\leq_Q$ must be reflexive, so for any $f\colon P \to Q$ we must have $f p \leq_Q f p$.

### 1.69
Let $X=Y=\{1,2,3\}$ and let $f$ swap $1$ and $2$. Let $P=\{\{1,2\},\{3\}\}$ and $Q=\{\{1\},\{2,3\}\}$. Then $f^{\*} P = P$ and $f^{\*} Q = \{\{1\}, \{2,3\}\}$.

### 1.71
- The identity function is monotone by reflexivity.
- Just chain the two implications from monotonicity of $f$ and $g$.

### 1.73
A dagger preorder is just an equivalence relation. "Skeletizing" means quotienting by it, so we end up with a set of parts that are not related by the preorder, i.e. a discrete preorder.

### 1.77
$\mathrm{Prt} S$ is ordered by coarseness, so if $a\leq_{\mathrm{Prt}} b$ it can't be that $1$ and $2$ are in the same part in $b$ but not in $a$, so $\Phi a \leq_{\mathbb{B}} \Phi b$.

### 1.79
TODO

### 1.80
1. Because $1/(n+1) > 0$ for all $n\in \mathbb{N}$.
2. Because there's no $\epsilon$ such that $0 < \epsilon < 1/(n+1)$ for all $n$, since for a given $\epsilon$ we can always take $n>(1-\epsilon)/\epsilon$.

### 1.85
1. Any candidate meet $m\neq p$ must be $m\leq p$. If we also want $m$ to be greater than any $m'\leq p$, we must have $p\leq m$, so $m\simeq p$.
2. If $P$ is a partial order, there are no elements order-equivalent to $p$ other than $p$ itself.
3. The same argument works for joins swapping the $\leq$'s for $\geq$'s.

### 1.90
The meet is the greatest common divisor and the join is the least common multiple.

### 1.98
Let's check $\lfloor - / 3 \rfloor$:
- $f(x) = 3x \leq y \implies x \leq y/3 \implies x \leq \lfloor y/3 \rfloor = g(y)$.
- $x \leq g(y) = \lfloor y/3 \rfloor \implies 3x = f(x) \leq 3 \lfloor y/3 \rfloor \leq y$.

### 1.99
1. Just look at how the arrows do not cross.
2. It fails because $g 1 = 2 \leq 2$ but $f 2 = 2 \geq 1$ -- RIGHT? DOUBLE CHECK THIS

### 1.101
TODO - you really want to get back to this because you don't understand it

### 1.103
TODO boooring might do it in python later

### 1.105
TODO boooring might do it in python later

### 1.106
TODO boooring might do it in python later

### 1.109
1. Set $p = g q$. In particular, we have $p \leq g q$. By the adjunction, this implies $f p \leq q$, which together with the definition of $p$ implies $f g q \leq q$.
2. Suppose $p \leq g q$. By monotonicity of $f$, we have $g f p \leq g q$ and by assumption $p \leq g f p$, so $p \leq g q$.

### 1.110
1. Not sure where to begin
2. No clue

### 1.112
Let $j = \bigwedge A$. By monotonicity, $f A \leq f j$. We want to show that any $b$ satisfying $f A \leq b$ is necessarily greater than $f j$. By adjunction and the universal property of $j$, we have $A \leq j \leq g b$. Finally, taking the adjunction in the other direction, we have $f j \leq b$.

### 1.114
I'd rather check the 7 things implied by the characterization given in Proposition 1.107. Both $f;g$ and $g;f$ are the identity when restricted to $\{1,2,4\}$, they're monotonic - that's 6 things. Finally, $3.9 \leq 4 = f;g (3.9)$.

### 1.118
See `problem118` in `1/adjoints.py`.

### 1.119
1. This is the content of Proposition 1.107.
2. $f;g p \leq f;g;f;g p$ by setting $p\mapsto f;g\,p$ in 1. For the converse, apply $g$ on both sides of $p\leq f;g p$, so we have $g p \leq g;f;g p$ by monotonicity of $g$, but also $g;f;g p \leq g p$ by $f\models g$ and Proposition 1.107. Now apply $f$ to get $f;g;f;g p \leq f;g p$ by monotonicity of $f$.

### 1.124
$\mathbf{Rel}(\{1,2\}) \simeq \mathcal{P} ([2]\times [2]) \simeq \mathcal{P} [4]$. The Hasse diagram is just the lattice with $\{\}$ at the bottom, $\{1,2,3,4\}$ at the top, and three "intermediate floors" containing 4 singletons, 6 2-element sets, and 4 3-element sets, ordered by inclusion.

### 1.125
1. Let's use the total order inherited from $\mathbb{N}$, $1\leq 2\leq 3$. Then $U(\leq) = \{(1,2), (1,2), (1,3), (2,2), (2,3), (3,3)\}$.
2. We may take $Q = \Delta S = \{(1,1), (2,2), (3,3)\}$ and $Q' = S\times S$.
3. $\mathrm{Cl}(Q)$ is the discrete preorder on $S$. $\mathrm{Cl}(Q)\subseteq \leq$ since $\leq$ is a preorder and therefore reflexive.
4. $\mathrm{Cl}(Q')=S\times S$ and $\mathrm{Cl}(Q') \not\subseteq \leq$ since $(3,2) \in S\times S$ but $3\not\leq 2$.

## 2. Resource theories: Monoidal preorders and enrichment

### 2.5
The obstruction is the negative half of $\mathbb{R}$. For instance, we have $-1\leq 1$ and $-2\leq 2$ but $(-1)\times(-2) = 4 \not\leq 1\times 2 = 2$. $(\mathbb{R}^{+}, \times)$ would work, because it's a commutative monoid.

### 2.8
Let's see
1. $x\times y$ better be equal to $x\times y$
2. $x\times e = e \times x = x$ by monoidal unital axiom.
3. Monoids are associative by definition.
4. We imposed commutativity.

### 2.20
1. $t+u \leq (v+w)+u = v+(w+u) \leq v+(x+z) = (v+x)+z \leq y + z$.
2. Reflexivity together with monotonicity of $+$ is used in all inequalities involving the same object on both sides, i.e. something of the form $x+y \leq x'+y$ or its symmetric. By transitivity, we have that the left-most term $t+u$ must be $\leq$ than the right-most term $y+z$.
3. No wires cross.

### 2.21
Two allowed chemical reactions can happen in parallel. Adding literally nothing to the reactants or the products changes nothing. Grouping or permuting compounds changes nothing, so we get associativity and commutativity.

### 2.31
Follows from the fact that $(\mathbb{N}, \times, 1)$ is a commutative monoid.

### 2.33
We have that $1|1$ and $1|2$, but $(1+1)=2\not{|}\,(1+2)=3$.

### 2.34
1. $\mathrm{min}(x,x)$ is just $x$ and $\mathrm{min}(x,y)$ is y if $x\leq y$ and $y\not{\leq}x$, otherwise it's $y$.
2. Let's see
    - If $x\leq x'$ and $y\leq y'$, then $\mathrm{min}(x,y) \leq \mathrm{min}(x',y')$.
    - $\mathrm{min}(x,Y) = \mathrm{min}(Y,x) = x$.
    - $\mathrm{min}$ is associative and commutative.

### 2.35
Let's see
    - If $A \subseteq B$ and $C \subseteq D$, then the intersection $A \cap C$ sits in $B \cap D$ since $A \cap C = (A \cap B) \cap (C \cap D) = (A \cap C) \cap (B \cap D)$.
    - $A \cap S = S \cap A = A$ for any $A \subseteq S$.
    - Intersection is associative and commutative.

### 2.36
Take conjunction $\wedge$ as monoidal functor and $\mathrm{True}$ as monoidal unit. Let's check the axioms:
    - If $p \implies q$ and $p' \implies q'$, then $p \wedge p' \implies q \wedge q'$.
    - $p \wedge \mathrm{True} \iff p$.
    - $\wedge$ is commutative and associative.

### 2.39
Boring and obvious, meh

### 2.40
They're the same? You just flip $\leq$ for $\geq$, right?

### 2.43
1. Let's see
    - $g$ is monotonic since $\mathrm{false} \leq \mathrm{true}$ and $0 \geq \infty$.
    - $g(\mathrm{true}) = 0 \geq 0$.
    - Let's write down some tables
        
| $g(b\wedge b')$ | 0 | 1 |
| ---: | ---: | ---: |
| 0 | $\infty$ | $\infty$ |
| 1 | $\infty$ | 0 |

| $g(b) + g(b')$ | 0 | 1 |
| ---: | ---: | ---: |
| 0 | $\infty$ | $\infty$ |
| 1 | $\infty$ | 0 |

2. The previous tables together with $g(\mathrm{true}) = 0$ show that $g$ is strict.

### 2.44
Yes to all, they're easy to check.

### 2.45
1. Yes, see exercise # whatever.
2. Yes, take the exponential map.
3. No, because negative numbers break everything.

### 2.50
1. Starting with a preorder, reflexivity gets you existence of identities and transitivity gets you associativity.
2. Same but in reverse.

### 2.52
`d(Spain,US) ~ d(Barcelona, NY) << d(US,Spain) ~ d(SF,Galicia)`

### 2.55
There is a family of oplax monoidal functors from $\mathbf{Cost'}=([0,\infty), \geq, 0, +)$ to $\mathbf{Cost'}=([0,\infty], \geq, 0, +)$: for every $K\in [0,\infty)$, take $F_K x = x$ if $K\geq x$ and $F_K x = \infty$ otherwise. This gives a recipe to construct another family of functors from a $\mathbf{Cost'}$-enriched category to a $\mathbf{Cost}$-enriched category: just take the identity on objects and apply $F_K$ on the morphisms. This is related to (the same as?) as "changing the base of enrichment", which is defined in Construction 2.64.

### 2.58
Trivial, a bit tedious.

### 2.60
Trivial, a bit tedious.

### 2.61
I want to interpret `false` as there being no arrows, `maybe` as there being only Kleisli arrows wrt the `Maybe` monad, and `true` as there being arrows. Taking the `min` says that the arrows that can exist between `x` and `z` going through `y` are constrained by the "weakest" kind of arrow between `x` and `y` and `y` and `z`. However, notice that nothing prevents an arrow `x -> z` even in the absence of `x -> y` and `y -> z` arrows - this is how you should read `min(C(x,y), C(y,z)) => True`.

### 2.62
TODO: maybe implement this

### 2.63
Not sure if I'm misunderstanding this problem. On the one hand, the definition of $d(x,y) = \max_{p\in\mathrm{Paths}(x,y)} \min_{i\in\{1,\dots,\mathrm{length}\,p\}} w_i$ is patently weird. On the other hand, by the identity axiom, we should have $\infty \leq d(x,x)$ for all vertices $x$, which is implied by the definition thanks to the $\max$ over _all_ paths, which includes infinite ones - just keep bouncing back and forth between nodes. But this means every node is infinitely far from any other node, including itself. Which is plain strange :_shrug\_emoji_:.

### 2.67
The only distance equal to zero in the Lawvere metric space is `d(Boston, US)`, so the preorder has `Boston <= US` and Spain is an isolated point.

### 2.68
1. For any $K\in\mathbb{R}$, we can set $g_K(x)=\mathrm{False}$ if $x>K$ and True otherwise.
2. The Lawvere metric space $X \to_{1} Y \to_{3} Z$ is mapped to a discrete preorder by $f$ and to the preorder $\{X, Y\leq Z\}$ by $g_2$.

### 2.73
1. The skeletal condition implies that the distance between two objects is zero, they must be the same object, and the dagger condition implies that distances are symmetric.
2. The skeletal condition quotients out isomorphic objects, while the dagger condition imposes antisymmetry. For preorders, this means that the resulting category will allow objects to appear only once and that there will be no relations between them, so we end up with a set - just a bunch of objects, no structure. For Cost-categories, the conditions turn the category into a(n extended) metric space.

### 2.75
1. $I_{X\times Y} = I_X \otimes I_Y \leq X(x,x)\otimes Y(y,y) = (X\times Y)((x,y),(x,y))$.
2. Same trick as above.
3. When translating the $\times$ into $\otimes$ on the left hand side of the expression in 2. the 2nd and 3rd factor need to be swapped in order to make use of monotonicity of the enriching functor on $X$ and $Y$ separately.

### 2.78
We get the Manhattan or $p=1$ distance $d((x,y),(x',y')) = d(x,x') + d(y,y') = |x-x'| + |y-y'|= 6 + 2 = 8$.

### 2.82
1. Parallel composition of string diagrams `w -- <= -- w'` and `v -- <= -- v` gives `w x v -- <= w' x v`.
2. If any of the inequalities in (2.80) is false, there's nothing to check. Assume both are true. Then we can modify the string diagram `a x v <= w` to insert `a <= (v -o w)` along the upper wire, resulting in `(v -o w) x v <= w`.
3. Take $(v \multimap -) \otimes v$ on both sides of $w\leq w'$. The inequality is respected by monotonicity shown in (2.). Now the parallel composition can be broken into $v\leq v$ and $v\multimap w \leq v \multimap w'$.
4. (2.80) together with monotonicity are the definition of a Galois connection i.e. an adjunction between preorders.

### 2.84
Remember that both $\leq$ and $\multimap$ should be read as $\implies$ - I'm sure there is a way to make this rigurous, something something internal logic blabla. With this in mind $a\wedge b \leq c \iff a \leq (b\multimap c)$ just says that an implication is the curried form of a product: $a\wedge b \implies c \iff a \implies (b\implies c)$. TL;DR: define $a\multimap b = \neg a \vee b$ which is secretely just $a\implies b$.

### 2.92
1. In Bool $0\leq b$ for any $b$, so $0 = \mathrm{false}$. In Cost it's the same but with the order reversed, so $0=\infty$.
2. In Bool the join is the logical or operation. In Cost, it's the infimum.

### 2.93
We just need to show that $\implies$ is adjoint to $\wedge$ and $\vee$ is a good candidate for join operation. This has been done in previous exercises.

### 2.94
Define $A\multimap B = (S \setminus A) \cup B$ and $A \vee B = A \cup B$. This should work because it does in Bool.

### 2.103
$$
M_{\mathbf{Bool}} = \begin{pmatrix}
    1 & 0 \\
    0 & 1
    \end{pmatrix}
$$
and
$$
M_{\mathbf{Cost}} = \begin{pmatrix}
    0 & \infty \\
    \infty & 0
    \end{pmatrix}
$$

### 2.104
1. We first need to show that $0 \otimes v \simeq 0$ and $0 \vee v = v$ for all $v\in V$. The fact that $0\leq 0\otimes v$ is a consequence of $0\leq x$ for any $x\in V$ since it's the join of the empty set (see example 2.91). The converse $0\otimes v \leq 0$ is true iff $0 \leq (x\multimap 0)$ by adjointness, and since $x\multimap 0$ is an element of $V$ because $V$ is closed, this must be true as well, so $0\simeq 0\otimes v$. To show $0 \vee v = v$ just notice that since $0\leq x$ for any $x$, the join conditions simply imply that $v\leq 0\vee v \leq x$ for any $v\leq x$, so taking $x\simeq v$ in particular shows that $0\vee v \simeq v$. Finally, we write $(I_X \dot M)(x,y) = \bigvee_{x'\in X} I_X(x,x') \otimes M(x',y) = (\bigvee_{x\neq x'} 0) \vee (\bigvee_{x=x'} M(x',y)) = M(x,y)$, where we have used the fact that the join distributes over the tensor product.

2. We need to use (2.87) twice and the fact that two successive join operations commute, meaning that $\bigvee_{a\in A} \bigvee_{b\in B} = \bigvee_{a\in A} \bigvee_{b\in B}$. Pretty sure we can prove this using Fubini theorem for coends, but that sounds like _extreme_ overkill. Maybe have a look at [Fosco](https://arxiv.org/pdf/1501.02503.pdf), section 1.3.

### 2.105
I need to go back to this because I misunderstood the definition of $M$ as I suspected - so TODO

## Databases: Categories, functors, and universal constructions

### 3.3
5 and 5, so each arrow is a non-ID column.

### 3.9
Since the points have no internal structure, we get unitality (walking a self-loop amounts to nothing). Path concatenation can be parenthesized however we want, so we get associativity.

### 3.10
Trivial, boring.

### 3.12
1. Single object, just the identity.
2. Empty, no objects or morphisms.
3. There are $n$ identities and $n-1$ generating morphisms. A morphism is univocally determined by its source and target, and the target cannot be to the left of the source, so we get $n(n+1)/2$ morphisms.

### 3.15
$m+n$

### 3.16
1. 4 identites, 4 (non-identity) generating morphisms, and 2 composites $f;h$ and $g;i$.
2. The two composites.
3. $f$ and $h$.

### 3.17
Same 4 identities, same 4 generating morphisms and now the composites are the same and equal to $j$ - so 9 in total.

### 3.19
The equation says there are only 4 classes: $\{z, s, s;s, s;s;s\}$. Any morphism $s^n$ with $n\geq 4$ would be $s;s$ if $n$ is even and $s;s;s$ if odd.

### 3.21
1. $f=g$
2. $f=id$
3. $f;h=g;i$
4. None

### 3.22
It's the most boring preorder possible: single element satisfying $x\leq x$.

### 3.25
Three constants, three order-preserving embeddings, and three non-order-preserving embeddings.

### 3.30
1. $f^{-1} 1 = b$, $f^{-1} 2 = a$, $f^{-1} 3 = c$.
2. $3^3 = 27$

### 3.31
Composing identity with itself yields the identity.

### 3.32
1. No, because there are no negative numbers and thus no inverses.
2. Yes, it's $\mathbb{Z}_2$.

### 3.33
Having isomorphisms would impose equations between morphisms, breaking assumption that the category is free.

### 3.37
Looking at exercise (3.25), there are 9 possible candidates. The three constants and the three order-preserving maps fit the bill because we can draw arrows as needed, but the three non-monotone maps don't work because there'd be no image for the arrow $f_1$.

### 3.39
The identities and generating morphisms go to the obvious places, and $F f';h' = F g';i' = f;h = g;i$.

### 3.40
$F$ and $G$ are the identity on objects but $F$ sends the only morphism in $C$ to the upper morphism in $D$ and $G$ sends it to the lower one.

### 3.43
1. Any category is a graph plus a bunch of equations. You just need the identity functor to be the identity on objects and sending every morphism to itself will respect the equations by functoriality.
2. Just do function composition on objects and hom-sets separately.
3. Again, using function composition on objects and hom-sets separately, we show unitality and associativity.

### 3.45
Any set has an identity morphism on itself, so that's it.

### 3.48
1. Examples of functions that are their own inverse:
    - $F z = \mathbb{Z}$ and $F s = (-1)*$.
    - $F z = \mathrm{List}[a]$ for some type $a$ and $F s = \mathrm{reverse}$.
2. Example of equalizer: let $F b$ be the set of binary strings; and let $Fg$ count the number of ones in the string, and $Fh$ be the length function. Then $a$ is the set of binary strings that contain no zeroes and $Ff$ is the canonical embedding of $Fa$ in $Fb$.

### 3.55
1. Literally that. Define $\gamma = \alpha;\beta$ to be $\gamma_a = \alpha_a;\beta_a$ for all $a \in \mathrm{Ob}(\mathcal{C})$. Naturality in $\alpha$ and $\beta$ implies naturality in $\gamma$ by pasting commutative squares. Associativity is inherited from associativity of morphisms in the category $F \mathcal{C}$.
2. Again, we do it component-wise: $id_a \colon F a \to F a$ is just the identity morphism on $F a$. Unitality is inherited from unitality of morphisms in the category $F\mathcal{C}$.

### 3.58
1. The components of any natural transformation $F\to G$ is a morphism in $\mathcal{P}$. Since any two morphisms in a preorder are the same, there can be no more than one natural transformation between any two functors.
2. Counter-example. Let:
    - $\mathcal{P} = \mathbf{Bool}$
    - $\mathcal{C}$ be the free category with
        - two objects $a$ and $b$
        - two parallel morphisms $F\leq, G\leq \colon a\to b$
        - two parallel morphisms $\alpha_a, \beta_a\colon a \to a$, and
        - two parallel morphisms $\alpha_b, \beta_b\colon b \to b$.
    - Then $\alpha$ and $\beta$ are two different natural transformations between $F$ and $G$.

### 3.62
The vertices are:

| Vertex |
| :--- |
| Employee |
| Department |
| string |

and the arrows are:

| Arrow | source | target |
| :--- | :--- | :--- |
| Mngr | Employee | Employee |
| WorksIn | Employee | Department |
| Secr | Department | Employee |
| FName | Employee | string |
| DName | Department | string |

### 3.64
1. Naturality imposes $\alpha_{Vertex} G s = H s \alpha_{Arrow}$ and $\alpha_{Vertex} G t = H t \alpha_{Arrow}$. Plugging $b$ in the left hand side of the first equation, we get $\alpha_{Vertex} 2 = H s \alpha_{Arrow} b$. From plugging $a$ into the second one, we know that $\alpha_{Vertex} 2 = 5$, so we must have $\alpha_{Arrow} b = e$, since this is the only arrow in $H$ with source $5$.
2. I drew it.
3. It does.

### 3.67
We get the same graph with the arrows reversed. Note that this no longer defines a deterministic machine, because the transition function defined in $I$ not injective.

### 3.73
1. $(f, id_B) = (x,b) \mapsto (f(x),b)$
2. $\lambda b. x \mapsto \lambda b. f(x)$
3. $p(3) = \lambda x. x+3$

### 3.76
Every object to the only possible object; every morphism to the identity.

### 3.78
We have one arrow per email sent, labeled by its ID, with source sender and target receiver.

### 3.81
From the definition of a preorder category, $c\leq z$ in $\mathcal{P}$ iff $c\to z$ in $\mathcal{C}$. Moreover, the morphism is unique since preorder categories are thin.

### 3.82
$\mathbf{1}$, the category with a single object and a single morphism.

### 3.83
The free category with two objects and two parallel arrows between them.

### 3.88
Replace all $\leq$ for $\to$ in the definition of meet and use the fact that preorders are thin.

### 3.90
1. Products of identities.
2. Because it's component-wise associative.
3. It's isomorphic to $\mathbf{2}$ - meaning there's a pair of functors between them that compose to the identity in both directions.
4. We get the preorder where $(a,b)\leq (a',b')$ iff $a\leq_P a'$ and $b\leq_Q b'$.

### 3.97
The definition reduces to the case of products by "forgetting" any morphisms in the diagram.

### 3.98
The diagram is its own limit since the projection is the identity?

### 3.101
Same on objects, morphisms flip source and target.

## Collaborative design: Profunctors, categorification, and monoidal categories

### 4.4
1. (cat, nothing) $\leq$ (-, this book)
2. If $x$ can be explained given $y$ and $x'$ is "simpler" than $x$ ($x'\leq x$) while $y'$ gives "more info" than $y$ ($y\leq y'$), then $(x,y)\leq (x',y')$ in $X^{op}\times Y$, meaning that $x'$ can be explained with $y'$.

### 4.7
Just check each case. Boring.

### 4.9
Follows from the definition of functor enriched in a quantale.

### 4.10
4.8 is more general, because $X$ and $Y$ aren't just preorders but categories enriched in $\mathbb{Bool}$, so we can do boolean algebra with their morphisms, i.e. there's a closed monoidal structure on them.

### 4.12
| $\Phi$ | a | b | c | d | e |
|---|---|---|---|---|---|
| N | true | false | true | false | true |
| E | true | true | true | true | true |
| W | true | false | true | false | true |
| S | true | true | true | true | true |

### 4.15
Boring if you did the previous one and can add small integers.

### 4.17
See `4/cost_product.py`

### 4.18
It's valid but I don't understand why they're not using $T^{op}$... and it means that producing a movie that's both good-natured and funny would cost more than $1M.

### 4.22
Boring, I'll do it later with my python implementation.

### 4.26
Trivial, just do the identity on objects.

### 4.30
1. Let's see
   - Definition of monoidal unit as identity for $\otimes$
   - Unitality and (lax monoida) functoriality of $\otimes$
   - Definition of join in a poset
   - Definition of matrix multiplication in a quantale
2. The first one because true is the top element in Bool; the second one because if $true \wedge b \leq \bigvee_{p} (b'(p) \wedge b) = b \wedge \bigvee_{p} b'(p)$ so the lhs equals the rhs regardless of the value of $b$.
3. So
    - Monoidal unit is the identity for $\otimes$
    - Unitality and (lax monoida) functoriality of $\otimes$
    - Associativity and (lax monoidal) functoriality of $\otimes$

### 4.31
We use that
- $\otimes$ distributes over $\vee$ (proposition 2.87),
- $\otimes$ is associative, and
- joins over different collections of objects commute (do I need the skeletal property here?).

### 4.36
$\hat{\mathrm{id}}(p,p') = P(\mathrm{id} p, p') = P(p,p') = U_P(p,p')$

### 4.38
$\breve{+} (d,a,b,c) = \mathrm{true}$ iff $d \leq a+b+c$.

### 4.41
1. Just apply definition 4.34.
2. The identity is adjoint to itself since $id;id=id$.

### 4.44
Tedious, will implement it later # TODO

### 4.48
Obvious, just replace $\leq$ with $\to$.

### 4.50
1. $g(5,3) = (false, 2)$
2. $g(3,5) = (true, -2)$
3. $h(5, true) = 5$
4. $h(-5, true) = -5$
5. $h(-5, false) = 6$
6. $q(-2,3) = (2,-13)$
7. $q(2,3) = (-1, 7)$

### 4.53
There are two main differences:
1. Definition 3.6 uses the language of ZF set theory and, in particular, uses the symbol $\in$. This is to be replaced by an arrow from the monoidal unit in category theory. Since in set we have that $S \simeq S^{1}$, i.e. an arrow from the singleton set to another set $S$ simply amounts to picking an element of $S$, this is a distinction without a difference.
2. This differences is more important: Unitality and associativity are strict in definition 3.6, but only hold up to isomorphism in definition 4.51. In particular, we need to make use of the left and right unitors and the associator in $\mathcal{V}$ to make sense of composition and identities. However, by Mac Lane's coherence theorem we can always think about $\mathcal{V}$ as being strict, so :shrug_emoji:.

### 4.54
Identity elements in Lawvere metric spaces state the fact that $0\geq d(x,x)$ i.e. the distance from any point to itself is zero.

### 4.62
1. $\eta_A (\emptyset) = \{\{(1,1), (1,2)\}, \{(2,1), (2,2)\}, \{(3,1), (3,2)\}\}$
2. $\epsilon_A x = \emptyset$
3. TODO - i don't really understand this example for the same reason I didn't understand it in the GoI paper; I need to work out the details re: transitive closure

### 4.64
"If I can get $x$ from $x'$ and $y$ from $y'$, then I can get $(x,y)$ from $(x',y')$"

### 4.65
They're inherited from the monoidal structure in $\mathcal{V}$. More concretely, they can be defined in terms of the left and right unitors of $\mathcal{V}$.

### 4.66
TODO: I'm getting confused with the type signature of profunctors because on the one hand they're $1 \to X^{op}\times X$ but on the other that's secretely $1\times X^{op} \times X \to V$.

## Signal flow graphs: Props, presentations, and proofs

### 5.5
1. Let $f 1 = 1$, $f 2 = f 3 = 2$, $g 1 = 1$, and $g 2 = 4$.
2. $(f+g) x = f x$ if $x\leq 3$ and $(f+g) x = 2 + g x$ if $x>3$.
3. Just function composition.
4. $f x = x$.
5. $\sigma_{m,n} (x, i) = (x, (i+1)\%2)$

### 5.9
1. $\mathbf{Bij}$ but quotienting out by bijection, so you get a discrete poset.
2. The skeleton (modding out permutations) of $(\mathbf{FinSet}, +)$ gives rise to the additive, totally ordered monoid $(\mathbb{N}\cup \{0\}, 0, +, \leq)$.
3. $(\mathbb{N}, 1, \times)$ with a morphism $f \colon n \to m$ iff $n$ divides $m$.

### 5.10
Let's take $\mathbf{Rel}$
1. $\mathbf{Rel}(m,n) = \mathcal{P}(m\times n)$
2. $\mathbf{Rel}(n,n) = \Delta n = \{(i,i)\colon i \in \{1,\dots,n\}\}$
3. $\sigma_{m,n} (x, i) = (x, (i+1)\%2)$ where $i\in \{0,1\}$.
4. See example 5.8
5. See footnote 3

### 5.16
Just stick the outputs of the first graph into the inputs of the second.

### 5.18
Just copy the diagram and put it in parallel.

### 5.20
1. $R x y \implies x\leq_P y$ so if this implies $f x \leq_Q f y$, then $f$ is monotone.
2. $R x y \implies x\leq_P y$ so if $f$ is monotone, then $f x \leq_Q f y$.

### 5.21
1. Yes, because $g a R g b \implies g a \leq_P g b$.
2. No, because the implication in 1. only goes one way. In particular, $g a$ and $g b$ may not be related by $R$ but become related once we take its reflexive, transitive, closure.

### 5.23
1. $\mathrm{dom} (f\colon x \to y) = x$ and $\mathrm{cod} (f\colon x \to y) = y$
2. Any functor needs to specify two pieces of data: how it acts on objects ($f$) and how it acts on morphisms ($g$), with the extra constraint that $\mathrm{dom} (g(a)) = f \mathrm{dom} a$ and similarly for the codomain. So this is just that statement together with $(s,t)$ being the (co)domain functions in $\mathrm{Free} G$.
3. Yes, perhaps one with infinitely many vertices. Not sure what the adjunction is.

### 5.24
1. They're strings on the one-letter alphabet $A$.
2. So it's isomorphic to the additive monoid $\mathbb{N}\cup \{0\}$.
3. Binary strings.

### 5.28
Intuitively, Free(G) has functions of "all possible arities" and these are not subject to any extra equations, so we can build any port graph.

### 5.32
Trivial

### 5.35
Even in the free prop we should mod out the diagonal of $\mathrm{Expr}(G)\times \mathrm{Expr}(G)$. However, this is accomplished by imposing the axioms of a monoidal category, so I think both definitions are the same.

### 5.41
$M(i,j) = 1$ if $i=j$ and $0$ otherwise.

### 5.43
$(16x+4y, x+4y)$

### 5.51
$A+B=$$\begin{pmatrix}
3 & 3 & 1 & 0 & 0 & 0 & 0 \\
2 & 0 & 4 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 2 & 5 & 6 & 1
\end{pmatrix}$

### 5.55
$\begin{pmatrix} 1 & 1 & 1 \end{pmatrix}$

### 5.58
I did it on paper - TODO w/ tikz

### 5.59
Let $M$ be an arbitrary $m$-by-$n$ matrix over a rig $R$ and let $x\in R^n$. The string diagram that implements $M$ consists of the following layers:
1. First layer is $m-1$ applications of copy on each of the $n$ inputs - the exact details don't matter because associativity is strict.
2. Second layer amplifies the $i$-th copy of the $j$-th input by $M_{ij}$ when this number is not zero and disard otherwise.
3. Third layer is the morphism sending $(x_1, x_1,\dots, x_2, x_2,\dots) \mapsto (x_1, x_2,\dots, x_n, x_1, x_2)$. TODO: write this in terms of contiguous swaps.
4. Fourth layer adds the wires in chunks of size $m$. Again, associativity guarantees that the details don't matter.

### 5.62
1. The only useful equation is $\times 0$ = discard and can be used in the first two diagrams.
2. Direct application of that equation.

### 5.63
1. How do I prove there is no application of the equations in 5.60 that maps the 2nd diagram into the 1st one?
2. Easy to see the resulting matrix ignores the first input and copies the second.

### 5.67
1. Multiplication of real numbers is associative, and its "curried" unit is $\lambda x. 1$
2. Addition of real numbers is associative, and its "curried" unit is $\lambda x. 0$

### 5.69
1. 
   * $U(0) = R^0 = \{f\colon \{\} \to R\mid f\,\mathrm{function}\} \simeq \{\star\}$
   * $U(m + n) = R^{m+n} = R^m \times R^n = U(m)\times U(n)$
2. Follows from the fact that $U$ is a functor (so it preserves composition) and the fact that it preserves the monoidal product.
3. The additive one since the monoidal product is $+$.

### 5.77
1. The behaviour of $+^{op}$ is $\mathrm{B}(+^{op}) = \{(x+y, (x,y)) \mid x,y \in R\} \subseteq R\times R^2$. Note that this is not a function but a relation, since addition is not injective, so for instance, if $R=\mathbb{N}$, $(+^{op})(3)$ would contain $(1,2)$ but also $(2,1)$, $(3,0)$ and $(0,3)$.
2. The behaviour of $\Delta^{op}$ is $\mathrm{B}(\Delta^{op}) = \{((x,x),x)\mid x\in R\} \subseteq R^2\times R$. Note that this is not a total function but a partial function, because $\Delta$ is not surjective. It sends the diagonal of $R^2$ to $R$ canonically and is undefined elsewhere.

### 5.80
$B+C = B\sqcup C = (B\times \{1\})\cup (C\times \{2\})$

### 5.82
Follows immediately from the definition of composite behaviour:

$
\\ \mathrm{B}(g;h^{op}) =\\
$
$
\{(x,z) \mid \exists y\in R^n \colon S(g)(x)=y\wedge y=S(h^{op})(z)\} =
$
$
\\ \{(x,z)\in R^m\times R^l\mid S(g)(x)=S(h)(z)\}
$

### 5.83
Similarly:

$
\\ \mathrm{B}(g^{op};h) =\\
$
$
\{(x,z) \mid \exists y\in R^n \colon S(g^{op})(x)=y\wedge S(h)(y)=z\} =
$
$
\\ \{(S(g)(y), S(h)(y)) \mid y \in R^m\}
$

### 5.84
1. The diagram's behaviour defines the kernel: $\mathrm{B}(g;0^n) = \{x\in R^m \mid S(g)(x) = \vec{0}\in R^n \} \overset{\mathrm{def}}{=} \ker S(g)$
2. Analogously, $\mathrm{B}((\mathrm{disc}^{op})^m; g) = \{z\in R^n \mid \exists x\in R^m\colon S(g)(x) = z \} \overset{\mathrm{def}}{=} \mathrm{im\,} S(g)$
3. Follows from the fact that $S$ preserves the monoidal product $+$ and composition.

### 5.85
We write down the behaviour of the composite of two linear relations $B;C$ and note that, if $(x,z)\in \mathrm{B}(B;C)$, then:
- so is $(rx, rz)$ for any $r\in R$ because there must be some $y$ such that $(rx,ry)\in B$ (by linearity of $B$) and $(ry,rz)\in C$ (by linearity of $C$); and
- an analogous argument applies to addition.

## 6 Electric circuits:Hypergraph categories and operads

### 6.3
1. Discrete preorder.
2. $a\leq b$.
3. $a\leq b$ and $b\leq a$.

### 6.6
1. The initial object is $a$. There is just one morphism $1_a\colon a\to a$.
2. The initial object is $a$, with unique morphisms $1_a\colon a \to a$, $f\colon a \to b$ and $f;g \colon a \to c$.
3. There are zero morphisms between $a$ and $b$, so none can be an initial object.
4. There is more than one morphism from $a$ to itself - the identity and the one pictured - so it can't be an initial object.

### 6.7
1. $f(1_R) = 1_S$ and $f(r_1 *_R r_2) = f(r_1) *_S f(r_2)$.
2. By analogy [with rings](https://www.wikiwand.com/en/Category_of_rings#/limits_and_colimits), I think it should be $(\mathbb{N}, 0, +, 1, \cdot)$ because it's the "freest" rig.

### 6.8
The universal object property is in this case satisfied by the initial object. A comparable object is any other object candidate to be initial but such that there is a unique morphism from the initial object to it. In particular, any two initial objects are isomorphic.

### 6.10
Since $c_1$ is initial, there is a unique $!_1\colon c_1 \to c_2$. Analogously, there is a unique $!_2\colon c_2\to c_1$. The isomorphism is $!_1 !_2$ together with its inverse.

### 6.13
Replace arrows with $\leq$.

### 6.16
| $x$ | $[f,g](x)$ |
| :--- | :--- |
| apple1 | a |
| banana1 | b |
| pear1 | p |
| cherry1 | c |
| orange1 | o |
| apple2 | e |
| tomato2 | o |
| mango2 | o |

### 6.17
1. Follows from the left commuting triangle in the definition of coproduct.
2. Follows from the right commuting triangle in the definition of coproduct.
3. Follows from the universal property of the coproduct applied to $\mathrm{cod} h$.
4. From the definition of $[f,g]$ and the fact that (roughly) $i^2=i$.

### 6.18
1. Given morphisms $a \to_{f} b \to_{g} c$ and $a' \to_{f'} b' \to_{g'} c'$, we get $a+a' \to_{[f,f']} b+b' \to_{[g,g']} c+c'$.
2. From the universal property of the coproduct, there is always a left inverse of the injection $i_A \colon A \to A + B$ as long as there is an arrow $g \colon B \to A$, since then we can do $[1_A, g] \colon A+B \to A$ and have $i_A; [1_A, g] = 1_A$. Since there is always a (unique) arrow from the initial object to any $A$, this left inverse exists. The other direction is even easier: because the triangle $\phi \to_{!} A+\phi \to_{f} A+\phi$ together with $phi \to_{!} A+\phi$ commutes for any $f$ (because of the universal property of the coproduct) and we have the same morphism on two sides (because of the universal property of the initial object) we have $! = !;f$ and hence $f=1_{A+\phi}$. The same arguments apply to $\phi+A$.
3. Let $i_{i,X,C}$ be the injection of the object $X$ onto the $i$-th component of a coproduct $C$. Then we have
   - TODO - tedious ugh
   - The unique map from $A+B$ to $B+A$ is $[i_{2,A,A+B}, i_{1,B,A+B}]$.

### 6.24
1. Since there are no morphisms other than identities, the existence of pushouts is vacuously true.
2. The singleton set for sure. And the empty set too, right?

### 6.26
Let $k_{n}$ denote the image of $k \in \underline{n}$ under the injection into $\underline{3} \sqcup \underline{5}$. Then the four equivalence classes in the pushout are:
- $1_3 \sim 1_5 \sim 2_3$
- $3_3 \sim 3_5 \sim 5_5$
- $2_5$
- $4_5$

### 6.28
1. Both arrows $f;i_X$ and $g;i_Y$ must equal the unique arrow $!\colon \phi \to X+Y$, so they're the same arrow.
2. Because of the universal property of the coproduct.
3. Because the morphisms $f$ and $g$, being unique, impose no restrictions on the commutativity of the pushout diagram and can be safely deleted.

### 6.35
TODO: kinda tedious. Need to show uniqueness of arrows in the larger diagram from uniqueness in the smaller components.

### 6.41
Taking $J = X \leftarrow_{f} N \rightarrow_{g} Y$ and $D\colon J \to \mathrm{Set}$, we have $\mathrm{colim}_J D = \{(v,d)\mid v\in \{X, N, Y\},\,d\in D(v)\} / \sim$ with $(N, n) \sim (X, f(n)) \sim (Y, g(n))$ for all $n\in D(N)$, so this is just the disjoint union $DX \sqcup DN \sqcup DY$ quotiented by classes in $N$, as in example 6.25 - note that the element $DN$ "disappears" when quotienting by $\sim$.

### 6.48
In $\mathcal{C}$ it looks like $A \sqcup B \to_f N \sqcup P \leftarrow_g B \sqcup C$ and we draw $X \sqcup Y$ by stacking $X$ on top of $Y$.

### 6.49
Let $A \overset{f}{\rightarrow} N \overset{g}{\leftarrow} B$ and $A \overset{f'}{\rightarrow} P \overset{g'}{\leftarrow} C$ be cospans. To compose them, we do the following:
- We construct the graph with nodes $A \sqcup N \sqcup B \sqcup P \sqcup C$ and edges given by the cospan arrows i.e. there is an edge between nodes $x$ and $y$ iff $y=h(x)$ or $x = h(y)$ for some $h\in \{f, g, f', g'\}$. We note that the resulting graph is 5-partite.
- Then we take the subgraph with nodes $N \sqcup B \sqcup P$ and quotient it by connectivity, i.e. we replace each connected component in this subgraph by a single node. This amounts to calculating $N +_B P$. The resulting tripartite graph with nodes $A \sqcup N +_B P \sqcup C$ is the composition of the cospans.

### 6.57
1 is the same as 4 and 6 because they all have just one connected component. 3 is the same as 5 because both have two connected components with the same arities, $(1,2)$ and $(1,1)$. Finally, 2 is its own thing because there is no "information flow" from inputs to outputs.

### 6.59
1. $B$ because it has to coincide with the 3rd output wire of the composite.
2. $D$ because it has to coincide with the 2nd output wire of $h$.
3. $D$ because it's the 1st output wire of $h$.

### 6.62
I drew them. Trivial to draw, hard to describe.

### 6.63
[not super sure about this proof] We need to show that the pushout $P$ of $X \overset{1+1}{\leftarrow} X+X \overset{1+1}{\rightarrow} X$ is $X$. Since both morphisms in the span are the same, the commutative square says that both morphisms of type $X\to P$ are also the same. Call this morphism $i$. Moreover, by the universal property, any other morphism $i'\colon X \to P'$ must factorize uniquely through $P$. We note that this requirement is satisfied by taking $P=X$ and $i=1_X$. Since limits are defined only up to isomorphism (?), we're done.

### 6.67
We have a diagram that is identical to the one on the right-hand side of the Frobenius law, except for the unit in the lower input wire and the counit in the upper output wire. We use the Frobenius law to deform it into the (more symmetric) diagram in the middle of equation (6.53.1), and then we use unitality to get rid of the unit/counit wires.

### 6.70
Let $A\subseteq S$ and $B\subseteq T$. Then
- $\phi_{S,T}; \mathrm{im}_{f\times g} (A, B) = \mathrm{im}_{f\times g} A\times B = \mathrm{im}_{f} A \times \mathrm{im}_g B$
- $\mathrm{im}_{f} \times \mathrm{im}_{g}; \phi_{S',T'} (A, B) = \phi_{S',T'} (\mathrm{im}_{f} A, \mathrm{im}_{g} B) = \mathrm{im}_f A \times \mathrm{im}_g B$

### 6.78
A regular cospan category $\mathbf{Cospan}_{\mathcal{C}}$ is a decorated cospan category where all decorations are the same and trivial.

### 6.79
$V = \{1,2,3,4\}$, $C=\Omega\mathbb{R} \sqcup F \mathbb{R} \sqcup H \mathbb{R}$, and
| $A$ | $s$ | $t$ | $\mathcal{l}$ |
|---|---|---|---|
| $a$ | 1 | 2 | $2\Omega$ |
| $a'$ | 1 | 2 | $3F$ |
| $b$ | 1 | 3 | $1\Omega$ |
| $c$ | 2 | 4 | $1\Omega$ |
| $d$ | 3 | 4 | $1H$ |

### 6.80
The circuit with the lightbulb and the resistor glued in series.

### 6.82
The circuit with the battery and the switch along separate, parallel wires.

### 6.84
$V=\{1,2\}$, $A=\{*\}$, $s(*)=1$, $t(*)=2$, $\mathcal{l}(*)=\mathrm{battery}$.

### 6.86
TODO - trivial but tedious

### 6.88
$\eta;x;\epsilon$ is built by identifying the loose end on the battery with the loose end on the lightbulb and the loose end on the switch with the loose end on the resistor.

### 6.96
TODO I really don't understand this construction

## Logic of behavior: Sheaves, toposes, and internal languages

### 7.4
Assume the square on the left is a pullback. Then

$$
AB; BB' = AA';A'B' \quad \text{(left square commutes)} \\
AB; BB'; B'C' = AA'; A'B'; B'C' \quad \text{(compose with $B'C'$)} \\
AB; BC; CC' = AA'; A'B'; B'C' \quad \text{(right square commutes)}
$$

so the large rectangle commutes. Moreover, the universal property for the left square implies the universal property for the large rectangle by composing the map to $B$ with $BC$.

Conversely, if the large rectangle is a pullback, we have

$$
AB; BC; CC' = AA'; A'B'; B'C' \quad \text{(rectangle commutes)} \\
AB; BB'; B'C' = AA'; A'B'; B'C' \quad \text{(right square commutes)} \\
AB; BB' = AA'; A'B' \quad \text{(deleting $B'C'$)}
$$

so the left square commutes. Moreover, the universal property for the rectangle implies the universal proeprty for the left square since any map to $B$ yields a map to $C$ by composing with $BC$.

### 7.6
TODO

### 7.7
1. TODO
2. Both maps from any other candidate object to $A$ have to be the same.

### 7.8
TODO

### 7.9
The surjection is $\underline{3}\to\underline{2}$ with $1\mapsto 1$, $2\mapsto 1$, and $3\mapsto 2$. The injection is $\underline{2} \to \underline{3}$ with $1\mapsto 2$ and $2\mapsto 3$.

### 7.11
TODO - key intuition is to work in bool, treat $\leq$ and $\multimap$ as implication

### 7.16
1. $[m](-5) = \mathrm{false}$
2. $[m](0) = \mathrm{true}$

### 7.17
1. $[\mathrm{id}_{\mathbb{N}}](n) = \mathrm{true}\quad\forall n \in \mathbb{N}$
2. $[\mathrm{!}_{\mathbb{N}}](n) = \mathrm{false}\quad\forall n \in \mathbb{N}$

### 7.19
1. $\neg$ is the characteristic function of a subobject of $\mathbb{B}$.
2. $\mathrm{false} \colon 1 \to \mathbb{B}$ makes the pullback diagram of the subobject classifier commute, so that's it.

### 7.20
1. So

| $P$ | $Q$ | $P\wedge Q$ | $P=(P\wedge Q)$ |
|---|---|---|---|
| T | T | T | T |
| T | F | F | F |
| F | T | F | T |
| F | F | F | T |

2. It's implication, yeah.
3. 1st, 2nd and 4th columns of the table
4. It classifies the morphisms in Bool seen as a preorder, i.e. the subobject
$$
\bigsqcup_{i,j\in\mathbb{B}} \mathrm{Set}(i,j) \to \mathbb{B\times B}\\
(f \colon i \to j) \mapsto (i,j)
$$

### 7.21
1. $[E](17) = \mathrm{false}$.
2. $[P](17) = \mathrm{true}$.
3. $[T](17) = \mathrm{true}$.
4. 2 is the only number that's even and prime, then 10, and 11.

### 7.27
1. Open intervals $(x-\epsilon, x+\epsilon)$.
2. Whenever $\forall x\in X$ there is an $\epsilon > 0$ such that $(x-\epsilon, x+\epsilon)\subseteq X$.
3. $U_1 = (-1/2, 1)$, $U_2 = (-1, 1/2)$, $U=(-1,1)$.
4. $U=(0,\infty)$ and $U_i = (0,i)$ for $i\in \mathbb{N}$.

### 7.29
1. yup
2. obvious
3. Let $f\colon X \to Y$. Given $B\subseteq Y$, its preimage $f^{-1}(B)$ is in $P(X)$ and since $\mathbf{Op}_{fine} = P(X)$, it's always open.

### 7.31
1. $\emptyset \subseteq \{1\} \subseteq X$.
2. Each open $U\in \mathbf{Op}$ has essentially just one cover: $U$ itself. However, any family of open sets containing an arbitrary number of copies of the empty set and an arbitrary number of copies of $U$ is also a cover.

### 7.32
1. $B=X$.
2. Everything carries over because topologies are closed under finite intersections.
3. Assume $B\subseteq Y$ is open in $X$. Then $f^{-1}(B)$ is open in $Y$ because $B\cap Y = B$.

### 7.34
A category enriched on the preorder of open sets of a topological space $X$ has:
- Hom-objects given by open sets of $X$. In particular, the hom-object of endomorphisms is $X$ for all objects.
- The condition that $\mathcal{X}(x,y) \otimes \mathcal{X}(y,z) \leq \mathcal{X}(x,z)$ reads $(x\to y) \cap (y\to z) \subseteq (x\to z)$ which can be interpreted as "the morphisms from $x$ to $z$ contain the morphisms that can be formed by composition going through $y$, plus maybe some other stuff".
- I wanna guess that $(x\to y) = X$ iff $x\simeq y$ but I don't know if it's true...

### 7.38
1. $\{a_1, a_2\}$
2. $\{c_1\}$
3. $\{\}$
4. $f'(x)=f(x)$ if $x\neq b_3$ and $f'(b_3) = d$

### 7.40
1. $\mathrm{Sec}_f V_1 \simeq \times_{v\in V_1} f^{-1}(v) \simeq = 2\times 3 \times 1 \simeq 2 \times 3 \simeq 6$
2. $\mathrm{Sec}_f V_2 \simeq \times_{v\in V_2} f^{-1}(v) \simeq = 2 \times 3 \times 1 \times 0 \simeq 0$
3. $\mathrm{Sec}_f V_3 \simeq \times_{v\in V_3} f^{-1}(v) \simeq = 2 \times 3 \times 0 \times 2 \simeq 0$

### 7.42
1. $\mathrm{Sec}_f (\{a,b,c\}) = 2\times 3\times 1$ and $\mathrm{Sec}_f (\{a,c\}) = 2 \times 1$.
2. The restriction is the projection $2 \times 3 \times 1 \to 2 \times 1$ that "forgets" the middle set $3$ i.e. it sends $(a,b,c)\mapsto (a,c)$.

### 7.44
1. Any pair of sections such that $s_1(b) \neq s_2(b)$ e.g. $s_1(b)=b_1$ and $s_2(b)=b_2$.
2. No, because they yield a contradiction on $b$.
3. Same as the previous ones but sending $h_1(b) = h_2(b) = b_1$.
4. Yes, defining $h(y) = h_1(y)$ if $y\in U_1$ and $h(y) = h_2(y)$ if $y\in U_2$.

### 7.47
A sheaf on $M$ assigns a set to every open set $U\subseteq M$, subject to gluing conditions. A vector field is a section, and the tangent bundle is a sheaf. Other bundles (fiber bundles, principal bundles) would be examples of different sheaves on $M$.

### 7.49
1. $\{\} \to \{1\} \to \{1,2\}$
2. A functor $P$ sending each of the 3 open sets in $\mathbf{Op}_1$ to a set and each of the arrows in $\mathbf{Op}^{op}$ to a function between sets.
3. From exercise 7.31 we know that the only covers of an open $U$ in this topology are of the form $(U,\dots,U,\{\},\dots,\{\})$ so any matching family of sections would need to satisfy:
   1. $s_i|_{\emptyset} = s_j|_{\emptyset}$
   2. $s_i|_{U} = s_j|_{U}$

    The first condition is always satisfied since we know from example 7.36 we know that $P(\{\}) = 1$. The second condition says essentially that any matching family must contain essentially just one section $s$, so obviously there is a unique gluing which is $s$ itself. TL;DR: since this topology only has trivial covers the sheaf condition is trivially satisfied.
4. Since the arrow $\{1\} \to \{\}$ in $\mathbf{Op}^{op}$ must go to the unique arrow to the terminal object in set, and the sheaf condition is trivially satsified, the only data needed to specify the sheaf is the function $P(\{1,2\}) \to P(\{1\})$.

### 7.52
The set of open subsets of $\{1\}$ is $\{\{\}, \{1\} \} \simeq \{\textrm{false}, \textrm{true}\} = \mathbb{B}$.

### 7.53
1. Follows from the fact that finite intersection of open sets is associative.
2. I think so?

### 7.55
- On vertices: 
  - $[H](A) = V$
  - $[H](B) = V$ 
  - $[H](C) = 0$
- On arrows:
  - $[H](f) = (V,V;A)$
  - $[H](g) = (V,V;0)$
  - $[H](h) = (V,0;0)$
  - $[H](i) = (0,0;0)$

### 7.59
1. The empty set.
2. $\mathbb{R}$.
3. Yes.
4. No.

### 7.60
1. $X$
2. Yes
3. Empty
4. Yes - the second one does vacuously

### 7.62
"People who like the weather"

### 7.64
Not super sure about this, but let's give it a go:

Let $X=\{0,1\}$ with the Sierpinski topology $\mathbf{Op}(X) = \{\emptyset, \{1\}, X\}$. Let $S(U) = \mathbb{R}$ for all $U\in\mathbf{Op}(X)$, and let

$$
p_X \colon \mathbb{R} \to \Omega(X) \simeq \mathbf{Op}(X)\\
r \mapsto \empty\,?[r<0] + \{1\}\,?[0\leq r\leq 2] + X\,?[r > 2]
$$

where $?[p] = 1$ if $p$ else $0$. Then $p_1(r) = \emptyset\,?[r<0] \{1\}\,?[r\geq 0]$. Therefore, $p_X$ classifies the subobject $(2,\infty)$ (since that's the subset of real numbers that evaluates to the largest open in $\Omega(X)$, i.e. $X$ itself) and $p_1$ classifies $[0,\infty)$ (same reasoning).

A more interesting example would be the tanget bundle of a manifold. Let $S^1$ be the unit circle. Its tanget bundle is $TS^1 \simeq S^1 \times \mathbb{R}$. This is the phase space of an ideal pendulum. Let's put $(\theta, k)$ coordinates on it, and write its Lagrangian as $L=k^2/2 + \cos{\theta}$. We may ask when do we have $L>0$? This defines a predicate:

$$
p \colon TS^1 \to \Omega S^1 \simeq \mathbf{Op} S^1\\
(\theta, k) \mapsto \{U\in \mathbf{Op} S^1 \mid k^2/2 + \cos{\theta} > 0 \}
$$

Let $V = \{(\theta, k)\in TS^1 \mid L(\theta, k) > 0\}$ be the open subset of $TS^1$ where the Lagrangian is positive. Then $p(\theta, k) = S^1$ iff $(\theta, k) \in V$ and $\emptyset$ otherwise. Thus, $V \succ\rightarrow TS^1$ is the subobject classified by $p$.

Furthermore, let $Q=\{(\theta, k)\in TS^1 \mid 0 < \theta < \pi/2 \}$ be the first quadrant. The restricted predicate $p|_Q$ evaluates to $Q$ in $Q\cap V$ and to $\emptyset$ in $Q\setminus (Q\cap V)$. In particular, if $Q\cap V = \emptyset$, then $p|_Q$ is the constant function sending every point in $Q$ to the empty set.

### 7.66
1. $\{\min \mathbb{N}\}$, which may be either $\{0\}$ or $\{1\}$ depending on convention.
2. $\mathbb{N}$
3. $\emptyset$
4. $\mathbb{Z}$

### 7.67
1. For each open $U\in\mathbf{Op}(X)$, $\forall (t\colon T). p(s,t)$ maps a person $s$ to the open set

$$
W = \bigcup_{V} \{V \in \mathbf{Op}(U) \mid\forall t\in T(V)\colon\, p(s|_V,t) = V\} \in \mathbf{Op}(U)
$$

2. The predicate maps a person $s$ to the largest open subset of $U$ in which this person is worried about every item in the news.

### 7.68
1. For each open $U\in\mathbf{Op}(X)$, $\exists (t\colon T). p(s,t)$ maps a person $s$ to the open set

$$
W = \bigcup_{V} \{V \in \mathbf{Op}(U) \mid\exists t\in T(V)\colon p(s|_V,t) = V\} \in \mathbf{Op}(U)
$$

2. The predicate maps a person $s$ to the largest open subset of $U$ in which this person is worried about *some* item in the news. Crucially, these may be different items at different times, the only thing that matters is that we can cover $W$ with "local items".

### 7.70
Applying $j$ to $p\leq jp$ yields $jp\leq jjp$ by monotonicity. Since $\Omega^{\Omega}$ is a poset, this inequality together with $jjp\leq jp$ implies $jjp=jp$. Conversely, if $jjp=jp$, we have in particular that $jjp\leq jp$.

### 7.72
1. "$\text{ate pasta}$"
2. If $U=\mathrm{today}$ and $s\in U$ then $p(s)$ is the proposition meaning "$\text{\textit{s} ate pasta today}$".
3. $j(p(s))$ is another proposition meaning "$\text{assuming Bob is in San Diego, \textit{s} ate pasta today}$".
4. Yes: if $s$ ate pasta today, then $s$ ate pasta today regardless of whether we assume Bob was in San Diego or not.
5. Yes: assuming Bob is in San Diego twice gets you no farther than assuming Bob is in San Diego once.
6. Yes: assumptions distribute over conjunctions.

### 7.76
Take the convention that the interval $[d,u]\subset \mathbb{R}$ is empty whenever $u<d$. Then

1. $o_{[0,8]} = \{[d,u]\subset \mathbb{R} \mid (d,u) \subseteq (0,8)\}$, so it contains $[2,6]$ since $(2,6) \subset (0,8)$.
2. $o_{[0,5]} \cup o_{[4,8]} = \{[d,u]\mid (d,u)\subseteq (0,5) \vee (d,u)\subseteq (4,8)\}$, so it doesn't contain $[2,6]$ since $(2,6)\nsubseteq (0,5)$ and $(2,6)\nsubseteq (4,8)$.

### 7.77
We note that $o_{[a,b]} \cap \mathbb{R} = \{[d,u]\mid (d,u)\subseteq (a,b) \wedge d=u\} \simeq (a,b)$, so both topologies are generated by the open intervals in $\mathbb{R}$ and are thus the same.

### 7.80
1. It's a presheaf with restriction maps given by

$$
r^U_V \colon \{f\colon U\cap R\to X\} \to \{f\colon V \cap R \to X\}\\
f \mapsto f|_{V\cap R}
$$

1. If $R$ is open, then $U\cap R$ is also open and $H_X$ is a sheaf on $\mathbb{IR}$ by continuity of the sections $f$. If $R$ is not open, then $H_X$ is still a sheaf on $R$ with the subspace topology, but I don't think it's a sheaf on $\mathbb{IR}$ in general.