# The derivative as a function

Since some functions have a derivative for all points x, the derivative of a function as a whole can be represented as its own function. 

![image](https://github.com/user-attachments/assets/1aaba453-4805-4655-9e96-a41d53d187c6)

## Calculating f'(x) for f(x)=x^2

If `f(x) = x^2`, then what is `f'x`?

First, we start with our definition of the derivative:

`f'(x) = lim(b->x) (f(b) - f(x))/(b-x)`

Next, we apply the function `f(x) = x^2` to that derivative definition: 

`f'(x) = lim(b->x) (b^2 - x^2)/(b-x)`

Next, we factor the numerator...

`f'(x) = lim(b->x) ((b+x) * (b-x))/(b-x)`

Next, we cancel-out the `(b-x)`...

`f'(x) = lim(b->x) (b+x)`

As `b` approaches `x`, the limit becomes `x+x`, or `2x`. 

**Therefore, if `f(x) = x^2`, then `f'(x) = 2x`.**

***

## Delta Notation

`f'(x) = lim(delta_x->0) delta_y / delta_x` or `f'(x) = lim(delta_x->0) (f(x+delta_x) - f(x)) / delta_x`

## Calculating f'(x) for f(x)=1/x

If `f(x) = 1/x`, then what is `f'(x)`?

Again, we start by bringing-out our definition of the derivative. This time, let's use our delta notation:

`f'(x) = lim(delta_x->0) (f(x+delta_x) - f(x)) / delta_x`

Next, we apply the function `f(x) = 1/x` to that derivative definition:

`f'(x) = lim(delta_x->0) ( (1/(x+delta_x)) - (1/(x)) ) / delta_x`

Next, let's look a the overall numerator `( (1/(x+delta_x)) - (1/(x)) )` and give it an internal common denominator by multiplying its sub-components by the internal denominator of the other respective component:

`f'(x) = lim(delta_x->0) ( (x/(x(x+delta_x))) - ((x+delta_x)/(x(x+delta_x))) ) / delta_x`

This can be simplified to...

`f'(x) = lim(delta_x->0) ( (x - (x+delta_x)) / (x(x+delta_x)) ) / delta_x`

...which can be further simplified to...

`f'(x) = lim(delta_x->0) ( -delta_x / (x(x+delta_x)) ) / delta_x`

...which can be further simplified to...

`f'(x) = lim(delta_x->0) ( -1 / (x(x+delta_x)) )`

Notice, as `x->0`, `f'(x)` the denominator now approaches `x*x` or `x^2`. 

**So, `f'(x) = lim(delta_x->0) -1/(x^2)`**










