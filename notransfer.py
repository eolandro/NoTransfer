#!/usr/bin/env python3
import argparse
import hashlib


def main():
	parser = argparse.ArgumentParser(
		description='No Transfer Data'
	)
	
	parser.add_argument(
		'file2NoTransfer', type=argparse.FileType('rb'),
		help='Origin File'
	)
	parser.add_argument(
		'file_output', type=argparse.FileType('wb'),
		help='Output File'
	)
	
	args = parser.parse_args()
	
	m = hashlib.md5()
	bt = True
	while bt:
		bt = args.file2NoTransfer.read(1)
		#print(bt)
		m.update(bt)
		args.file_output.write(m.digest())
	args.file2NoTransfer.close()
	args.file_output.close()


if __name__ == '__main__':
	main()
