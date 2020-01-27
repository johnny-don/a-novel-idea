A Novel Idea
This app/website is a memory bank for all those books you read and loved, read and hated or read and forgot all about. You can create, edit, review, delete reviews on all the countless books that you have read,
you can also see which books you loved and which books you didn't with out 'Top-Rated' function.
Furthermore you can contact the secondhand bookstore to offload those unwanted books that are cloggin up your living room and study. In the future we hope to connect our users and allow hem to trade books and reviews.



UX
I wanted to create a very straightforward UX for this project. The website is for the over 35 market. While most people around that age are tech-savvy, the older users will have no problem navigating website. 
The Headers are in a big font and the buttons are clearly displayed. There is no excess baggage or clutter. The website is extremely basic in its content and navigation. The user movies from once page to another 
via the menu links or the various buttons. 

The user wants to simply add a review to their database, they want to easily access this review and edit or delete it with the click of a button and also view which books they have rated the highest.
A Novel Idea provides all this functionality in an easy to use way. 

-- User Stories
- As an older user I want a way to store the novels that I have read, I don't want to read the same book twice
- As an avid reader, I would be curious as to which of the hundreds books I have read, what have I rated the highest.
- As a new reader I use an e-reader so I don't have physical copies of books, I would like a digital collection
- As an avid reader I have hundreds of books clogging up my house, I want to catalogue hem and them sell them onto a secondhand bookstore
- As a user I want to be able to edit and delete my reviews as my taste changes


Mock ups and wireframes are in a folder called 'wireframes'



Features

--Add a Review
Allows the user to add a book (title, author, genre, rating, review) to your collection
and save it for life


--Reviews
Allows the user to display all their reviews  


--Edit Review
The user can edit their reviews, change their rating or their comments


--Update Database
Once they click the edit button their collection will be updated

--Delete Review
The user can delete an unwanted book from their collection


--Top-Rated
The user can view which books they have rated the highest and lowest


--Link to Secondhand Bookstore
Connect with a secondhand bookstore to offload your books

FEATURES LEFT TO IMPLEMENT

-I would like to add a search feature which would allows users to search for specific titles in their collection

-I will add a function where the user can interact with other users, allowing them to exchange opinions on different books and also 
trade books between them.

-I think that the layout of the website has space for future advertising or links next to each book to their amazon page


TECHNOLOGIES USED

--HTML5

--CSS
Used to design the website and over-ride some materializecss.com stylings
--JQUERY
Used to add functionality from the Materializecss.com framework
--PYTHON
Used to for the back-end functionailty, to connect with MongoDB and manipulate the database
--MONGODB
Used to store hte data
--FLASK

--HEROKU
Used to host the app

TESTING

--Add Review
Go to the home page, fill in the form (title, author, genre, rating, review) and click the submit button.
You should be redirected to the Reviews page and your new review should be displayed.

--Reviews
Go to the Reviews page. All your reviews should be displayed along with the title, author, genre and rating.
Click th edit button to redirect to the Edit page. Click the Delete button to remove the book from the reviews table.

--Edit Review
The edit page will have a similar display to the add review page but the books data will be displayed in the appropraite fields
You can change the information and press the edit button. The database will be updated and you will be redirected to the reviews page where the changes
will be displayed

--Delete Review
When you press the delete button on the reviews page the book will be deleted from the database, the page will refresh and the deleted book will no longer be 
displaed

--Top-Rated
Once you open this page your books will be displayed according to their rating, from highest to lowest.

--Sell Books
Multiple pages have an image slider. The final image contains a link to the secondhand bookstore website.


-More testing

I tested this website using DevTools to check if it was responsive and it functioned at different sizes. I also tested it on a Samsung J5, a Acer laptop, a 32" TV and a HP monitor.

In some display forms the arrow on the edit or submit button drops and isnt centered.

On my HP monitor there is a gray bar below the footer on the homepage.

When I add the endblock tag  to the top-rated page it gives me a jinja error. It seems to work without the endblock. I do not understand why this is happening.

In the add review page I have the input for the rating set to number but when it is submitted to my database it is recorded as a string. This then 
chnages the top-rated page.

DEPLOYMENT

This project was continually saved and committed to github and then pushed to heroku master. 
Heroku config VARS were entered before the project 
IP: 0.0.0.0
PORT: 5000

Website can be accessed locally through Heroku or github pages.

CREDITS

--Content
The book reviews were taken from wikipedia's list of top 100 books.
Google fonts were used for the fonts.
Material icons for the icons.
Materializecss.com for the design framework

Media
Pictures were taken from pexels.com 

Acknowledgements
I received inspiration for this project from the project ideas from Code Institute and the mini-project in the data centric development module.
Help on design and some technical problems was received from Russell, who is a software developer and a friend of mine from Liverpool.