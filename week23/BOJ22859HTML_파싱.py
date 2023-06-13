html = input()

def div(html):
    if "</div>" not in html:
        result = "title : " + html[html.index('"')+1:html.rindex('"')]
        print(result)

def p(html):
    startIdx,endIdx = find(html)
    res = ''
    for i in range(1,len(startIdx)):
        start = startIdx[i]
        end = endIdx[i-1]
        res += html[end+1:start]

    result = ' '.join(res.split())
    print(result)

def start(html):
    startIdx,endIdx = find(html)
    ps,pe = 0,0
    for i in range(len(startIdx)):
        start = startIdx[i]
        end = endIdx[i]
        if "<div title=" in html[start:end+1]:
            div(html[start:end+1])
        if "</p>" in html[start:end+1]:
            pe = end
            p(html[ps:pe+1])
        if "<p>" in html[start:end+1]:
            ps = start

def find(html):
    startIdx = []
    endIdx = []
    for idx in range(len(html)):
        if html[idx] == "<":
            startIdx.append(idx)
        elif html[idx] == ">":
            endIdx.append(idx)
    return [startIdx,endIdx]

start(html)