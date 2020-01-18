import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'novel_idea'
app.config["MONGO_URI"] = 'mongodb+srv://johnny_don:2gardensmon@cluster0-kzp63.mongodb.net/novel_idea?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')

    
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", reviews=mongo.db.info.find())
    
@app.route('/add_review')
def add_review():
    return render_template('addreview.html')
    
@app.route('/submit_review', methods=['POST'])
def submit_review():
    info = mongo.db.info
    info.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews')) 
    
@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = mongo.db.info.find_one({"_id": ObjectId(review_id)})
    return redirect('editreview.html', review=the_review)
    

@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
    reviews=mongo.db.info
    reviews.update( {'_id': ObjectId(review_id)},
    {
        'title':request.form.get('title'),
        'author':request.form.get('author'),
        'genre':request.form.get('genre'),
        'rating':request.form.get('rating'),
        'review':request.form.get('review')
    })
        
    return redirect(url_for('get_reviews'))
    
@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.info.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('get_reviews'))
    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)