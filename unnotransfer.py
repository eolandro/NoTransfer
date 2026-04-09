#!/usr/bin/env python3
import argparse
import hashlib
from pathlib import Path
CHUNK = 128

def getHash(Stream):
	bt = True
	while bt:
		bt = Stream.read(16)
		yield bt

def findByte(md5obj,hashbyte, bt):
	md5obj.update(bt)
	return md5obj if md5obj.digest() == hashbyte else False

def main():
	parser = argparse.ArgumentParser(
		description='(Un) No Transfer Data'
	)
	
	parser.add_argument(
		'NoTransfer2File', type=argparse.FileType('rb'),
		help='Origin File'
	)
	parser.add_argument(
		'file_output', type=str,
		help='Output File'
	)
	
	args = parser.parse_args()
	
	m = None
	# check if output exists
	fout = Path(args.file_output)
	hsout = None
	if not fout.exists():
		hsout = fout.open("wb")
		m = hashlib.md5()
	else:
		size = fout.stat().st_size
		hsout = fout.open("rb")
		m = hashlib.md5(hsout.read())
		hsout.close()
		hsout = fout.open("ab",buffering=0)
	
	
	gh = getHash(args.NoTransfer2File)
	Bts = [bytes([a]) for a in range(256)]
	outbt = b''
	btcounter = 0
	for hs in gh:
		R = None
		for bt in Bts:
			R = findByte(m.copy(),hs,bt)
			if R:
				m = R
				outbt = outbt + bt
				btcounter = btcounter + 1
				if btcounter == CHUNK:
					hsout.write(outbt)
					outbt = b''
					btcounter = 0
				break
	# si hay algo que no se haya guardado
	if btcounter != 0:
		hsout.write(outbt)
		
	args.NoTransfer2File.close()
	hsout.close()


if __name__ == '__main__':
	main()
