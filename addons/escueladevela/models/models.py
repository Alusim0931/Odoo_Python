# -*- coding: utf-8 -*-

from odoo import models, fields

class escueladevela_cursos(models.Model):
    _name = 'escueladevela.curso'
    _description = 'Curso de la Escuela de Vela'

    title = fields.Char(string="Título", required=True, help="Introduce el título del curso")
    duration_days = fields.Integer(string="Duración en días")
    duration_hours = fields.Integer(string="Duración en horas")
    price = fields.Float(string="Precio")

class escueladevela_monitor(models.Model):
    _name = 'escueladevela.monitor'
    _description = 'Monitor de la Escuela de Vela'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del monitor")
    contact_info = fields.Char(string="Información de contacto")
    unique_id = fields.Char(string="Código de Identificación Único")
    school = fields.Many2one("escueladevela.escuela", string="Escuela(s) de Vela")

class escueladevela_alumno(models.Model):
    _name = 'escueladevela.alumno'
    _description = 'Alumno de la Escuela de Vela'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del alumno")
    contact_info = fields.Char(string="Información de contacto")
    enrollment_number = fields.Char(string="Número de Matrícula")

    school = fields.Many2one("escueladevela.escuela", string="Escuela de Vela")

class escueladevela_escuela(models.Model):
    _name = 'escueladevela.escuela'
    _description = 'Escuela de Vela'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre de la escuela de vela")
    logo = fields.Binary(string="Logotipo")
    address = fields.Text(string="Dirección")
    phone = fields.Char(string="Teléfono")
    email = fields.Char(string="Correo Electrónico")

    monitors = fields.Many2one("escueladevela.monitor", string="Monitores")
    students = fields.One2many("escueladevela.alumno", "school", string="Alumnos")

