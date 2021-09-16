targetImage = imread('lena512color.tiff');

hsvImage = rgb2hsv(targetImage);
processingHsvImage = hsvImage;
processingHsvImage(:, :, 3) = histeq(hsvImage(:, :, 3));
processedImage = hsv2rgb(processingHsvImage);

ycbcrImage = rgb2ycbcr(targetImage);
processedYcbcrImage = histeq(ycbcrImage);

subplot(2, 2, 1), imshow(targetImage), title('Original');
subplot(2, 2, 3), imshow(processedImage), title('Processed');

subplot(2, 2, 2), imshow(ycbcrImage), title('Original - YCbCr');
subplot(2, 2, 4), imshow(processedYcbcrImage), title('Processed - YCbCr');