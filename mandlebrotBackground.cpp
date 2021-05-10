#include <png++/png.hpp>
#include <string>
#include <unistd.h>
#include <complex>
#include <stdio.h>
#include <cmath>
using namespace std;

int r1, g1, b1, r2, g2, b2;

void SetColors(string flag);

int resolution;

int value ( int x, int y, float xDiv, float yDiv, float xoff, float yoff )  {
	//creates a complex point for each pixel in the screen, using the x&yDiv vars for zoom
	complex<float> point((float)-1*(1280-x)/(2560/xDiv), (float)(800-y)/(1600/yDiv));

	//creates a point for the offset, which asymptotically approaches the point we'd like to focus in on
	complex<float> zoomOffset((float)xoff, (float)yoff);
	//and adds the offset to point so that the center of the screen approaches the point we'd like to see
	point = zoomOffset + point;

	//creates point 0, 0i to be used in determining if points are in the set
	complex<float> z(0, 0);
	//varialbes for current iteration and total iterations desired. raising tot_iter makes the
	//image more detailed(esp at higher zooms) but also makes CPU go into kill state 9
	unsigned int nb_iter = 0;
	unsigned int tot_iter = 34 + (3.5/xDiv);

	resolution = tot_iter;

	//iterates zsubc = z^2 + point (mandlebrot formula) for the current point. breaks if the point diverges from 0 too hard
	while (abs (z) < 2 && nb_iter <= tot_iter) {
        	z = z * z + point;
        	nb_iter++;
    	}
	//if the num of iterations is less than the desired total iterations, we return a red value that
	//decreases based on how "not in the set" the point was
    	if (nb_iter < tot_iter) return (130*nb_iter)/50;
   	else return r2;
	//else, the point is in the set and returns the "in the set" red value
}

int main(int argv, char* argc[]){
	string flag = "e"; //argc[1]

	SetColors(flag);

	int i = 30; //starts at 30 to avoid weird zooming at the start

	do{
	//creates png image ing RGB colorspace using png++
	png::image< png::rgb_pixel > image(2560, 1600);

	//sets variables that are used to edit the zoom of the function
	float divMultiplier = (pow(1.00125, i)) +1.0;
	float offMultiplierX = ((1/(.3 * i + 1)) - .925);
	float offMultiplierY = ((-1/(.3 * i + 1)) + .2666);

	//creates variables for x and y manipulators to be passed for each pixel into mandlebrot function
	float xDiv = 3.5/divMultiplier;
	float yDiv = 2.5/divMultiplier;
	float xoff = offMultiplierX;
	float yoff = offMultiplierY;

	//i++ here so we don't pass zero at the start
	i++;

	//calls  mandlebrot function for each pixel in png file
	for (png::uint_32 y = 0; y < image.get_height(); ++y){
   		 for (png::uint_32 x = 0; x < image.get_width(); ++x){
			//calls mandlebrot function
			int redVal = value(x, y, xDiv, yDiv, xoff, yoff);

			//adds the returned color red w/ some blue and green to each pixel in file
			image[y][x] = png::rgb_pixel(redVal, 30, 30);
            		}
	}

	//creates filenames in sequential order to be created into gif
	string filename = "./mandlebrot_red/mandlebrot_red_" + std::to_string(i-30) + ".png";
	//writes image to filename using png++
	image.write(filename);
	cout << "With a resolution of " << resolution << " iterations, image written to " << filename << endl;

	if(i%100 == 0) sleep(60);

	} while(i <= (3600*2)+30); //program halts after creating 10 hours  worth of images, at .2 images every sec



	return 0;
}

void SetColors(string flag){
	//red
	if(true){
		r1 = 200;
		g1 = 41;
		b1 = 72;
		r2 = 155;
		g2 = 41;
		b2 = 72;
	}
}
