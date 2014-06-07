# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User_Feed'
        db.delete_table(u'earthmiles_user_feed')

        # Adding model 'User_Post'
        db.create_table(u'earthmiles_user_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('feed_text', self.gf('django.db.models.fields.TextField')(max_length=3000)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['earthmiles.User'])),
            ('creation_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'earthmiles', ['User_Post'])

        # Adding field 'User.email'
        db.add_column(u'earthmiles_user', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='abc@gmail.com', max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'User_Feed'
        db.create_table(u'earthmiles_user_feed', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['earthmiles.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('feed_text', self.gf('django.db.models.fields.TextField')(max_length=3000)),
        ))
        db.send_create_signal(u'earthmiles', ['User_Feed'])

        # Deleting model 'User_Post'
        db.delete_table(u'earthmiles_user_post')

        # Deleting field 'User.email'
        db.delete_column(u'earthmiles_user', 'email')


    models = {
        u'earthmiles.user': {
            'Meta': {'object_name': 'User'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_log_in_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'earthmiles.user_post': {
            'Meta': {'object_name': 'User_Post'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feed_text': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['earthmiles.User']"})
        }
    }

    complete_apps = ['earthmiles']