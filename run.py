import pycurl
import cStringIO
import re


docs = 'http://sovminlnr.su/akty-soveta-ministrov/postanovleniya/'


def main():
    buf = cStringIO.StringIO()

    c = pycurl.Curl()
    c.setopt(c.URL, docs)
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()

    content = buf.getvalue()
    buf.close()

    body = re.compile(r"<\s*/?\s*body\s*>")
    tag = re.compile("<(.*)")
    # doc = re.compile(r"\s*<div class=\"list-docs-i?!>*>")
    doc = re.compile(r"<div\s*class=\"list-docs-*>")

    parts = body.split(content)
    main_part = parts[1].decode('cp1251').encode('utf8')
    doclist = doc.split(main_part)

    for s in content:
        print("--->\t" + s)

    for i in tag.finditer(content):
        print(i.group(0))

    print("="*80)
    print(main_part)

    print("="*80)
    for d in doclist:
        print(d)
        print('_' * 80)


if __name__ == "__main__":
    main()
