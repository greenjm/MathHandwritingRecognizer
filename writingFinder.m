% clear workspace
clear all; close all;

% convert to HSV
img = imread('IMAG1480_1.jpg');
BW = imbinarize(rgb2gray(img),'adaptive','ForegroundPolarity','dark','Sensitivity',0.5);

imshow( repmat(BW,1,1,3) .* double(img))

[h s v] = rgb2hsv(img);

% get edge gradients
gradV = imgradient(v);
gradV = medfilt2(gradV);

% convert to regions where characters might be
regions = imdilate((BW<0.35), strel('square',10));
new = uint8((repmat(regions,1,1,3) .* double(img)));
grayd = rgb2gray(new);
ar = double(new);

% display image
subplot(1,2,1)
imshow(img)
title('original')

subplot(1,2,2)
imshow(grayd)
title('segmented areas of interest')
