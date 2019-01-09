import re
konter = 1
contents = open("isi.txt","r")
with open("copythis.html", "w") as e:
    for lines in contents.readlines():
        if re.match(r'#', lines):
            print("<div class='container' id='and" + str(konter) + "'>\n<h3 class='s-title'>"+ lines + "</h3>\n")
            e.write("<div class='container' id='and" + str(konter) + "'>\n<h3 class='s-title'>"+ lines + "</h3>\n")
            konter += 1
        elif re.match(r'\s', lines):
            print("<li>\n" + lines + "</li>\n")
            e.write("<ul>\n<li>\n" + lines + "</li>\n</ul>\n")
            konter += 1
        elif re.match(r'\%', lines):
            print("<p>\n" + lines + "</p>\n")
            e.write("<p>\n" + lines + "</p>\n")
            konter += 1
        elif (r'#|$', lines):
            print("</div>\n")
            e.write("</div>\n")
            konter += 1

