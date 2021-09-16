function[] = histogramEqualization(imageName)
    
	% read image
	targetImage = imread(imageName);
    
	% rgb --> graylevel --> double
    grayImage = rgb2gray(targetImage);
	grayImage = im2double(grayImage);
	
	% get size
	[height, width] = size(grayImage);
	imageSize = height*width;

	% get histogram
    [pixelCounts, grayLevels] = imhist(grayImage);
	nonZeroCounts = find(pixelCounts > 0);
	
	% Histogram Equalization
	resultImage = grayImage;
	currentCDF = double(0);
	for i = 1 : length(nonZeroCounts)
		currentCDF = currentCDF + pixelCounts(nonZeroCounts(i));
		currentPixels = grayImage == grayLevels(nonZeroCounts(i));
		resultImage(currentPixels) = currentCDF/imageSize;
	end
	
	% show original image(graylevel)
	subplot(1, 2, 1);
	imshow(grayImage)
	title('Original');
	
	% show processed image
	subplot(1, 2, 2);
	imshow(resultImage)
	title('After Histogram Equalization');
	
return