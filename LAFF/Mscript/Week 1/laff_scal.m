function [ x_out ] = laff_scal( alpha,x )
% x = laff_scal (alpha,x) scales vector x by alpha

% Extract the row and column sizes of x.
[m_x,n_x] = size(x);

if ~isscalar(alpha) || ~isvector(x)
    x_out = 'FAILED';
    return
end


% check whether column or row and scale elements
if ( n_x == 1)
    for i=1:m_x
       x(i,1) = alpha*x(i,1);
    end
end
if (m_x == 1)
    for i=1:n_x
        x(1,i) = alpha*x(1,i);
    end
end 

x_out = x;
return
end