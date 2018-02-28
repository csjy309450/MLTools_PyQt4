% 2D gaussian distribution
function [z] = Gaussian2D(x, y, theta)
u1=theta(1);d1=theta(2);u2=theta(3);d2=theta(4);p=theta(5);
z = (power(x - u1,2)/power(d1,2) + power(y - u2,2)/power(d2,2) - 2*p*(x - u1)*(y - u2)/(d1*d2));
z = exp(-1/2*(1-power(p,2))*z);
z = power(2*pi*d1*d2*sqrt(1-power(p,2)),-1) * z;
end






