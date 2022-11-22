class IterInt(int):
    def __iter__(self):
        for i in str(self):
            yield int(i)

    def __getitem__(self, index):
        res = str(self)[index]
        return int(res)
    
    def __len__(self):
        res = len(str(self))
        return res

    def __add__(self,other):
        new_num = super().__add__(other)
        return IterInt(new_num)

iter_num = IterInt(6748395)

# print(dir(int))
# for i in IterInt(1234567):
#     print((i*2))
#     # print(i)
# print(iter_num[1])  #7
# print(iter_num[1:3])  #74
# print(len(iter_num))

new_num = iter_num + 10
for i in new_num:
    print(i)
# print(new_num)