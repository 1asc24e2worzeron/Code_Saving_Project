function idealLowpassFilter(imageName)

    % read image
    targetImage = imread(imageName);    
    
    % cut-off frequency = 200
    D0 = 200;
    % get size
    [width, height] = size(targetImage);
    
    % Fourier Transform 
    imageFT = fft2(double(targetImage));
    
    % get Euclidean Distances
    u = 0 : width-1;
    for i = floor(width/2) + 2 : width
        u(i) = width - u(i);
    end
    v = 0 : height-1;
    for i = floor(height/2) + 2 : height
        v(i) = height - v(i);
    end
    [V, U] = meshgrid(v, u);
    D = sqrt(U.^2+V.^2);
    % get mask
    H = double(D <= D0);
    % calculate result 
    G = H.*imageFT;
    
    % get result image
    resultImage = real(ifft2(double(G))); 
    
    % show original image
    subplot(2, 3, 1), imshow(targetImage), title('Original Image');
    % show processed image
    subplot(2, 3, 2), imshow(mat2gray(resultImage)), title('Processed Image');
    % show mask
    subplot(2, 3, 3), imshow(mat2gray(1+abs(fftshift(H)))), title('Mask');
    % show original image's Fourier Spectrum
    subplot(2, 3, 4), imshow(mat2gray(log(1+abs(fftshift(imageFT))))), title('Fourier Spectrum of Orignial Image');
    % show processed image's Fourier Spectrum
    subplot(2, 3, 5), imshow(mat2gray(log(1+abs(fftshift(G))))), title('Fourier Spectrum of Processed Image');

end