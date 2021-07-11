from typing import List

def ext(file):
    if '.config' in file:
        temp = ['.config', '']
    temp = file.split('.')
    
    if temp[0] == "" and len(temp) == 2:
        temp = [''.join(temp[1:]), '']
    
    return temp[::-1]

def sort_by_ext(files: List[str]) -> List[str]:
    return sorted(files, key=ext)


if __name__ == '__main__':
    
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))
    
    # These are used for self-checking
    print( '\n',
        sort_by_ext(['1.cad', '1.bat', '1.aa']), '\n',
        #== ['1.aa', '1.bat', '1.cad']
        sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']), '\n',
        #== ['1.aa', '1.bat', '2.bat', '1.cad']
        sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']), '\n',
        #== ['.bat', '1.aa', '1.bat', '1.cad']
        sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']), '\n',
        #== ['.aa', '.bat', '1.bat', '1.cad']
        sort_by_ext(['1.cad', '1.', '1.aa']), '\n',
        #== ['1.', '1.aa', '1.cad']
        sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']), '\n',
        #== ['1.aa', '1.bat', '1.cad', '1.aa.doc']
        sort_by_ext(['1.cad', '1.bat', 'config.aa', '.aa.doc']))
        #== ['config.aa', '1.bat', '1.cad', '.aa.doc']
