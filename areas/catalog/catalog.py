import uuid
from flask import Blueprint, flash, redirect, request, render_template, session
from flask.ext.login import login_required
from areas.catalog.models.book import Book
from areas.catalog.models.forms import NewBookForm
import infrastructure

__author__ = 'carlozamagni'


catalog_app = Blueprint('catalog', __name__, static_folder='static', template_folder='templates')

login_manager = infrastructure.login_manager
admin = infrastructure.admin
db = infrastructure.db


@catalog_app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = NewBookForm()
    form.owner = session.get('user_id', None)

    if request.method == 'GET':
        return render_template('catalog/new.html', form=form)
    try:
        if form.validate_on_submit():
            flash('Success')
            book = Book()
            form.populate_obj(book)
            book.id = str(uuid.uuid4())  # workaround: duplication errors during item creation
            book.owner = session.get('user_id', None)
            book.save()

            return redirect('/catalog/my')
    except Exception, e:
        print str(e)

    return render_template('catalog/new.html', form=form)


@catalog_app.route('/my')
@catalog_app.route('/my/<page_id>')
def my_books_list(page_id=1):
    user_id = session.get('user_id', None)
    if user_id:
        paginated_books = Book.objects(owner=user_id).paginate(page=page_id, per_page=15)
        return render_template('catalog/my_list.html', books=paginated_books, user=session.get('user_name'))

    return redirect('user/login')


@catalog_app.route('details/<book_id>')
def book_details(book_id):
    book = Book.objects(id=book_id).first()
    if book:
        is_owner = book.owner == session.get('user_id', None)
        return render_template('catalog/details.html', book=book, is_owner=is_owner)

    return redirect('/catalog/my')

'''
@catalog_app.route('/search')
@catalog_app.route('/search/<page_id>')
def search(page_id=0):
    # search performed with GET request
    full_text_search_query = request.args.get('q')
    isbn_query = request.args.get('isbn')

    q_result = None
    if isbn_query:
        q_result = Book.objects(isbn=isbn_query).paginate(page=page_id, per_page=15)

    if not q_result and full_text_search_query:
        # TODO: full text query
'''