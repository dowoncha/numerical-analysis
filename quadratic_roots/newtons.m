function [x0, x1] = newtons(a, b, c)
    % Finds root of a quadratic using quadratic equation
    % Considering two forms of the quadratic formula
    % Inaccuracies occur due to +- of same sign values and floating point numbers
    
    % @param f A function, easiest to pass an anonymous function
    %   e.g. newtons(@(x)x^2, ...)
    % @param x0 The inital start value to begin root search
    % @param n # of iterations
    % @return x Calculated x root value    
    if (b >= 0) 
        x0 = (-b - sqrt(b* b-4*a*c)) / 2*a;
        x1 = 2*c/(-b-sqrt(b*b-4*a*c));
    else
        x0 = 2*c/(-b+sqrt(b*b-4*a*c));
        x1 = (-b+sqrt(b*b-4*a*c))/2*a;
    end
end
