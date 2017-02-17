function [ alpha ] = laff_norm2( x )
% alpha = laff_norm2(x)
%   returns length of vector x

[m_x,n_x] = size(x);

if ~isvector(x)
    alpha = 'FAILED';
    return
end

alpha = 0;

if (m_x ~=1)
    for i=1:m_x
        alpha = alpha + x(i,1)^2;
    end
else
    for i=1:n_x
        alpha = alpha + x(1,i)^2;
    end
end

alpha = sqrt(alpha)

return
end