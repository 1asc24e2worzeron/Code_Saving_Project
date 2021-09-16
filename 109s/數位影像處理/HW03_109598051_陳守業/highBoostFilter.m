function[] = highBoostFilter(imageName)
    
	% read image
	targetImage = imread(imageName);
    % copy image, 'targetImage' has to be used in calculation
    originalImage = targetImage;
    % use 'targetImage' to initialize 'resultImage'
    resultImage = targetImage;
    
	% get Gaussian filter...
    % kernel size = 31 * 31
    kernelEdge = 31;
    % this will be used in the following calculation
    difference = floor(kernelEdge / 2);
    % get kernel
	kernel = fspecial('gaussian', [kernelEdge, kernelEdge], 5);
    % kernel --> rotate 180 degrees(actually not needed, because the kernel is centrosymmetric)
    kernel = rot90(kernel, 2);
    % ...get Gaussian filter
    
    % Gaussian Blurring...
    % padding zeros, element type transform to double
    targetImage = double(padarray(targetImage, [difference, difference], 0));
    % get size
	[height, width] = size(targetImage);
	% convolution, result --> resultImage
    for i = 1 + difference : height - difference
        for j = 1 + difference : width - difference
			temp = targetImage(i-difference : i+difference, j-difference : j+difference) .* kernel;
			resultImage(i-difference, j-difference) = sum(temp(:));
        end
    end
    % ...Gaussian Blurring
    
	% high boost, weight = 4.5
    mask = double(originalImage) - double(resultImage);
    resultImage = uint8(double(originalImage) + 4.5*mask);
	
    % show original image(graylevel)
	subplot(1, 3, 1), imshow(originalImage), title('Original Image');
	% show mask
	subplot(1, 3, 2), imshow(mat2gray(mask)), title('Mask');
	% show processed image
	subplot(1, 3, 3), imshow(resultImage), title('After High Boost');
	
return