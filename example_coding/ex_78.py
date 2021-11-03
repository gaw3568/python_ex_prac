tv_programs = ["산촌생활", "신서유기", "쇼미더머니", "지리산"]
for each_program in tv_programs:
    print(each_program)

favorite_program = input("Enter a program name : ")
favorite_indexing_location = int(input("Enter a location of index : "))
tv_programs.insert(favorite_indexing_location,favorite_program)

print(tv_programs)