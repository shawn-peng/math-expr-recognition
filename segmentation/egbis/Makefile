CXXFLAGS+=-g

%.o : %.cpp
	g++ $(CXXFLAGS) -c $^ -o $@

egbis: disjoint-set.o misc.o segment-graph.o filter.o segment.o segment-image.o
	g++ $(CXXFLAGS) $^ -o $@ -lopencv_core

clean:
	rm *.o egbis -rf
