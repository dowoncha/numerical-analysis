clear all; clc;

f = @(x)x^2-2;
root = newtons(f, 0.1);
sprintf('(x,y) = (%.16e, %.16e)', root, f(root))