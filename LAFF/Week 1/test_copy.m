x = [1;2;3]
y=[0;-1;-2]
z=[4;3;2;1]

% test column to column
disp('column->column')
if (isequal(laff_copy(x,y),x))
    disp('PASSED')
else
    disp('FAILED')
end

% test column to row
disp('column->row')
if(isequal(laff_copy(x,y'),x'))
    disp('PASSED')
else
    disp('FAILED')
end

% test row to column
disp('row->column')
if(isequal(laff_copy(x',y),x))
    disp('PASSED')
else
    disp('FAILED')
end

% test row to row
disp('row->row')
if(isequal(laff_copy(x',y'),x'))
    disp('PASSED')
else
    disp('FAILED')
end

%test wrong size
disp('WRONG SIZE TESTS')
disp('column->column')
if(isequal(laff_copy(x,z),'FAILED'))
    disp('PASSED')
else
    disp('FAILED')
end
disp('column->row')
if(isequal(laff_copy(x,z'),'FAILED'))
    disp('PASSED')
else
    disp('FAILED')
end