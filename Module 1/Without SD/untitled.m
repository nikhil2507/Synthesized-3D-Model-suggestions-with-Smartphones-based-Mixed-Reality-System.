clc;
close all;
clear all;

prompt = 'What is the length of your room? ';
s = input(prompt);

I1 = imread('test1.jpg');
I = rot90(I1, 3);
I2 = imgaussfilt(I); 
figure;
imshow(I)

[J, rect] = imcrop(I2);
[height, width, dim] = size(J);

info = imfinfo('1.jpg');
%s = info.DigitalCamera.SubjectDistance;
S = s * 3.281;

disp(S);

Fl = info.DigitalCamera.FocalLengthIn35mmFilm;
F = info.DigitalCamera.FocalLength;

x = Fl/F;

H = 2 * atan(x/(2*F));
h = rad2deg(H);

W = info.Height;
w = width/W;

a = (w * h);
b = deg2rad(a);

wall = 2 * S * tan(b/2);

Final_Length = S;
Final_breadth = wall;

disp(Final_Length)
disp(Final_breadth)

disp(tan(b/2));

