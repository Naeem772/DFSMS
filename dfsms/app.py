from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, func
import datetime, hashlib
import random

from werkzeug import datastructures
app = Flask(__name__)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Wel_Come123@localhost/dfsms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class tbladmin(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    AdminName = db.Column(db.String(50))
    UserName = db.Column(db.String(50))
    MobileNumber = db.Column(db.String(50))
    Email = db.Column(db.String(50))
    Password = db.Column(db.String(50))
    AdminRegdate = db.Column(default=datetime.datetime.utcnow)
    UpdationDate = db.Column(default=datetime.datetime.utcnow)

class tblcategory(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    CategoryName = db.Column(db.String(200))
    CategoryCode = db.Column(db.String(50))
    PostingDate = db.Column(default=datetime.datetime.utcnow)

    def __init__(self, CategoryName, CategoryCode):
 
        self.CategoryName = CategoryName
        self.CategoryCode = CategoryCode
 
class tblcompany(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    CompanyName = db.Column(db.String(50))
    PostingDate = db.Column(default=datetime.datetime.utcnow)

    def __init__(self, CompanyName):
        self.CompanyName = CompanyName

class tblproducts(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    Category = db.Column(db.String(50))
    Company = db.Column(db.String(50))
    Product = db.Column(db.String(50))
    Pricing = db.Column(db.Integer)
    PostingDate = db.Column(default=datetime.datetime.utcnow)

    def __init__(self,Category,Company,Product,Pricing):
 
        self.Category = Category
        self.Company = Company
        self.Product = Product
        self.Pricing = Pricing

class tblproductstemp(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    Category = db.Column(db.String(50))
    Company = db.Column(db.String(50))
    Product = db.Column(db.String(50))
    Pricing = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    PostingDate = db.Column(default=datetime.datetime.utcnow)

    def __init__(self,Category,Company,Product,Pricing,quantity):
 
        self.Category = Category
        self.Company = Company
        self.Product = Product
        self.Pricing = Pricing
        self.quantity = quantity

class tblcustomers(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    orderID = db.Column(db.Integer)
    Name = db.Column(db.String(50))
    contact = db.Column(db.String(50))
    paymentMode = db.Column(db.String(50))
    postingDate = db.Column(default=datetime.datetime.utcnow)

    def __init__(self,orderID,Name,contact,paymentMode):
 
        self.orderID = orderID
        self.Name = Name
        self.contact = contact
        self.paymentMode = paymentMode
class tblorders(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    orderID = db.Column(db.Integer)
    productName = db.Column(db.String(50))
    category = db.Column(db.String(50))
    company = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    unitPrice = db.Column(db.Integer)
    postingDate = db.Column(default=datetime.datetime.utcnow)

    def __init__(self,orderID,productName,category,company,quantity,unitPrice):
 
        self.orderID = orderID
        self.productName = productName
        self.category = category
        self.company = company
        self.quantity = quantity
        self.unitPrice = unitPrice


@app.route("/login", methods=['GET','POST'])
def login():
    
    
        if "user" in session:
            return redirect(url_for("dashboard"))
        else:
            if request.method == "POST":
                user = request.form["username"]
                inputVar = request.form["password"]
                password = hashlib.md5()
                password.update(inputVar.encode("utf-8"))
                data = tbladmin.query.filter_by(UserName=user,Password=password.hexdigest()).first()
                if not data:
                    flash("Incorrect User and Password!") 
                    return redirect(url_for("login"))
                else:
                    session["user"] = user
                    return redirect(url_for("dashboard"))
            else:
                return render_template("index.html")
    

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/dashboard", methods=['GET'])
def dashboard():
    if "user" in session:
        countcategories = tblcategory.query.count()
        countcompanies = tblcompany.query.count()
        countproducts = tblproducts.query.count()
        today = datetime.datetime.now()
        DD7 = datetime.timedelta(days=7)
        DD1 = datetime.timedelta(days=1)
        DD0 = datetime.timedelta(hours = 24)
        earlier7days = today - DD7
        earlier1day = today - DD1
        earlier0day = today - DD0
        sales = db.session.execute('SELECT SUM(quantity*unitPrice) AS total_Sales FROM tblorders').scalar()
        last7days = db.session.execute("SELECT SUM(quantity*unitPrice) AS total_Sales FROM tblorders WHERE postingDate BETWEEN :from AND :to",{"from":earlier7days,"to":today}).scalar()
        yesterday = db.session.execute("SELECT SUM(quantity*unitPrice) AS total_Sales FROM tblorders WHERE postingDate LIKE '%':from'%'",{"from":earlier1day}).scalar()
        todaysales = db.session.execute("SELECT SUM(quantity*unitPrice) AS total_Sales FROM tblorders WHERE postingDate BETWEEN :from AND :to",{"from":earlier0day,"to":today}).scalar()
        return render_template("dashboard.html",countcategories = countcategories, countcompanies =countcompanies,
        countproducts = countproducts , sales = sales, last7days = last7days, yesterday = yesterday , todaysales = todaysales)
    else:
        return render_template("index.html")




@app.route("/addCategory", methods=['GET','POST'])
def addCategory():
    if "user" in session:
        if request.method == 'POST':
    
            Category = request.form['category']
            CategoryCode = request.form['categorycode']
        
    
    
            my_data = tblcategory(Category, CategoryCode)
            db.session.add(my_data)
            db.session.commit()
    
            flash("Category Added Successfully")
    
            return redirect(url_for('manageCategories'))
        else: 
            return render_template('add-category.html')
        
    else:
        return render_template("index.html")
    


@app.route("/editCategory/<id>/", methods=['GET'])
def editCategory(id):
    
    if "user" in session:
        Search_Category = tblcategory.query.get(id)
        return render_template("edit-category.html",Search_Category = Search_Category)
    else:
        return render_template("index.html")



@app.route('/updateCategory/<id>', methods = ['GET', 'POST'])
def updateCategory(id):
    if "user" in session:
        if request.method == 'POST':
            my_data = tblcategory.query.get(id)
    
            my_data.CategoryName = request.form['category']
            my_data.CategoryCode = request.form['categorycode']
    
            db.session.commit()
            flash("Category Updated Successfully")
    
            return redirect(url_for('manageCategories'))
    else:
        return render_template("index.html")
    
    


@app.route("/manageCategories", methods=['GET','POST'])
def manageCategories():
    if "user" in session:
        all_Category = tblcategory.query.all()
        return render_template("manage-categories.html", all_Category = all_Category)
    else:
        return render_template("index.html")
    




@app.route('/deleteCategory/<id>/', methods = ['GET', 'POST'])
def deleteCategory(id):
    my_data = tblcategory.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Category Deleted Successfully")
 
    return redirect(url_for('manageCategories'))



@app.route("/addCompany", methods=['GET','POST'])
def addCompany():
    if "user" in session:
        if request.method == 'POST':
    
            Company = request.form['companyname']
        
    
    
            my_data = tblcompany(Company)
            db.session.add(my_data)
            db.session.commit()
    
            flash("Company Added Successfully")
    
            return redirect(url_for('manageCompanies'))
        else: 
            return render_template('add-company.html')
        
    else:
        return render_template("index.html")    
    


@app.route("/editCompany/<id>", methods=['GET','POST'])
def editCompany(id):
    if "user" in session:
        Search_Company = tblcompany.query.get(id)
        return render_template("edit-company.html",Search_Company = Search_Company)
    else:
        return render_template("index.html")

@app.route('/updateCompany/<id>', methods = ['GET', 'POST'])
def updateCompany(id):
    if "user" in session:
        if request.method == "POST":
            my_data = tblcompany.query.get(id)
    
            my_data.CompanyName = request.form['companyname']
            
    
            db.session.commit()
            flash("Company Updated Successfully")
    
            return redirect(url_for('manageCompanies'))
    else:
        return render_template("index.html")

@app.route("/manageCompanies", methods=['GET','POST'])
def manageCompanies():
    if "user" in session:
        all_Category = tblcompany.query.all()
        return render_template("manage-companies.html", all_Category = all_Category)
    else:
        return render_template("index.html")

@app.route('/deleteCompany/<id>/', methods = ['GET', 'POST'])
def deleteCompany(id):
    my_data = tblcompany.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Company Deleted Successfully")
 
    return redirect(url_for('manageCompanies'))

@app.route("/addProduct", methods=['GET','POST'])
def addProduct():
    if "user" in session:
        if request.method == 'POST':
            Category = request.form['category']
            Company = request.form['company']
            Product = request.form['productname']
            Pricing = request.form['productprice']


            my_data = tblproducts(Category,Company,Product,Pricing)
            db.session.add(my_data)
            db.session.commit()

            flash("Product Added Successfully")

            return redirect(url_for('manageProducts'))
        else:
            all_Category = tblcategory.query.all() 
            all_Company = tblcompany.query.all() 
            return render_template('add-product.html',all_Company=all_Company,all_Category = all_Category)
    else:
        return render_template("index.html")

@app.route("/editProduct/<id>", methods=['GET','POST'])
def editProduct(id):
    if "user" in session:
        Search_Product = tblproducts.query.get(id)
        all_Category = tblcategory.query.all() 
        all_Company = tblcompany.query.all() 
        return render_template("edit-product.html",Search_Product = Search_Product,all_Company=all_Company,all_Category = all_Category)
    else:
        return render_template("index.html")

@app.route('/editProduct/updateProduct/<id>', methods = ['GET','POST'])
def updateProduct(id):
    if "user" in session:
        if request.method == "POST":
            my_data = tblproducts.query.get(id)
    
            my_data.Category = request.form['category']
            my_data.Company = request.form['company']
            my_data.Product = request.form['productname']
            my_data.Pricing = request.form['productprice']
    
            db.session.commit()
            flash("Company Updated Successfully")
    
            return redirect(url_for('manageProducts'))
    else:
        return render_template("index.html")

@app.route("/manageProducts", methods=['GET','POST'])
def manageProducts():
    if "user" in session:
        all_Category = tblproducts.query.all()
        return render_template("manage-products.html", all_Category = all_Category)
    else:
        return render_template("index.html")
@app.route("/deleteProduct/<id>", methods=['GET','POST'])
def deleteProduct(id):
    if "user" in session:
        checkout = tblproducts.query.get(id)
        db.session.delete(checkout)
        db.session.commit()
        flash("Product Deleted Successfully")
    
        return redirect(url_for('manageProducts'))
    else:
        return render_template("index.html")


@app.route("/searchProduct", methods=['GET','POST'])
def searchProduct():
    if "user" in session:
        
        return render_template("search-product.html")
    else:
        return render_template("index.html")

@app.route("/searchBuy", methods=['GET','POST'])
def searchBuy():
    if "user" in session:
        if request.method == "POST":
            product = request.form["productname"]
            Search_Product = tblproducts.query.filter(tblproducts.Product.like(product)).all()
            return render_template("search-product.html",Search_Product=Search_Product, show="false")
        else:
            return render_template("search-product.html")
    else:
        return render_template("index.html")
@app.route("/addToCart", methods=['GET','POST'])
def addToCart():
    if "user" in session:
        if request.method == "POST":
            id = request.form["cartid"]
            my_data = tblproducts.query.filter_by(id=id).first()
    
            Category = my_data.Category
            Company = my_data.Company
            Product = my_data.Product 
            Pricing= my_data.Pricing 
            quantity = request.form["quantity"]

            addCart = tblproductstemp(Category, Company, Product, Pricing, quantity)
            db.session.add(addCart)
            db.session.commit()
            flash("Added to Cart Successfully Please")
            return redirect(url_for('searchBuy'))
    
            
    else:
        return render_template("index.html")

@app.route("/checkout", methods=['GET','POST'])
def checkout():
    if "user" in session:
        checkout = tblproductstemp.query.all();
        total = 0
        for row in checkout:
            total = total + (row.Pricing * row.quantity)
        return render_template("checkout.html",checkout =checkout, total =total)    
    
            
    else:
        return render_template("index.html")

@app.route("/deleteCart/<id>", methods=['GET','POST'])
def deletecart(id):
    if "user" in session:
        checkout = tblproductstemp.query.get(id)
        db.session.delete(checkout)
        db.session.commit()
        flash("Deleted Successfully")
    
        return redirect(url_for('checkout'))
    else:
        return render_template("index.html")


@app.route("/purchase", methods=['GET','POST'])
def purchase():
    if "user" in session:
        if request.method == "POST":
            while True:
                rand = random.randint(10000000,99999999)
                data = tblcustomers.query.filter_by(orderID=rand).first()
                if not data:
                    name = request.form["customername"]
                    contact = request.form["mobileno"]
                    if name == "" and contact == "":
                        flash("Please enter Customer Name and Mobile Number")
                        return redirect(url_for('checkout'))
                    else:
                        paymentMode = request.form["paymentmode"]
                        addCart = tblcustomers(rand, name,contact, paymentMode)
                        db.session.add(addCart)
                        db.session.commit()
                        trans = tblproductstemp.query.all()
                        for row in trans:

                            addp =tblorders(rand, row.Product, row.Category, row.Company, row.quantity, row.Pricing) 
                            db.session.add(addp)
                            db.session.commit()
                        db.session.query(tblproductstemp).delete()
                        db.session.commit()
                        flash("You have Successfully parchased products")
                        return redirect(url_for('invoices'))
                        break
                    
                else:
                    pass
        else:
            return render_template("checkout.html")

    else:
        return render_template("index.html")

@app.route("/invoices", methods=['GET','POST'])
def invoices():
    if "user" in session:
        all_customers = tblcustomers.query.all()
        return render_template("invoices.html", all_customers = all_customers)
    else:
        return render_template("index.html")

@app.route("/invoice/<orderID>", methods=['GET','POST'])
def invoice(orderID):
    if "user" in session:
        customer = tblcustomers.query.filter_by(orderID = orderID).first()
        orders = tblorders.query.filter_by(orderID = orderID).all()
        total = 0 
        for rows in orders:
            total = total + (rows.quantity * rows.unitPrice)
        return render_template("invoice.html", orders = orders , customer = customer , total = total)
    else:
        return render_template("index.html")

@app.route("/bwdateReportDetails", methods=['GET','POST'])
def bwdateReportDetails():
    if "user" in session:
        if request.method == "POST":
            fromdate = request.form["fromdate"]
            todate = request.form["todate"]
            query = db.session.query(tblcustomers).filter(and_(func.date(tblcustomers.postingDate) >= fromdate),\
                                                (func.date(tblcustomers.postingDate) <= todate)).all()
            return render_template("bwdate-report-details.html", search = query , fromdate = fromdate, todate = todate )
        else:
            return render_template("bwdate-report-ds.html")
    else:
        return render_template("index.html")
    



@app.route("/bwdateReportDs", methods=['GET'])
def bwdateReportDs():
    return render_template("bwdate-report-ds.html")



@app.route("/changePassword", methods=['GET'])
def changePassword():
    return render_template("change-password.html")

@app.route("/updatepassword", methods=['GET','POST'])
def updatepassword():
    if "user" in session:
        data = tbladmin.query.filter_by(UserName=session.get('user')).first()
        cpass = request.form['currentpassword']
        cpassword = hashlib.md5()
        cpassword.update(cpass.encode("utf-8"))
        if cpassword.hexdigest() == data.Password:
            getpass = request.form['newpassword']
            password = hashlib.md5()
            password.update(getpass.encode("utf-8"))
            data.Password = password.hexdigest()
            db.session.commit()
            flash('Password successfully updated')
            return redirect(url_for('changePassword'))
        else:
            flash("Incorrect current password")
            return render_template('change-password.html', msg = "False")
            
    else:
        return render_template("index.html")

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")








@app.route("/profile", methods=['GET','POST'])
def profile():
    if "user" in session:
        data = tbladmin.query.filter_by(UserName=session.get('user')).first()
        return render_template("profile.html", data = data)
    else:
        return render_template("index.html")
@app.route("/updateprofile", methods=['GET','POST'])
def updateprofile():
    if "user" in session:
        data = tbladmin.query.filter_by(UserName=session.get('user')).first()
        
        data.AdminName = request.form['adminname']
        data.UserName = request.form['username']
        data.Email = request.form['emailid']
        data.MobileNumber =request.form['mobilenumber']

        db.session.commit()
        flash('profile successfully updated')
        return redirect(url_for('profile'))
    else:
        return render_template("index.html")



@app.route("/salesReportDetails", methods=['GET','POST'])
def salesReportDetails():
    return render_template("sales-report-details.html")


@app.route("/salesReportDs", methods=['GET','POST'])
def salesReportDs():
    return render_template("sales-report-ds.html")





@app.route("/viewInvoice", methods=['GET','POST'])
def viewInvoice():
    return render_template("view-invoice.html")

if __name__ == "__main__":
    app.run(debug=True) 
