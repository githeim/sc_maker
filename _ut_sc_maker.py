#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import unittest
import os
import imp
import filecmp

utFixture_Path='ut_fixture'
utFixture_basescriptPath='base_script'
utFixture_scriptfilePath='sc_file'

from sc_maker import *
class sc_maker_Common_Test(unittest.TestCase):
  def setUp(self):
    # setup ; change current dir
    return

  def tearDown(self):
    # teardown ; back to original dir
    return

  def test_FileNameChanger(self):
    self.assertEqual(FileNameChanger('test-ac.cpp'),'test_ac_cpp')
    self.assertEqual(FileNameChanger('testpy--d.py'),'testpy__d_py')

  def test_Make_Script(self):
    Make_Script('ut_fixture/generated_script.py',
        'ut_fixture/base_script/basescript_00.py',
        'ut_fixture/sc_file')


  def test_FileText2FuncScript(self):
    fixture_path =utFixture_Path+'/'+utFixture_scriptfilePath
    try :
      with open (fixture_path+'/testfixture00.py','r',errors='ignore') as f:
        filetext=f.read()
        testfixture00_txt =FileText2FuncScript(filetext,'testfixture00.py')
    except FileNotFoundError as e:
      self.fail('Check your test fixture-->'+str(e))

    # make file with testfixture output
    try :
      with open (fixture_path+'/test00_output.py','w',errors='ignore') as f:
        f.write(testfixture00_txt)
    except FileNotFoundError as e:
      self.fail('making file error-->'+str(e))
    if ( os.path.isfile(fixture_path+'/test00_output.py') == False ):
      self.fail('making file error-->'+str(fixture_path+'/test00_output.py'))

    # run the testfixture output script
    fp,pathname,description=imp.find_module('test00_output',[fixture_path])
    instance=imp.load_module('test00_output',fp,fixture_path,description)

    # write file with testfixture output script
    with open (fixture_path+'/test00_generated.py','w',errors='ignore') as f:
      f.write(instance.getScript_testfixture00_py())

    # compare the generated file with original file
    self.assertEqual(
    filecmp.cmp(fixture_path+'/test00_generated.py',
        fixture_path+'/testfixture00.py') , True)


    # clean up
    if (os.path.isfile(fixture_path+'/test00_output.py') == True):
      os.remove(fixture_path+'/test00_output.py')
    if (os.path.isfile(fixture_path+'/test00_generated.py') == True):
      os.remove(fixture_path+'/test00_generated.py')
    fp.close()

if __name__ == "__main__":
    unittest.main()


