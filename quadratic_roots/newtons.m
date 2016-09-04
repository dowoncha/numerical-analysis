function [x] = newtons(f, x0)
    % Finds root of a polynomial
    % Uses Newton's method,
    % @param f A function, easiest to pass an anonymous function
    %   e.g. newtons(@(x)x^2, ...)
    % @param x0 The inital start value to begin root search
    % @param n # of iterations
    % @return x Calculated x root value    
    n = 0;
    while abs(f(x0)) > 1.0e-13
            x1 = x0 / 2 + 1 / x0;
            
            n = n + 1;
            % error(n) = abs(x1 - sqrt(2));
            
            % Matlab print statement sprintf
            x0 = x1;
    end
    
    x = x0;
end
