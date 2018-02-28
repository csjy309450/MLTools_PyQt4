label_dir_path = '/home/yz/testData/ucsd/labels/vidf1_33_000.y/point_mat/';
gaussian_label_dir = '/home/yz/testData/ucsd/labels/vidf1_33_000.y/gaussain_mat/';
point_label_path = '%svidf1_33_000_f%.3d_point_label.mat';

range_size = [240,240];
X = 1 : 1 : range_size(1);Y = 1 : 1: range_size(2);
img_size = [238,158];

for i = 1:1:200
    t_point_label_path = sprintf(point_label_path,label_dir_path,i);
    fprintf('%s\n', t_point_label_path);
    gaussian_labe_data = gaussian_label(t_point_label_path,img_size,range_size);
%     gaussian_labe_data=fliplr(gaussian_labe_data);
%     gaussian_labe_data = flipud(gaussian_labe_data);
    gaussian_labe_data=gaussian_labe_data';
    % 绘制三维图像
%     surf(X, Y, gaussian_labe_data);
    gaussian_label_path = get_save_path(t_point_label_path, gaussian_label_dir);
    save(gaussian_label_path,'gaussian_labe_data')
end
%gaussian_label('vidf1_33_000_f001_point_label')