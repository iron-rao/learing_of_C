
import sys
import re

# stopword="}"
# s=""
# for line in iter(input,stopword):
#     s=s+line+"\n"
#     if '}' in line:
#         # s= s+'}\n'
#         break 

s="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  x= !y;
    2:  z= !x;
    3:  if ( (x & y) | (! z) )
    4:      y= !y;
    5:      pass;
        fi
    6:  x=!y;
    7:  z=!z;
    8:  while ( ( x|y)&(a | z) )
    9:      a=!y;
    10:     y=!z;
        done
    11: return x;
    } 
""" 

class program():
    def __init__(self,str):
        self.str = str

    def getCFG(self):
        self.Main()
        print(self.an)

    def evaluate(self):
        self.Sp()
        self.ResetSp()
        self.FindVarible()
        self.FindValue()
        # self.NotVal()



    def FindVarible(self):
        loc_main = self.sp.index('main')
        # print('find main',self.sp.index('main'))
        VarSet = set(self.sp[0:loc_main])
        VarSet.remove('True')
        VarSet.remove('False')
        VarSet.remove(';')
        VarSet.remove('=')
        VarSet.remove('bool')
        # print('VarSet',VarSet)
        self.Varible = list(VarSet)
        print('Varible',self.Varible)
    def FindValue(self):
        self.Value = []
        for i in range(len(self.Varible)):
            self.Value.append ( self.sp[self.sp.index(self.Varible[i])+2])
        print('Value',self.Value)




        

    def Main(self):
        self.Sp()
        self.ResetSp()
        self.GetId()
        self.Find()
        self.Sort()
        self.SetM()
        self.Set()
        self.Transpose()
        
    
    def Sp(self):#split the string by Tokenize
        self.sp = []
        self.str = re.sub(';',' ; \n',self.str)
        self.str = re.sub('\sfi\s','\n fi \n',self.str)
        self.str = re.sub('\sdone\s','\n done \n',self.str)
        self.str = re.sub(': ',' : ',self.str)
        self.str = re.sub('{',' { \n',self.str)
        self.str = re.sub('\)',' ) \n',self.str)
        self.str = re.sub('\(',' ( \n',self.str)
        self.str = re.sub('\|',' | \n',self.str)
        self.str = re.sub('\&',' & \n',self.str)
        self.str = re.sub('\!',' ! \n',self.str)
        self.str = re.sub('\=',' = \n',self.str)
        self.str = self.str.split('\n')
        for i in range(len(self.str)):
            for j in range (len(self.str[i].split())):
                self.sp.append(self.str[i].split()[j])
        # print('self.sp :',self.sp)

    def ResetSp(self):# selete '' '\n' '\t''utf-8'
        num = self.sp.count('')
        for i in range(num):
            self.sp.remove('')
        num = self.sp.count('\n')
        for i in range(num):
            self.sp.remove('\n')
        num = self.sp.count('\t')
        for i in range(num):
            self.sp.remove('\t')
        # self.sp.remove('utf-8')
        print('self.sp after:',self.sp)#test
    def GetId(self):#get the id of each sentence
        self.id = []
        for i in range(len(self.sp)):
            if self.sp[i] == ':':
                self.id.append(self.sp[i-1])
        # print("self.id:",self.id)# test
    def Find(self):
        loc_1 = self.sp.index(':')-1
        num_1 =self.sp[loc_1]
        self.BacisBlock = []
        self.BacisBlock.append(num_1)
        self.FindIf()
        self.FindFi()
        self.FindWhile()
        self.FIndDone()
        # print("self.BB:",self.BacisBlock)# test

    def Index(self,num):
        id = self.id.index(num)
        return id
    def FindIf(self):
        for i in range(len(self.sp)):
            if self.sp[i] == 'if':
                num = self.sp[i-2]
                # print(num)
                # print(self.Index(num))
                self.BacisBlock.append(self.id[self.Index(num)+1])
                # print("if id:",self.id[self.Index(num)+1])# test
    def FindFi(self):
         for i in range(len(self.sp)):
            if self.sp[i] == 'fi':
                self.BacisBlock.append(self.sp[i+1])
    def FindWhile(self):
        for i in range(len(self.sp)):
            if self.sp[i] == 'while':
                num = self.sp[i-2]
                self.BacisBlock.append(self.id[self.Index(num)+1])
                self.BacisBlock.append(self.id[self.Index(num)])
    def FIndDone(self):
        for i in range(len(self.sp)):
            if self.sp[i] == 'done':
                self.BacisBlock.append(self.sp[i+1])
    def Sort(self):
        tem = self.BacisBlock
        an = []
        for ele in tem:
            if ele not in an:
                an.append(ele)                    
        # print (an)
        self.BacisBlock = an
        self.BacisBlock.sort()
        
        # print('self.BacisBlock after:',self.BacisBlock)

    def SetM(self):
        length = len(self.BacisBlock)
        self.m = [[0 for i in range(length)] for i in range(length)]

    def Set(self):
        self.SetIF()
        self.SetWhile()
        self.SetDone()
        for i in range(len(self.BacisBlock)):
            self.m[self.SetXY(self.BacisBlock[i],self.BacisBlock[i])[0]][self.SetXY(self.BacisBlock[i],self.BacisBlock[i])[1]]=0

        # print('m set',self.m)#test

    def SetXY(self,x,y):
        XSite = self.BacisBlock.index(str(x))
        YSite = self.BacisBlock.index(str(y))
        return [XSite,YSite]

    def Set1(self,loc_now):
        # print('LOC_NUM in set1',self.sp[loc_now])#test
        loc1 = self.sp.index(':')-1
        num_1 = self.sp[loc1]
        num_now = self.sp[loc_now]
        # print(num_1)
        self.m[self.SetXY(num_1,num_now)[0]][self.SetXY(num_1,num_now)[1]]=1
        return loc1

        # print('loc1:',self.sp[loc1])#test


    def FindBefore(self,loc_now):
        global loc_fi ,loc_done
        flag = 0
        loc_fi = -1
        loc_done = -1
        for m in range (loc_now):
            if self.sp[m] == 'fi':
                loc_fi = m+1
                flag = 1
            if self.sp[m] == 'done':
                loc_done = m+1
                flag = 1
        if flag == 0:
            # print("Do set1")#test
            return self.Set1(loc_now)
        else:
            if (loc_done<loc_fi or loc_done == -1):
                return loc_fi
            elif(loc_done>loc_fi or loc_fi == -1):
                return loc_done
            
                
    def SetIF(self):
        for i in range(len(self.sp)):
            if self.sp[i] == 'if':
                If = self.sp[i::][self.sp[i::].index(':')-1]
                # print(self.sp[i::])#test
                # print('block after fi:',self.sp[i::][self.sp[i::].index('fi')+1])#test)
                Fi = self.sp[i::][self.sp[i::].index('fi')+1]
                self.m[self.SetXY(If,Fi)[0]][self.SetXY(If,Fi)[1]]=1
                # print("m if:",self.m)#test
                FindBefore = self.FindBefore(i+self.sp[i::].index(':')-1)
                # if (FindBefore != -1):
                FiBefore = self.sp[FindBefore]
                self.m[self.SetXY(FiBefore,Fi)[0]][self.SetXY(FiBefore,Fi)[1]]=1
                self.m[self.SetXY(FiBefore,If)[0]][self.SetXY(FiBefore,If)[1]]=1


    def SetWhile(self):
        for i in range(len(self.sp)):
            if self.sp[i] == 'while':
                W = self.sp[i-2]
                WD = self.sp[i::][self.sp[i::].index(':')-1]
                loc_WB = self.FindBefore(i-2)
                WB = self.sp[loc_WB]
                # print('WB',WB,'W',W ,'WD',WD)#test
                self.m[self.SetXY(W,WD)[0]][self.SetXY(W,WD)[1]]=1
                self.m[self.SetXY(WD,W)[0]][self.SetXY(WD,W)[1]]=1
                self.m[self.SetXY(WB,W)[0]][self.SetXY(WB,W)[1]]=1

    def SetDone(self):
            for i in range(len(self.sp)):
                if self.sp[i] == 'done':
                    loc_d = i+1
                    for n in range(i+1):
                        if self.sp[n] == 'while':
                            loc_while = n-2
                    num_d = self.sp[loc_d]
                    num_while = self.sp[loc_while]
                    # print('done',num_d,'while',num_while)
                    self.m[self.SetXY(num_while,num_d)[0]][self.SetXY(num_while,num_d)[1]]=1



    def Transpose(self):
        self.an='['
        # self.an="[\n"
        # print (len(self.m[0]))
        for i in range(len(self.m[0])):
            for j in range(len(self.m[0])):
                if (j == len(self.m[0])-1):   
                    if (i == len(self.m[0])-1 ):
                        self.an += (str(self.m[i][j])+']')
                    else:
                        self.an+=(str(self.m[i][j])+';')
                        # self.an+=(str(self.m[i][j])+";\n")
                else:
                    self.an+=(str(self.m[i][j])+',')

# if __name__ == '__main__':
#     s = ''
#     for line in sys.stdin:
#         s += line
#         if '}' in line:
#             break



p=program(s)
p.evaluate()
# print("[0,1,1,0,0;1,0,0,0,0;0,0,0,1,1;0,0,1,0,0;0,0,0,0,0]")
