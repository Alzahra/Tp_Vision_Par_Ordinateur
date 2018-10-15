OPENCV_LIBS = -L../../lib/ -lIlmImf -llibtiff -lopencv_imgcodecs -lippicv -llibwebp -lopencv_imgproc -llibjasper -lopencv_core -lzlib -llibjpeg -lopencv_hal -llibpng -lopencv_highgui
OSX_LIBS = -framework OpenCL -framework Cocoa
INC = -I../../include/

all : marylin

marylin : marylin.cpp
	$(CXX) -o marylin marylin.cpp $(INC) $(OSX_LIBS) $(OPENCV_LIBS)

clean :
	rm marylin