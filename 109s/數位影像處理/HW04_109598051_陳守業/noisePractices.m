% Example of classical resoration filter -- motion deblurring by Wiener Filters.

clear

d = 40;
h = zeros(2*d+1, 2*d+1);
for i = 1 : 2*d+1
    for j = 1 : 2*d+1
        if i + j == 2*d+2
            h(i, j) = 1/(2*d);
        end
    end
end

%blurred image
[f, map] = imread('lena_gray.bmp'); % original image
[m, n] = size(f);

fe = zeros(m+2*d, n+2*d);
fe(1:m, 1:n) = f; % original image --> (m+2d)*(n+2d) size, zero padded image

he=zeros(m+2*d, n+2*d);
he(1:2*d+1, 1:2*d+1)=h; % noise --> (m+2d)*(n+2d) size, zero padded noise matrix

n=3*rand(m+2*d,n+2*d); % (m+2d)*(n+2d) size, 0~3 random integer matrix

F_f=fftshift(fft2(f)); % original image --> FT

F_fe=fftshift(fft2(fe)); % padded original image --> FT
F_he=fftshift(fft2(he)); % padded noise matrix --> FT

g=ifft2(F_fe.*F_he); % motion blurred image (FT)
gn=ifft2(F_fe.*F_he)+n; % motion blurred image + noises (FT)

F_g=fft2(g); % motion blurred image
F_gn=fft2(gn); % motion blurred image + noises

% figure 1
figure, image(f);colormap(map);

% figure 2
flog = log(1+abs(F_f));
fm = max(flog(:));
figure,image(flog*255/fm);
colormap(map);

% figure 3
figure, image(g);colormap(map);

% figure 4
flog = log(1+abs(F_g));
fm = max(flog(:));
figure,image(flog*255/fm);
colormap(map);

% figure 5
figure, image(gn);colormap(map);

% figure 6
flog = log(1+abs(F_gn));
fm = max(flog(:));
figure,image(flog*255/fm);
colormap(map);

% figure 7
K=0.0009;
f_hat=((F_he.^2)./(F_he.^2+K)).*F_g./F_he;
f_hat=real(ifft2(f_hat)); % restored image - motion blurred image
figure, image(f_hat);colormap(map);

% figure 8
K=0.0009;
f_hat=((F_he.^2)./(F_he.^2+K)).*F_gn./F_he;
f_hat=real(ifft2(f_hat)); % restored image - motion blurred image + noises
figure, image(f_hat);colormap(map);

% figure 9
K=0.0002;
f_hat=((F_he.^2)./(F_he.^2+K)).*F_g./F_he;
f_hat=real(ifft2(f_hat)); % restored image - motion blurred image
figure, image(f_hat);colormap(map);

% figure 10
K=0.0002;
f_hat=((F_he.^2)./(F_he.^2+K)).*F_gn./F_he;
f_hat=real(ifft2(f_hat)); % restored image - motion blurred image + noises
figure, image(f_hat);colormap(map);

% figure 11
K=0.01;
f_hat=((F_he.^2)./(F_he.^2+K)).*F_g./F_he;
f_hat=real(ifft2(f_hat)); % restored image - motion blurred image
figure, image(f_hat);colormap(map);

% figure 12
K=0.01;
f_hat=((F_he.^2)./(F_he.^2+K)).*F_gn./F_he;
f_hat=real(ifft2(f_hat)); % restored image - motion blurred image + noises
figure, image(f_hat);colormap(map);