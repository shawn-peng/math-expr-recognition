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

void get_image(string filename)
{

}

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


dict segment(const string &filename, float sigma, float c, int min_size)
{
	int num_ccs;
	Mat img = imread(filename, CV_LOAD_IMAGE_COLOR);

	image<rgb> *natImage = convertMatToNativeImage(img);
	universe *u = segmentation(natImage, sigma, c, min_size, &num_ccs);

	dict forests;

	//for (int i = 0; i < num_ccs; i++)
	//{
	//	forests.append(list());
	//}
	cout << len(forests) << endl;

	for (int i = 0; i < img.rows; i++)
	{
		for (int j = 0; j < img.rows; j++)
		{
			int id = u->find(i*img.rows + j);
			//list p(forests[id]);
			//p.insert(0, make_tuple(i, j));
			cout << id << endl;
			//forests[id] = p;
			if (!forests.has_key(id))
			{
				forests[id] = list();
			}
			list tmp;
			tmp.append(make_tuple(i, j));
			forests[id] += tmp;
		}
	}
	return forests;
}

char const * print_str(const string &str)
{
	//printf(str.c_str());
	return str.c_str();
}

BOOST_PYTHON_MODULE(segmentation)
{
    using namespace boost::python;
    def("print_str", print_str);
    def("segment", segment);
}


//BOOST_PYTHON_MODULE(print_str)
//{
//    using namespace boost::python;
//    def("print_str", print_str);
//}


