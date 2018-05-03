# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext as _

from utils import storage
from config import codes

class KYCInfo(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=200, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=200, verbose_name=_('Last Name'))
    cellphone = models.CharField(max_length=128, db_index=True, default='')
    country_code = models.CharField(max_length=4, db_index=True, default=settings.CHINA_COUNTRY_CALLING_CODE)
    id_number = models.CharField(max_length=200, verbose_name=_('ID Number'))
    id_card = models.ImageField(upload_to=storage.hashfile_upload_to('id_card', path_prefix='id_card'), verbose_name=_('ID Card'))
    emergency_contact_first_name = models.CharField(max_length=200, verbose_name=_('Emergency Contact First Name'))
    emergency_contact_last_name = models.CharField(max_length=200, verbose_name=_('Emergency Contact Last Name'))
    emergency_contact_cellphone = models.CharField(max_length=128, db_index=True, default='')
    emergency_contact_country_code = models.CharField(max_length=4, db_index=True, default=settings.CHINA_COUNTRY_CALLING_CODE)
    relationships_with_emergency_contacts = models.CharField(max_length=200)
    location = models.CharField(max_length=1000, verbose_name=_('Address'))
    how_to_contribute = models.TextField(verbose_name=_('Describe yourself & how you can help as a community member'))
    what_is_newton = models.TextField(verbose_name=_('Tell us your understanding about Newton'))
    # base fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=codes.TokenExchangeStatus.CANDIDATE.value, db_index=True)

class AddressTransaction(models.Model):
    user = models.ForeignKey(User)
    phase_id = models.IntegerField(default=codes.FundPhase.PRIVATE.value)
    txid = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128)
    address_type = models.IntegerField()    
    # base fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=codes.TokenExchangeStatus.CANDIDATE.value, db_index=True)
    
class KYCAudit(models.Model):
    user = models.ForeignKey(User)
    is_pass = models.BooleanField()
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=codes.TokenExchangeStatus.CANDIDATE.value, db_index=True)



class InvestInvite(models.Model):
    user = models.ForeignKey(User)
    phase_id = models.IntegerField()
    round_id = models.IntegerField(default=1)
    expect_btc = models.FloatField(blank=True, null=True, verbose_name=_('How much do you want to contribute in BTC'))
    expect_ela = models.FloatField(blank=True, null=True, verbose_name=_('How much do you want to contribute in ELA'))
    assign_btc = models.FloatField(blank=True, null=True)
    assign_ela = models.FloatField(blank=True, null=True)
    receive_btc_address = models.CharField(max_length=128, unique=True, blank=True, null=True)
    receive_ela_address = models.CharField(max_length=128, unique=True, blank=True, null=True)
    status = models.IntegerField(default=codes.TokenExchangeStatus.INVITE_AMOUNT.value, db_index=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
