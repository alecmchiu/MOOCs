function [ alpha ] = laff_dot( x,y )
% alpha = laff_dot(x,y)
%   returns inner product/dot product of two vectors

[m_x,n_x] = size(x);
[m_y,n_y] = size(y);

% check if x,y are vectors with compatible dimensions
if ~isvector(x) | ~isvector(y) | (m_x*n_x ~= m_y*n_y)
    alpha = 'FAILED';
    return
end

alpha = 0;

if m_x ~= 1
    for i=1:m_x
        if m_y ~= 1
            alpha = alpha + (x(i,1) * y(i,1));
        else
            alpha = alpha + (x(i,1) * y(1,i));
        end
    end
else
    for i=1:n_x
        if m_y ~=1
            alpha = alpha + (x(1,i) * y(i,1));
        else
            alpha = alpha + (x(1,i) * y(1,i));
        end
    end
end

return
end