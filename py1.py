# coding=utf-8
import database
import xlwings as xw
#当中是你的程序
def main():
    msg = database.SQLServer(server="127.0.0.1", user="sa", password="houweikang123", database="QXT")
    result = msg.ExecQuery("select convert(date,[提交时间]), count(*) from [Tg] group by convert(date,[提交时间]) order by convert(date,[提交时间])")
    # app = xw.App(visible=True, add_book=False)
    # wb = app.books.open('c:\\Users\Administrator\\Desktop\\新建 Microsoft Excel 工作表.xlsx')
    wb = xw.Book('新建 Microsoft Excel 工作表.xlsx')
    wb.sheets[0].range(2, 1).value=result

if __name__ == '__main__':
    main()