range_size = [240,240];
X = 1 : 1 : range_size(1);Y = 1 : 1: range_size(2);
data = load('/home/yz/testData/ucsd/labels/vidf1_33_000.y/gaussain_mat/vidf1_33_000_f009_gaussian_label.mat');
labels_ = zeros(240);
lab = data.gaussian_labe_data;
labels_(1:158,1:238) = lab;
surf(X, Y, labels);
sum(sum(lab))