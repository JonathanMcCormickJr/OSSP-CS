# Geometric interpretation of the derivative

There are 3 main ways to interpret the derivative: 
1. Physical: the instantaneous rate of change.
2. Geometric: the slope of the tangent line.
3. Sensitivity measurement: If we change something by a small amount, how much does that change our results?

In this lesson, we will be covering the second of the three: The Geometric approach. 

Geometry problem. 

## Visualization of tangent approximation trough zooming-in on a continuous graph:

![image](https://github.com/user-attachments/assets/3ae6bb5e-8015-4b2d-be5d-de8e7a66f5fb)

![image](https://github.com/user-attachments/assets/44e8bf5f-c490-43ce-8274-56d54afc92d8)

![image](https://github.com/user-attachments/assets/3a14bad2-0c50-44e0-8cdb-be3323f0da10)

![image](https://github.com/user-attachments/assets/eaee92dc-4779-4c7d-8a03-32c29427a41b)

## Slope

slope = rise / run = (f(b)-f(a))/(b-a) = "average rate of change"

What if point `b` approaches point `a`? Then our secant starts to more and more resemble a tangent. 

To define the derivative (slope for the tangent), we define it as this:
```
f'a = (f(b)-f(a))/(b-a) as b->a 
```

Keep in mind, a function can be continuous at point `a` without necessarily being differentiable at `a`. On the other hand, if a function is not continuous at `a`, then it is definitely not differentiable at `a` (although you can still sometimes identify left- and right-hand limits of slopes at `a`. 

TRICKY BIT: If a tangent line exists at `a`, it will almost always have a derivative EXCEPT when the tangent line is vertical, like with `f(x) = cube_root(x)` where `a=0`, for example.

![image](https://github.com/user-attachments/assets/40343abd-f42a-4b61-8e43-45d788c18223)

