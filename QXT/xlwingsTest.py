import xlwings as xw
app=xw.App(visible=True,add_book=False)
wb=app.books.open('c:\\Users\Administrator\\Desktop\\新建 Microsoft Excel 工作表.xlsx')
lst=[[1],[2],[3]]
wb.sheets[0].range('A1').value = lst