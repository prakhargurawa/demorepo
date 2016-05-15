#!/Python27/python
import cgi,cgitb
cgitb.enable()
form = cgi.FieldStorage()
search_item = form.getvalue('search_item')
#from search_engine import crawl_web(seed)
#from search_engine import compute_ranks(graph)


print("Content-type: text/html \n\r\n\r")
print("<HTML>")
print("<HEAD>")
print("<TITLE>SAMPLE CGI PROGRAM</TITLE>")
print("</HEAD>")
#index, graph = crawl_web('https://udacity.com/cs101x/urank/index.html')
#ranks = compute_ranks(graph)
print("<BODY>")
print("Welcome to my first CGI program<br/><h2> Hello</h2>")
print "Searching item=",search_item
print ""
print "<a href=\"https://www.google.com\"></a>"
#print ordered_search(index, ranks, search_item)
#print(first_name,last_name)
print("</BODY>")
print("</HTML>")
