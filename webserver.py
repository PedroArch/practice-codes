from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Restaurants Main Page
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<a href='/restaurants/new'><h4>Make a new restaurant</h4></a></br></br>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    output += "<a href='/restaurants/%s/edit'>Edit</a>" % restaurant.id
                    output += "</br>"
                    output += "<a href='#'>Delete</a>"
                    output += "</br></br>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("restaurants/new"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h2>Make a new restaurant</h2></br></br>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>" \
                          "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name' >" \
                          "<input type='Submit' value='Create'></form>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                pass





        except IOError:
            error = self.path
            self.send_error(404, 'File Not Found: %s' % error)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    print messagecontent

                # Create a new restaurant
                newRestaurant = Restaurant(name=messagecontent[0])
                session.add(newRestaurant)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

            # self.send_response(301)
            # self.end_headers()
            #
            # ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
            # if ctype == 'multipart/form-data':
            #     fields = cgi.parse_multipart(self.rfile, pdict)
            #     messagecontent = fields.get('message')
            #
            #     output = ""
            #     output += "<html><body>"
            #     output += "<h2>Okay, how about this: </h2>"
            #     output += "<h1> %s </h1>" % messagecontent[0]
            #
            #     output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
            #               "<h2>What would you like me to say?</h2>" \
            #               "<input name='message' type='text'><input type='Submit'></form>"
            #     output += "</body></html>"
            #     self.wfile.write(output)
            #     print output

        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Webserver running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C entered, stopping webserver"
        server.socket.close()


# End of File #


if __name__ == '__main__':
    main()
