# -*- coding: utf-8 -*-

from odoo import models, fields

class lapeliculera_pelicula(models.Model):
    _name = 'lapeliculera.pelicula'
    _description = 'Pelicula'
    name = fields.Char(string="Titulo",required=True,help="Introduce el titulo de la pelicula")
    director = fields.Char(string="Director",required=True,help="Introduce el director")
    color = fields.Boolean(string="Color")
    duracion = fields.Integer(string="Duracion en minutos")
    industria = fields.Selection([('0','Hollywood'),('1','Europea'),('2','Bollywood'),('3','Otras')],default="1",string="Industria")
    fecha = fields.Date(string="Fecha de estreno en España")
    sinopsis = fields.Text(string="Sinopsis")

    genero = fields.Many2one("lapeliculera.genero",string="Género",required=True)

class lapeliculera_genero(models.Model):
    _name = 'lapeliculera.genero'
    _description = 'Género cinematográfico'
    name = fields.Char(string = "Género",requierd=True, help="Introduce el género cinematográfico")
    comentario = fields.Text(string="Comentarios")

    pelicula = fields.One2many("lapeliculera.pelicula","genero",string="Peliculas")


