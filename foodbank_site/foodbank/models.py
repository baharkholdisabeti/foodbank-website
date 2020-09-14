from django.db import models

"""
class MyModelName(models.Model):
                        A typical class defining a model, derived from the Model class.
    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...
    # Metadata
    class Meta: 
        ordering = ['-my_field_name']
    # Methods
    def get_absolute_url(self):
                        Returns the url to access a particular instance of MyModelName.
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
                        String for representing the MyModelName object (in Admin site etc.).
        return self.my_field_name """


class Branch(models.Model):
    # Fields
    branch_ID = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)

    # Metadata
    class Meta: 
        ordering = ['branch_ID'] # - before branchID does reverse ordering

    # Methods
    # Returns the url to access a particular instance of MyModelName
    #def get_absolute_url(self):
     #   return reverse('model-detail-view', args=[str(self.branchID)])
    
    def __str__(self):
        response = self.address + ", " + self.city + "\n" + self.postal_code + "\n" + self.phone_number + "\n" + self.email_address
        return response

class BranchNeed(models.Model):
    # Fields
    branch_ID = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True)
    need = models.ForeignKey('Need', on_delete=models.SET_NULL, null=True)

    # Metadata
    class Meta: 
        ordering = ['branch_ID'] # - before branchID does reverse ordering

    # Methods
    # Returns the url to access a particular instance of MyModelName
    #def get_absolute_url(self):
     #   return reverse('model-detail-view', args=[str(self.branchID)])
    
    def __str__(self):
        response = str(self.need)
        return response

class Need(models.Model):
    # Fields
    need_ID = models.IntegerField()
    need_str = models.CharField(max_length=200)

    # Metadata
    class Meta: 
        ordering = ['need_ID'] # - before branchID does reverse ordering

    # Methods
    # Returns the url to access a particular instance of MyModelName
    #def get_absolute_url(self):
     #   return reverse('model-detail-view', args=[str(self.needID)])
    
    def __str__(self):
        response = self.need_str
        return response