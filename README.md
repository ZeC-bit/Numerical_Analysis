# Numerical_Analysis With Optimization

This is a collection of algorithms learnt during numerical analysis and optimisation. 
Code includes libraries: Numpy and Pyplot


# Interpolation 

**Newton Interpolation** 


![cher_polynomal](https://user-images.githubusercontent.com/74304944/158596680-1ad38b64-a89b-4914-9eff-ffbc21afd4ec.png)

![cher_error](https://user-images.githubusercontent.com/74304944/158596710-99839b5f-8508-454c-89cd-cf67a833aa2f.png)


**Error Analysis**

    I have chosen a fixed x-value to compare the error of polynomials of different orders. 
    As the order increases it is clear that the error is lower.
    However due to the runge's phenomenon, as the polynomial's order increase and further the x-value is from the nodes chosen, the error becomes       significant.




# Integral Approximation

**Simpson's Rule and Trapezoid Rule comparison**

![simpson_err](https://user-images.githubusercontent.com/74304944/158597668-07bb3b60-98b6-4a7a-b7a8-3688a7490a28.png)

![trapezoid_err](https://user-images.githubusercontent.com/74304944/158597686-f087d666-14da-44a2-ae1e-29687003ac91.png)


**Error Analysis**

    The code is an approximation of integral of the function e^x * cos(x) from 0 to pi.
    It is clear that the trapezoid rule is much effective in terms of approximation.
    However the computational power is the trade off.





# ODE Approximation

**Runge-Kutta 4th Order approximation**

![rk_method](https://user-images.githubusercontent.com/74304944/158992055-494c1efb-c3cf-4b94-b9b0-35a15431bc02.png)

![rk_erro](https://user-images.githubusercontent.com/74304944/158992066-e3b8d186-111c-4194-8c18-78cc54744de9.png)


**Error Analysis**

    It can be noticed that the local errors of the method accumulates over iterations hence the error increases as t increases from the initial value 0. A  method of reducing error would be to implement with a higher order runge-kutta method.





# Solving Linear-System equations

**Gauss-Seidel, Jacobi Iterative Method

![Jacobi_Question](https://user-images.githubusercontent.com/74304944/158992557-6df8a55e-4a7d-4544-b31a-5e05d085109f.png)


![Gauss_Seidel](https://user-images.githubusercontent.com/74304944/158992645-d0ea116d-4858-4991-9fbc-a3a7f9fd2e7a.png)

![Jacobi_iteration](https://user-images.githubusercontent.com/74304944/158992658-83e85b1f-36ac-4abc-a18a-5b58ecd761f6.png)


**Error Analysis**

    I have approximated the error as the distance between the approximation vector and solution vector with the usual metric. 
    It is clear that Gauss Seidel Method converges faster to the solution than Jacobi Iteration method.
