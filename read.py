import pyodbc
import os
import webbrowser


server = '322-a2.database.windows.net'
dbname = 'mapreduce'
user = 'shivam'
passWord = 'tayal@123'



conn  = pyodbc.connect(
        "Driver={SQL Server};Server=322-a2.database.windows.net,1433;",
        user=user,password=passWord,database=dbname
)


def readTextFile(fileName):
    resulting_list = []
    lineList = list()
    with open(fileName) as f:
      for line in f:
        lineList.append(line)
    lineList = [line.rstrip('\n') for line in open(fileName)]
    j=1
    for i in lineList:
        one_row = i.split("\t")
        resulting_list.append(one_row)
    return resulting_list



def query_mysql(query):
	cnx  = pyodbc.connect(
            "Driver={SQL Server};Server=322-a2.database.windows.net,1433;",
            user=user,password=passWord,database=dbname
    )
	cursor = cnx.cursor()
	cursor.execute(query)
	#get header and rows
	header = [i[0] for i in cursor.description]
	rows = [list(i) for i in cursor.fetchall()]
	#append header to rows
	rows.insert(0,header)
	cursor.close()
	cnx.close()
	return rows

#take list of lists as argument
def nlist_to_html(list2d):
	#bold header
	htable=u'<table border="1" bordercolor=000000 cellspacing="0" cellpadding="1" style="table-layout:fixed;vertical-align:bottom;font-size:13px;font-family:verdana,sans,sans-serif;border-collapse:collapse;border:1px solid rgb(130,130,130)" >'
	list2d[0] = [u'<b>' + i + u'</b>' for i in list2d[0]]
	for row in list2d:
		newrow = u'<tr>'
		newrow += u'<td align="cneter" style="padding:1px 4px">'+str(row[0])+u'</td>'
		row.remove(row[0])
		newrow = newrow + ''.join([u'<td align="right" style="padding:1px 4px">' + str(x) + u'</td>' for x in row])
		newrow += '</tr>'
		htable+= newrow
	htable += '</table>'
	return htable


def openInBrowser(fileName):
    new = 2 # open in a new tab, if possible

    # open an HTML file on my own (Windows) computer
    url =  os.path.join(current_working_directory,fileName)
    webbrowser.open(url,new=new)

def sql_html(query):
	return nlist_to_html(query_mysql(query))




#READ ALL TABLE
query = "select * from Data;"
html_str = sql_html(query)

htmlFile = "finalReport.html"

# save queury result in html file
Html_file= open(htmlFile,"w")
Html_file.write(html_str)
Html_file.close()


# Open in browser.
openInBrowser(htmlFile)




# deleteAllRows()
# data = readTextFile(data_file)
# for row in data:
#     insert(row)
# conn.commit()
