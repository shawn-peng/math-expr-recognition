#CXXFLAGS+=-g -I/usr/include/python2.7 -fPIC
CXXFLAGS+=-g -I/usr/include/python2.7 -fPIC

%.o : %.cpp
	gcc $(CXXFLAGS) -c $^ -o $@

segmentation.so: segment_graph_py.o egbis/libegbis.so
	gcc -shared $(CXXFLAGS) -lstdc++ $^ -o $@ -Legbis/ -legbis -lpython2.7 -lboost_python `pkg-config --libs opencv` -Wl,-rpath="./egbis/"

egbis/libegbis.so:
	make -C egbis

clean:
	rm -f *.o hello.so
