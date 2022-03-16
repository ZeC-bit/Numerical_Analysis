# Numerical_Analysis With Optimization

This is a collection of algorithms learnt during numerical analysis and optimisation. Code includes libraries: Numpy and Pyplot


# Interpolation 

**Newton Interpolation** 


![cher_polynomal](https://user-images.githubusercontent.com/74304944/158596680-1ad38b64-a89b-4914-9eff-ffbc21afd4ec.png)

![cher_error](https://user-images.githubusercontent.com/74304944/158596710-99839b5f-8508-454c-89cd-cf67a833aa2f.png)


**Error Analysis**

I have chosen a fixed x-value to compare the error of polynomials of different orders. 
As the order increases it is clear that the error is lower.
However due to the runge's phenomenon, as the polynomial's order increase and further the x-value is from the nodes chosen, the error becomes significant.




# Integral Approximation

**Simpson's Rule and Trapezoid Rule comparison**

![simpson_err](https://user-images.githubusercontent.com/74304944/158597668-07bb3b60-98b6-4a7a-b7a8-3688a7490a28.png)

![trapezoid_err](https://user-images.githubusercontent.com/74304944/158597686-f087d666-14da-44a2-ae1e-29687003ac91.png)


**Error Analysis**

The code is an approximation of integral of the function e^x * cos(x) from 0 to pi.
It is clear that the trapezoid rule is much effective in terms of approximation.
However the computational power is the trade off.
