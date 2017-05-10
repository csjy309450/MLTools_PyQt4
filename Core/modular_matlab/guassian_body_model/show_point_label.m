% show head point labels(head position)

data = load('vidf1_33_000_f001_point_label.mat');
labels = data.data;

img_name = 'vidf1_33_000_f001.png';

im = imread(img_name);

imshow(im); hold on;
plot(labels(:,1),labels(:,2),'r*');