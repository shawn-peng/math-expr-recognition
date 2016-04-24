#include <iostream>

#include <boost/python.hpp>

#include "egbis/image.h"
#include "egbis/misc.h"
#include "egbis/segment-graph.h"
#include "egbis/segment-image.h"

#include <string.h>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>


using namespace cv;

using namespace std;

using namespace boost::python;

// THE CODE BELOW THIS POINT WAS TAKEN FROM opencv-wrapper-egbis

image<rgb>* convertMatToNativeImage(const cv::Mat& input)
{
	int w = input.cols;
	int h = input.rows;
	image<rgb> *im = new image<rgb>(w,h);

	for(int i=0; i<h; i++)
	{
		for(int j=0; j<w; j++)
		{
			rgb curr;
			cv::Vec3b intensity = input.at<cv::Vec3b>(i,j);
			curr.b = intensity.val[0];
			curr.g = intensity.val[1];
			curr.r = intensity.val[2];
			im->data[i*w+j] = curr;
		}
	}
	return im;
}

// END CODE FROM opencv-wrapper-egbis

dict segment(const string &filename, float sigma, float c, int min_size)
{
	int num_ccs;
	Mat img = imread(filename, CV_LOAD_IMAGE_COLOR);

	image<rgb> *natImage = convertMatToNativeImage(img);
	universe *u = segmentation(natImage, sigma, c, min_size, &num_ccs);

	dict forests;

	for (int i = 0; i < img.rows; i++)
	{
		for (int j = 0; j < img.cols; j++)
		{
			int id = u->find(i*img.cols + j);
			if (!forests.has_key(id))
			{
				forests[id] = list();
			}
			list tmp;
			tmp.append(make_tuple(j, i));
			forests[id] += tmp;
		}
	}
	return forests;
}

char const * print_str(const string &str)
{
	return str.c_str();
}

BOOST_PYTHON_MODULE(segmentation)
{
    using namespace boost::python;
    def("print_str", print_str);
    def("segment", segment);
}


