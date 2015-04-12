# coding=utf-8
from django.shortcuts import render

# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
import datetime
from evernote_web import model
import random

def index(request):
    return HttpResponse('Hello world!')
def detail(request, user_id):
#     return HttpResponse('hello detail,{0}'.format(user_id))
    print user_id
    return notebooks(request)

def notebooks(request, user_id):
    now = datetime.datetime.now()
    books = []
    for i in range(0, 10):
        book = model.notebook()
        book.set_id(i)
        book.set_name('笔记本%d' % i)
        book.set_count(random.randint(10, 200))
        books.append(book)
    t = loader.get_template('evernote_web/index.html')
    c = Context({
                 'nodebookName':'wangjie',
                 'time':now,
                 'user_name':user_id,
                 'user_id':user_id,
                 'notebooks':books
    })
    return HttpResponse(t.render(c))
def notes(request, user_id, notebook_id):
    now = datetime.datetime.now()
    notes = []
    for i in range(0, 7):
        n = model.note()
        n.set_id(i)
        n.set_name('笔记%d' % i)
        notes.append(n)
    t = loader.get_template('evernote_web/notes.html')
    c = Context({
                 'notes':'heheh',
                 'time':now,
                 'notebook':notebook_id,
                 'notes':notes
    })
    return HttpResponse(t.render(c))

def note_detial(request, user_id, notebook_id, note_id):
    now = datetime.datetime.now()
    t = loader.get_template('evernote_web/notes.html')
    c = Context({
                 'notes':'hahah',
                 'time':now
    })
    return HttpResponse(t.render(c))

    

    
