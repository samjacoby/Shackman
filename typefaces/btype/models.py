from django.db import models


class Typeface(models.Model):
    '''
    Describes a typeface along with its variants.
    '''
    def __unicode__(self):
        return self.name

    # All typefaces must have these.
    name = models.CharField(max_length=100)
    designer = models.CharField(max_length=100, blank=True)
    blurb = models.TextField(blank=True)
    # Blurb and such, should automatically be populated.
    # As should full alphabet display.

class Variant(models.Model):
    '''
    Describes a single (case, weight, etc.) variant of a single typeface.
    '''
    def __unicode__(self):
        return self.typeface.name + " " + self.get_case_display()

    CASE_CHOICES = (
            ('u', 'uppercase'),
            ('l', 'lowercase'),
    )
    typeface = models.ForeignKey(Typeface)
    case = models.CharField(max_length=1, choices=CASE_CHOICES)

    def locator_str(self):
        url_loc = self.typeface.name.lower().replace(' ', '-')
        return url_loc + '/' + url_loc
