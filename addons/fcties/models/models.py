# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Alumno(models.Model):
    _name = 'mimodulo.alumno'
    _description = 'Modelo de Alumno'

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", required=True)
    curso_academico = fields.Char(string="Curso Académico", required=True)
    correo_electronico = fields.Char(string="Correo Electrónico")
    telefono = fields.Char(string="Telefono")
    ciclo_formativo = fields.Selection([('0', 'DAM'), ('1', 'DAW'), ('2', 'ASIR')], string='Ciclo Formativo', required=True)
    periodo_practica = fields.Selection([('0', 'Abril'), ('1', 'Septiembre')], string='Periodo de Práctica', required=True)
    nota_media = fields.Float(string="Nota Media", required=True)
    nota_media_texto = fields.Char(string="Nota Media en Texto", compute='_compute_nota_media_texto', store=True)

    @api.depends('nota_media')
    def _compute_nota_media_texto(self):
        for alumno in self:
            if 0 <= alumno.nota_media <= 5:
                alumno.nota_media_texto = "Insuficiente"
            elif 5 < alumno.nota_media <= 7:
                alumno.nota_media_texto = "Suficiente"
            elif 7 < alumno.nota_media <= 9:
                alumno.nota_media_texto = "Notable"
            elif 9 < alumno.nota_media <= 10:
                alumno.nota_media_texto = "Sobresaliente"
            else:
                alumno.nota_media_texto = "Sin Calificación"

class Empresa(models.Model):
    _name = 'mimodulo.empresa'
    _description = 'Modelo de Empresa'

    name = fields.Char(string="Nombre", required=True)
    persona_contacto = fields.Char(string="Persona de Contacto", required=True)
    telefono_contacto = fields.Char(string="Teléfono de Contacto", required=True)
    correo_electronico = fields.Char(string="Correo Electrónico", required=True)
    direccion = fields.Text(string="Dirección", required=True)

