%%
clear 
clc
load data.mat

%%
%计算样本协方差矩阵
[N_sample, P_target] = size(x)
n = N_sample
p = P_target
R = corrcoef(x)

%%
% 计算协方差矩阵的特征值和特征向量
[value, vector] = eig(R)
value = rot90(value)'
lambda = diag(vector)
lambda = lambda(end:-1:1)

%%
%计算贡献率和累计贡献率
contribution_rate = lambda ./ sum(lambda)
accumulate_contribution_rate = cumsum(lambda) ./ sum(lambda)
% accumulate_contribution_rate > 0.85 且尽量指标越少的作为主成分，即前两个，选出主成系数
K = min(find(accumulate_contribution_rate > 0.80))
disp('***********************')
disp('Result: ')
M = value([1:K],:)'


% 色块矩阵绘图
pos = 1

if pos == 1
    M = (-1*M)
    mappedX = R * M
    mapping.M = M
    %     因为M 有两列
    xvar = {'指标一','指标二'}
    %     因为M 有五行
    yvar = {'指标一','指标二','指标三','指标四','指标五'}
    matrixplot(M,'FillStyle','nofill','xvar',xvar,'yvar',yvar)
    figure(1)
    hold on
    matrixplot(M,'xvar',xvar,'yvar',yvar,'DisplayOpt','off','FigSize','Auto','ColorBar','on')
else
    
end