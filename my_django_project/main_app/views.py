from django.shortcuts import render
from main_app.models import Book


all_book_styles = [ 'Историческая', 'Военная', 'Научная фантастика', 'Художественная', 'Образование' ]
all_age_ristrictions = [ '6+', '12+', '16+', '18+' ]


#----------------------------------------------------------------------------------------------------
def home(request):
    return render(request, 'home.html')


#----------------------------------------------------------------------------------------------------
def add_book(request):    

    if (request.POST.get('save_book') != None):
        Book.objects.create(
            title           = request.POST.get('book_title'), 
            author          = request.POST.get('book_author'), 
            discription     = request.POST.get('book_discription'), 
            style           = ', '.join(request.POST.getlist('book_style[]')), 
            age_restriction = request.POST.get('book_age_restriction')
        )

    context = { 
        'all_book_styles' : all_book_styles, 
        'all_age_ristrictions' : all_age_ristrictions 
    }

    return render(request, 'add_book.html', context)


#----------------------------------------------------------------------------------------------------
def checking_style_book(selected_book_styles, book_styles):
    if selected_book_styles == [] or book_styles == []: 
        return True
    else:
        if len(selected_book_styles) > len(book_styles):
            return set(book_styles).issubset(selected_book_styles)
        elif len(book_styles) >= len(selected_book_styles):
            return set(selected_book_styles).issubset(book_styles)


#----------------------------------------------------------------------------------------------------
def checking_age_ristriction_book(selected_age_restriction, book_age_restriction):
    if selected_age_restriction == None or book_age_restriction == None:
        return True
    else:
        return selected_age_restriction == book_age_restriction


#----------------------------------------------------------------------------------------------------
def show_book_list(request):
    book_list = Book.objects.all()
    context = None

    if request.POST.get('apply_filters') == 'Применить':
        selected_book_styles = request.POST.getlist('book_style[]')
        selected_age_restriction = request.POST.get('book_age_restriction')
        book_id_set = set()

        for book in Book.objects.all():
            if checking_age_ristriction_book(selected_age_restriction, book.age_restriction) and checking_style_book(selected_book_styles, book.style.split(", ")):
                book_id_set.add(book.id)
        
        book_list = Book.objects.filter(id__in=book_id_set)

        context = { 
            'book_list' : book_list, 
            'all_book_styles' : all_book_styles, 
            'all_age_ristrictions' : all_age_ristrictions, 
            'selected_book_styles' : selected_book_styles, 
            'selected_age_restriction' : selected_age_restriction 
        }
    
    elif request.POST.get('apply_filters') == 'Сброс' or request.POST.get('apply_filters') == None:
        context = { 
            'book_list' : book_list, 
            'all_book_styles' : all_book_styles, 
            'all_age_ristrictions' : all_age_ristrictions
        }
    
    return render(request, 'book_list.html', context)


#----------------------------------------------------------------------------------------------------
def edit_book(request, book_id):
    book_for_edit = Book.objects.get(id=book_id)

    selected_book_styles = book_for_edit.style.split(", ")

    if request.POST.get('edit_book') != None:
        book_for_edit.title =           title =           request.POST.get('book_title')
        book_for_edit.author =          author =          request.POST.get('book_author') 
        book_for_edit.discription =     discription =     request.POST.get('book_discription')
        book_for_edit.style =           style =           ', '.join(request.POST.getlist('book_style[]'))
        book_for_edit.age_restriction = age_restriction = request.POST.get('book_age_restriction')

        Book.objects.filter(id=book_id).update(
            title=title, 
            author=author, 
            discription=discription, 
            style=style, 
            age_restriction=age_restriction
        )
        
        book_for_edit = Book.objects.get(id=book_id)
        
        selected_book_styles = book_for_edit.style.split(", ")

        context = { 
            'book_for_edit' : book_for_edit, 
            'all_book_styles' : all_book_styles, 
            'all_age_ristrictions' : all_age_ristrictions, 
            'selected_book_styles' : selected_book_styles 
        }

    return render(request, 'edit_book.html', context)


#----------------------------------------------------------------------------------------------------
def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete() 

    context = { 
        'book_list' : Book.objects.all(), 
        'all_book_styles' : all_book_styles, 
        'all_age_ristrictions' : all_age_ristrictions
    }

    return render(request, 'book_list.html', context)


