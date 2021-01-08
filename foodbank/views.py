# from django.http import HttpResponse
from django.shortcuts import render
from foodbank.models import Branch, BranchNeed
from django.db.models import Q
from .forms import SearchForm
from .forms import FilterForm

def index(request):
    branches_list = Branch.objects.all()
    # stores branch names
    branches_names = []
    # stores other branch info such as location, contact
    branches_strs = []
    branches_needs = []
    results = []
    query = False
    # search by branch form
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # check which form
        if 'search' in request.POST:
            if form.is_valid():
                query = form.cleaned_data['branch_form']
                branches_list = Branch.objects.all()
                for branch in branches_list:
                    for word in query.split(): 
                        if ((branch.branch_info.upper() in word.upper()) or (word.upper() in branch.branch_info.upper())) \
                            or (branch.branch_name.upper() in word.upper()) or (word.upper() in branch.branch_name.upper()):
                            results.append(branch)
                            break
                    continue
        elif 'reset' in request.POST:
            branches_list = Branch.objects.all()
            form = SearchForm()
            results = branches_list

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
        results = branches_list
    
    # find all needs
    for x in results:
            branches_names.append(str(x))
            branches_strs.append(x.branch_info)
            all_needs = BranchNeed.objects.filter(branch_ID=x.branch_ID)
            this_needs = []
            for y in all_needs:
                this_needs.append(str(y))
            branches_needs.append(this_needs)
    num_branches = len(results)
    num_branch_needs = len(branches_needs)

    context = {
        'query': query,
        'num_branches': num_branches,
        'num_branch_needs': num_branch_needs,
        'branches_zip': zip(branches_names, branches_strs, branches_needs),
        'form': form,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')