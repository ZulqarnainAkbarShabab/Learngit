# Constants for Parser

# Sections coordinates tuples
#AU ----> Automobile Liability
#CGL----> Commercial General Liability
#UML----> Umbrella Liability
#WCE----> Workers Compensation and Employment Liability
#OTH----> OTHERS
#PN-----> Policy Number
#DATE---> Date
#PL-----> Policy Limit
#TOI----> Type of Insurance
#PLM----> Policy Limit
#INFO---> Information
#IMGEXT--> Image Extension (Cropped images name extension)


PATH = {
        "INPUT" : "C:/Users/Zulqarnain/Desktop/ABHISHEKCODE/"
        }

##UPPERCORD = {
##            "PRODUCER": (0+10,0+350,0+1250,0+800) ,
##            "INSURED" :(0+10,0+600,0+1170,0+1200) ,
##            "PRODUCERINFO": (0+1170,0+350,0+2600,0+800),
##            "INSURER":(0+1170,0+600,0+2600,0+1200) ,
##            "INSURER1": (0+1170,0+600,0+2600,0+800),
##            "INSURER2": (0+1170,0+800,0+2600,0+1000),
##            "INSURER3": (0+1170,0+1000,0+2600,0+1200),
##            "TOPDATE": (0+2000,0,0+2500,0+300)
##            
##            }

#Files with this list element name will only be saved
IMGEXT = ["PRODUCER","INSURED", "INSURER", "TOPDATE", "CGLPN", "AULPN", "UMLPN", "WCEPN", "OTHPN",
          "CGLDATE","AULDATE","UMLDATE","WCEDATE","OTHDATE", "CGLPLS", "AULPLS", "UMLPLS", "WCEPLS", "OTHPLS", "CGLTOIS",
          "AULTOIS", "UMLPLS", "WCETOIS", "OTHTOIS"  ]


#These Coordinates are having reference as X=0 and Y=0
x =0; y = 0
DEFAULT = {
           #Policy Numbers
           "CGLPN": (x+700,y+1120,x+1300,y+1550),
           "AULPN": (x+700,y+1450,x+1300,y+1750),
           "UMLPN": (x+700,y+1750,x+1300,y+1900),
           "WCEPN": (x+700,y+1860,x+1300,y+2100),
           "OTHPN": (x+700,y+2020,x+1300,y+2300),

           #Policy Dates
           "CGLDATE": (x+1220,y+1120,x+1790,y+1500) ,
           "AULDATE": (x+1220,y+1450,x+1790,y+1750),
           "UMLDATE": (x+1220,y+1750,x+1790,y+1900),
           "WCEDATE": (x+1220,y+1860,x+1790,y+2100),
           "OTHDATE": (x+1220,y+2020,x+1790,y+2300),

           #Policy Limits
           "CGLPLS" : (x+1650,y+1100,x+2500,y+1540),     #[It crops entire section CGLPL ] use this for image

           "AULPLS" : (x+1650,y+1430,x+2500,y+1790),     # [It crops entire AULPL section] use this for image

           "UMLPLS" : (x+1650,y+1730,x+2500,y+1940),     # [It crops entire UMLPL section] use this for image

           "WCEPLS" : (x+1650,y+1840,x+2500,y+2140),     # [It crops entire WCEPL section] use this for image

           "OTHPLS" : (x+1650,y+2000,x+2500,y+2340),    #[It crops entire OTHPL section] use this for image

           "CGLTOIS" : (x+10,y+1100,x+760,y+1540),   #[It crops entire CGLTOI section] use this for image

           "AULTOIS" : (x+10,y+1430,x+760,y+1790),   #[It crops entire AULTOI section] use this for image

           "UMLTOIS" : (x+10,y+1730,x+760,y+1940),   #[It crops entire UMLTOI section] use this for image

           "WCETOIS" : (x+10,y+1840,x+760,y+2140),   #[It crops entire WCETOI section] use this for image

           "OTHTOIS" : (x+10,y+2000,x+760,y+2340),   #[It crops entire OTHTOI section] use this for image

           "PRODUCER": (0+10,0+350,0+1250,0+800) ,
           "INSURED" :(0+10,0+600,0+1170,0+1200) ,
           "PRODUCERINFO": (0+1170,0+350,0+2600,0+800),
           "INSURER":(0+1170,0+600,0+2600,0+1200) ,
           "INSURER1": (0+1170,0+600,0+2600,0+800),
           "INSURER2": (0+1170,0+800,0+2600,0+1000),
           "INSURER3": (0+1170,0+1000,0+2600,0+1200),
           "TOPDATE": (0+2000,0,0+2500,0+300)
           
           }



