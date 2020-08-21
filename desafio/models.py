"""
Código para criação das tabelas. Foi utilizado o ORM do django
para facilitar a tarefa.

django installation:

pip install django

Usage:
python manage.py makemigrations desafio
python manage.py migrate desafio

"""

from django.db import models


class Tabela_0000(models.Model):
    REG = models.CharField(max_length=4, null=False, blank=False)
    COD_VER = models.CharField(max_length=3, null=False, blank=False)
    TIPO_ESCRIT = models.CharField(max_length=1, null=False, blank=False)
    IND_SIT_ESP = models.CharField(max_length=1)
    NUM_REC_ANTERIOR = models.CharField(max_length=41)
    DT_INI = models.DateField(null=False, blank=False)
    DT_FIN = models.DateField(null=False, blank=False)
    NOME = models.CharField(max_length=100, null=False, blank=False)
    CNPJ = models.CharField(max_length=14, null=False, blank=False)
    UF = models.CharField(max_length=2, null=False, blank=False)
    COD_MUN = models.CharField(max_length=7, null=False, blank=False)
    SUFRAMA = models.CharField(max_length=9)
    IND_NAT_PJ = models.CharField(max_length=2)
    IND_ATIV = models.CharField(max_length=1, null=False, blank=False)
    # campo criado para cruzar regitros mensais
    DATA = models.DateField()

    def __str__(self):
        return self.REG


class Tabela_0140(models.Model):
    REG = models.CharField(max_length=4, null=False, blank=False)
    COD_EST = models.CharField(max_length=3, null=False, blank=False)
    NOME = models.CharField(max_length=100, null=False, blank=False)
    CNPJ = models.CharField(max_length=14, null=False, blank=False)
    UF = models.CharField(max_length=2, null=False, blank=False)
    IE = models.CharField(max_length=14)
    COD_MUN = models.CharField(max_length=7, null=False, blank=False)
    IM = models.CharField(max_length=255)
    SUFRAMA = models.CharField(max_length=9)
    # campo DATA criado para cruzar regitros mensais
    DATA = models.DateField()

    def __str__(self):
        return self.REG


class Tabela_0150(models.Model):
    REG = models.CharField(max_length=4, null=False, blank=False)
    COD_PART = models.CharField(max_length=60, null=False, blank=False)
    NOME = models.CharField(max_length=100, null=False, blank=False)
    COD_PAIS = models.CharField(max_length=5, null=False, blank=False)
    CNPJ = models.CharField(max_length=14)
    CPF = models.CharField(max_length=11)
    IE = models.CharField(max_length=14)
    COD_MUN = models.CharField(max_length=7)
    SUFRAMA = models.CharField(max_length=9)
    END = models.CharField(max_length=60)
    NUM = models.CharField(max_length=255)
    COMPL = models.CharField(max_length=60)
    BAIRRO = models.CharField(max_length=60)
    # campo DATA criado para cruzar regitros mensais
    DATA = models.DateField()

    def __str__(self):
        return self.REG


class Tabela_0200(models.Model):
    REG = models.CharField(max_length=4, null=False, blank=False)
    COD_ITEM = models.CharField(max_length=60, null=False, blank=False)
    DESCR_ITEM = models.CharField(
        max_length=255, null=False, blank=False)
    COD_BARRA = models.CharField(max_length=255)
    COD_ANT_ITEM = models.CharField(max_length=60)
    UNID_INV = models.CharField(max_length=6)
    TIPO_ITEM = models.CharField(max_length=2, null=False, blank=False)
    COD_NCM = models.CharField(max_length=8)
    EX_IPI = models.CharField(max_length=3)
    COD_GEN = models.CharField(max_length=2)
    COD_LIST = models.CharField(max_length=4)
    ALIQ_ICMS = models.CharField(max_length=6)
    # campo DATA criado para cruzar regitros mensais
    DATA = models.DateField()

    def __str__(self):
        return self.REG


