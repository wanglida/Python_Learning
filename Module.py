#==模块，使用Python标准库的方法==

  #使用sys模块
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\nThe PYTHON PATH is', sys.path, '\n')

  #使用模块的__name__
if __name__=='__main__':
    print('This program is being run by itself.')
else:
    print('I am being imported from another module')
import PersonalModule
PersonalModule.firstMoudule()
print('Module Version=',PersonalModule.version)

print(dir(sys))   #列出模块定义的标识符

