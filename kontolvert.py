import re
konter = 1
contents = open("isi.txt","r")
with open("copythis.html", "w") as e:
    for lines in contents.readlines():
        if re.match(r'#', lines):
            newlines = lines.replace(r'#', "")
            print("<div class='container' id='and" + str(konter) + "'>\n<h3 class='s-title'>"+ newlines + "</h3>\n")
            e.write("<div class='container' id='and" + str(konter) + "'>\n<h3 class='s-title'>"+ newlines + "</h3>\n")
        elif re.match(r'\s', lines):
            newlines = lines.replace(r'\s', "")
            print("<li>\n" + newlines + "</li>\n")
            e.write("<ul>\n<li>\n" + newlines + "</li>\n</ul>\n")
        elif re.match(r'\%', lines):
            newlines = lines.replace(r'%', "")
            print("<p>\n" + newlines + "</p>\n")
            e.write("<p>\n" + newlines + "</p>\n")
        elif re.match(r'#|$', lines):
            print("</div>\n")
            e.write("</div>\n")
        else:
            print(lines)
            e.write(lines)
