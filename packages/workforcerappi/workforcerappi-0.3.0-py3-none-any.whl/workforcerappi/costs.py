import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def costs_webhelp(budget, SERVICE, budget_month):
    WEBHELP=budget[(budget["Aliado"]=="WEBHELP") & (budget["Mes"]==budget_month)].reset_index(drop=True)
    WEBHELP_CustomerLiveOrders=WEBHELP[WEBHELP["Servicio"]==str.upper(SERVICE)]
    costs_webhelp=WEBHELP_CustomerLiveOrders[['Aliado', 'Mes', 'Servicio', 'Año', '-', 'Tarifa USD','TIPO CONTRATO']]
    
    return costs_webhelp


def costs_brm(budget, SERVICE, budget_month):
 
    BRM=budget[(budget["Aliado"]=="BRM") & (budget["Mes"]=="Septiembre")].reset_index(drop=True)
    BRM_CustomerLiveOrders=BRM[BRM["Servicio"]==str.upper(SERVICE)]
    costs_brm = BRM_CustomerLiveOrders[['Aliado', 'Mes', 'Servicio', 'Año', '-', 'Tarifa USD','TIPO CONTRATO']]
    return costs_brm


def costs_aec(budget, SERVICE, budget_month):

    AEC=budget[(budget["Aliado"]=="AEC") & (budget["Mes"]=="Septiembre")].reset_index(drop=True)
    AEC_CustomerLiveOrders=AEC[AEC["Servicio"]==str.upper(SERVICE)]
    costs_aec = AEC_CustomerLiveOrders[['Aliado', 'Mes', 'Servicio', 'Año',  '-', 'Tarifa USD','TIPO CONTRATO']]

    return costs_aec