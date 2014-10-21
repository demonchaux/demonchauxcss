# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'base_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('body', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('json_path', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('image_path', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('post_type', self.gf('django.db.models.fields.CharField')(max_length='5')),
        ))
        db.send_create_signal(u'base', ['Post'])

        # Adding model 'PostImage'
        db.create_table(u'base_postimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Post'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'base', ['PostImage'])

        # Adding model 'Event'
        db.create_table(u'base_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateField')()),
            ('short_desc', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'base', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'base_post')

        # Deleting model 'PostImage'
        db.delete_table(u'base_postimage')

        # Deleting model 'Event'
        db.delete_table(u'base_event')


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
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Post']"})
        }
    }

    complete_apps = ['base']