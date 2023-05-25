clear
clc

n = 10000;
Not_change = 0;
Change = 0;

for i = 1:n
    chosen_door = randi([1,3]);
    fact_door = randi([1,3]);
    if chosen_door == fact_door
        Not_change = Not_change + 1;
        Change = Change + 0;
    else
        Not_change = Not_change + 0;
        Change = Change + 1;
    end
end

disp('不改变门的得奖概率为： ');
disp(Not_change/n);
disp('改变门的得奖概率为： ');
disp(Change/n);