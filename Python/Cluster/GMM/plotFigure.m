clear
clc

M = importdata("./OptimalClusterResult/Intrinsic_Exponential.txt").data;
N = length(M);
GMM_DBI = M(1:2:N-1);
GMM_DI = M(2:2:N);
ClusterNumbers = [2:1:(N/2+1)];

subplot(2,1,1)
plot(ClusterNumbers,GMM_DBI,"r.--","MarkerSize",20)
grid on
title("Expect the DBI to be smaller")
xlabel("Cluster Numbers")
ylabel("Internal Index")

subplot(2,1,2)
plot(ClusterNumbers,GMM_DI,"b.--","MarkerSize",20)
grid on
title("Expect the DI to be larger")
xlabel("Cluster Numbers")
ylabel("Internal Index")

set(gcf,"Units","Inches");
pos = get(gcf,"Position");
set(gcf,"PaperPositionMode","Auto","PaperUnits","Inches","PaperSize",[pos(3), pos(4)])
filename = "Internal Index Figure";
print(gcf,filename,"-dpdf","-r0")

disp("<<------------------Executed------------------>>")