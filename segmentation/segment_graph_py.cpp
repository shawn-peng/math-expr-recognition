
#include <boost/python.hpp>

#include "egbis/segment_graph.h"

img * get_image(string filename)
{

}

void* segment(const string &filename, float sigma, float c, int min_size)
{
   return ;
}

BOOST_PYTHON_MODULE(get_image)
{
    using namespace boost::python;
    def("get_image", get_image);
}


