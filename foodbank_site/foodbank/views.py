# from django.http import HttpResponse
from django.shortcuts import render
from foodbank.models import Branch, BranchNeed
from django.db.models import Q
from .forms import SearchForm

def index(request):
     # Generate counts of some of the main objects
    num_branches = Branch.objects.all().count()
    num_branch_needs = BranchNeed.objects.all().count()
    branches_list = Branch.objects.all()
    branches_strs = []
    branches_needs = []
    for x in branches_list:
        branches_strs.append(str(x))
        all_needs = BranchNeed.objects.filter(branch_ID=x.branch_ID)
        this_needs = []
        for y in all_needs:
            this_needs.append(str(y))
        branches_needs.append(this_needs)
    
    # search by branch form
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            # redirect to a new URL:
            return render(request, 'search_results.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    context = {
        'num_branches': num_branches,
        'num_branch_needs': num_branch_needs,
        'branches_zip': zip(branches_strs, branches_needs),
        'form': form,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def search_results(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['branch_form']
            results = []
            branches_list = Branch.objects.all()
            for branch in branches_list:
                for word in search.split(): 
                    if (branch.address.upper() in word.upper()) or (branch.city.upper() in word.upper()) or \
                         (branch.province.upper() in word.upper()) or (branch.postal_code.upper() in word.upper()) or \
                            (word.upper() in branch.address.upper()) or (word.upper() in branch.city.upper()) or \
                                (word.upper() in branch.province.upper()) or (word.upper() in branch.postal_code.upper()):
                        results.append(str(branch))
                        break
                continue
            # redirect to a new URL:
            context = {
                'query': search,
                'results': results,
            }
            return render(request, 'search_results.html', context=context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    context = {
        'form': form,
    }
    return render(request, 'search_results.html', context = context)

def about(request):
    return render(request, 'about.html')