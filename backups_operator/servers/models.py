import uuid

from cryptography.fernet import Fernet

# from django_celery_results.models import TaskResult

from django.conf import settings
from django.db import models
from django.db.models.enums import Choices

# Create your models here.


class AuthData(models.Model):
    METHOD_LIST = [
        ('pass', 'Password'),
        ('key', 'Private Key'),
    ]

    name = models.CharField(max_length=50)
    method = models.CharField(max_length=10, choices=METHOD_LIST, default='key')
    ssh_key = models.TextField(max_length=1000)
    ssh_key_passphrase = models.CharField(max_length=50, default=None, blank=True, null=True)

    # Decrypt Methods
    @property
    def name_decrypted(self):
        return self.name

    # Log Time
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(null=True)
    last_used = models.DateTimeField(null=True)


class Server(models.Model):
    name = models.CharField(max_length=30)
    active = models.BooleanField()
    uuid = models.UUIDField(default=uuid.uuid4)

    #
    # Connection Details
    #
    ssh_host = models.CharField(max_length=100)
    ssh_port = models.PositiveIntegerField()
    ssh_user = models.CharField(max_length=50)
    ssh_auth = models.ForeignKey(AuthData, on_delete=models.SET_NULL, blank=True, null=True)
    #


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('servers', args=[str(self.id)])

    class Meta:
        ordering = ["id"]