class Tabela_C100(models.Model):
    REG = models.CharField(max_length=4, null=False, blank=False)
    IND_OPER = models.CharField(max_length=1, null=False, blank=False)
    IND_EMIT = models.CharField(
        max_length=1, null=False, blank=False)
    COD_PART = models.CharField(max_length=60, null=False, blank=False)
    COD_MOD = models.CharField(max_length=2, null=False, blank=False)
    COD_SIT = models.CharField(max_length=2, null=False, blank=False)
    SER = models.CharField(max_length=3)
    NUM_DOC = models.CharField(max_length=9, null=False, blank=False)
    CHV_NFE = models.CharField(max_length=44)
    DT_DOC = models.CharField(max_length=8, null=False, blank=False)
    DT_E_S = models.CharField(max_length=8)
    VL_DOC = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False)
    IND_PGTO = models.CharField(max_length=1, null=False, blank=False)
    VL_DESC = models.DecimalField(max_digits=9, decimal_places=2)
    VL_ABAT_NT = models.DecimalField(max_digits=9, decimal_places=2)
    VL_MERC = models.DecimalField(max_digits=9, decimal_places=2)
    IND_FRT = models.CharField(max_length=1, null=False, blank=False)
    VL_FRT = models.DecimalField(max_digits=9, decimal_places=2)
    VL_SEG = models.DecimalField(max_digits=9, decimal_places=2)
    VL_OUT_DA = models.DecimalField(max_digits=9, decimal_places=2)
    VL_BC_ICMS = models.DecimalField(max_digits=9, decimal_places=2)
    VL_ICMS = models.DecimalField(max_digits=9, decimal_places=2)
    VL_BC_ICMS_ST = models.DecimalField(max_digits=9, decimal_places=2)
    VL_ICMS_ST = models.DecimalField(max_digits=9, decimal_places=2)
    VL_IPI = models.DecimalField(max_digits=9, decimal_places=2)
    VL_PIS = models.DecimalField(max_digits=9, decimal_places=2)
    VL_COFINS = models.DecimalField(max_digits=9, decimal_places=2)
    VL_PIS_ST = models.DecimalField(max_digits=9, decimal_places=2)
    VL_COFINS_ST = models.DecimalField(max_digits=9, decimal_places=2)
    # campo DATA criado para cruzar regitros mensais
    DATA = models.DateField()

    def __str__(self):
        return self.REG


class Tabela_C170(models.Model):
    REG = models.CharField(max_length=4, null=False, blank=False)
    NUM_ITEM = models.CharField(max_length=3, null=False, blank=False)
    COD_ITEM = models.CharField(max_length=60, null=False, blank=False)
    DESCR_COMPL = models.CharField(max_length=255)
    QTD = models.DecimalField(max_digits=9, decimal_places=5)
    UNID = models.CharField(max_length=6)
    VL_ITEM = models.FloatField(null=False, blank=False)
    VL_DESC = models.DecimalField(max_digits=9, decimal_places=2)
    IND_MOV = models.CharField(max_length=1)
    CST_ICMS = models.CharField(max_length=3)
    CFOP = models.CharField(max_length=4, null=False, blank=False)
    COD_NAT = models.CharField(max_length=10)
    VL_BC_ICMS = models.DecimalField(
        max_digits=9, decimal_places=2)
    ALIQ_ICMS = models.DecimalField(
        max_digits=6, decimal_places=2)
    VL_ICMS = models.DecimalField(max_digits=9, decimal_places=2)
    VL_BC_ICMS_ST = models.DecimalField(max_digits=9, decimal_places=2)
    ALIQ_ST = models.DecimalField(max_digits=6, decimal_places=2)
    VL_ICMS_ST = models.DecimalField(max_digits=9, decimal_places=2)
    IND_APUR = models.CharField(max_length=1)
    CST_IPI = models.CharField(max_length=2)
    COD_ENQ = models.CharField(max_length=3)
    VL_BC_IPI = models.DecimalField(max_digits=9, decimal_places=2)
    ALIQ_IPI = models.DecimalField(max_digits=6, decimal_places=2)
    VL_IPI = models.DecimalField(max_digits=9, decimal_places=2)
    CST_PIS = models.CharField(max_length=2, null=False, blank=False)
    VL_BC_PIS = models.DecimalField(max_digits=9, decimal_places=2)
    ALIQ_PIS = models.DecimalField(max_digits=8, decimal_places=4)
    QUANT_BC_PIS = models.DecimalField(max_digits=9, decimal_places=3)
    ALIQ_PIS_QUANT = models.DecimalField(max_digits=9, decimal_places=4)
    VL_PIS = models.DecimalField(max_digits=9, decimal_places=2)
    CST_COFINS = models.CharField(max_length=2, null=False, blank=False)
    VL_BC_COFINS = models.DecimalField(max_digits=9, decimal_places=2)
    ALIQ_COFINS = models.DecimalField(max_digits=8, decimal_places=4)
    QUANT_BC_COFINS = models.DecimalField(max_digits=9, decimal_places=3)
    ALIQ_COFINS_QUANT = models.DecimalField(max_digits=9, decimal_places=4)
    VL_COFINS = models.DecimalField(max_digits=9, decimal_places=2)
    COD_CTA = models.CharField(max_length=255)
    # campo DATA criado para cruzar regitros mensais
    DATA = models.DateField()

    def __str__(self):
        return self.REG
