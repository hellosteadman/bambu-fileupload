from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from bambu_attachments.models import Attachment

class FileUploadContext(models.Model):
    uuid = models.CharField(max_length = 36, unique = True)
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey('auth.User', related_name = 'file_upload_contexts')
    attachments = GenericRelation(Attachment)

    def __unicode__(self):
        return self.uuid

    class Meta:
        db_table = 'attachments_uploadcontext'
        ordering = ('-created',)
        get_latest_by = ('created',)
