load M.mat;
%获取二维矩阵行数
[m, n] = size(M);

%画出散点图
x = M(:,1);
y = M(:,2);
plot(x,y,'o');
figure(1);

%计算最小二乘法
x_bar = sum(x) ./ m;
y_bar = sum(y) ./ m;
k = (sum(x.*y)-m.*x_bar.*y_bar) ./ (sum(x.*x)-m.*x_bar.*x_bar);
b = y_bar - k.*x_bar;
hold on;
grid on

%匿名画出拟合图像
f = @(x)k.*x+b;
xinterval = [2,9];
fplot(f,xinterval);

%标记
xlabel("x轴")
ylabel("y轴")
legend('散点数据','拟合函数');

%计算参数式线性函数的拟合优度
disp('是否进行拟合优度检验，是1，否0 ： ');
i = input('');
if i == 1
    SSR = sum((k.*x+b-mean(y)).^2);
    SSE = sum((k.*x+b-y).^2);
    SST = sum((y-mean(y)).^2);
    R_2 = SSR / SST;
    disp(R_2);
elseif i == 0
    disp("end");
end