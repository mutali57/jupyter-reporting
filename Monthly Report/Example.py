# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 07:08:06 2022

@author: Mutali
"""
import  os , sys
from docxtpl import DocxTemplate
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Cm, Inches, Mm, Emu
#os.chdir(sys.path[0])

doc=DocxTemplate('Template.docx')
Placeholder1 = InlineImage(doc, 'Graph.png', Cm(5))

context ={'name':' seven',
          'Placeholder1':Placeholder1}
doc.render(context)
doc.save('temp.docx')