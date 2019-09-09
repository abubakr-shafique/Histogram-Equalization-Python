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
def Calculate_Histogram_Color(Image):
	Image_Height = Image.shape[1] #get the Height of the Image
	Image_Width = Image.shape[0] #get the Width of the Image
	Image_Channels = Image.shape[2] #get the Channels of the Image
	
	Max_Intensity = np.zeros([Image_Channels], np.int32)
	Min_Intensity = np.full([Image_Channels], 255, np.int32)
	
	Hist = np.zeros([256,Image_Channels], np.int32) #Initialize an empty 256 array for each channel
	
	for x in range(0,Image_Width): # loop through the Image
		for y in range(0,Image_Height):
			for c in range(0, Image_Channels):
				Hist[Image[x,y,c],c] +=1 # increment the same intensity values
				Max_Intensity[c] = Max(Max_Intensity[c], Image[x,y,c])
				Min_Intensity[c] = Min(Min_Intensity[c], Image[x,y,c])
			
	return Hist, Max_Intensity, Min_Intensity

def New_Pixel_Value(Previous_Value, Max, Min):
	Target_Max = 255
	Target_Min = 0
	return (Target_Min + (Previous_Value - Min) * int((Target_Max - Target_Min)/(Max-Min)))

def Histogram_Equalization(Image, Max, Min):
	Image_Height = Image.shape[1] #get the Height of the Image
	Image_Width = Image.shape[0] #get the Width of the Image
	Image_Channels = Image.shape[2] #get the Channels of the Image
	
	Size = (Image_Width, Image_Height, Image_Channels)
	New_Image = np.zeros(Size, np.uint8)
	
	for x in range(0,Image_Width): # loop through the Image
		for y in range(0,Image_Height):
			for c in range(0, Image_Channels):
				New_Image[x,y,c] = New_Pixel_Value(Image[x,y,c], Max[c], Min[c])
	
	return New_Image
	
def main():
	Input_Image = cv.imread('Low_Contrast_Color.jpg')
	Histogram, Max_Intensity, Min_Intensity = Calculate_Histogram_Color(Input_Image)
	
	New_Image = Histogram_Equalization(Input_Image, Max_Intensity, Min_Intensity)
	
	#Now We Will show the result
	cv.imshow("Fixed_Image", New_Image)
	cv.waitKey()
	
	input("Press Enter to continue...")


if __name__ == '__main__':
	main() #Our main function