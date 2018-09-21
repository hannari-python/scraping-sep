from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://pycon.jp/2018/event/sessions')
r.html.render(sleep=5)

sel = '.session-summary h3'
elems = r.html.find(sel)

print([i.text for i in elems])