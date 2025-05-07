function [u,vHat] = leastSquaresFit(X,v)
% LEASTSQUARESFIT Mindste kvadraters metode
%   Find mindste kvadraters løsning u
%   til Xu=vHat, så ||v-vHat||^2 minimeres 
    u = (X'*X)\(X'*v)
    vHat = X*u

    % Plot datapunkterne y sammen med modellen
    clf('reset');
    plot3(X(:,2),X(:,3),v,'o')
    hold on;

    [T1,T2] = meshgrid(-10:0.1:10, -10:0.1:10);
    Z = arrayfun(@(t1,t2) [1, t1, t2, t1^2, t1*t2, t2^2]*u, T1, T2);

    mesh(T1,T2,Z)
end
