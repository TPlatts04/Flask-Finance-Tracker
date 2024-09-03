from flask import render_template, request, redirect, url_for, flash
from finance_manager import app
from finance_manager.forms import userLogin, userCreate
from finance_manager.database import userInfo
from finance_manager import bcrypt, db

@app.route("/home")
@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/accounts", methods=["GET", "POST"])
def accounts():
    loginForm = userLogin()
    createForm = userCreate()
    if request.method == "POST":

        if request.form.get("login-form") == "login-confirm":
            # Get login information ----------------------------------
            loginUsername = request.form.get("loginUsername")
            loginPassword = request.form.get("loginPassword")
            found_user_login = userInfo.query.filter_by(username=loginUsername).first()

            # Login to account -------------------------------------
            if found_user_login:

                if bcrypt.check_password_hash(found_user_login.password, loginPassword):
                    flash(f"{loginUsername}, you have successfully logged in!")
                    return render_template("home.html")
                
                else:
                    flash("Invalid password, please try again")
                    return redirect(url_for("accounts"))
                
            else:
                flash("No user exists, please create an account")
                return redirect(url_for("accounts"))
            
            # Create Account ---------------------------------------
        elif request.form.get("create-form") == "create-confirm":
            # Get create account information --------------------------------
            createUsername = request.form.get("createUsername")
            createPassword = request.form.get("createPassword")
            found_user_create = userInfo.query.filter_by(username=createUsername).first()

            if found_user_create:
                flash(f"User already exists under the username {createUsername}")
                return redirect(url_for("accounts"))
            
            else:
                # Hash the password
                hashPassword = bcrypt.generate_password_hash(createPassword).decode('utf-8')
                # Add to database
                user = userInfo(createUsername, hashPassword)
                db.session.add(user)
                db.session.commit()
                flash(f"Account {createUsername} has been created!")
                return render_template("home.html")
            
        else:
            return render_template("accountPage.html", form=loginForm, createForm=createForm)
        
    else:
        return render_template("accountPage.html", form=loginForm, createForm=createForm)