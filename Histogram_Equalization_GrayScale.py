##This Program is written by Abubakr Shafique (abubakr.shafique@gmail.com)
import numpy as np
import cv2 as cv

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
		
#This Histogram Function Takes in a Mat Image and Calculate Histogram
def Calculate_Histogram_Gray(Image):
	Image_Height = Image.shape[1] #get the Height of the Image
	Image_Width = Image.shape[0] #get the Width of the Image
	
	Max_Intensity = 0
	Min_Intensity = 255
	
	Hist = np.zeros([256], np.int32) #Initialize an empty 256 array
	
	for x in range(0,Image_Width): # loop through the Image
		for y in range(0,Image_Height):
			Hist[Image[x,y]] +=1 # increment the same intensity values
			Max_Intensity = Max(Max_Intensity, Image[x,y])
			Min_Intensity = Min(Min_Intensity, Image[x,y])
			
	return Hist, Max_Intensity, Min_Intensity

def New_Pixel_Value(Previous_Value, Max, Min):
	Target_Max = 255
	Target_Min = 0
	return (Target_Min + (Previous_Value - Min) * int((Target_Max - Target_Min)/(Max-Min)))

def Histogram_Equalization(Image, Max, Min):
	Image_Height = Image.shape[1] #get the Height of the Image
	Image_Width = Image.shape[0] #get the Width of the Image
	Size = (Image_Width, Image_Height)
	New_Image = np.zeros(Size, np.uint8)
	
	for x in range(0,Image_Width): # loop through the Image
		for y in range(0,Image_Height):
			New_Image[x,y] = New_Pixel_Value(Image[x,y], Max, Min)
	
	return New_Image
	
def main():
	Input_Image = cv.imread('Low_Contrast.jpg',0) #This will read a GrayScale Image (Even if it is RGB it will read GrayScale)
	Histogram_GrayScale, Max_Intensity, Min_Intensity = Calculate_Histogram_Gray(Input_Image)
	
	New_Image = Histogram_Equalization(Input_Image, Max_Intensity, Min_Intensity)
	
	#Now We Will show the result
	cv.imshow("Fixed_Image", New_Image)
	cv.waitKey()
	
	input("Press Enter to continue...")


if __name__ == '__main__':
	main() #Our main function