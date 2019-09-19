# This program is written by Abubakr Shafique (abubakr.shafique@gmail.com) 
import numpy as np	#This is to deal with numbers and arrays
import cv2 as cv	#This is to deal with images

def Max(Current_Value, New_Value):
	if New_Value > Current_Value:
		return New_Value
	else:
		return Current_Value
		
def Min(Current_Value, New_Value):
	if New_Value < Current_Value:
		return New_Value
	else:
		return Current_Value

def Histogram_Computation(Image):
	Image_Height = Image.shape[0]
	Image_Width = Image.shape[1]
	Histogram = np.zeros([256], np.int32)
	
	Max_Intensity = 0
	Min_Intensity = 255
	
	for x in range(0, Image_Height):
		for y in range(0, Image_Width):
			Histogram[Image[x,y]] +=1
			Max_Intensity = Max(Max_Intensity, Image[x,y])
			Min_Intensity = Min(Min_Intensity, Image[x,y])
	
	return Histogram, Min_Intensity, Max_Intensity

def New_Pixel_Value(Current_Value, Min, Max):
	Target_Max = 255
	Target_Min = 0
	return (Target_Min + (Current_Value - Min) * int(Target_Max-Target_Min)/(Max-Min))

def Histogram_Equalization(Image, Min, Max):
	Image_Height = Image.shape[0]
	Image_Width = Image.shape[1]
	Size = (Image_Height, Image_Width)
	
	New_Image = np.zeros(Size, np.uint8)
	
	for x in range(0, Image_Height):
		for y in range(0, Image_Width):
			New_Image[x,y] = New_Pixel_Value(Image[x,y], Min, Max)
	
	return New_Image
def main():
	Input_Image = cv.imread("Low_Contrast.jpg",0) # This is to read Gray Scale Image
	
	Histogram_GrayScale, Min, Max = Histogram_Computation(Input_Image)
	
	New_Image = Histogram_Equalization(Input_Image, Min, Max)
	#Now to print our output Histogram
	cv.imwrite("Fixed_Low_Contrast.png", New_Image)
	input("Please Enter to Continue...")
	
if __name__ == '__main__':
	main()