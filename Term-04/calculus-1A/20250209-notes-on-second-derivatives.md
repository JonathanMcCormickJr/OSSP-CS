# Second derivatives

What if you want to determine a derivative OF a derivative? That's where second-order derivatives come in. 

First order derivatives: 

If `f(x) = x^3 - 6x`, then what is `df/dx`?

`df/dx = ___`

`f + df = (x + dx)^3 - 6(x + dx)`

`f + df = { (x + dx) * (x + dx) * (x + dx) } - 6x - 6*dx`

`f + df = { (x^2 + x*dx + x*dx + dx^2) * (x + dx) } - 6x -6*dx`

`f + df = { (x^2 + 2x*dx + dx^2) * (x + dx) } - 6x -6*dx`

`f + df = { x^3 + dx*x^2 + dx*2x^2 + 2x*dx^2 + x*dx^2 + dx^3 } - 6x -6*dx`

We can safely ignore all elements of this that are multiplied by a second- or third-power of `dx`, leaving us with: `f + df = x^3 + dx*x^2 + dx*2x^2 - 6x -6*dx`

Simplify further: `f + df = x^3 + 3x^2 * dx - 6x -6*dx`

Subtract our original `f = x^3 - 6x`, and we get `df = 3x^2 * dx - 6*dx`. 

We can now divide both sides by `dx`, leaving us with `df/dx = 3x^2 - 6` ✅

***
`3x^2 - 6` is itself a function, so if `g(x) = df/dx`, then what is the derivative of g?

`g = 3x^2 - 6`

`g + dg = 3(x + dx)^2 - 6`

`g + dg = 3(x + dx)(x + dx) - 6`

`g + dg = 3(x^2 + 2x*dx + dx^2) - 6`

Ignoring all higher powers of `dx`, we get: 

`g + dg = 3(x^2 + 2x*dx) - 6`

`g + dg = 3x^2 + 6x*dx - 6`

Subtract our equation `g = 3x^2 - 6`, and we get 
`dg = 6x*dx`

Divide by `dx` on both sides... 
`dg/dx = 6x` ✅

This is our second-derivative. 

***

