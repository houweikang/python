import pprint

cats = [{'name':'1','desc':'2'},{'name':'3','desc':'4'}]
catsfomat = pprint.pformat(cats)
fileObj = open('myCats.py','w')
fileObj.write('cats=' + catsfomat + '\n')
fileObj.close()