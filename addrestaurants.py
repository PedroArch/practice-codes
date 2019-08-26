#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# STARTING SESSION
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# ADD RESTAURANTS

# Mexican Restaurant
tacolibre = Restaurant(name="TACO LIBRE")
session.add(tacolibre)
session.commit()

nachoscalientes = MenuItem(name="Nachos Calientes",
                           course="Entrada",
                           description="Deliciosos nachos crocantes com diversos molhos",
                           price="$8.90",
                           restaurant=tacolibre)
session.add(nachoscalientes)
session.commit()

quesadillasardentes = MenuItem(name="Quesadillas Ardesntes",
                               course="Entrada",
                               description="Quesadillas feitas ao melhor molho picante Mexicano",
                               price="$9.90",
                               restaurant=tacolibre)
session.add(quesadillasardentes)
session.commit()

fajitascoloridas = MenuItem(name="Fajitas Coloridas",
                            course="Entrada",
                            description="Porcao de Fajitas com os mais coloridos vegetais",
                            price="$9.90",
                            restaurant=tacolibre)
session.add(fajitascoloridas)
session.commit()

chilipicante = MenuItem(name="Chili Picante",
                        course="Principal",
                        description="Chili picante um dos principais pratos Mexicanos",
                        price="$19.90",
                        restaurant=tacolibre)
session.add(chilipicante)
session.commit()

tacolibredish = MenuItem(name="Taco Libre Dish",
                         course="Principal",
                         description="Leva o name da casa nosso principal prato",
                         price="$18.90",
                         restaurant=tacolibre)
session.add(tacolibredish)
session.commit()

burritomanso = MenuItem(name="Burrito Manso",
                        course="Principal",
                        description="Um burrito vegano com muita verdura e sabor",
                        price="$15.90",
                        restaurant=tacolibre)
session.add(burritomanso)
session.commit()

nievedegarrafa = MenuItem(name="Nieve de Garrafa",
                          course="Sobremesa",
                          description="Um sorvete ao estilo Mexicano servido no balde de madeira",
                          price="$7.90",
                          restaurant=tacolibre)
session.add(nievedegarrafa)
session.commit()

crispychurros = MenuItem(name="Crispy Churros",
                         course="Sobremesa",
                         description="Churros super crocantes servido com doce de leite",
                         price="$8.90",
                         restaurant=tacolibre)
session.add(crispychurros)
session.commit()

# Japanese Restaurant
saykoto = Restaurant(name="Saykoto")
session.add(saykoto)
session.commit()

sunomo = MenuItem(name="Sunomomo",
                  course="Entrada",
                  description="Salada de pepino japones",
                  price="$4.90",
                  restaurant=saykoto)
session.add(sunomo)
session.commit()

shitake = MenuItem(name="Shitake",
                   course="Entrada",
                   description="Porcao de Shitake na chapa",
                   price="$5.90",
                   restaurant=saykoto)
session.add(shitake)
session.commit()

lulaempanada = MenuItem(name="Lula Empanada",
                        course="Entrada",
                        description="Rodelas de lula empanada no Panko",
                        price="$9.90",
                        restaurant=saykoto)
session.add(lulaempanada)
session.commit()

barca24 = MenuItem(name="Barca 24",
                   course="Principal",
                   description="Barca com 24 pecas de sushis e sashimis",
                   price="$12.90",
                   restaurant=saykoto)
session.add(barca24)
session.commit()

barca48 = MenuItem(name="Barca 48",
                   course="Principal",
                   description="Barca com 48 pecas de sushis e sashimis",
                   price="$22.90",
                   restaurant=saykoto)
session.add(barca48)
session.commit()

lamen = MenuItem(name="Lamen",
                 course="Principal",
                 description="Lamen com carne de porco e ovos",
                 price="$15.90",
                 restaurant=saykoto)
session.add(lamen)
session.commit()

furutsusando = MenuItem(name="Furutsu Sando",
                        course="Sobremesa",
                        description="Sanduiche doce com frutas e chantilly",
                        price="$7.90",
                        restaurant=saykoto)
session.add(furutsusando)
session.commit()

wagashi = MenuItem(name="Wagashi",
                   course="Sobremesa",
                   description="Doces tradicionais japoneses servidos com cha",
                   price="$8.90",
                   restaurant=saykoto)
session.add(wagashi)
session.commit()

# Italian Restaurant
gioristorante = Restaurant(name="Gio Ristorante")
session.add(gioristorante)
session.commit()

paesitalianos = MenuItem(name="Paes italianos",
                         course="Entrada",
                         description="Paes Italianos quentinhos e frescos",
                         price="$3.90",
                         restaurant=gioristorante)
session.add(paesitalianos)
session.commit()

entrepasto = MenuItem(name="Entrepasto",
                      course="Entrada",
                      description="Entrepasto de berinjela com torradinhas",
                      price="$5.90",
                      restaurant=gioristorante)
session.add(entrepasto)
session.commit()

brusqueta = MenuItem(name="Brusquetas",
                     course="Entrada",
                     description="3 Brusquetas feita com os mais frescos tomates",
                     price="$6.90",
                     restaurant=gioristorante)
session.add(brusqueta)
session.commit()

massacarbonara = MenuItem(name="Massa a Carbonara",
                          course="Principal",
                          description="Penne feito ao molho Carbonara mais tradicional",
                          price="$20.90",
                          restaurant=gioristorante)
