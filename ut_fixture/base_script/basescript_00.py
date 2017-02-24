#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import sys

"""+++script_delimeter+++"""

def main(argv):
  print("\033[1;31m :x: BaseScript ;"+str(argv)+"\033[m\n");
  print(getScript_testfixture00_py())
  print(getScript_testfixture01_py())
  print(getScript_testfixture02_py())

  return ;
  
if __name__ == "__main__":
  main(sys.argv)
