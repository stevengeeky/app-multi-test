#!/usr/bin/env python

def main():
	f = open("config.json")
	print(f.read())
	f.close()

main()