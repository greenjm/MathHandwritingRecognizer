% clear workspace
clear all; close all;

% convert to HSV
img = imread('IMAG1480_1.jpg');
[h s v] = rgb2hsv(img);

% get edge gradients
gradV = imgradient(v);
gradV = medfilt2(gradV);

% convert to regions where characters might be
regions = imdilate((gradV>0.35), strel('square',15));
new = uint8(repmat(regions,1,1,3) .* double(img));
ar = double(new);

% display image
subplot(1,2,1)
imshow(img)
title('original')

subplot(1,2,2)
imshow(rgb2gray(new))
title('segmented areas of interest')

