% label gaussian labels
%
function[gaussian_label_path] = gaussian_label(point_label_path)
index = strfind(point_label_path,'point');
gaussian_label_path = strcat(point_label_path(1:index-1),'gaussian_label.mat');
% load pedestrians' point label(position of heads)
mat_struct = load(point_label_path);
% labels = fgt.frame{1,1}.loc;
labels = double(mat_struct.data);
% plot range
range_x = 240;range_y = 240;
% image width and height
img_w = 238;img_h = 158;
% plot array
X = 0 : 1 : range_x;Y = 0 : 1: range_y;
Z = zeros(range_x+1, range_y+1);

for i = 1:1:length(labels)
%     theata1 = [labels(i,1) 1 labels(i,2) 1 0];
%     theata2 = [labels(i,1) 2 labels(i,2)+5 4 0];
% 构造混合高斯模型参数
    theta = theta_maker(labels(i,1), labels(i,2));
    for row = 1 : 1 : img_w
        for col = 1 : 1 : img_h
            Z(row, col) = Z(row, col) + (Gaussian2D(X(row), Y(col), theta(1,:))+Gaussian2D(X(row), Y(col), theta(2,:)))/2;
        end
    end
end
surf(X, Y, Z);
% data = Z(1:img_w,1:img_h).';
% save(gaussian_label_path,'data')