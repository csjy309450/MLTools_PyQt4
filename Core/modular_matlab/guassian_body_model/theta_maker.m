%通过头部高斯曲线在x,y轴的均值(head_x,head_y)和方差(delta_head)
function [theta] = theta_maker(label_x, label_y)
delta_head = 2*(1+(label_y-45)/39)/3;
head_x = label_x;head_y = label_y+3*delta_head;
delta_body_x = 1.8*delta_head;delta_body_y = 5*delta_head;
body_x = head_x;body_y = head_y+3*delta_head;
theta = [head_x, delta_head, head_y, delta_head, 0;body_x, delta_body_x, body_y, delta_body_y, 0];
end