session.add(massacarbonara)
session.commit()

pizzamargarita = MenuItem(name="Pizza Maragarita",
                          course="Principal",
                          description="Pizza feita ao estilo Napolitano",
                          price="$30.90",
                          restaurant=gioristorante)
session.add(pizzamargarita)
session.commit()

lasagnabolognese = MenuItem(name="Lasagna Bolognese",
                            course="Principal",
                            description="Lasanha recheada com molho de Carne Bolognes ",
                            price="$20.90",
                            restaurant=gioristorante)
session.add(lasagnabolognese)
session.commit()

tiramisu = MenuItem(name="Tiramisu",
                    course="Sobremesa",
                    description="Tiramisu o doce italiano mais vendido no mundo",
                    price="$8.90",
                    restaurant=gioristorante)
session.add(tiramisu)
session.commit()

pannacotta = MenuItem(name="Panna Cotta",
                      course="Sobremesa",
                      description="Delicado creme cozido e saborizado com baunilha",
                      price="$8.90",
                      restaurant=gioristorante)
session.add(pannacotta)
session.commit()

# Chinese Restaurant
shanlong = Restaurant(name="Shan Long")
session.add(shanlong)
session.commit()

rolinhoprimavera = MenuItem(name="Rolinho Primavera",
                            course="Entrada",
                            description="Os famosos rolinhos primavera em sua receita original da chinesa",
                            price="$5.00",
                            restaurant=shanlong)
session.add(rolinhoprimavera)
session.commit()

niouroumien = MenuItem(name="Niou Rou Mien",
                       course="Entrada",
                       description="Prato de origem Taiwanesa um sopa de carne na pressao",
                       price="$6.00",
                       restaurant=shanlong)
session.add(niouroumien)
session.commit()

frangogeneraltso = MenuItem(name="Frango do General Tso",
                            course="Entrada",
                            description="Suculento entranda de frango feito em homenagem ao Gen. Tso",
                            price="$10.00",
                            restaurant=shanlong)
session.add(frangogeneraltso)
session.commit()

yakisoba = MenuItem(name="Yakisoba",
                    course="Principal",
                    description="Tradicional massa chinesa",
                    price="$15",
                    restaurant=shanlong)
session.add(yakisoba)
session.commit()

frangoxadrez = MenuItem(name="Frango Xadrez",
                        course="Principal",
                        description="Classico da cozinha chinesa",
                        price="$14",
                        restaurant=shanlong)
session.add(frangoxadrez)
session.commit()

chopsuey = MenuItem(name="Chop Suey",
                    course="Principal",
                    description="Carnes cozidas com legumes e brotos de feijao",
                    price="$13",
                    restaurant=shanlong)
session.add(chopsuey)
session.commit()

niangao = MenuItem(name="Nian Gao",
                   course="Entrada",
                   description="Principal sobremesa do Ano Novo Chines",
                   price="$4",
                   restaurant=shanlong)
session.add(niangao)
session.commit()

mooncake = MenuItem(name="Mooncake",
                    course="Sobremesa",
                    description="Servida durante o festival lunar chines esse delicioso bolo",
                    price="$12",
                    restaurant=shanlong)
session.add(mooncake)
session.commit()

# Brazilian Restaurant
brasileires = Restaurant(name="Brasileires")
session.add(shanlong)
session.commit()

caldodefeijao = MenuItem(name="Caldo de Feijao",
                         course="Entrada",
                         description="Caldinho de feijao quentinho feito no dia",
                         price="$5.99",
                         restaurant=brasileires)
session.add(caldodefeijao)
session.commit()

coxinhadefrango = MenuItem(name="Coxinha de Frango",
                           course="Entrada",
                           description="Coxinha de frango croconte por fora macia por dentro",
                           price="$2.99",
                           restaurant=brasileires)
session.add(coxinhadefrango)
session.commit()

saladadefolhas = MenuItem(name="Salada de Folhas",
                          course="Entrada",
                          description="Salada de folhas selecionadas da estacao do ano",
                          price="$4.99",
                          restaurant=brasileires)
session.add(saladadefolhas)
session.commit()

picanha = MenuItem(name="Picanha",
                   course="Principal",
                   description="Tradicional corte de carne brasileira",
                   price="$20.99",
                   restaurant=brasileires)
session.add(picanha)
session.commit()

feijoada = MenuItem(name="Feijoada",
                    course="Principal",
                    description="O mais classico prato brasileiro",
                    price="$19.99",
                    restaurant=brasileires)
session.add(feijoada)
session.commit()

acaraje = MenuItem(name="Acaraje",
                   course="Principal",
                   description="Famoso bolo a base de feijao e recheado com pimentas",
                   price="$10.99",
                   restaurant=brasileires)
session.add(acaraje)
session.commit()

brigadeiro = MenuItem(name="Brigadeiro",
                      course="Entrada",
                      description="Principal doce brasileiro feito a base de leite condesado",
                      price="$4.99",
                      restaurant=brasileires)
session.add(brigadeiro)
session.commit()

quindim = MenuItem(name="Quindim",
                   course="Sobremesa",
                   description="tortinha a base de ovo",
                   price="$3.99",
                   restaurant=brasileires)
session.add(quindim)
session.commit()

print("Added Restaurants!!!")