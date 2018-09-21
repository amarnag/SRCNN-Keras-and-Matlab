clc
clear all
close all
up_scale=3;
im=imread('Set5/butterfly_GT.bmp');
% work on illuminance only
if size(im,3)>1
    im = rgb2ycbcr(im);
    im = im(:, :, 1);
end
im_gnd = modcrop(im, up_scale);
im_gnd = single(im_gnd)/255;
%% bicubic interpolation
 im_l = imresize(im_gnd, 1/up_scale, 'bicubic');
 im_b = imresize(im_l, up_scale, 'bicubic');
 im_h=imread('butterfly_SRCNN.bmp');
% %% remove border
im_h = shave(uint8(im_h), [up_scale, up_scale]);
im_gnd = shave(uint8(im_gnd*255), [up_scale, up_scale]);
 im_b = shave(uint8(im_b*255), [up_scale, up_scale]);
%% compute PSNR
psnr_bic = compute_psnr(im_gnd,im_b);
psnr_srcnn = compute_psnr(im_gnd,im_h);

figure, imshow(im_b); title('Bicubic Interpolation');
figure, imshow(im_h); title('SRCNN Reconstruction');
%% show results
fprintf('PSNR for Bicubic Interpolation: %f dB\n', psnr_bic);
fprintf('PSNR for SRCNN Reconstruction: %f dB\n', psnr_srcnn);
