//Inclusions
#include <stdlib.h>
#include <iostream>

//Definitions
#define rgbcmy converter.rgbToCmy(rgb)
#define cmyrgb converter.cmyToRgb(cmy)
#define rgbhsl converter.rgbToHsl(rgb)
#define hslrgb converter.hslToRgb(hsl)
#define transp converter.transparency(rgb, transparency, rgbBack)

//Namespace
using namespace std;

//Class assignment
class ColourConverter {
public:
	//Constructor
	ColourConverter() {

	}

	//Destructor
	~ColourConverter() {

	}

	//Methods
	float* rgbToCmy(float rgb[3]) {
		//Read RGB values from array
		float r = rgb[0];	//Red at index 0
		float g = rgb[1];	//Green at index 1
		float b = rgb[2];	//Blue at index 2

		//Calculate CMY from RGB - Note division by 255 to get RGB values between 1 (full) and 0 (none)
		float c = 1.0 - r;	//Cyan is full minus red
		float m = 1.0 - g;	//Magenta is full minus green
		float y = 1.0 - b;	//Yellow is full minus blue

		//Store CMY values in new array and return it
		float cmy[3] = { c, m, y };
		return cmy;
	}

	float* cmyToRgb(float cmy[3]) {
		//Read CMY values from array
		float c = cmy[0];	//Cyan at index 0
		float m = cmy[1];	//Magenta at index 1
		float y = cmy[2];	//Yellow at index 2

		//Calculate RGB from CMY - Again note the division by 255
		float r = 1.0 - c;	//Red is full minus cyan
		float g = 1.0 - m;	//Green is full minus magenta
		float b = 1.0 - y;	//Blue is full minus yellow

		//Store RGB values in new array and return it
		float rgb[3] = { r, g, b };
		return rgb;
	}

	float* rgbToHsl(float rgb[3]) {
		//Read RGB values from array
		float r = rgb[0];	//Red at index 0
		float g = rgb[1];	//Green at index 1
		float b = rgb[2];	//Blue at index 2

		//Predefine HSL floats
		float h;	//Hue
		float s;	//Saturation
		float l;	//Luminance

		//Store minimum and maximum RGB values
		float min;
		float max;

		//Find minimum and maximum
		if (r < g) {			//Red smaller than Green...
			if (r < b) {			//...and Red smaller than Blue...
				min = r;				//...Red is smallest
				if (g < b) {				//If Green is smaller than Blue...
					max = b;					//...Blue is biggest
				}
				else if (g > b) {			//If Green is bigger than Blue...
					max = g;					//...Green is biggest
				}				
			}
			else if (r > b) {		//...and Red is bigger than Blue...
				min = b;				//...Blue is smallest
				max = g;				//...Green is biggest
			}
		}
		else if (r > g) {		//Red bigger than Green...
			if (r < b) {			//...and Red smaller than Blue...
				min = g;				//...Green is smallest
				max = b;				//...Blue is biggest
			}
			else if (r > b) {		//...and Red is bigger than Blue...
				max = r;				//...Red is biggest
				if (g < b) {			//...and Green is smaller than Blue...
					min = g;				//...Green is smallest
				}
				else if (g > b) {		//...and Green is bigger than Blue...
					min = b;				//...Blue is smallest
				}
			}
		}

		//Luminance is average of min and max
		l = (max + min) / 2.0;

		//Check if saturation is present
		bool hasSaturation = true;	//By default true
		if (min == max) {	//If minimum and maximum are the same...
			hasSaturation = false;	//...there is no saturation
		}

		//If there is saturation, calculate it
		if (hasSaturation) {
			if (l < 0.5) {
				s = (max - min) / (max + min);	//Formula for saturation
			}
			else {
				s = (max - min) / (2.0 - max - min);	//Formula for saturation
			}
		}
		else {	//If there is no saturation, set it to 0
			s = 0.0;	//No saturation
			h = 0.0;	//Without saturation there is no hue
		}

		//If there is saturation, calculate hue
		if (hasSaturation) {
			float rawH;	//Store raw h
			if (max == r) {
				rawH = (g - b) / (max - min);	//Formula for raw h when Red is biggest
			}
			else if (max == g) {
				rawH = 2.0 + ((b - r) / (max - min));	//Formula for raw h when Green is biggest
			}
			else if (max == b) {
				rawH = 4.0 + ((r - g) / max - min);	//Formula for raw h when Blue is biggest
			}

			h = rawH * 60;	//Converted h to degrees
			if (h < 0) {	//If negative hue
				h += 360;	//Add 360 degrees
			}
		}


		float hsl[3] = { h, s, l };
		return hsl;
	}

