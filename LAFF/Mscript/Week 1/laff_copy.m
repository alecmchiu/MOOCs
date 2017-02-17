function [ y_out ] = laff_copy( x,y )
% y = copy ( x, y) copies vector x into vector y
%   Vectors x and y can be a mixture of column and/or row vector. In other
%   words, x and y can be n x 1 or 1 x n arrays. However, one size must
%   equal 1 and the other size equal n.

% Extract the row and column sizes of x and y.
[m_x,n_x] = size(x);
[m_y,n_y] = size(y);

% Check if dimensions match
if (m_x ~= 1 & n_x ~= 1) | (m_y ~= 1 & n_y ~=1)
    y_out = 'FAILED';
    return
end
if (m_x * n_x ~= m_y * n_y )
    y_out = 'FAILED';
    return
end

% check whether column or row and copy elements
if ( n_x == 1)
    if (n_y == 1)
        for i=1:m_x
            y(i,1) = x(i,1);
        end
    else
        for i=1:m_x
            y(1,i)=x(i,1);
        end
    end
else
    if (n_y == 1)
        for i=1:n_x
            y(i,1)=x(1,i);
        end
    else
        for i=1:n_x
            y(1,i)=x(1,i);
        end
    end
end

y_out = y;
return
end