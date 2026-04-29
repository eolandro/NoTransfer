#!/usr/bin/env python3
import random
import argparse

def byte2sum(NA, N):
    if NA > N:
        return (NA,'-',(NA - N))
    if NA < N:
        return ((N - NA), '+',NA)
    if N == 0:
        return (1,'-',1)
    if NA == N:
        return (N - 1, '+',1)


def main():
        parser = argparse.ArgumentParser(
                description='No Transfer Data'
        )

        parser.add_argument(
                'file2NoTransfer', type=argparse.FileType('rb'),
                help='Origin File'
        )

        args = parser.parse_args()

        bt = True
        while bt:
                bt = args.file2NoTransfer.read(1)
                if not bt:
                    continue
                m = byte2sum(random.randint(0,255),bt[0])
                m = [ str(s) for s in m]
                m = ''.join(m)
                print(m)
        args.file2NoTransfer.close()


if __name__ == '__main__':
        main()

