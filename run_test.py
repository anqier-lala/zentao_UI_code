import os
import  time
import unittest
import HTMLTestRunner

current_path=os.path.dirname(__file__)
report_path=os.path.join(current_path,'report')

cases_path=os.path.join(current_path,'test_casees')
html_path=os.path.join(report_path,'report_s%.html'%time.strftime('%Y_%m_%d_%H_%M_%S'))

discover=unittest.defaultTestLoader.discover(start_dir=cases_path,
                                             pattern='*_case.py',
                                             top_level_dir=cases_path
                                                )

main_suit=unittest.TestSuite
main_suit.addTest(discover)

file=open(html_path,'wb')
html_runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                          title='调试自动化测试项目',
                                          description='先把框架调通')

html_runner.run(main_suit)
