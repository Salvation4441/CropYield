from taipy.gui import Gui
import taipy.gui.builder as tgb

with tgb.Page() as page:
    with tgb.part(class_name='container'):
        tgb.text('# 🌾 Crop Yield Production Analysis',mode='md')

        '''cards'''
        with tgb.part(class_name='card'):
            tgb.text('Enter your year',mode='md')
            tgb.input('Year',type='select',width='100%')
            tgb.input('Average Rainfall/per(mm)',type='number')
            
        
Gui(page=page).run(use_reloader=True,dark_mode=False)