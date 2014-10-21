# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PostImage.image_preview'
        db.add_column(u'base_postimage', 'image_preview',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PostImage.image_preview'
        db.delete_column(u'base_postimage', 'image_preview')


    models = {
        u'base.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_desc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.DateField', [], {})
        },
        u'base.post': {
            'Meta': {'object_name': 'Post'},
            'body': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'json_path': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'post_type': ('django.db.models.fields.CharField', [], {'max_length': "'5'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'base.postimage': {
            'Meta': {'object_name': 'PostImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_preview': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Post']"})
        }
    }

    complete_apps = ['base']