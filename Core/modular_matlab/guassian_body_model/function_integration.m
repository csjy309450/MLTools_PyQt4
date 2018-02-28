% 计算函数积分
syms x y;
range_x = 20;range_y = 20;
x1 = 0;x2=range_x;
y1 = 0;y2=range_y;
theata = [range_x/2 3 range_y/2 1 0];
z = Gaussian2D(x,y, theata);

int(int(z,y,y1,y2),x,x1,x2)