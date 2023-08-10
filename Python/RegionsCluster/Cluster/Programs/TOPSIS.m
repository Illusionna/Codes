clear
clc
% ----------------------------------------------
% % 读取 txt 文件数据.
M = importdata("./SOM_Intrinsic_Exponential/Intrinsic_Exponential.txt").data;
N = length(M);
GMM_DBI = M(1:2:N-1);
GMM_DI = M(2:2:N);
% ----------------------------------------------
% % 指标正向化处理，采用 max - x 变换.
DBI = max(GMM_DBI) - GMM_DBI;
DI = GMM_DI;
% ----------------------------------------------
% % 标准化处理.
matrix = [[DBI], [DI]];
[n,m] = size(matrix);
standardMartix = matrix ./ repmat(sum(matrix .* matrix) .^ 0.5, n, 1);
% ----------------------------------------------
% % 指标 DBI 和 DI 赋权重.
judge = true
if judge == true
    % 填充权重向量，求和为 1
    weight = [0.25 0.75];
    if isempty(weight)
        error("空权重向量，程序终止.")
    else
        disp("权重已赋值.")
    end
elseif judge == false
    % DBI 和 DI 指标权重相等，均为 0.5
    weight = ones(1,m) ./ m;
end
% ----------------------------------------------
% % 计算得分.
maxIntercept = sum([(standardMartix - repmat(max(standardMartix),n,1)) .^ 2 ] .* repmat(weight, n, 1) ,2) .^ 0.5;
minIntercept = sum([(standardMartix - repmat(min(standardMartix),n,1)) .^ 2 ] .* repmat(weight, n, 1) ,2) .^ 0.5;
unnormalizedScore = minIntercept ./ (maxIntercept + minIntercept);
disp("最终得分：")
standardScore = unnormalizedScore / sum(unnormalizedScore);
[sortScore,index] = sort(standardScore, "descend")
% ----------------------------------------------
% % 绘图.
plot(index+1,sortScore,"--.","MarkerSize",20)
grid on
xlabel("聚类数目")
ylabel("综合得分")
title("TOPSIS")
% % 保存图片.
% ----------------------------------------------
set(gcf,"Units","Inches");
pos = get(gcf,"Position");
set(gcf,"PaperPositionMode","Auto","PaperUnits","Inches","PaperSize",[pos(3), pos(4)])
filename = "TOPSIS";
print(gcf,filename,"-dpdf","-r0")