A python based snappy compress/decompress tool
Require:
	python-snappy
	OptParse

Usage:
	chmod +x snzip.py
	./snzip.py -c /path/to/your_file (The output is /path/to/your_file.snappy)
	./snzip.py -d /path/to/your_file (The output is /path/to/your_file.unsnappy, zlib compatible)
