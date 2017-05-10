% overlapping gaussian label to image
load('vidf1_33_000_f001_gaussian_label.mat')
labels = data;
img = imread('vidf1_33_000_f001.png');
shape_img = size(img);
% assert(shape_img==size(labels))
for col = 1:1:shape_img(1)
    for row = 1:1:shape_img(2)
        if labels(col,row) > 0.001
            img(col,row) = 255;
        end
    end
end
peolpe_count = sum(labels(:))
imshow(img);
