#CXXFLAGS+=-g -I/usr/include/python2.7 -fPIC
CXXFLAGS+=-g -I/usr/include/python2.7 -fPIC

%.o : %.cpp
	gcc $(CXXFLAGS) -c $^ -o $@

segmentation.so: segment_graph_py.o egbis/libegbis.a
	gcc -shared $(CXXFLAGS) segment_graph_py.o egbis/libegbis.a -o $@ -lstdc++ \
		-lpython2.7 -lboost_python `pkg-config --libs opencv`

egbis/libegbis.a:
	make -C egbis/

clean:
	rm -f *.o hello.so
	make -C egbis/

remake:
	make clean && make

