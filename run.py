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
    doc = re.compile(r"\s*<div\s*class=\"list-docs-i\s*[\s\w\-]*\">\s*" +
                     "<div\s*class=\"title\".*>\s*<a\s*href=\"(.*)\".*>(.*)</a>\s*</div>([^<]*)" +
                     "\s*<(.*?)>", re.MULTILINE | re.DOTALL)
    #                 # "<div\s*class=\"reg\".*>(.*)</div>", re.DOTALL)

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

    for i in doc.finditer(main_part):
        print("="*80)
        for j in range(10):
            try:
                print(i.group(j))
            except IndexError:
                print("...")
            print("-" * 80)


if __name__ == "__main__":
    main()
