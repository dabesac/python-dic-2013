# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Boleta'
        db.create_table(u'ventas_boleta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('anulada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha_emision', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal(u'ventas', ['Boleta'])

        # Adding model 'Factura'
        db.create_table(u'ventas_factura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('anulada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha_emision', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal(u'ventas', ['Factura'])


    def backwards(self, orm):
        # Deleting model 'Boleta'
        db.delete_table(u'ventas_boleta')

        # Deleting model 'Factura'
        db.delete_table(u'ventas_factura')


    models = {
        u'clientes.cliente': {
            'Meta': {'unique_together': "(('documento', 'tipo_documento'),)", 'object_name': 'Cliente'},
            'documento': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tipo_documento': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tipo_persona': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'ventas.boleta': {
            'Meta': {'object_name': 'Boleta'},
            'anulada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'fecha_emision': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'ventas.factura': {
            'Meta': {'object_name': 'Factura'},
            'anulada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'fecha_emision': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['ventas']