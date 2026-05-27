from html.parser import HTMLParser
path = 'c:\\Users\\Spencer Du\\Documents\\portfolio-website\\index.html'
with open(path, encoding='utf-8') as f:
    data = f.read()
class TagParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack=[]
        self.errors=[]
    def handle_starttag(self, tag, attrs):
        if tag in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'):
            return
        self.stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if not self.stack:
            self.errors.append((tag,'unexpected end', self.getpos()))
            return
        last = self.stack.pop()
        if last[0] != tag:
            self.errors.append((tag, 'mismatch '+last[0], self.getpos()))
parser = TagParser()
parser.feed(data)
print('errors', parser.errors)
print('stack len', len(parser.stack))
print('top tags', parser.stack[-10:])
