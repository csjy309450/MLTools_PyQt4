% plot function on 3D diagram
range_x = 100;range_y = 100;
X = 0 : 1 : range_x;Y = 0 : 1: range_y;
Z = zeros(range_x+1, range_y+1);

% delta_head = 5;delta_body_x = 2*delta_head;delta_body_y = 4*delta_head;
head_x = range_x/2;head_y = range_y/2;
% body_x = head_x;
% 
% body_y = head_y+3*delta_head;
% body_y = head_y+3*delta_head+3*delta_body_y;

% theta1 = [head_x delta_head head_y delta_head 0];
% theta2 = [body_x delta_body_x body_y delta_body_y 0];

% theta1 = [range_x/2 1 range_y/2 1 0];
% theta2 = [range_x/2 2 range_y/2+5 4 0];

theta = theta_maker(head_x, head_y, 1);

for row = 1 : 1 : range_x
    for col = 1 : 1 : range_y
        Z(row, col) = Z(row, col) + (Gaussian2D(X(row), Y(col), theta(1,:))+Gaussian2D(X(row), Y(col), theta(2,:)))/2;
    end
end
surf(X, Y, Z);
