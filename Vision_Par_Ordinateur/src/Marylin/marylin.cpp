#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <iostream>
#include <string>

using namespace cv;
using namespace std;

Vec3b v1,v2,vj;
Mat image;
Mat img,img2,img3,img4,img5,img6,img7,img8,img9;
Mat out1,out2,out3,out4;
Mat finale;


///Cherche la Couleur de fond et la remplace par le parametre couleur
void chercheCouleurFond(Mat photo, int couleur){
    
    v1 = photo.at<Vec3b>(3,3); //pixel de reference de la couleur de fond
    //cout << "V1 : " << v1 << endl;
    //vj = img.at<Vec3b>(30,30); //Pour isoler la couleur jaune des cheveux
    int diff = 50; //intervalle de la couleur de fond
    //bool contour = 0; //si on rencontre la couleur jaune on est dans le visage donc pas de remplacement
    for (int y = 0; y < photo.rows; y++){
        for (int x = 0; x < photo.cols; x++){
            v2 = photo.at<Vec3b>(y,x); //pixel du parcours
            //cout <<"V2 : " <<v2 << endl;
            if( v1[0] + diff >= v2[0] && v2[0]>= v1[0] - diff ){
                if( v1[1] + diff >= v2[1] && v2[1]>= v1[1] - diff ){
                    if( v1[2] + diff >= v2[2] && v2[2]>= v1[2] - diff ){
                        
                        photo.at<Vec3b>(y,x)[0] = couleur+20;
                        photo.at<Vec3b>(y,x)[1] = couleur-50;
                        photo.at<Vec3b>(y,x)[2] = couleur+70;
                    }
                }
            }
            
        }
    }
}

int main( int argc, char** argv )
{
 char* imageName = argv[1];

 image = imread (imageName, 1);
 img = image.clone();
 img2 = image.clone();
 img3 = image.clone();
 img4 = image.clone();
 img5 = image.clone();
 img6 = image.clone();
 img7 = image.clone();
 img8 = image.clone();
 img9 = image.clone();

 if( argc != 2 || !img.data )
 {
   printf( " No image data \n " );
   return -1;
 }

 chercheCouleurFond(img,255);
 chercheCouleurFond(img2,200);
 chercheCouleurFond(img3,150);
 chercheCouleurFond(img4,130);
 chercheCouleurFond(img5,120);
 chercheCouleurFond(img6,100);
 chercheCouleurFond(img7,50);
 chercheCouleurFond(img8,30);
 chercheCouleurFond(img9,0);
 
 //Mat mask;
 //inRange(image, s, s, mask);
 //image.setTo(Scalar(0,0,0),mask);
    
 hconcat(img,img2,out1);
 hconcat(out1,img3,out2); //ligne de 3
 
 hconcat(img4,img5,out1);
 hconcat(out1,img6,out3); //ligne de 3
 
 hconcat(img7,img8,out1);
 hconcat(out1,img9,out4); //ligne de 3
    
 vconcat(out2,out3,out1);
 vconcat(out4,out1,finale);
    
    
 namedWindow( imageName, CV_WINDOW_AUTOSIZE );
 namedWindow("Concat", CV_WINDOW_AUTOSIZE);
    
    
 imshow(imageName, image );
 imshow("Concat",finale);

 waitKey(0);

 return 0;
}
