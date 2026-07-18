# Parity-State-Dynamics
Research on the digit dynamical system f(n)=(E(n). O(n))^2 and also studying the behavior and salient features of attractors created by it.
Parity State Dynamics

## Definition: -

Let E(n) denote the sum of the even digits of n and O(n) denote the sum of the odd digits of n.
so we get a composite digit based arithmetic funtion- 
f(n) = (E(n)·O(n))².
The dynamical system is studied under repeated iteration of f.
which gives some pecuilar results.

### Proven Results: -

We get some Fixed Points by plain implementation of this funtion in computer.
The following integers are the fixed points:
- 0
- 324
- 5184
But sadly, there are no more fixed points in whole of the number system other than these can be demonstared by the proof in later files.
 Yet Indeed: -
- 324 = (3·6)²
- 5184 = (9·8)²
- 0 maps to itself.
  
## Absorbing State: -

0 is an absorbing state. Once an iterate reaches 0, all subsequent iterates remain 0.
Its like a punishment given to those numbers whose even and odd pairs are not blanced and the attractor 0 devours it. 

Finite Fixed-Point Search:-
I found his sytem accidently while carrying out certain programs and I noticed these things in it.
Exhaustive computation found no fixed points other than:
0, 324, 5184.(old)

### Finiteness Argument(new)

  Let
  
  \[
  f(n)=(E(n).O(n))^2,
  \]

 where \(E(n)\) and \(O(n)\) denote    the sums of the even and odd decimal digits of \(n\), respectively. Suppose that \(n\) is a fixed point, i.e.,
 
$$\[
 n=f(n).
 \]$$
 If \(n\) has \(d\) decimal digits, let \(d_0\) and \(d_1\) denote the numbers of even and odd digits, respectively, so that
 $$\[
 d_0+d_1=d.
 \]$$

 Since every even digit is at most \(8\) and every odd digit is at most \(9\),
 $$\[
 E(n)\le8d_0,\qquad
 O(n)\le9d_1.
 \]$$
Hence,

$$\[
 E(n).O(n)\le72d_0d_1.
 \]$$

 Using the inequality

 $$\[
 d_0d_1\le\frac{(d_0+d_1)^2}   {4}=\frac{d^2}{4},
 \]$$

we obtain

 $$\[
 E(n).O(n)\le18d^2.
 \]$$

Therefore,

 $$\[
 n=(E(n).O(n))^2\le(18d^2)^2.
 \]$$

Since every positive \(d\)-digit integer satisfies

 $$\[
 n\ge10^{d-1},
 \]$$

it follows that

 $$\[
 10^{d-1}\le(18d^2)^2.
 \]$$

 This inequality is false for every $$\(d\ge7\)$$. Hence every fixed point has at most six decimal digits.

Substituting \(d=6\) into the above bound gives

 $$\[
 n\le(18\cdot6^2)^2=648^2=419904.
 \]$$

Furthermore, \(E(n)\) is always even, so \(E(n).O(n)\) is also even. Therefore every fixed point is an **even perfect square**, and it suffices to test only the 324 even perfect squares not exceeding \(648^2\).

An exhaustive search over these candidates yields the only fixed points

$$\[
\boxed{0,\;324,\;5184.}
\]$$

 {Acknowledgements}

The improved finiteness argument presented above is based on helpful comments and answers from the following Math Stack Exchange discussion:

**How can I prove that 0, 324 and 5184 are the only fixed points of \(f(n)\)?**

https://math.stackexchange.com/questions/5144103/how-can-i-prove-that-0-324-and-5184-are-the-only-fixed-points-of-fn#5144110


 ## Computational Observations
 ### Basin Structure
 Many integers eventually reach one 
 of:
      - 0
      - 324
      - 5184
      Examples:
      16 → 36 → 324
      47 → 784 → 7056 → 5184   {in all there is continoious iteration of f(n) = (E(n)·O(n))²}
      17 → 0

### No Nontrivial Cycles Found
  No cycles other than the fixed points have been found by exhaustive computation up to at least 10^7.
    State-Space Reduction:
      The dynamics appear to be governed primarily by the pair:
          (E(n), O(n))
      rather than by n itself.(n-denotes any integer)
      
### Bounded Behavior
Iterates quickly enter a bounded region determined by the digit sums, although the set of initial values is infinite.

###  Direct Terminal Pairs
Pairs producing 324 satisfy:
      EO = 18
    Examples:
      (1,18), (2,9), (3,6), (6,3), (9,2), (18,1)
      and their reversals.
    Pairs producing 5184 satisfy:
      EO = 72
    Examples:
      (1,72), (2,36), (3,24), (4,18), (6,12), (8,9)
    and their reversals.
      
## Graphical observations: -

###  Ladder Structure
Plots of the state pairs (E,O) exhibit staircase-like or ladder-like patterns consisting of discrete levels and bands.

 ### Hyperbolic Structure
The terminal states satisfy:
      EO = 18 → 324
      EO = 72 → 5184
    These correspond to discrete hyperbolas in (E,O)-space.

###  Growth Reduction
For large integers, the iteration greatly reduces magnitude compared with the size of the original integer. The map appears globally contracting despite possible local increases.(observation only)

###  Scaling Symmetry 
The terminal hyperbola for 5184 is obtained from that of 324 by the scaling:
   (E,O) → (4E,O) or (E,4O) (corresponding pairs)
   Since,
     72 = 4²·18.

## Conjectures and Open Questions: -

###  Global Attractor Conjecture
Does every positive integer eventually reach one of:
    0, 324, or 5184? - Till now, Yes

###  Cycle Conjecture
Do any nontrivial cycles exist?
    -None have been found up to 10^7.
    
###  State-Space Theory
Can the iteration be completely described in terms of transitions between (E,O) states?
    -Till now what i have found was completely based on thses pairs.
  
###  Asymptotic Behavior and Growth
What is the exact asymptotic growth law of the map for large n? - Still ssearching.It does not have single growht law but a)Balanced regime b)one-sided regime     and c)Pure parity regime
    
###  Geometric Structure
Can the observed ladder structure and hyperbolic organization be explained theoretically? - idk
    
Current Status: -

This project investigates a parity-based arithmetic dynamical system exhibiting:

- fixed-point attractors,
- basin structure,
- state-space reduction,
- hyperbolic geometry,
- scaling symmetries,
- bounded dynamics,
- and apparent contraction under iteration.

Theoretical explanations for several observed phenomena remain open.
