import termplotlib as tpl
import numpy

while(True):
  numpy.random.seed(123)
  sample = numpy.random.normal(size=1000)
  counts, bin_edges = numpy.histogram(sample)

  fig = tpl.figure()
  fig.hist(counts, bin_edges, orientation="horizontal", force_ascii=False)
  fig.show()
