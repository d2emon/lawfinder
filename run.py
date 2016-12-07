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

    parts = body.split(content)
    main_part = parts[1]

    for s in content:
        print("--->\t" + s)

    for i in tag.finditer(content):
        print(i.group(0))

    print("="*80)
    print(main_part)


if __name__ == "__main__":
    main()
