from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    
    #get username, cash, and portfolio
    username = db.execute("SELECT username FROM users WHERE id = :id",id=session["user_id"])[0]["username"]
    cash = db.execute("SELECT cash FROM users WHERE id = :id",id=session["user_id"])[0]["cash"]
    portfolio = db.execute("SELECT * FROM portfolio WHERE username = :username", username=username)
    
    #initialize total value of stocks as zero
    sum_of_stocks = 0
    
    #get info for each stock and add value for each stock
    for each in portfolio:
        stock_dat = lookup(each["stock"])
        each["price"] = usd(stock_dat["price"])
        each["name"] = stock_dat["name"]
        each["total"] = usd(stock_dat["price"] * each["shares"])
        sum_of_stocks += (stock_dat["price"] * each["shares"])
    
    # total money
    total = cash + sum_of_stocks
    
    return render_template("index.html", stocks=portfolio, cash=usd(cash), total=usd(total))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        
        # check both fields have valid inputs
        if not request.form.get("stock_symbol"):
            return apology("must input stock symbol")
        elif not request.form.get("shares") or int(request.form.get("shares")) <= 0:
            return apology("must input valid number of shares")
        
        # look up stock
        stock = lookup(request.form.get("stock_symbol"))
        
        # if stock exists, get cash and cost for buying requested shares
        if stock != None:
            cash = db.execute("SELECT cash FROM users WHERE id = :id",id=session["user_id"])[0]["cash"]
            shares = int(request.form.get("shares"))
            cost = shares * stock["price"]
            
            # check if user can buy shares
            if (cash >= cost):
                
                # get username, record tansaction, update cash, and insert or update database entries
                username = db.execute("SELECT username FROM users WHERE id = :id",id=session["user_id"])[0]["username"]
                db.execute("INSERT INTO transactions (username, stock, shares, cost, price, type) VALUES (:username, :stock, :shares, :cost, :price, :type)", username=username, stock = stock["symbol"], shares = shares, cost = cost, price = stock["price"], type="BUY")
                db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=(cash-cost),id=session["user_id"])
                if (len(db.execute("SELECT * FROM portfolio WHERE username = :username AND stock = :stock",username=username,stock=stock["symbol"])) != 1):
                    db.execute("INSERT INTO portfolio (username, stock, shares) VALUES (:username, :stock, :shares)",username=username,stock=stock["symbol"],shares=shares)
                else:
                    db.execute("UPDATE portfolio SET shares = shares + :shares WHERE username = :username AND stock = :stock",shares=shares,username=username,stock=stock["symbol"])
                return redirect(url_for("index"))
            else:
                return apology("not enough cash")
        else:
            return apology("stock invalid")
    
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    
    # get username and transactions, reverse for latest transactions first
    username = db.execute("SELECT username FROM users WHERE id = :id",id=session["user_id"])[0]["username"]
    transactions = db.execute("SELECT * FROM transactions WHERE username = :username", username=username)
    transactions.reverse()
    
    # stylize money
    for each in transactions:
        each["price"] = usd(each["price"])
        each["cost"] = usd(each["cost"])
    
    return render_template("history.html", stocks=transactions)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        
        # check if field is filled
        if not request.form.get("stock_symbol"):
            return apology("must input stock symbol")
        
        # look up
        stock = lookup(request.form.get("stock_symbol"))
        
        # if valid, print the information
        if stock != None:
            return render_template("quoted.html",symbol = stock["symbol"], name = stock["name"], price = usd(stock["price"]) )
        else:
            return apology("stock invalid")
    
    else:
        return render_template("quote.html")

@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """ Deposit more money """
    if request.method == "POST":
        
        # check if form is filled
        if not request.form.get("deposit"):
            return apology("must input amount")
        
        # get amount
        amount = int(request.form.get("deposit"))
        
        # add amount if valid
        if amount >= 0:
            db.execute("UPDATE users SET cash = cash + :amount WHERE id = :id",amount=amount,id=session["user_id"])
        else:
            return apology("amount invalid")
        
        return redirect(url_for("index"))
        
    else:
        return render_template("deposit.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        # check if all fields are filled
        if not request.form.get("username") or not request.form.get("password") or not request.form.get("confirm_password"):
            return apology("must fill out all fields")
        
        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        
        # check if username is taken
        if len(rows) > 0:
            return apology("username is taken")
        else:
            
            #check if passwords are the same and insert if so
            if request.form.get("password") == request.form.get("confirm_password"):
                db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=pwd_context.encrypt(request.form.get("password")))
                rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        
                # remember which user has logged in
                session["user_id"] = rows[0]["id"]

                # redirect user to home page
                return redirect(url_for("index"))
            else:
                return apology("passwords don't match")
        
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    
    if request.method == "POST":
        
        # check if fields have valid input
        if not request.form.get("stock_symbol"):
            return apology("must input stock symbol")
        elif not request.form.get("shares") or int(request.form.get("shares")) <= 0:
            return apology("must input valid number of shares")
        
        # get user name and check if they have shares
        username = db.execute("SELECT username FROM users WHERE id = :id",id=session["user_id"])[0]["username"]
        if (len(db.execute("SELECT shares FROM portfolio WHERE username = :username AND stock = :stock",username=username,stock=request.form.get("stock_symbol"))) != 1):
            return apology("stock invalid")
        max_shares = db.execute("SELECT shares FROM portfolio WHERE username = :username AND stock = :stock",username=username,stock=request.form.get("stock_symbol"))[0]["shares"]
        stock = lookup(request.form.get("stock_symbol"))
        shares = int(request.form.get("shares"))
        
        # check if trying to sell more shares than have
        if shares > max_shares:
            return apology("not enough shares")
        
        # if valid stock, sell the stocks and update
        if stock != None:
            cash = db.execute("SELECT cash FROM users WHERE id = :id",id=session["user_id"])[0]["cash"]
            cost = shares * stock["price"]
            db.execute("INSERT INTO transactions (username, stock, shares, cost, price, type) VALUES (:username, :stock, :shares, :cost, :price, :type)", username=username, stock = stock["symbol"], shares = shares, cost = cost, price = stock["price"], type="SELL")
            db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=(cash+cost),id=session["user_id"])
            if (shares == max_shares):
                db.execute("DELETE FROM portfolio WHERE username = :username AND stock = :stock AND shares = :shares",username=username,stock=stock["symbol"],shares=shares)
            else:
                db.execute("UPDATE portfolio SET shares = :shares WHERE username = :username AND stock = :stock",shares=(max_shares-shares),username=username,stock=stock["symbol"])
            return redirect(url_for("index"))
        else:
            return apology("stock invalid")
    
    else:
        return render_template("sell.html")

