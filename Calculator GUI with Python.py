from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class myApp(App):
    def build(self):
        root_widget = BoxLayout(orientation='vertical')
        output_label = Label(size_hint_y = 0.75, font_size=50)
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')
        button_grid = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))

        clear_button = Button(text = 'Clear', size_hint_y=None, height=100)
        def print_button_text(instance):
            output_label.text += instance.text
        for button in button_grid.children[1:]:
            button.bind(on_press=print_button_text)
        def resize_label_text(label, new_height):
            label.fontsize = 0.5*label.height
        output_label.bind(height=resize_label_text)

        def evaluate_result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                output_label.text = 'Python Syntax error!'
        button_grid.children[0].bind(on_press=evaluate_result)

        def clear_label(instance):
            output_label.text = " "
        clear_button.bind(on_press=clear_label)

        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)
        return root_widget
myApp().run()
"""Kivy is a free, Open Source Python library that enables the rapid and easy development of highly interactive cross-platform applications. Kivy’s execution speed is the same as compared to the other mobile development alternatives like Java for Android and Objective C for iOS.

Additionally, Kivy has the huge advantage of being able to run on multiple platforms, just like HTML5 does; in this case, Kivy works best because it doesn’t rely on a heavy browser, and many of its components are implemented in C using the Cython library so that most of the graphics processing runs directly in the GPU."""