	float* hslToRgb(float hsl[3]) {
		//Read HSL values from array
		float h = hsl[0];	//Hue at index 0
		float s = hsl[1];	//Saturation at index 1
		float l = hsl[2];	//Luminance at index 2

		//Predefine RGB floats
		float r;	//Red
		float g;	//Green
		float b;	//Blue

		//Check if there is saturation
		bool hasSaturation = true;
		if (s == 0) {
			hasSaturation = false;
		}

		if (!hasSaturation) {
			r = l;
			g = l;
			b = l;
		}

		else {
			//Temp floats for readability
			float temp1;
			float temp2;
			if (l < 0.5) {
				temp1 = l * (1.0 + s);	//Formula for first temp value when l < 0.5
			}
			else {
				temp1 = (l + s) - (l * s);	//Formula for first temp value when l > 0.5
			}
			temp2 = (2 * l) - temp1;	//Formula for second temp value

			float rawH = h / 360.0;	//Degree to decimal
			
			//Temporary RGB values
			float tempR = rawH + (1.0/3.0);
			if (tempR < 0) {	//If smaller than 0
				tempR += 1;	//Add one
			}
			else if (tempR > 1) {	//If bigger than 1
				tempR -= 1;	//Subtract one
			}

			float tempG = rawH;
			if (tempG < 0) {	//If smaller than 0
				tempG += 1;	//Add one
			}
			else if (tempG > 1) {	//If bigger than 1
				tempG -= 1;	//Subtract one
			}

			float tempB = rawH - (1.0/3.0);
			if (tempB < 0) {	//If smaller than 0
				tempB += 1;	//Add one
			}
			else if (tempB > 1) {	//If bigger than 1
				tempB -= 1;	//Subtract one
			}

			//Tests to find correct formula
			//Red
			if ((6 * tempR) < 1) {	//Possibility one
				r = temp2 + (temp1 - temp2) * 6 * tempR;
			}
			else if ((2 * tempR) < 1) {	//Possibility two
				r = temp1;
			}
			else if ((3 * tempR) < 2) {	//Possibility three
				r = temp2 + (temp1 - temp2) * ((2.0/3.0) - tempR) * 6;
			}
			else {	//If all fail
				r = temp2;
			}

			//Green
			if ((6 * tempG) < 1) {	//Possibility one
				g = temp2 + (temp1 - temp2) * 6 * tempG;
			}
			else if ((2 * tempG) < 1) {	//Possibility two
				g = temp1;
			}
			else if ((3 * tempG) < 2) {	//Possibility three
				g = temp2 + (temp1 - temp2) * ((2.0/3.0) - tempG) * 6;
			}
			else {	//If all fail
				g = temp2;
			}

			//Blue
			if ((6 * tempB) < 1) {	//Possibility one
				b = temp2 + (temp1 - temp2) * 6 * tempB;
			}
			else if ((2 * tempB) < 1) {	//Possibility two
				b = temp1;
			}
			else if ((3 * tempB) < 2) {	//Possibility three
				b = temp2 + (temp1 - temp2) * ((2.0/3.0) - tempB) * 6;
			}
			else {	//If all fail
				b = temp2;
			}
		}

		float rgb[3] = { r, g, b };
		return rgb;
	}

