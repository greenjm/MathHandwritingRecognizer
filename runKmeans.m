function [img means]=runKmeans(img, k)
% Runs the entire k-means algorithm on img
% with k clusters

seed = 0;
rand('state', seed);
means = rand(k,3).*255;
hasMoved = 1;
img = double(img);
iter = 0;

while hasMoved
    %Initialize starting distance
    resImg = zeros(size(img));
    resImg(:,:,1) = img(:,:,1) - means(1,1);
    resImg(:,:,2) = img(:,:,2) - means(1,2);
    resImg(:,:,3) = img(:,:,3) - means(1,3);
    resImg = resImg.^2;
    resImg = sum(resImg,3);
    resImg = sqrt(resImg);
    resClusterIds = ones(size(resImg));
    
    % Loop k-1 times, finding all cluster ids
    for i=2:k
        currImg = zeros(size(img));
        currImg(:,:,1) = img(:,:,1)-means(i,1);
        currImg(:,:,2) = img(:,:,2)-means(i,2);
        currImg(:,:,3) = img(:,:,3)-means(i,3);
        currImg = currImg.^2;
        currImg = sum(currImg,3);
        currImg = sqrt(currImg);
        resClusterIds(find(currImg < resImg)) = i;
        [r, c] = find(resClusterIds == i);
        for j=1:numel(r)
            resImg(r(j),c(j)) = currImg(r(j),c(j));
        end
    end
    
    % Update means
    newMeans = means;
    for i=1:k
        [r, c] = find(resClusterIds == i);
        numPixels = numel(r);
        if numPixels > 0
            sum1 = 0;
            sum2 = 0;
            sum3 = 0;
            for j=1:numPixels
                sum1 = sum1+img(r(j),c(j),1);
                sum2 = sum2+img(r(j),c(j),2);
                sum3 = sum3+img(r(j),c(j),3);
            end
            newMeans(i,1) = sum1/numPixels;
            newMeans(i,2) = sum2/numPixels;
            newMeans(i,3) = sum3/numPixels;
        end
    end
    
    hasMoved = numel(find(means ~= newMeans));
    iter = iter+1;
    means = newMeans;
end

for i=1:k
    [r, c] = find(resClusterIds==i);
    for j=1:numel(r)
        img(r(j),c(j),1) = means(i,1);
        img(r(j),c(j),2) = means(i,2);
        img(r(j),c(j),3) = means(i,3);
    end
end

img = uint8(img);