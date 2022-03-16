# 开发人：彭协宇
# 开发时间 ：2022/3/6 14:19
import os

filename = 'student.txt'
def main():
    while True:
        input('按任意键继续：')
        menu()
        choice = int(input('请选择功能'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定退出系统吗？Y/N\n')
                if answer=='y' or answer=='Y':
                    print('谢谢你的使用！')
                    break #退出系统
                else:
                    continue
            elif choice==1:
                insert() #录入学生信息

            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()


def menu():
    print('====================学生管理系统====================')
    print('--------------------功能菜单--------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生的信息')
    print('\t\t\t\t\t0.退出')
    print('-----------------------------------------------')

def insert():
    student_list=[]
    while True:
        id=input('请输入ID(如1001):')
        if not id:
            break
        name=input('请输入姓名:')
        if not name:
            break

        try:
            english=int(input('请输入英语成绩:'))
            python=int(input('请输入python成绩:'))
            java=int(input('请输入java成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入！')
            continue
        #将录入的信息保存到字典当中
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加？y/n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break

    #调用save（）函数
    save(student_list)
    print('学生信息录入完毕！')

def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()


def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            model=input('按ID查找请输入1，按姓名查找请输入2：')
            if model == '1':
                id=input('请输入学生的ID:')
            elif model == '2':
                name=input('请输入学生的姓名:')
            else:
                print('您的输入有误，请重新输入：')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id != '':
                        if d['id']==id:
                            student_query.append(d)
                    elif name != '':
                        if d['name']==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否要继续查询？y/n\n')
            if answer=='y' or answer=='Y':
                continue
            else:
                break
        else:
            print('暂未保存该学生的信息。')
            return

def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生的信息，无数据显示！')
        return
    #定义标题显示格式
    # {:^10}中的^表示输出时右对齐，中的10表示输出宽度约束为10个字符；若宽度小于字符串的实际宽度，以实际宽度输出。
    # ^是居中的意思,^为居中对齐，后面的数字为总的字符数
    # {}占位符，：后面定义占有几个t的位置
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                 ))

def delete():
    while True:
        student_id=input('请输入要删除的学生的ID:')
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item)) #将字符串转换为字典
                        #eval()方法是将字符串的双引号或单引号去掉。
                        if d['id']!=student_id:
                            # 这句的意思是：重新写入数据，而唯独不写要删除的那一条。
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'ID为{student_id}的学生信息已经删除。')
                    else:
                        print(f'没有找到ID为{student_id}的学生的信息。')
            else:
                print('无此学生信息')
                break
            show()
            answer=input('是否继续删除操作？y/n\n')
            if answer=='y' or answer=='Y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改学员的ID：')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            #其实不用写dict，因为eval之后结果就是字典，不信可以自己试试
            if d['id']==student_id:
                print('找到学生的信息，可以进行修改。')
                while True:
                    try:
                        d['name'] = input('请输入姓名:')
                        d['english'] = int(input('请输入英语成绩:'))
                        d['python'] = int(input('请输入python成绩:'))
                        d['java'] = int(input('请输入java成绩:'))
                    except:
                        print('您的输入有误，请重新输入！')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功！')
            else:
                print(f'未找到ID为{student_id}的学生')
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改其他学生的信息？y/n\n')
        if answer=='y' or answer=='Y':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input('请选择（0：升序 1：降序):\n')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入！')
        sort()
    model=input('请选择排序方式（1：按照英语成绩排序 2：按照Python成绩排序  3：按照Java成绩排序    0：安按照总成绩排序）:\n')
    if model=='1':
        student_new.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool)
        #x['key']表示获取这些字典的对应键的值（这些字典是列表student_new中的元素）
        #x : x表示x是一个字典，这里x可以用任意字符代替
        #['英语']表示以字典x中的关键字为‘英语’的值来排序整个列表
        # x就相当于匿名函数的形参，
        # 并且传入形参的就是调用sort方法的student_new列表对象本身，然后x：后面就是匿名函数返回值。
    elif model=='2':
        student_new.sort(key=lambda x:int(x['python']),reverse=asc_or_desc_bool)
    elif model=='3':
        student_new.sort(key=lambda x:int(x['java']),reverse=asc_or_desc_bool)
    elif model=='0':
        student_new.sort(key=lambda x:int(x['english'])+int(x['python'])+int(x['java']),reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生的信息')
    else:
        print('暂未保存数据信息。。。')

def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存数据信息。。。')

if __name__=='__main__':
    main()