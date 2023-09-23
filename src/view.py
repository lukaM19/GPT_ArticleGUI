import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color
import model


class QueryConstructor(FloatLayout):
    def __init__(self,a, **kwargs):
        super(QueryConstructor, self).__init__(**kwargs)
        self.API_Key=a
        # Create input fields
        self.input1 = TextInput(size_hint=(0.5, 0.1), pos_hint={"x": 0.2, "y": 0.85})
        self.input2 = TextInput(size_hint=(0.5, 0.15), pos_hint={"x": 0.2, "y": 0.7})

        # Create "Run" button
        run_button = Button(text="Run", size_hint=(0.1, 0.1), pos_hint={"x": 0.8, "y": 0.78})
        run_button.bind(on_press=self.run_query)

        # Create output field
        self.output = TextInput(size_hint=(0.5, 0.5), pos_hint={"x": 0.5, "y": 0.1}, readonly=True)
        self.webText = TextInput(size_hint=(0.5, 0.5), pos_hint={"x": 0, "y": 0.1}, readonly=True)


        # Add widgets to the layout
        self.add_widget(Label(text="Article Link:", size_hint=(0.1, 0.1), pos_hint={"x": 0.1, "y": 0.85}))
        self.add_widget(self.input1)
        self.add_widget(Label(text="ChatGPT"+"\n" +" command:", size_hint=(0.1, 0.1), pos_hint={"x": 0.1, "y": 0.7}))
        self.add_widget(self.input2)
        self.add_widget(run_button)
        self.add_widget(Label(text="Output:", size_hint=(1, 1), pos_hint={"x": 0.05, "y": 0.15}))
        self.add_widget(Label(text="Article text:", size_hint=(1, 1), pos_hint={"x": -0.45, "y": 0.15}))
        self.add_widget(self.output)
        self.add_widget(self.webText)

    def run_query(self, instance):
        input1 = self.input1.text
        
        article_text = model.extract_article_text(input1)
        article_text=article_text[:19000]
        article_text.replace("\n"," ")
        input2 = self.input2.text
        self.webText.text=article_text
        result = model.chat_gpt_api(input2 + article_text)
        self.output.text=result

class QueryConstructorApp(App):
    def __init__(self, api_key, **kwargs):
        super(QueryConstructorApp, self).__init__(**kwargs)
        self.api_key = api_key

    def build(self):
        return QueryConstructor(self.api_key)


if __name__ == '__main__':
    QueryConstructorApp(api_key='YOUR_API_KEY').run()
