import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'novel_idea'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


mongo = PyMongo(app)



@app.route('/')

    # This view retrieves the reviews from the database and displays them in the reviews.html page
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", reviews=mongo.db.info.find())
    
    
    # This page is where the users creates a review
@app.route('/add_review')
def add_review():
    return render_template('addreview.html')
    
    
    # This view activates on the click of the submit button, the review is added to the database and the user is redirected to the reviews.html
@app.route('/submit_review', methods=['POST'])
def submit_review():
    info = mongo.db.info
    info.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews')) 
    
    
    # This view retrieves the review info and displays it for editing
@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = mongo.db.info.find_one({"_id": ObjectId(review_id)})
    return render_template('editreview.html', review=the_review)
    

   # Updates the database with the new information and redirects to the reviews.html
@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
    reviews=mongo.db.info
    reviews.update( {'_id': ObjectId(review_id)},
    {
        'title':request.form.get('title'),
        'author':request.form.get('author'),
        'genre':request.form.get('genre'),
        'rating':int(request.form.get('rating')),
        'review':request.form.get('review')
    })
        
    return redirect(url_for('get_reviews'))
    
    
    # Deletes a record from the database
@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.info.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('get_reviews'))
    
    
    # sorts the reviews and displays them in a list
@app.route('/top_rated')
def top_rated():
    return render_template("toprated.html", ratings=mongo.db.info.find().sort("rating", -1))
    

    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)