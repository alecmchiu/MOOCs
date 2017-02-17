function [ y_out ] = laff_axpy( alpha,x,y )
%Scalar addition y_out=laff_axpy(alpha,x,y)
%   y_out = alpha*x + y

[m_x,n_x] = size(x);
[m_y,n_y] = size(y);

% check if alpha is scalar and check if x and y are vectors matching in size
if ~isscalar(alpha) | ~isvector(x) | ~isvector(y)
    y_out = 'FAILED';
    return
end

% test if compatible dimensions
if (m_x * n_x ~= m_y * n_y )
    y_out = 'FAILED';
    return
end

if (m_x ~= 1)
    for i=1:m_x
        if (m_y ~= 1)
            y(i,1) = alpha*x(i,1) + y(i,1);
        else
            y(1,i) = alpha*x(i,1) + y(1,i);
        end
    end
else
    for i=1:n_x
        if (n_y ~= 1)
            y(1,i) = alpha*x(1,i) + y(1,i);
        else
            y(i,1) = alpha*x(1,i) + y(i,1);
        end
    end
end

y_out = y;
return
end