#-*-coding:utf-8-*-
__author__ = 'howie'
import tornado.web
import tornado.escape
from handlers.base import BaseHandler

class UmMyNote(BaseHandler):

    @tornado.web.authenticated
    def get(self, *args, **kwargs):


        self.render("umMyNote.html")