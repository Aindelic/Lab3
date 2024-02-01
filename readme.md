# Question 1

Write a function that takes in a list of integers as an argument
and returns true if it contains two integers that are the same, false
otherwise.

For the nested loop solution you start with the first element and compare it against all other elements one by one, then move to the second element and repeat the process, returning true if a duplicate is found. This solution is simple and straightfoward however, when the arrays are large this solution massevely slows down as the iterations are quite time consuming.

For the set solution, you add each element to the set and chech if that element has already been added, if so return true. This is much faster than the previous solution as it only has to iterate through the set once per element, but is slightly more complex to implement.
