#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import sys

def getScript_testfixture00_py() :
  return \
"""#!/usr/bin/python3
# -*- coding: utf-8 -*- 

def main(argv):
  print("\\033[1;31m :x: chk testfixture00 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;32m :x: chk testfixture00 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;33m :x: chk testfixture00 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;34m :x: chk testfixture00 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;35m :x: chk testfixture00 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;35m :x: chk testfixture00 ;"+str(argv)+"\\033[m\\n");
  return ;
  
if __name__ == "__main__":
  main(sys.argv)
"""
def getScript_testfixture02_py() :
  return \
"""#!/usr/bin/python3
# -*- coding: utf-8 -*- 

def main(argv):
  print("\\033[1;31m :x: chk testfixture02 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;32m :x: chk testfixture02 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;33m :x: chk testfixture02 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;34m :x: chk testfixture02 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;35m :x: chk testfixture02 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;35m :x: chk testfixture02 ;"+str(argv)+"\\033[m\\n");
  return ;
  
if __name__ == "__main__":
  main(sys.argv)
"""
def getScript_testfixture01_py() :
  return \
"""#!/usr/bin/python3
# -*- coding: utf-8 -*- 

def main(argv):
  print("\\033[1;31m :x: chk testfixture01 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;32m :x: chk testfixture01 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;33m :x: chk testfixture01 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;34m :x: chk testfixture01 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;35m :x: chk testfixture01 ;"+str(argv)+"\\033[m\\n");
  print("\\033[1;35m :x: chk testfixture01 ;"+str(argv)+"\\033[m\\n");
  return ;
  
if __name__ == "__main__":
  main(sys.argv)
"""


def main(argv):
  print("\033[1;31m :x: BaseScript ;"+str(argv)+"\033[m\n");
  print(getScript_testfixture00_py())
  print(getScript_testfixture01_py())
  print(getScript_testfixture02_py())

  return ;
  
if __name__ == "__main__":
  main(sys.argv)
