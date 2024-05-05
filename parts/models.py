from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Brand(models.Model):
    name = models.CharField(
        max_length = 200,
        unique = True,
        help_text = "Enter the name of the brand"
    )
    def __str__(self):
        return self.name

class CPU(models.Model):
    name = models.CharField(
        max_length = 200,
        unique = True,
        help_text = "Enter the name of the CPU"
    )
    brand = models.ManyToManyField(Brand,
        help_text = "Choose the company that made this CPU",
    )
    price = models.DecimalField(
        max_digits = 7,
        decimal_places = 2
    )
    rank = models.IntegerField(
        help_text = "Enter the rank of the CPU compared to other CPUs"
    )
    num_cores = models.IntegerField(
        help_text = "Enter the number of cores the CPU has"
    )
    core_speed = models.IntegerField(
        help_text = "Enter the speed of the cores in megahertz"
    )
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        return reverse('cpu-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.name}'

class GPU(models.Model):
    name = models.CharField(
        max_length = 200,
        unique = True,
        help_text = "Enter the name of the GPU"
    )
    brand = models.ManyToManyField(
        Brand,
        help_text = "Choose the company that made this GPU"
    )
    price = models.DecimalField(
        max_digits = 7,
        decimal_places = 2
    )
    rank = models.IntegerField(
        help_text = "Enter the rank of the GPU compared to other GPUs"
    )
    memory = models.IntegerField(
        help_text = "Enter the internal memory the GPU has"
    )
    core_speed = models.IntegerField(
        help_text = "Enter the speed of the cores in megahertz"
    )
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        return reverse('gpu-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.name}'

class Storage(models.Model):
    name = models.CharField(
        max_length = 200,
        unique = True,
        help_text = "Enter the name of the storage device"
    )
    brand = models.ManyToManyField(
        Brand,
        help_text = "Choose the company that made this storage device"
    )
    price = models.DecimalField(
        max_digits = 7,
        decimal_places = 2
    )
    rank = models.IntegerField(
        help_text = "Enter the rank of the storage device compared to other storage devices"
    )
    amount_of_space = models.IntegerField(
        help_text = "Enter the amount of space in gigabytes"
    )
    TYPE_CHOICES = (
        ("1", "HDD"),
        ("2", "SSD")
    )
    type = models.CharField(
        max_length = 3,
        choices = TYPE_CHOICES,
        help_text = ""
    )
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        return reverse('storage-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.name}'

class RAM(models.Model):
    name = models.CharField(
        max_length = 200,
        unique = True,
        help_text = "Enter the name of the RAM"
    )
    brand = models.ManyToManyField(
        Brand,
        help_text = "Choose the company that made this RAM"
    )
    price = models.DecimalField(
        max_digits = 7,
        decimal_places = 2
    )
    rank = models.IntegerField(
        help_text = "Enter the rank of the RAM compared to other RAM sticks"
    )
    TYPE_CHOICES = (
        ("1", "DDR1"),
        ("2", "DDR2"),
        ("3", "DDR3"),
        ("4", "DDR4")
    )
    DDR_type = models.CharField(
        max_length = 4,
        choices = TYPE_CHOICES,
        help_text = "Choose the type of DDR this RAM is"
    )
    amount = models.IntegerField(
        help_text = "Enter the amount of RAM one stick gives in gigabytes"
    )
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        return reverse('ram-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.name}'

class Build(models.Model):
    cpu = models.ForeignKey('CPU', on_delete=models.SET_NULL, null=True, blank=True)
    gpu = models.ForeignKey('GPU', on_delete=models.SET_NULL, null=True, blank=True)
    storage = models.ForeignKey('Storage', on_delete=models.SET_NULL, null=True, blank=True)
    ram = models.ForeignKey('RAM', on_delete=models.SET_NULL, null=True, blank=True)

    builder = models.ForeignKey(settings.AUTH_USER_MODEL, 
    on_delete=models.SET_NULL, null=True,)

    # Methods
    def get_absolute_url(self):
        return reverse('build-update', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.id}'
    
    def total_price(self):
        if(self.cpu == None):
            cpu_price = 0
        else:
            cpu_price = self.cpu.price
        
        if(self.gpu == None):
            gpu_price = 0
        else:
            gpu_price = self.gpu.price

        if(self.storage == None):
            storage_price = 0
        else:
            storage_price = self.storage.price

        if(self.ram == None):
            ram_price = 0
        else:
            ram_price = self.ram.price

        return cpu_price + gpu_price + storage_price + ram_price
