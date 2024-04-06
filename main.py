from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class SMSApp(App):
    def send_sms(self, phone_number, message):
            # تنظیمات مربوط به sms.ir
                    SMS_IR_API_KEY = "YOUR_SMS_IR_API_KEY"
                            SMS_IR_SECRET_KEY = "YOUR_SMS_IR_SECRET_KEY"
                                    SMS_IR_LINE_NUMBER = "YOUR_SMS_IR_LINE_NUMBER"

                                            url = "https://ws.sms.ir/api/MessageSend"
                                                    headers = {
                                                                "Content-Type": "application/json",
                                                                            "x-sms-ir-secure-token": SMS_IR_API_KEY
                                                                                    }
                                                                                            payload = {
                                                                                                        "LineNumber": SMS_IR_LINE_NUMBER,
                                                                                                                    "MobileNo": phone_number,
                                                                                                                                "Message": message
                                                                                                                                        }

                                                                                                                                                response = requests.post(url, headers=headers, json=payload)
                                                                                                                                                        if response.status_code != 200:
                                                                                                                                                                    return "Failed to send SMS"
                                                                                                                                                                            return "SMS sent successfully"

                                                                                                                                                                                def build(self):
                                                                                                                                                                                        layout = BoxLayout(orientation="vertical")
                                                                                                                                                                                                
                                                                                                                                                                                                        self.phone_input = TextInput(multiline=False)
                                                                                                                                                                                                                self.message_input = TextInput(multiline=True)

                                                                                                                                                                                                                        send_buttons_layout = BoxLayout(orientation="horizontal")

                                                                                                                                                                                                                                for feature in range(1, 13):
                                                                                                                                                                                                                                            feature_button = Button(text=f"Feature {feature}")
                                                                                                                                                                                                                                                        feature_button.bind(on_press=self.on_send_sms)
                                                                                                                                                                                                                                                                    send_buttons_layout.add_widget(feature_button)

                                                                                                                                                                                                                                                                            layout.add_widget(Label(text="Phone Number:"))
                                                                                                                                                                                                                                                                                    layout.add_widget(self.phone_input)
                                                                                                                                                                                                                                                                                            layout.add_widget(Label(text="Message:"))
                                                                                                                                                                                                                                                                                                    layout.add_widget(self.message_input)
                                                                                                                                                                                                                                                                                                            layout.add_widget(send_buttons_layout)

                                                                                                                                                                                                                                                                                                                    self.report_label = Label(text="")
                                                                                                                                                                                                                                                                                                                            layout.add_widget(self.report_label)
                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                            return layout

                                                                                                                                                                                                                                                                                                                                                def on_send_sms(self, instance):
                                                                                                                                                                                                                                                                                                                                                        phone_number = self.phone_input.text.strip()
                                                                                                                                                                                                                                                                                                                                                                message = self.message_input.text.strip()
                                                                                                                                                                                                                                                                                                                                                                        feature = instance.text.split()[1]

                                                                                                                                                                                                                                                                                                                                                                                if not phone_number or not message:
                                                                                                                                                                                                                                                                                                                                                                                            self.report_label.text = "Phone number and message are required"
                                                                                                                                                                                                                                                                                                                                                                                                        return

                                                                                                                                                                                                                                                                                                                                                                                                                result = self.send_sms(phone_number, message)
                                                                                                                                                                                                                                                                                                                                                                                                                        self.report_label.text = f"Feature {feature}: {result}"


                                                                                                                                                                                                                                                                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                                            SMSApp().run()