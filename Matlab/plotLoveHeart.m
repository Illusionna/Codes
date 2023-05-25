clear
clc

density = 0.01;windings = 5;velocity = 0.001;R = 255; G = 150; B= 200;
disp("*************************************")
disp("1.重置参数    0.默认参数")
judge = input('输入： ');
if judge == 1
    density = input('♥的密度(参考值0.01)：');
    windings = input('♥的匝数(参考值5)：');
    velocity = input('♥跳速率(参考值0.05)：');
    R = input('红R(参考值255)： ');
    G = input('绿G(参考值150)： ');
    B = input('蓝B(参考值200)： ');
end

generate_colour = @(n) repmat([R,G,B]./255,[n,1]) + repmat([-40,-80,-50]./255,[n,1]) .* repmat(rand([n,1]),1,3);
generate_x = @(t) 16 .* sin(t) .^ 3;
generate_y = @(t) 13 .* cos(t) - 5 .* cos(2.*t) - 2 .* cos(3.*t) - cos(4.*t);
time = 0:density:(10-density);
x = generate_x(time)';
y = generate_y(time)';
len = size(x,1);

axis([-25 25 -25 20])
axis off
fig = gcf;
set(fig,'color',[0 0 0]);

X = zeros(size(time,2),windings);
Y = zeros(size(time,2),windings);
PI = [-pi/2:(pi/windings):pi/2]';
for i = 1:windings
     X(:,i) = x*(sin(PI(i)/2)/10 + 1);
     Y(:,i) = y*(sin(PI(i)/2)/10 + 1);
end

hold on
Mark = '.';
for i=1:windings
    eval(['x',num2str(i),'=X(:,',num2str(i),');']);
    eval(['y',num2str(i),'=Y(:,',num2str(i),');']);
    eval(['object',num2str(i),'=scatter(x',num2str(i),',y',num2str(i),');']);
    eval(['object',num2str(i),'.Marker','=','Mark;']);
    eval(['object',num2str(i),'.CData=generate_colour(len);']);
    eval(['object',num2str(i),'.SizeData=24;']);
end

pic_num = 1;
for j = 1:0.2:1e4
    for i = 1:windings
        eval(['object',num2str(i),'.XData=x',num2str(i),'*(sin(j)/10 + 1);']);
        eval(['object',num2str(i),'.YData=y',num2str(i),'*(sin(j)/10 + 1);']);
    end
    
    F=getframe(gcf);
    I=frame2im(F);
    [I,map]=rgb2ind(I,256);
    if pic_num == 1
        imwrite(I,map,'Love_Heart.gif','gif','Loopcount',inf,'DelayTime',0);
    else
        imwrite(I,map,'Love_Heart.gif','gif','WriteMode','append','DelayTime',0);
    end
    pic_num = pic_num + 1;
    
    pause(velocity)
end