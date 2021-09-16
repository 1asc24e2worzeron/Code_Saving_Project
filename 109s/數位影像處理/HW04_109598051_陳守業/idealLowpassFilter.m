function idealLowpassFilter(imageName)

    % read image
    targetImage = imread(imageName);    
    
    % cut-off frequency = 200
    D0 = 200;
    % get size
    [width, height] = size(targetImage);
    
    % Fourier Transform 
    imageFT = padarray(double(targetImage), [width, height], 'replicate', 'post');
    imageFT = fft2(fftshift(imageFT));
    
    % get Euclidean Distances
    u = [0 : width - 1, width - 1 : -1 : 0];
    v = [0 : height - 1, height - 1 : -1 : 0];
    [V, U] = meshgrid(v, u);
    D = sqrt(U.^2+V.^2);
    % get mask
    H = double(D <= D0);
    % calculate result
    G = H.*imageFT;
    % get result image
    resultImage = fftshift(real(ifft2(double(G))));
    resultImage = resultImage(1 : width, 1 : height);
    
    % show original image
    subplot(2, 3, 1), imshow(targetImage, []), title('Original Image');
    % show processed image
    subplot(2, 3, 2), imshow(mat2gray(resultImage)), title('Processed Image');
    % show mask
    subplot(2, 3, 3), imshow(mat2gray(log(1+abs(fftshift(H))))), title('Mask');
    % show original image's Fourier Spectrum
    subplot(2, 3, 4), imshow(mat2gray(log(1+abs(fftshift(imageFT))))), title('Spectrum(Original)');
    % show processed image's Fourier Spectrum
    subplot(2, 3, 5), imshow(mat2gray(log(1+abs(fftshift(G))))), title('Spectrum(Processed)');

end