clc;
close all;
clear all;

%prompt = 'What is the length of your room? ';
%S = input(prompt);

I = imread('12.jpg');
I2 = imgaussfilt(I); 
figure;
imshow(I)

[J, rect] = imcrop(I2);
[height, width, dim] = size(J);

info = imfinfo('12.jpg');
%s = info.DigitalCamera.SubjectDistance;
s = 4.295;
S = s * 32.81;

disp(s);

Fl = info.DigitalCamera.FocalLengthIn35mmFilm;
F = info.DigitalCamera.FocalLength;

x = Fl/F;

H = 2 * atan(x/Fl);
h = rad2deg(H);

W = info.Width;
w = width/W;

a = (w * h) / 100;
b = deg2rad(a);

wall = 2 * S * tan(b/2);

Final_Length = S;
Final_breadth = wall;

disp(Final_Length)
disp(Final_breadth)


