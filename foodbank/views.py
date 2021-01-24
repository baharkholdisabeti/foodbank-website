# from django.http import HttpResponse
from django.shortcuts import render
from foodbank.models import Branch, BranchNeed, Need
from django.db.models import Q
from .forms import SearchForm
from .forms import FilterForm
from django.conf import settings

def index(request):
    branches_list = Branch.objects.all()
    # stores branch names
    branches_names = []
    # stores branch longitudes and latitudes
    branches_lng = []
    branches_lat = []
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
                add = True
                for branch in branches_list:
                    for word in query.split(): 
                        if ((branch.branch_info.upper() in word.upper()) or (word.upper() in branch.branch_info.upper())) \
                            or (branch.branch_name.upper() in word.upper()) or (word.upper() in branch.branch_name.upper()):
                            pass
                        else:
                            add = False
                    if add:
                        results.append(branch)
                    add = True
        elif 'reset' in request.POST:
            branches_list = Branch.objects.all()
            form = SearchForm()
            results = branches_list
        # filter by post request
        else:
            form = SearchForm()
            filterby = request.POST.get('filterby','')
            # check each branch need for the 'filterby' need and
            # adding that branch to result if found
            branches_needs = BranchNeed.objects.all()
            for need in branches_needs:
                if need.need == filterby:
                    results.append(need.branch_ID)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
        results = branches_list
    
    # find all needs
    for x in results:
        branches_names.append(str(x))
        branches_strs.append(x.branch_info)
        branches_lng.append(x.lng)
        branches_lat.append(x.lat)
        all_needs = BranchNeed.objects.filter(branch_ID=x.branch_ID)
        this_needs = []
        for y in all_needs:
            this_needs.append(str(y))
        branches_needs.append(this_needs)
    num_branches = len(results)
    num_branch_needs = len(branches_needs)

    # get a list of needs the user can filter by
    possible_needs = Need.objects.values_list('need_str', flat=True)

    context = {
        'possible_needs': possible_needs,
        'query': query,
        'num_branches': num_branches,
        'num_branch_needs': num_branch_needs,
        'branches_zip': zip(branches_names, branches_strs, branches_needs, branches_lng, branches_lat),
        'form': form,
        'maps_key': settings.GOOGLE_MAPS_API_KEY,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')