#CHRISTOPHER M. CHURCH
#ASSISTANT PROFESSOR OF HISTORY
#UNIVERSITY OF NEVADA, RENO

urls = ["http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-0.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-1.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-2.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-3.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-4.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-5.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-6.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-7.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-8.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-9.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-a.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-b.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-c.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-d.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-e.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-f.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-g.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-h.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-i.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-j.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-k.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-l.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-m.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-n.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-o.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-other.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-p.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-pos.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-punctuation.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-q.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-r.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-s.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-t.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-u.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-v.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-w.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-x.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-y.gz",
"http://storage.googleapis.com/books/ngrams/books/googlebooks-fre-all-1gram-20120701-z.gz"]


import urllib2
for url in urls:
    dfile = urllib2.urlopen(url)
    output = open(url.split("/")[-1],'wb')
    output.write(dfile.read())
    output.close()