import parser

#Construct HTML
def getHTML():
    results = parser.getAllHandles()
    html = ''
    for url in results:
        html += '<h3><a href="' + url  + '" target="_blank">'
        html +=  url + '</a></h3><ul>'
        for handle in results[url]:
            html += '<li>' + '<a href="https://twitter.com/'
            html += handle + '" target="_blank">'+ handle +'</a>' '</li>'
        html += '</ul><hr>'
    return html

#print (getHTML())