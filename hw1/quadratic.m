function [x0, x1] = quadratic(a, b, c)
    % Finds root of a quadratic using quadratic equation
    % Considering two forms of the quadratic formula
    % Inaccuracies occur due to +- of same sign values and floating point numbers
    % Worried about b >> ac so we check value of b to make sure inside of sqrt is okay

    % @param a x^2 coefficient
    % @param b x coefficient
    % @param c constant
    % @return x0, x1 roots

    if (b >= 0)
        x0 = (-b - sqrt(b* b-4*a*c)) / 2*a;
        x1 = 2*c/(-b-sqrt(b*b-4*a*c));
    else
        x0 = 2*c/(-b+sqrt(b*b-4*a*c));
        x1 = (-b+sqrt(b*b-4*a*c))/2*a;
    end
end
