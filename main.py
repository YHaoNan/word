import os
import re
import sys
import random
import colorama
from colorama import init,Fore,Back,Style
init(autoreset=True)


dict_list = []
current_list = []

word_token = re.compile(r'^\[(.*?)\]\s(.*?)$')
not_spell = False

def print_r(str):
    print('\033[31m%s\033[0m' % str)

def print_g(str):
    print('\033[32m%s\033[0m' % str)

def print_b(str):
    print('\033[34m%s\033[0m' % str)

def start_exec():
    while len(current_list)!=0:
        random.shuffle(current_list)
        item = current_list.pop()
        print('[remain: %d]'%(len(current_list)+1))
        if not_spell:
            print_b(item['word'] )
            yon = input('Enter to remove this word. Or type "n" to see mean：')
            if yon=='n':
                current_list.append(item)
                print_r(item['trans'])
            else:
                print_g(item['trans'])
        else:
            print(item['trans'])
            spell = input('Spell it: ')
            if item['word'] == spell:
                print_g('[+] Right!')
            else:
                print_r('[-] Wrong, is '+item['word'])
                current_list.append(item)

        print('\n')
    print_g('All words are learned!!!!')

def load_dict(idx):
    global not_spell
    current_list.clear()
    with open('./%s'%dict_list[idx],encoding='utf-8') as file:
        first_line = True
        for line in file:
            if first_line:
                if 'NOT SPELL' in line:
                    not_spell = True
                else:
                    not_spell = False
                first_line = False
                continue

            m = word_token.match(line)
            if m != None:
                current_list.append({'word': m.group(1),'trans': m.group(2)})
            else:
                print("NOT FOUNd")
            
        print('Load completed, %d words has found.'%len(current_list))

        start_exec()


def main():
    for root,dir,files in os.walk('.'):
        for file in files:
            if file.endswith('.dict'):
                dict_list.append(file)

    while True:
        print('Dict list: \n')
        for idx in range(len(dict_list)):
            print('[%d]. %s' % (idx,dict_list[idx]))
        dict_choose = int(input('\nChoose dict list: '))
        if dict_choose < 0 or dict_choose >= len(dict_list):
            sys.exit(0)
        else:
            load_dict(dict_choose)



if __name__ == '__main__':
    main()
