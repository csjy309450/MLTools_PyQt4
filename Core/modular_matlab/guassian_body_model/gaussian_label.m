% label gaussian labels, 输入一个标签.mat路径，
%
function[gaussian_label] = gaussian_label(point_label_path, img_size, range_size)
if(length(img_size)~=2 || length(range_size)~=2)
    return
end
% load pedestrians' point label(position of heads)
mat_struct = load(point_label_path);
% labels = fgt.frame{1,1}.loc;
labels = double(mat_struct.point);
% plot range
%range_x = 240;range_y = 240;
% image width and height
% img_w = 238;img_h = 158;
% plot array
X = 0 : 1 : range_size(1)-1;Y = 0 : 1: range_size(2)-1;
Z = zeros(range_size(1), range_size(2));

for i = 1:1:length(labels)
%     theata1 = [labels(i,1) 1 labels(i,2) 1 0];
%     theata2 = [labels(i,1) 2 labels(i,2)+5 4 0];
% 构造混合高斯模型参数
    theta = theta_maker(labels(i,1), labels(i,2));
   
    for row = 1 : 1 : img_size(1)
        for col = 1 : 1 : img_size(2)
%             if row==219 && col==8 && i==16
%                 (Gaussian2D(X(row), Y(col), theta(1,:))+Gaussian2D(X(row), Y(col), theta(2,:)))/2
%             end
            Z(row, col) = Z(row, col) + (Gaussian2D(X(row), Y(col), theta(1,:))+Gaussian2D(X(row), Y(col), theta(2,:)))/2;
            if Z(row, col) > 1
                % 这里增加阈值判定主要是为了解决数值计算上产生的误差，造成计算得到的概率值大于1的情况
                Z(row, col)=0.8;
            end
        end
    end
end
% 截取有效数据
gaussian_label = Z(1:img_size(1),1:img_size(2));
% save(gaussian_label_path,'data')