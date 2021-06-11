from main import load_dict


final_file = "final.dict"
compare_files = ['read_comp.dict','read_comp_2.dict']


current_list = []
def load_to_list(filename,list):
    list.clear()
    with open(filename,encoding='utf-8') as file:
        for line in file:
            list.append(line[:-1])


final_words = []
load_to_list(final_file,final_words)
# print(final_words)

for f in compare_files:
    load_to_list(f,current_list)
    for fw in final_words:
        for cl in current_list:
            if fw in cl:
                print(cl)
