clear
clc

C = [0 3 3 7 1
    4 0 1 3 1
    1 4 0 3 3
    1 1 4 0 4
    6 5 1 3 0];

V = [];
for i = 1:(size(C)-1)
    V = [V,i];
end
solution = d(0,V,C)

function solution= d(s,V,C)
    n = nnz(V);
    if n == 0
        solution = C(s+1,1);
    else
        M = [];
        for i = 1:(size(C,1)-1)
            if V(i) ~= 0
                v = V;
                v(i) = 0;
                temp = C(s+1,V(i)+1) + d(V(i),v,C);
                M = [M,temp];
            end
        end
        solution = min(M);
    end
end