x =91
y = 1014
#These Coordinates are having reference of the coordinate of the word |"COVERAGES"| in The Insurance Form 
DFRAME = {
           #Policy Numbers
           "CGLPN": (x+580,y+250,x+1280,y+550),
           "AULPN": (x+600,y+530,x+1280,y+840),
           "UMLPN": (x+600,y+820,x+1280,y+960),
           "WCEPN": (x+620,y+940,x+1280,y+1170),
           "OTHPN": (x+620,y+1150,x+1280,y+1360),

           #Policy Dates
           "CGLDATE": (x+1170,y+200,x+1770,y+550)  ,
           "AULDATE": (x+1150,y+530,x+1770,y+840)  ,
           "UMLDATE": (x+1150,y+820,x+1770,y+960)  ,
           "WCEDATE": (x+1150,y+940,x+1690,y+1170) ,
           "OTHDATE": (x+1150,y+1150,x+1690,y+1360),

           #Policy Limits
           #"CGLPLS" : ,     #[It crops entire section ] use for Image
           "CGLPL1": (x+1600,y+200,x+2450,y+350),
           "CGLPL2": (x+1600,y+250,x+2450,y+430),
           "CGLPL3": (x+1600,y+400,x+2400,y+570),
           "CGLPL4": (x+1600,y+500,x+2400,y+670),
           "CGLPL5": (x+1600,y+600,x+2400,y+770),
           #"AULPLS" : ,     #[It crops entire section] use for Image
           "AULPL1": (x+1600,y+550,x+2400,y+750),
           "AULPL2": (x+1600,y+650,x+2400,y+850),
           "AULPL3": (x+1600,y+750,x+2400,y+950),
          # "UMLPLS" : ,     #[It crops entire section] use for Image
           "UMLPL1": (x+1610,y+820,x+2400,y+990),
           "UMLPL2": (x+1610,y+940,x+2400,y+1150),
           "UMLPL3": (x+1610,y+1050,x+2400,y+1250),
           #"WCEPLS" : ,     #[It crops entire section] use for Image
           "WCEPL1": (x+1610,y+970,x+2400,y+1100),
           "WCEPL2": (x+1610,y+1080,x+2400,y+1300),
           "WCEPL3": (x+1610,y+1250,x+2400,y+1450),
           #"OTHPLS" : ,    #[It crops entire section] use for Image
           "OTHPL1": (x+1610,y+1200,x+2400,y+1400),
           "OTHPL2": (x+1610,y+1350,x+2400,y+1550),
           "OTHPL3": (x+1610,y+1450,x+2400,y+1650),

           #Type of Insurance
           "CGLTOIS" : (x+10,y+220,x+750,y+700),# [It crops entire CGLTOI section]
           "CGLTOI1": (x+10,y+220,x+750,y+500),
           "CGLTOI2": (x+10,y+400,x+750,y+700),
           "AULTOIS" : (x+10,y+650,x+750,y+900),   # [It crops entire AULTOI section]   
           "AULTOI1": (x+10,y+650,x+750,y+800),
           "AULTOI2": (x+10,y+750,x+750,y+900),
           "UMLTOIS" : (x+10,y+850,x+750,y+1150),  # [It crops entire UMLTOI section]
           "UMLTOI1": (x+10,y+850,x+750,y+1000),
           "UMLTOI2": (x+10,y+950,x+750,y+1150),
           "WCETOIS" : (x+10,y+1050,x+750,y+1350), # [It crops entire UMLTOI section]
           "WCETOI1": (x+10,y+1050,x+750,y+1250),
           "WCETOI2": (x+10,y+1150,x+750,y+1350),
           "OTHTOIS" : (x+10,y+1200,x+750,y+1450), # [It crops entire OTHTOI section]
           "OTHTOI1": (x+10,y+1200,x+750,y+1350),
           "OTHTOI2": (x+10,y+1300,x+750,y+1450),

           "PRODUCER": (0+10,0+350,0+1250,0+800) ,
           "INSURED" :(0+10,0+600,0+1170,0+1200) ,
           "PRODUCERINFO": (0+1170,0+350,0+2600,0+800),
           "INSURER":(0+1170,0+600,0+2600,0+1200) ,
           "INSURER1": (0+1170,0+600,0+2600,0+800),
           "INSURER2": (0+1170,0+800,0+2600,0+1000),
           "INSURER3": (0+1170,0+1000,0+2600,0+1200),
           "TOPDATE": (0+2000,0,0+2500,0+300)
           
           }