	float* transparency(float rgbFront[3], float transparency, float rgbBack[3]) {
		//Read Front RGB values from array
		float rFront = rgbFront[0];	//Red at index 0
		float gFront = rgbFront[1];	//Green at index 1
		float bFront = rgbFront[2];	//Blue at index 2

		//Read back RGB values from array
		float rBack = rgbBack[0];	//Red at index 0
		float gBack = rgbBack[1];	//Green at index 1
		float bBack = rgbBack[2];	//Blue at index 2

		//Calculate opacity of front RGB
		float opacity = 1 - transparency;

		//Calculate RGB values of colliding area
		float rFinal = (opacity * rFront) + (transparency * rBack);
		float gFinal = (opacity * gFront) + (transparency * gBack);
		float bFinal = (opacity * bFront) + (transparency * bBack);

		float finalRgb[3] = { rFinal, gFinal, bFinal };
		return finalRgb;
	}
};

//Main method
int main() {
	//Converter object
	ColourConverter converter;	//Converter object

	//Random RGB and CMY values for testing
	float rgb[3] = { 0.79, 0.55, 0.02 };
	float cmy[3] = { rgbcmy[0], rgbcmy[1], rgbcmy[2] };
	float hsl[3] = { rgbhsl[0], rgbhsl[1], rgbhsl[2] };
	float rgbBack[3] = { 0.65, 0.81, 0.05 };
	float transparency = 0.44;

	//RGB -> CMY test
	cout << "RGB to CMY conversion:" << endl;
	cout << "\tRGB: \t\tR:" << rgb[0] << "\t\tG:" << rgb[1] << "\t\tB:" << rgb[2] << endl;
	cout << "\tCMY: \t\tC:" << rgbcmy[0] << "\t\tM:" << rgbcmy[1] << "\t\tY:" << rgbcmy[2] << endl;

	cout << endl;	//Separator

	//CMY -> RGB test
	cout << "CMY to RGB conversion:" << endl;
	cout << "\tCMY: \t\tC:" << cmy[0] << "\t\tM:" << cmy[1] << "\t\tY:" << cmy[2] << endl;
	cout << "\tRGB: \t\tR:" << cmyrgb[0] << "\t\tG:" << cmyrgb[1] << "\t\tB:" << cmyrgb[2] << endl;

	cout << endl;	//Separator

	//RGB -> HSL test
	cout << "RGB to HSL conversion:" << endl;
	cout << "\tRGB: \t\tR:" << rgb[0] << "\t\tG:" << rgb[1] << "\t\tB:" << rgb[2] << endl;
	cout << "\tHSL: \t\tH:" << rgbhsl[0] << "\tS:" << rgbhsl[1] << "\tL:" << rgbhsl[2] << endl;

	cout << endl;	//Separator

	//HSL -> RGB test
	cout << "HSL to RGB conversion:" << endl;
	cout << "\tHSL: \t\tH:" << hsl[0] << "\tS:" << hsl[1] << "\tL:" << hsl[2] << endl;
	cout << "\tRGB: \t\tR:" << hslrgb[0] << "\t\tG:" << hslrgb[1] << "\t\tB:" << hslrgb[2] << endl;

	cout << endl;	//Separator

	//RGB + RGB test
	cout << "RGB + RGB conversion:" << endl;
	cout << "\tRGB Front: \tR:" << rgb[0] << "\t\tG:" << rgb[1] << "\t\tB:" << rgb[2] << endl;
	cout << "\tRGB Back: \tR:" << rgbBack[0] << "\t\tG:" << rgbBack[1] << "\t\tB:" << rgbBack[2] << endl;
	cout << "\tTransparency: \t" << transparency << " (" << transparency * 100 << "%)" << endl;
	cout << "\tCombined RGB: \tR:" << transp[0] << "\t\tG:" << transp[1] << "\t\tB:" << transp[2] << endl;

	system("Pause");
	return 0;
}