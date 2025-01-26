# The derivative as a function

Since some functions have a derivative for all points x, the derivative of a function as a whole can be represented as its own function. 

![image](https://github.com/user-attachments/assets/1aaba453-4805-4655-9e96-a41d53d187c6)

## Calculating f'(x) for f(x)=x^2

If `f(x) = x^2`, then what is `f'x`?

First, we start with our definition of the derivative:

`f'(x) = lim(b->x) (f(b) - f(x))/(b-x)`

Next, we apply the function `f(x) = x^2` to that derivative function: 

`f'(x) = lim(b->x) (b^2 - x^2)/(b-x)`

Next, we factor the numerator...

`f'(x) = lim(b->x) ((b+x) * (b-x))/(b-x)`

Next, we cancel-out the `(b-x)`...

`f'(x) = lim(b->x) (b+x)`

As `b` approaches `x`, the limit becomes `x+x`, or `2x`. 

**Therefore, if `f(x) = x^2`, then `f'(x) = 2x`.**





