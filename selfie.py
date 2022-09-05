from kivy.app import App
from kivy.uix.camera import Camera  #it is use for setting up the layout in the camera
from kivy.uix.boxlayout import BoxLayout#it is use for making box layout in the camera
from kivy.uix.button import Button#it is use for a clickable button 
from kivy.core.window._window_sdl2 import _WindowSDL2Storage
class app_selfie(App):
    def build(self):
        self.obj_camera=Camera()
        self.obj_camera.resolution =(800,800)
        obj_button=Button(text='Click Me')
        obj_button.size_hint=(.5,.2)
        obj_button.pos_hint = {'x':.25,'y':25}
        obj_button.bind(on_press =self.selfie_take())
        obj_layout=BoxLayout()
        obj_layout.add_widget(self.obj_camera)
        obj_layout.add_widget(obj_button)
        return obj_layout
    
    def selfie_take(self , *args):
        print('Selfie has been taken successfully')
        self.obj_camera.export_to_png('./demoselfie.png')
        
        
if __name__ == '__main__':
    app_selfie().run()