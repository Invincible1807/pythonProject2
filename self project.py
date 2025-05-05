# import unittest
# def task1():
#     file=open("QA_Pairs.txt","r")
#     s=file.readlines()
#     print(s)
#     d=0
#     c=0
#     for i in range(len(s)):
#          if 'answer' in s[i]:
#             # k=s[i]
#              c+=1
#          if 'question' in s[i]:
#                 # l[s[i]]=k
#                 d+=1
#     (min(c,d))
# a=task1()
# class test(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(task1(),5728)
#
#
# if _name_ =="_main_":
#     unittest.main(exit=True)

# import unittest
#
# def task1():
#     file=open("QA_Pairs.txt","r")
#     s=file.readlines()
#     print(s)
#     d=0
#     c=0
#     for i in range(len(s)):
#          if 'answer' in s[i]:
#             # k=s[i]
#              c+=1
#          if 'question' in s[i]:
#                 # l[s[i]]=k
#                 d+=1
#     return (min(c,d))
#
# class test(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(task1(),5728)
#
#
# if _name_ == "_main_":
#     unittest.main(exit=True)

# import unittest
#
# def func_name():
#     file=open("a.txt","r")
#     f=file.readlines()
#     f1=(list(tuple(tuple(line.split()) for line in f)))
#    # print(f1)
#     #print("The original list is:"+str(f1))
#     res=list(set(f1))
#     #print("List after"+str(res))
#     #print("sorted",sorted(res))
#
# x="sorted [(), ('Answer1', 'abc'), ('Question', 'abcd'), ('answer', 'Rahul'), ('answer', 'town'), ('question', 'do', 'live', 'in', 'town', 'or', 'village'), ('question', 'what', 'is', 'your', 'name')]"
# class test(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(func_name(),x)
#
#
# # if _name=="_main":
#     unittest.main(exit=True)



# import unittest
#
# file=open("QA_Pairs.txt","r")
# s=file.readlines()
# f=open("Questions.txt","w")
# for i in range(len(s)):
#        if 'question' in s[i]:
#               f.write(str(s[i]))
# def t1():
#        f1=open("Questions.txt",'r')
#        s1=f1.readline()
# x="question Who is Arya Stark's wife"
# def t2():
#        f2=open("Questions.txt",'r')
#        s2 = f2.readlines()
#        a=s2[1]
#        return a
# y="Who escaped the persecution of House Stark"
#
# class test(unittest.TestCase):
#        def test1(self):
#               self.assertEqual(t1(),x)
#        def test2(self):
#               self.assertEqual(t2(),y)

################################################################################################################

# import unittest
# file=open("QA_Pairs.txt","r")
# s=file.readlines()
# f=open("Answers.txt","w")
# for i in range(len(s)):
#      if 'answer' in s[i]:
#               f.write(str(s[i]))
# def task51():
#        file=open("Answers.txt","r")
#        s1=file.readline()
# x='answer Lady Catelyn Stark'
# def task52():
#        file=open("Answers.txt",'r')
#        s2=file.readlines()
#        return s2[1]
# y='answer House Lannister'
#
# class test(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(task51(),x)
#     def test2(self):
#            self.assertEqual(taks52(),y)

################################################################################################################

import unittest

def t2():
       file = open("QA_Pairs.txt", "r")
       f = open("unique_QA_pairs.txt", 'w')
       f1 = open("Overlapping.txt", 'w')
       s = file.readlines()
       q = []
       a = []
       overlap = []
       duplicate = []
       id1 = []
       for i in range(len(s)):
              if 'answer ' in s[i]:
                     a.append(s[i])

              if "question " in s[i]:
                     q.append(s[i])

       # identical
       for i in range(len(q)):
              for j in range(1, len(q)):
                     if i == j:
                            continue
                     if q[i] == '' or a[i] == '':
                            continue
                     if q[i] == q[j]:
                            if a[i] == a[j]:
                                   id1.append((q[i], a[i]))
                                   q[i] = ""
                                   a[i] = ""

       # overlap

       for i in range(len(q)):
              for j in range(1, len(q)):
                     if i == j:
                            continue
                     if q[i] == '' or a[i] == '':
                            continue

                     if q[i] == q[j]:
                            if a[i] != a[j]:
                                   overlap.append((q[i], a[i]))
                                   q[i] = ""
                                   a[i] = ""

       # different

       for i in range(len(q)):
              for j in range(1, len(q)):
                     if i == j:
                            continue
                     if q[i] == '' or a[i] == '':
                            continue

                     if a[i] == a[j]:
                            if q[i] != q[j]:
                                   duplicate.append((q[i], a[i]))
                                   q[i] = ""
                                   a[i] = ""

       for i in id1:
              f1.write(str(i) + "\n")
       for j in overlap:
              f1.write(str(j) + "\n")
       for z in duplicate:
              f.write(str(z) + '\n')


t2()


def t21():
       file1 = open("Overlapping.txt", 'r')
       s1 = file1.readlines()
       return (s1[5:9])


x = '[ "("question What does Arya break down into after seeing that the queen\'s order will be carried out?\\n", \'answer tears\\n\')\n", "("question What bodyguard murdered Mycah?\\n","answer Hound\\n")\n", "("question Who admits that her children were fathered by her brother Jaime?\\n", "answer Cersei\\n")\n", "("question What is the name of the man who kills the King when he is hunting?\\n","answer boar\\n")\n"]'

def t22():
       file2 = open("unique_QA_Pairs.txt", 'r')
       s2 = file2.readlines()
       return (s2[10:15])


y = '["("question Who are Arya Stark\'s daughters?\\n", \'answer Lady Catelyn and Lord Ned Stark\\n\')\n", "("question Where was Arya born and raised?\\n", "answer Winterfell\\n")\n", "("question Who is Arya\'s bastard half-brother?\\n", \'answer Jon Snow\\n\')\n", "("question Who is Arya\'s older sister?\\n", \'answer Sansa\\n\')\n" , "("question Who rejects the notion that she must become a lady and marry for influence and power?\\n", "answer Arya\\n")\n"]'


class test(unittest.TestCase):
       def test1(self):
              self.assertEqual(t21(), x)

       def test2(self):
              self.assertEqual(t22(), y)