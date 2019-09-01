from flask import Flask, render_template, url_for, request, redirect

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine


@app.route("/")
@app.route("/restaurants/<int:restaurant_id>")
def restaurantMenu(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template("menu.html", restaurant=restaurant, items=items)


@app.route("/restaurants/<int:restaurant_id>/new", methods=["GET", "POST"])
def newMenuItem(restaurant_id):
    if request.method == "POST":
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        newItem = MenuItem(name=request.form['name'],
                           description=request.form['description'],
                           price=request.form['price'],
                           restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    return render_template("newmenuitem.html", restaurant_id=restaurant_id)

@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/edit", methods=["GET", "POST"])
def editMenuItem(restaurant_id, menu_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    edititem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == "POST":
        edititem.name = request.form['name']
        session.add(edititem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    return render_template("editmenuitem.html", item=edititem, restaurant_id=restaurant_id, menu_id=menu_id)


@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/delete")
def deleteMenuItem(restaurant_id, menu_id):
    def deleteMenuItem(restaurant_id, menu_id):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        deleteitem = session.query(MenuItem).filter_by(id=menu_id).one()
        if request.method == "POST":
            session.delete(deleteitem)
            session.commit()
            return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
        return render_template("deletemenuitem.html", item=deleteitem, restaurant_id=restaurant_id, menu_id=menu_id)
# End of File #

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)