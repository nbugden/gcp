import webapp2
import urllib2
class HourCronPage(webapp2.RequestHandler):
    def get(self):
        request = urllib2.Request('<GCF URL>', headers={"cronrequest" : "true"})
        contents = urllib2.urlopen(request).read()
app = webapp2.WSGIApplication([
    ('/hour', HourCronPage),
    ], debug=True)