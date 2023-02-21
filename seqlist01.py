# -*- coding: utf-8 -*-
# 作 者：uua
# 时 间：2023/2/16 9:07

class SL:
    #初始化
    def __init__(self, max):
        self.max = max
        self.index = 0
        self.data = [None for _ in range(self.max)]

    def empty(self):
        '''
        判断列表是否为空
        '''
        return self.index == 0

    def append(self,value):
        '''
        表尾插入元素
        value:待插入的元素
        return:顺序表已满的出口
        '''
        if self.index is self.max:
            return
        else:
            self.data[self.index] = value
            self.index +=1


    def Length(self):
        '''
        获取顺序表的长度
        :return:返回顺序表的元素个数
        '''
        return self.index

    def __getitem__(self, index):
        '''
        获取下标值为index的元素
        index:下标值
        '''
        if index < 0 or index >= self.index:
            raise IndexError('index非法')
        else:
            return self.data[index]

    def FindElement(self,value):
        if value in self.data:
            key_pos = self.data.index(value)

            print("查找成功,在顺序表中的索引为：%d" % key_pos)
            return key_pos
        else:
            print("查找失败，在顺序表中不存在这样的元素")




    def insert(self,index,value):
        '''
        在顺序标中任意位置插入元素
        index:待插入元素位置
        vaule:元素
        '''
        #若index非法,则抛出异常
        if index < 0 or index > self.index:
            raise IndexError('infex非法')
        #若index刚好为顺序表表尾
        if index == self.index:
            self.append(value)
        #通过for 将下标值为index及之后元素后移一位
        else:
            self.data += [value]
            for i in range(self.index,index,-1):
                self.data[i] = self.data[i-1]
            self.data[index] = value
            #修改长度
            self.index += 1

    def delete(self, index):
        '''
           任意位置删除
        :param
        index: 删除下标
        '''
        if index < 0 or index > + self.index:
            raise IndexError('index的值不合法')
        # 循环刪除后的元素往前移动
        for i in range(index, self.index):
            self.data[i] = self.data[i + 1]
        # 删除操作，长度减
        self.index -= 1

    def traversal(self):
        '''
        遍历顺序表
        111
        '''
        for i in range(self.index):
            print(self.data[i], end=' ')
        print()


if __name__=='__main__':
    #初始化顺序表
    SL=SL(10)

    #判断是否为空
    SL.empty()

    #添加元素
    list = [2,5,16,55,8]
    for i in list:
        SL.append(i)
    SL.traversal()

    #输出 SL 中元素的个数。
    print('SL 中元素的个数有:',SL.Length(),'个')

    #获取 SL 中元素 5 的位置
    print('获取 SL 中元素 5 的位置')
    SL.FindElement(5)

    #在元素 5 之后插入元素 11。
    print('在元素 5 之后插入元素 11。')
    index= int(SL.FindElement(5)+1)
    SL.insert(index,11)
    SL.traversal()


    #删除值为 16 的元素
    print('删除值为 16 的元素')
    SL.delete(SL.FindElement(16))
    SL.traversal()


    #将 SL 中元素依次输出。
    print('将 SL 中元素依次输出。')
    SL.traversal()


