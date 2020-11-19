from django.db import models
import re

class UserManager(models.Manager):
    def validate_user(self, postdata):
        email_check =re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postdata['f_name'])<2:
            errors['f_name']= 'First name must be at least 2 characters'
        if len(postdata['l_name'])<2:
            errors['l_name']= 'First name must be at least 2 characters'
        if not email_check.match(postdata['email']):
            errors['email'] = "Email must be valid format: x@y.zzz"
        if len(postdata['password'])<8:
            errors['password']='Password must be at least 8 characters'
        if postdata['password'] != postdata['conf_password']:
            errors['conf_password']='Password and confirm password must match'
        return errors


class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()

class QuoteManager(models.Manager):
    def valadator_quote(self, postdata):
        errors={}
        if len(postdata['quote']) < 10:
            errors['quote']='Quote must be 10 charaters long.'
        if len(postdata['author'])< 3:
            errors['author']='Author must be 3 charaters long.'
        return errors

class Quote(models.Model):
    author=models.TextField()
    quote= models.TextField()
    poster = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=QuoteManager()