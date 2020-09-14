# from django.http import HttpResponse
from django.shortcuts import render
from foodbank.models import Branch, BranchNeed

def index(request):
     # Generate counts of some of the main objects
    num_branches = Branch.objects.all().count()
    num_branch_needs = BranchNeed.objects.all().count()
    branches_list = Branch.objects.all()
    branches_strs = ""
    for x in branches_list:
        branches_strs+= '\n\n\n ' + str(x) + '\n\n'
        all_needs = BranchNeed.objects.filter(branch_ID=x.branch_ID)
        first = True
        for y in all_needs:
            if first:
                branches_strs+= "Needs: "
                branches_strs+= str(y)
                first = False
            else:
                branches_strs+= ', ' + str(y)
    
    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    # num_authors = Author.objects.count()
    
    context = {
        'num_branches': num_branches,
        'num_branch_needs': num_branch_needs,
        'branches_list': branches_strs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)