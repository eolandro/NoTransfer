#!/usr/bin/env python3
import random
import argparse

def byte2sum(NA, N):
    if NA > N:
        return (NA,'-',(NA - N))
    if NA < N:
        return ((N - NA), '+',NA)
    if NA == N:
        return (N - 1, '+',1)

#N = [ byte2sum(random.randint(0,255),a) for a in range(256) ]

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

        bt = True
        while bt:
                bt = args.file2NoTransfer.read(1)
                if not bt:
                    continue
                m = byte2sum(random.randint(0,255),bt[0])
                m = [ str(s) for s in m]
                m = ''.join(m).encode()
                args.file_output.write(m)
                args.file_output.write(b'\x0a')
        args.file2NoTransfer.close()
        args.file_output.close()


if __name__ == '__main__':
        main()

