from flask import render_template, Blueprint
from models.items import items

items_blueprint = Blueprint("items", __name__)


@items_blueprint.route("/items")  # when this is in url then return thefollwoing
def index():  # called index as it wil render the order of index
    return render_template("index.html", title="Pink Floyd Tennis", items=items) 

@items_blueprint.route("/items/<index>")  #code for viewing single order url/items/<index position of order>
def show(index):
    chosen_item = items[int(index)]  # as it extracted as a str it needs converting to Int

    return render_template("items.html", item=chosen_item)  #whatever item is aateched to chosen_order will be returned