# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Audit.user'
        db.alter_column(u'tally_audit', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Archive.user'
        db.alter_column(u'tally_archive', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'QualityControl.user'
        db.alter_column(u'tally_qualitycontrol', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'UserProfile.tally'
        db.alter_column(u'tally_userprofile', 'tally_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['tally.Tally']))

        # Changing field 'ResultForm.created_user'
        db.alter_column(u'tally_resultform', 'created_user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['auth.User']))

        # Changing field 'ResultForm.user'
        db.alter_column(u'tally_resultform', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Clearance.user'
        db.alter_column(u'tally_clearance', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'ReconciliationForm.user'
        db.alter_column(u'tally_reconciliationform', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Result.user'
        db.alter_column(u'tally_result', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL))

    def backwards(self, orm):

        # Changing field 'Audit.user'
        db.alter_column(u'tally_audit', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']))

        # Changing field 'Archive.user'
        db.alter_column(u'tally_archive', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']))

        # Changing field 'QualityControl.user'
        db.alter_column(u'tally_qualitycontrol', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']))

        # Changing field 'UserProfile.tally'
        db.alter_column(u'tally_userprofile', 'tally_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['tally.Tally']))

        # Changing field 'ResultForm.created_user'
        db.alter_column(u'tally_resultform', 'created_user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'ResultForm.user'
        db.alter_column(u'tally_resultform', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'Clearance.user'
        db.alter_column(u'tally_clearance', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']))

        # Changing field 'ReconciliationForm.user'
        db.alter_column(u'tally_reconciliationform', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']))

        # Changing field 'Result.user'
        db.alter_column(u'tally_result', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tally.archive': {
            'Meta': {'object_name': 'Archive'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'result_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tally.ResultForm']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'tally.audit': {
            'Meta': {'object_name': 'Audit'},
            'action_prior_to_recommendation': ('django.db.models.fields.IntegerField', [], {'default': '4', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'blank_reconciliation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blank_results': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'damaged_form': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'for_superadmin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quarantine_checks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tally.QuarantineCheck']", 'symmetrical': 'False'}),
            'resolution_recommendation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'result_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tally.ResultForm']"}),
            'reviewed_supervisor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reviewed_team': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'audit_user'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'supervisor_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'team_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'unclear_figures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'tally.ballot': {
            'Meta': {'ordering': "['number']", 'object_name': 'Ballot'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'disable_reason': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'race_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'tally': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ballots'", 'null': 'True', 'to': "orm['tally.Tally']"})
        },
        'tally.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ballot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'candidates'", 'to': "orm['tally.Ballot']"}),
            'candidate_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'race_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'tally': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'candidates'", 'null': 'True', 'to': "orm['tally.Tally']"})
        },
        'tally.center': {
            'Meta': {'ordering': "['code']", 'unique_together': "(('code', 'tally'),)", 'object_name': 'Center'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'center_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'code': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'disable_reason': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'mahalla': ('django.db.models.fields.TextField', [], {}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tally.Office']", 'null': 'True'}),
            'region': ('django.db.models.fields.TextField', [], {}),
            'sub_constituency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'centers'", 'null': 'True', 'to': "orm['tally.SubConstituency']"}),
            'tally': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'centers'", 'null': 'True', 'to': "orm['tally.Tally']"}),
            'village': ('django.db.models.fields.TextField', [], {})
        },
        'tally.clearance': {
            'Meta': {'object_name': 'Clearance'},
            'action_prior_to_recommendation': ('django.db.models.fields.IntegerField', [], {'default': '4', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'center_code_mismatching': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'center_code_missing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'center_name_mismatching': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'center_name_missing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_supervisor_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_team_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'form_already_in_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'form_incorrectly_entered_into_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resolution_recommendation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'result_form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clearances'", 'to': "orm['tally.ResultForm']"}),
            'reviewed_supervisor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reviewed_team': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clearance_user'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'supervisor_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'team_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'tally.office': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'tally'),)", 'object_name': 'Office'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tally': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'offices'", 'null': 'True', 'to': "orm['tally.Tally']"})
        },
        'tally.qualitycontrol': {
            'Meta': {'object_name': 'QualityControl'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'passed_general': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'passed_reconciliation': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'passed_women': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'result_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tally.ResultForm']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'tally.quarantinecheck': {
            'Meta': {'object_name': 'QuarantineCheck'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'percentage': ('django.db.models.fields.FloatField', [], {'default': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'tally.reconciliationform': {
            'Meta': {'object_name': 'ReconciliationForm'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ballot_number_from': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'ballot_number_to': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entry_version': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_stamped': ('django.db.models.fields.BooleanField', [], {}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number_ballots_inside_and_outside_box': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_ballots_inside_box': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_ballots_outside_box': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_ballots_received': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_cancelled_ballots': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_invalid_votes': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_signatures_in_vr': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_sorted_and_counted': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_spoiled_ballots': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_unstamped_ballots': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_unused_ballots': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_valid_votes': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'result_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tally.ResultForm']"}),
            'signature_dated': ('django.db.models.fields.BooleanField', [], {}),
            'signature_polling_officer_1': ('django.db.models.fields.BooleanField', [], {}),
            'signature_polling_officer_2': ('django.db.models.fields.BooleanField', [], {}),
            'signature_polling_station_chair': ('django.db.models.fields.BooleanField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'tally.result': {
            'Meta': {'object_name': 'Result'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': "orm['tally.Candidate']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entry_version': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'result_form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': "orm['tally.ResultForm']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'tally.resultform': {
            'Meta': {'unique_together': "(('barcode', 'tally'), ('serial_number', 'tally'))", 'object_name': 'ResultForm'},
            'audited_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ballot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tally.Ballot']", 'null': 'True'}),
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'center': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tally.Center']", 'null': 'True', 'blank': 'True'}),
            'clearance_printed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_user'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['auth.User']"}),
            'date_seen': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'form_stamped': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'form_state': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intake_printed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_replacement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tally.Office']", 'null': 'True', 'blank': 'True'}),
            'rejected_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'serial_number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'skip_quarantine_checks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'station_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tally': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'result_forms'", 'null': 'True', 'to': "orm['tally.Tally']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'tally.station': {
            'Meta': {'object_name': 'Station'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'center': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stations'", 'to': "orm['tally.Center']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'disable_reason': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'percent_archived': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'percent_received': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'registrants': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'station_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sub_constituency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stations'", 'null': 'True', 'to': "orm['tally.SubConstituency']"})
        },
        'tally.subconstituency': {
            'Meta': {'object_name': 'SubConstituency'},
            'ballot_component': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sc_component'", 'null': 'True', 'to': "orm['tally.Ballot']"}),
            'ballot_general': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sc_general'", 'null': 'True', 'to': "orm['tally.Ballot']"}),
            'ballot_women': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sc_women'", 'null': 'True', 'to': "orm['tally.Ballot']"}),
            'code': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'field_office': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number_of_ballots': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'races': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'tally': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sub_constituencies'", 'null': 'True', 'to': "orm['tally.Tally']"})
        },
        'tally.tally': {
            'Meta': {'object_name': 'Tally'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'disable_reason': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'tally.userprofile': {
            'Meta': {'object_name': 'UserProfile', '_ormbases': [u'auth.User']},
            'administrated_tallies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'administrators'", 'default': 'None', 'to': "orm['tally.Tally']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'reset_password': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tally': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'users'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['tally.Tally']"}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['tally']