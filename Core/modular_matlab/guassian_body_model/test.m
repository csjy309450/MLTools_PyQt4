point_label_path = 'vidf1_33_000_f%.3d_point_label.mat';
for i = 0:1:200
    sprintf(point_label_path,i)
end
gaussian_label('vidf1_33_000_f001_point_label')