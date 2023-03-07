# -*- coding: utf-8 -*-

from odoo import models, fields

class Cliente(models.Model):
    _name = 'cliente.model'
    _description = 'Clientes del ejercicio'
    
    nombre = fields.Char(string = "Nombre",  required = True)
    direccion = fields.Char(string = "Direccion")
    ciudad = fields.Char(string = "Ciudad")
    estado = fields.Char(string = "Estado")
    codigo_postal = fields.Char(string = "Código Postal")
    pais = fields.Char(string = "Pais")
    facturas_id = fields.One2many(comodel_name = 'factura.model', inverse_name = 'cliente_id', string = "Factura", required = False)


class Factura(models.Model):
    _name = 'factura.model'
    _description = 'Factura del ejercicio'
    
    numero_factura = fields.Char(string = "Número Factura")
    fecha_emision = fields.Date(default = fields.Date.today(), string = "Fecha Emisión")
    fecha_vencimiento = fields.Date(string = "Fecha Vencimiento")
    monto_total = fields.Float(string = "Monto total")
    cliente_id = fields.Many2one(comodel_name = 'cliente.model', ondelete = 'set null', string = "Cliente", index = True)


class Producto(models.Model):
    _name = 'producto.model'
    _description = 'Producto del ejercicio'

    nombre = fields.Char(string = "Nombre")
    descripcion = fields.Text(string = "Descripcion")
    precio = fields.Float(string = "Precio")