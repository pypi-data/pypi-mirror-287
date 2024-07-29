import tkinter as tk
from .gui import MainApp

def initiate_annotation_app(parent_frame):
    from .gui_utils import generate_annotate_fields, annotate_app
    # Set up the settings window
    settings_window = tk.Toplevel(parent_frame)
    settings_window.title("Annotation Settings")
    settings_window.configure(bg='black')  # Set the background color to black
    
    # Use the existing function to create the settings UI
    settings_frame = tk.Frame(settings_window, bg='black')  # Set the background color to black
    settings_frame.pack(fill=tk.BOTH, expand=True)
    vars_dict = generate_annotate_fields(settings_frame)
    
    def start_annotation_app():
        settings = {key: data['entry'].get() for key, data in vars_dict.items()}
        settings['channels'] = settings['channels'].split(',')
        settings['img_size'] = list(map(int, settings['img_size'].split(',')))  # Convert string to list of integers
        settings['percentiles'] = list(map(int, settings['percentiles'].split(',')))  # Convert string to list of integers
        settings['normalize'] = settings['normalize'].lower() == 'true'
        settings['rows'] = int(settings['rows'])
        settings['columns'] = int(settings['columns'])

        try:
            settings['measurement'] = settings['measurement'].split(',') if settings['measurement'] else None
            settings['threshold'] = None if settings['threshold'].lower() == 'none' else int(settings['threshold'])
        except:
            settings['measurement']  = None
            settings['threshold'] = None

        settings['db'] = settings.get('db', 'default.db')

        # Convert empty strings to None
        for key, value in settings.items():
            if isinstance(value, list):
                settings[key] = [v if v != '' else None for v in value]
            elif value == '':
                settings[key] = None

        settings_window.destroy()
        annotate_app(parent_frame, settings)
    
    start_button = tk.Button(settings_window, text="Start Annotation", command=start_annotation_app, bg='black', fg='white')
    start_button.pack(pady=10)

def start_annotate_app():
    app = MainApp(default_app="Annotate")
    app.mainloop()

if __name__ == "__main__":
    start_annotate_app()