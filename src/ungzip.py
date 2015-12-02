import glob
import gzip

path = '/Users/mitsueiwata/CAPP/bigdata/mpcs_bigdata/data/test_data/*.gz'

files = glob.glob(path)
for f in files:
	with gzip.open(f, 'rb') as fn:
		file_content = fn.read()
		print len(file_content)
