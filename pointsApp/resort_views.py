from django.shortcuts import render, redirect # this takes REQUEST as parm and either RENDERS or REDIRECTS
from pointsApp.forms import ResortsForm # import form to diplay
from pointsApp.models import Resorts   # import actual data to display in list and get rows as OBJECTS to process

# The home page calls this python function to work with members_form.html to display a form for ADDING or UPDATING Members 
# in the POSTGRES database 'craigpgdb' located in AWS into table 'pointsApp_members'
# 1) insert members
# The function 'members_form' is passed the HTTP REQUEST or either GET or POST
# If it is a INSERT then there is no PK set yet - it has a PK id =0
# If is is an update then already have a PK = 1...num rows in db (but not 0)

def resorts_form(request, id=0):      # have to give default of 0 because insert form has no value

  if id == 0:
    op_type = 'insert'
  else:
    op_type ='update'

  #print('id: ', id, ' ', op_type)
  #print('id {} so operation is {} and method is {}'.format(id,op_type, request.method))

  if request.method == "GET":

    if op_type == 'insert' :  #INSERT operation - display BLANK FORM
      resort_form = ResortsForm()

    else:  # UPDATE operation so step a) get the current member from db and display in FORM
      current_resort = Resorts.objects.get(pk=id)
      resort_form = ResortsForm(instance = current_resort)

    return render(request,"pointsAppDir/resorts_form.html",{'form':resort_form}) #return the FORM object

  else: #POST - so SUBMIT button hit

    if op_type == 'insert' : #INSERT OPERATION - actual POST value and SAVE the new record in DB
      resort_form = ResortsForm(request.POST)
    
    else:  # UPDATE operation so step b) the FORM already has the current DB resort displayed
           # but still have to load into variable again and then POST it, and then SAVE the updated record to DB              
      current_resort = Resorts.objects.get(pk=id)
      resort_form = ResortsForm(request.POST, instance = current_resort) #current resort record updated with form POST data

    # common to both INSERT and UPDATE operations
    if resort_form.is_valid():
      resort_form.save()  # save to database    
    
    return redirect('/pointsApp/resortlist') # call the LIST screen to show all resorts
    # Careful: redirect uses URL not HTML  


########################################################################################################################
# The LIST page calls this python function to work with database object to display ALL records from the database table
# 2) return a list of resorts and update
def resorts_list(request):
    resort_list = Resorts.objects.all()
    total_num_resorts = Resorts.objects.count()
    context = {'resort_list': resort_list}
    return render(request,"pointsAppDir/resorts_list.html",context)

########################################################################################################################
# The LIST page calls this python function to work with a specific database object to delete a Member from the database table
# 3) delete resorts 
def resorts_delete(request,id):
  current_resort = Resorts.objects.get(pk=id) 
  current_resort.delete()
  return redirect('/pointsApp/resortlist') # call the LIST screen to show all resorts and that this member DELETED
