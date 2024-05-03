from django.db import models
from django.urls import reverse

# Create your models here.

class Brand(models.Model):
    name = models.CharField(
        max_length = 200,
        unique = True,
        help_text = "Enter the name of the brand"
    )

class CPU(models.Model):
    name = models.CharField(
        max_length = 200,
        unique = True,
        help_text = "Enter the name of the CPU"
    )
    brand = models.ManyToManyField(
        Brand,
        help_text = "Choose the company that made this CPU"
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
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])


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
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

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
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])


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
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
