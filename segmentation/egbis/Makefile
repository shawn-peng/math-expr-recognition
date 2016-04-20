CXXFLAGS+=-g -fPIC

all: egbis libegbis.so libegbis.a

%.o : %.cpp
	g++ $(CXXFLAGS) -c $^ -o $@

egbis: disjoint-set.o misc.o segment-graph.o filter.o segment.o segment-image.o
	g++ $(CXXFLAGS) $^ -o $@ -lopencv_core

libegbis.so: disjoint-set.o misc.o segment-graph.o filter.o segment.o segment-image.o
	g++ -shared $(CXXFLAGS) $^ -o $@ -lopencv_core

libegbis.a: disjoint-set.o misc.o segment-graph.o filter.o segment.o segment-image.o
	rm -f $@
	ar rcs $@ $^

clean:
	rm *.o egbis -f
