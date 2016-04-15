CXXFLAGS+=-g -I/home/yang/miniconda2/include/python2.7 -fPIC

%.o : %.cpp
	gcc $(CXXFLAGS) -c $^ -o $@

hello.so: hello.o
	gcc -shared $(CXXFLAGS) -lstdc++ $^ -o $@ -lpython2.7 -lboost_python

clean:
	rm -f *.o hello.so
