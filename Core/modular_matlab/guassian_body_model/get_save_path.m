function [ gaussian_label_path ] = get_save_path( point_label_path, gaussian_label_dir )
%GET_SAVE_PATH Summary of this function goes here
%   Detailed explanation goes here
index = strfind(point_label_path, '/');
name = point_label_path(index(length(index))+1:length(point_label_path));
index = strfind(name, 'point');
mat_name = strcat(name(1:index(length(index))-1),'gaussian_label.mat');
gaussian_label_path = strcat(gaussian_label_dir, mat_name);
end

