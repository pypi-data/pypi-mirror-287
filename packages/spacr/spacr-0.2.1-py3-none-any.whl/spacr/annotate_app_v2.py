import sqlite3
from queue import Queue
from tkinter import Label
import tkinter as tk
from tkinter import ttk
import os, threading, time, sqlite3
import numpy as np
from PIL import Image, ImageOps
from concurrent.futures import ThreadPoolExecutor
from PIL import ImageTk
from skimage.exposure import rescale_intensity
from IPython.display import display, HTML
from tkinter import font as tkFont

from .gui_utils import ScrollableFrame, CustomButton, set_dark_style, set_default_font, style_text_boxes, create_menu_bar

class ImageApp:
    def __init__(self, root, db_path, src, image_type=None, channels=None, grid_rows=None, grid_cols=None, image_size=(200, 200), annotation_column='annotate', normalize=False, percentiles=(1,99), measurement=None, threshold=None):
        """
        Initializes an instance of the ImageApp class.

        Parameters:
        - root (tkinter.Tk): The root window of the application.
        - db_path (str): The path to the SQLite database.
        - src (str): The source directory that should be upstream of 'data' in the paths.
        - image_type (str): The type of images to display.
        - channels (list): The channels to filter in the images.
        - grid_rows (int): The number of rows in the image grid.
        - grid_cols (int): The number of columns in the image grid.
        - image_size (tuple): The size of the displayed images.
        - annotation_column (str): The column name for image annotations in the database.
        - normalize (bool): Whether to normalize images to their 2nd and 98th percentiles. Defaults to False.
        - measurement (str): The measurement column to filter by.
        - threshold (float): The threshold value for filtering the measurement column.
        """

        self.root = root
        self.db_path = db_path
        self.src = src
        self.index = 0
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.image_size = image_size
        self.annotation_column = annotation_column
        self.image_type = image_type
        self.channels = channels
        self.normalize = normalize
        self.percentiles = percentiles
        self.images = {}
        self.pending_updates = {}
        self.labels = []
        self.adjusted_to_original_paths = {}
        self.terminate = False
        self.update_queue = Queue()
        self.status_label = Label(self.root, text="", font=("Arial", 12))
        self.status_label.grid(row=self.grid_rows + 1, column=0, columnspan=self.grid_cols)
        self.measurement = measurement
        self.threshold = threshold

        self.filtered_paths_annotations = []
        self.prefilter_paths_annotations()

        self.db_update_thread = threading.Thread(target=self.update_database_worker)
        self.db_update_thread.start()

        for i in range(grid_rows * grid_cols):
            label = Label(root)
            label.grid(row=i // grid_cols, column=i % grid_cols)
            self.labels.append(label)

    def prefilter_paths_annotations(self):
        """
        Pre-filters the paths and annotations based on the specified measurement and threshold.
        """
        from .io import _read_and_join_tables
        from .utils import is_list_of_lists

        if self.measurement and self.threshold is not None:
            df = _read_and_join_tables(self.db_path)
            df[self.annotation_column] = None
            before = len(df)

            if is_list_of_lists(self.measurement):
                if isinstance(self.threshold, list) or is_list_of_lists(self.threshold):
                    if len(self.measurement) == len(self.threshold):
                        for idx, var in enumerate(self.measurement):
                            df = df[df[var[idx]] > self.threshold[idx]]
                        after = len(df)
                    elif len(self.measurement) == len(self.threshold)*2:
                        th_idx = 0
                        for idx, var in enumerate(self.measurement):
                            if idx % 2 != 0:
                                th_idx += 1
                                thd = self.threshold
                                if isinstance(thd, list):
                                    thd = thd[0]
                                df[f'threshold_measurement_{idx}'] = df[self.measurement[idx]]/df[self.measurement[idx+1]]
                                print(f"mean threshold_measurement_{idx}: {np.mean(df['threshold_measurement'])}")
                                print(f"median threshold measurement: {np.median(df[self.measurement])}")
                                df = df[df[f'threshold_measurement_{idx}'] > thd]
                        after = len(df)
            elif isinstance(self.measurement, list):
                df['threshold_measurement'] = df[self.measurement[0]]/df[self.measurement[1]]
                print(f"mean threshold measurement: {np.mean(df['threshold_measurement'])}")
                print(f"median threshold measurement: {np.median(df[self.measurement])}")
                df = df[df['threshold_measurement'] > self.threshold]
                after = len(df)
                self.measurement = 'threshold_measurement'
                print(f'Removed: {before-after} rows, retained {after}')
            else:
                print(f"mean threshold measurement: {np.mean(df[self.measurement])}")
                print(f"median threshold measurement: {np.median(df[self.measurement])}")
                before = len(df)
                if isinstance(self.threshold, str):
                    if self.threshold == 'q1':
                        self.threshold = df[self.measurement].quantile(0.1)
                    if self.threshold == 'q2':
                        self.threshold = df[self.measurement].quantile(0.2)
                    if self.threshold == 'q3':
                        self.threshold = df[self.measurement].quantile(0.3)
                    if self.threshold == 'q4':
                        self.threshold = df[self.measurement].quantile(0.4)
                    if self.threshold == 'q5':
                        self.threshold = df[self.measurement].quantile(0.5)
                    if self.threshold == 'q6':
                        self.threshold = df[self.measurement].quantile(0.6)
                    if self.threshold == 'q7':
                        self.threshold = df[self.measurement].quantile(0.7)
                    if self.threshold == 'q8':
                        self.threshold = df[self.measurement].quantile(0.8)
                    if self.threshold == 'q9':
                        self.threshold = df[self.measurement].quantile(0.9)
                print(f"threshold: {self.threshold}")

                df = df[df[self.measurement] > self.threshold]
                after = len(df)
                print(f'Removed: {before-after} rows, retained {after}')

            df = df.dropna(subset=['png_path'])
            if self.image_type:
                before = len(df)
                if isinstance(self.image_type, list):
                    for tpe in self.image_type:
                        df = df[df['png_path'].str.contains(tpe)]
                else:
                    df = df[df['png_path'].str.contains(self.image_type)]
                after = len(df)
                print(f'image_type: Removed: {before-after} rows, retained {after}')

            self.filtered_paths_annotations = df[['png_path', self.annotation_column]].values.tolist()
        else:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            if self.image_type:
                c.execute(f"SELECT png_path, {self.annotation_column} FROM png_list WHERE png_path LIKE ?", (f"%{self.image_type}%",))
            else:
                c.execute(f"SELECT png_path, {self.annotation_column} FROM png_list")
            self.filtered_paths_annotations = c.fetchall()
            conn.close()

    def load_images(self):
        """
        Loads and displays images with annotations.

        This method retrieves image paths and annotations from a pre-filtered list,
        loads the images using a ThreadPoolExecutor for parallel processing,
        adds colored borders to images based on their annotations,
        and displays the images in the corresponding labels.

        Args:
            None

        Returns:
            None
        """

        for label in self.labels:
            label.config(image='')

        self.images = {}
        paths_annotations = self.filtered_paths_annotations[self.index:self.index + self.grid_rows * self.grid_cols]

        adjusted_paths = []
        for path, annotation in paths_annotations:
            if not path.startswith(self.src):
                parts = path.split('/data/')
                if len(parts) > 1:
                    new_path = os.path.join(self.src, 'data', parts[1])
                    self.adjusted_to_original_paths[new_path] = path
                    adjusted_paths.append((new_path, annotation))
                else:
                    adjusted_paths.append((path, annotation))
            else:
                adjusted_paths.append((path, annotation))

        with ThreadPoolExecutor() as executor:
            loaded_images = list(executor.map(self.load_single_image, adjusted_paths))

        for i, (img, annotation) in enumerate(loaded_images):
            if annotation:
                border_color = 'teal' if annotation == 1 else 'red'
                img = self.add_colored_border(img, border_width=5, border_color=border_color)

            photo = ImageTk.PhotoImage(img)
            label = self.labels[i]
            self.images[label] = photo
            label.config(image=photo)

            path = adjusted_paths[i][0]
            label.bind('<Button-1>', self.get_on_image_click(path, label, img))
            label.bind('<Button-3>', self.get_on_image_click(path, label, img))

        self.root.update()

    def load_single_image(self, path_annotation_tuple):
        """
        Loads a single image from the given path and annotation tuple.

        Args:
            path_annotation_tuple (tuple): A tuple containing the image path and its annotation.

        Returns:
            img (PIL.Image.Image): The loaded image.
            annotation: The annotation associated with the image.
        """
        path, annotation = path_annotation_tuple
        img = Image.open(path)
        img = self.normalize_image(img, self.normalize, self.percentiles)
        img = img.convert('RGB')
        img = self.filter_channels(img)
        img = img.resize(self.image_size)
        return img, annotation

    @staticmethod
    def normalize_image(img, normalize=False, percentiles=(1, 99)):
        """
        Normalize the pixel values of an image based on the 2nd and 98th percentiles or the image min and max values,
        and ensure the image is exported as 8-bit.

        Parameters:
        - img: PIL.Image.Image. The input image to be normalized.
        - normalize: bool. Whether to normalize based on the 2nd and 98th percentiles.
        - percentiles: tuple. The percentiles to use for normalization.

        Returns:
        - PIL.Image.Image. The normalized and 8-bit converted image.
        """
        img_array = np.array(img)

        if normalize:
            if img_array.ndim == 2:  # Grayscale image
                p2, p98 = np.percentile(img_array, percentiles)
                img_array = rescale_intensity(img_array, in_range=(p2, p98), out_range=(0, 255))
            else:  # Color image or multi-channel image
                for channel in range(img_array.shape[2]):
                    p2, p98 = np.percentile(img_array[:, :, channel], percentiles)
                    img_array[:, :, channel] = rescale_intensity(img_array[:, :, channel], in_range=(p2, p98), out_range=(0, 255))

        img_array = np.clip(img_array, 0, 255).astype('uint8')

        return Image.fromarray(img_array)
    
    def add_colored_border(self, img, border_width, border_color):
        """
        Adds a colored border to an image.

        Args:
            img (PIL.Image.Image): The input image.
            border_width (int): The width of the border in pixels.
            border_color (str): The color of the border in RGB format.

        Returns:
            PIL.Image.Image: The image with the colored border.
        """
        top_border = Image.new('RGB', (img.width, border_width), color=border_color)
        bottom_border = Image.new('RGB', (img.width, border_width), color=border_color)
        left_border = Image.new('RGB', (border_width, img.height), color=border_color)
        right_border = Image.new('RGB', (border_width, img.height), color=border_color)

        bordered_img = Image.new('RGB', (img.width + 2 * border_width, img.height + 2 * border_width), color='white')
        bordered_img.paste(top_border, (border_width, 0))
        bordered_img.paste(bottom_border, (border_width, img.height + border_width))
        bordered_img.paste(left_border, (0, border_width))
        bordered_img.paste(right_border, (img.width + border_width, border_width))
        bordered_img.paste(img, (border_width, border_width))

        return bordered_img
    
    def filter_channels(self, img):
        """
        Filters the channels of an image based on the specified channels.

        Args:
            img (PIL.Image.Image): The input image.

        Returns:
            PIL.Image.Image: The filtered image.
        """
        r, g, b = img.split()
        if self.channels:
            if 'r' not in self.channels:
                r = r.point(lambda _: 0)
            if 'g' not in self.channels:
                g = g.point(lambda _: 0)
            if 'b' not in self.channels:
                b = b.point(lambda _: 0)

            if len(self.channels) == 1:
                channel_img = r if 'r' in self.channels else (g if 'g' in self.channels else b)
                return ImageOps.grayscale(channel_img)

        return Image.merge("RGB", (r, g, b))

    def get_on_image_click(self, path, label, img):
        """
        Returns a callback function that handles the click event on an image.

        Parameters:
        path (str): The path of the image file.
        label (tkinter.Label): The label widget to update with the annotated image.
        img (PIL.Image.Image): The image object.

        Returns:
        function: The callback function for the image click event.
        """
        def on_image_click(event):
            new_annotation = 1 if event.num == 1 else (2 if event.num == 3 else None)
            
            original_path = self.adjusted_to_original_paths.get(path, path)
            
            if original_path in self.pending_updates and self.pending_updates[original_path] == new_annotation:
                self.pending_updates[original_path] = None
                new_annotation = None
            else:
                self.pending_updates[original_path] = new_annotation
            
            print(f"Image {os.path.split(path)[1]} annotated: {new_annotation}")
            
            img_ = img.crop((5, 5, img.width-5, img.height-5))
            border_fill = 'teal' if new_annotation == 1 else ('red' if new_annotation == 2 else None)
            img_ = ImageOps.expand(img_, border=5, fill=border_fill) if border_fill else img_

            photo = ImageTk.PhotoImage(img_)
            self.images[label] = photo
            label.config(image=photo)
            self.root.update()

        return on_image_click

    @staticmethod
    def update_html(text):
        display(HTML(f"""
        <script>
        document.getElementById('unique_id').innerHTML = '{text}';
        </script>
        """))

    def update_database_worker(self):
        """
        Worker function that continuously updates the database with pending updates from the update queue.
        It retrieves the pending updates from the queue, updates the corresponding records in the database,
        and resets the text in the HTML and status label.
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        display(HTML("<div id='unique_id'>Initial Text</div>"))

        while True:
            if self.terminate:
                conn.close()
                break

            if not self.update_queue.empty():
                ImageApp.update_html("Do not exit, Updating database...")
                self.status_label.config(text='Do not exit, Updating database...')

                pending_updates = self.update_queue.get()
                for path, new_annotation in pending_updates.items():
                    if new_annotation is None:
                        c.execute(f'UPDATE png_list SET {self.annotation_column} = NULL WHERE png_path = ?', (path,))
                    else:
                        c.execute(f'UPDATE png_list SET {self.annotation_column} = ? WHERE png_path = ?', (new_annotation, path))
                conn.commit()

                # Reset the text
                ImageApp.update_html('')
                self.status_label.config(text='')
                self.root.update()
            time.sleep(0.1)

    def update_gui_text(self, text):
        """
        Update the text of the status label in the GUI.

        Args:
            text (str): The new text to be displayed in the status label.

        Returns:
            None
        """
        self.status_label.config(text=text)
        self.root.update()

    def next_page(self):
        """
        Moves to the next page of images in the grid.

        If there are pending updates in the dictionary, they are added to the update queue.
        The pending updates dictionary is then cleared.
        The index is incremented by the number of rows multiplied by the number of columns in the grid.
        Finally, the images are loaded for the new page.
        """
        if self.pending_updates:  # Check if the dictionary is not empty
            self.update_queue.put(self.pending_updates.copy())
        self.pending_updates.clear()
        self.index += self.grid_rows * self.grid_cols
        self.load_images()

    def previous_page(self):
        """
        Move to the previous page in the grid.

        If there are pending updates in the dictionary, they are added to the update queue.
        The dictionary of pending updates is then cleared.
        The index is decremented by the number of rows multiplied by the number of columns in the grid.
        If the index becomes negative, it is set to 0.
        Finally, the images are loaded for the new page.
        """
        if self.pending_updates:  # Check if the dictionary is not empty
            self.update_queue.put(self.pending_updates.copy())
        self.pending_updates.clear()
        self.index -= self.grid_rows * self.grid_cols
        if self.index < 0:
            self.index = 0
        self.load_images()

    def shutdown(self):
        """
        Shuts down the application.

        This method sets the terminate flag to True, clears the pending updates,
        updates the database, and quits the application.

        """
        self.terminate = True  # Set terminate first
        self.update_queue.put(self.pending_updates.copy())
        self.pending_updates.clear()
        self.db_update_thread.join()  # Join the thread to make sure database is updated
        self.root.quit()
        self.root.destroy()
        print(f'Quit application')

def get_annotate_default_settings(settings):

    settings.setdefault('image_type', 'cell_png')
    settings.setdefault('channels', ['r', 'g', 'b'])
    settings.setdefault('geom', "3200x2000")
    settings.setdefault('img_size', (200, 200))
    settings.setdefault('rows', 10)
    settings.setdefault('columns', 18)
    settings.setdefault('annotation_column', 'recruited_test')
    settings.setdefault('normalize', False)
    settings.setdefault('percentiles', (2,98))
    settings.setdefault('measurement', ['cytoplasm_channel_3_mean_intensity', 'pathogen_channel_3_mean_intensity'])
    settings.setdefault('threshold', 2)

    return settings

def annotate(settings):
    """
    Annotates images in a database using a graphical user interface.

    Args:
        db (str): The path to the SQLite database.
        src (str): The source directory that should be upstream of 'data' in the paths.
        image_type (str, optional): The type of images to load from the database. Defaults to None.
        channels (str, optional): The channels of the images to load from the database. Defaults to None.
        geom (str, optional): The geometry of the GUI window. Defaults to "1000x1100".
        img_size (tuple, optional): The size of the images to display in the GUI. Defaults to (200, 200).
        rows (int, optional): The number of rows in the image grid. Defaults to 5.
        columns (int, optional): The number of columns in the image grid. Defaults to 5.
        annotation_column (str, optional): The name of the annotation column in the database table. Defaults to 'annotate'.
        normalize (bool, optional): Whether to normalize images to their 2nd and 98th percentiles. Defaults to False.
        measurement (str, optional): The measurement column to filter by.
        threshold (float, optional): The threshold value for filtering the measurement column.
    """

    settings = get_annotate_default_settings(settings)
    src  = settings['src']

    db = os.path.join(src, 'measurements/measurements.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('PRAGMA table_info(png_list)')
    cols = c.fetchall()
    if settings['annotation_column'] not in [col[1] for col in cols]:
        c.execute(f"ALTER TABLE png_list ADD COLUMN {settings['annotation_column']} integer")
    conn.commit()
    conn.close()

    root = tk.Tk()
    root.geometry(settings['geom'])
    app = ImageApp(root, db, src, image_type=settings['image_type'], channels=settings['channels'], image_size=settings['img_size'], grid_rows=settings['rows'], grid_cols=settings['columns'], annotation_column=settings['annotation_column'], normalize=settings['normalize'], percentiles=settings['percentiles'], measurement=settings['measurement'], threshold=settings['threshold'])
    next_button = tk.Button(root, text="Next", command=app.next_page)
    next_button.grid(row=app.grid_rows, column=app.grid_cols - 1)
    back_button = tk.Button(root, text="Back", command=app.previous_page)
    back_button.grid(row=app.grid_rows, column=app.grid_cols - 2)
    exit_button = tk.Button(root, text="Exit", command=app.shutdown)
    exit_button.grid(row=app.grid_rows, column=app.grid_cols - 3)
    
    app.load_images()
    root.mainloop()

# Global list to keep references to PhotoImage objects
global_image_refs = []

def initiate_annotation_app_root(parent_frame):
    style = ttk.Style(parent_frame)
    set_dark_style(style)
    style_text_boxes(style)
    set_default_font(parent_frame, font_name="Arial", size=8)

    parent_frame.configure(bg='black')
    
    container = tk.PanedWindow(parent_frame, orient=tk.HORIZONTAL, bg='black')
    container.pack(fill=tk.BOTH, expand=True)

    scrollable_frame = ScrollableFrame(container, bg='black')
    container.add(scrollable_frame, stretch="always")

    # Setup input fields
    vars_dict = {
        'src': ttk.Entry(scrollable_frame.scrollable_frame),
        'image_type': ttk.Entry(scrollable_frame.scrollable_frame),
        'channels': ttk.Entry(scrollable_frame.scrollable_frame),
        'geom': ttk.Entry(scrollable_frame.scrollable_frame),
        'img_size': ttk.Entry(scrollable_frame.scrollable_frame),
        'rows': ttk.Entry(scrollable_frame.scrollable_frame),
        'columns': ttk.Entry(scrollable_frame.scrollable_frame),
        'annotation_column': ttk.Entry(scrollable_frame.scrollable_frame),
        'normalize': ttk.Entry(scrollable_frame.scrollable_frame),
        'percentiles': ttk.Entry(scrollable_frame.scrollable_frame),
        'measurement': ttk.Entry(scrollable_frame.scrollable_frame),
        'threshold': ttk.Entry(scrollable_frame.scrollable_frame),
    }

    default_settings = {
        'src': 'path',
        'image_type': 'cell_png',
        'channels': 'r,g,b',
        'geom': "3200x2000",
        'img_size': '(200, 200)',
        'rows': '10',
        'columns': '18',
        'annotation_column': 'recruited_test',
        'normalize': 'False',
        'percentiles': '(2,98)',
        'measurement': 'None',
        'threshold': 'None'
    }

    # Arrange input fields and labels
    row = 0
    for name, entry in vars_dict.items():
        ttk.Label(scrollable_frame.scrollable_frame, text=f"{name.replace('_', ' ').capitalize()}:",
                  background="black", foreground="white").grid(row=row, column=0)
        entry.insert(0, default_settings[name])
        entry.grid(row=row, column=1)
        row += 1

    # Function to be called when "Run" button is clicked
    def run_app():
        settings = {key: entry.get() for key, entry in vars_dict.items()}
        settings['channels'] = settings['channels'].split(',')
        settings['img_size'] = tuple(map(int, settings['img_size'][1:-1].split(',')))
        settings['percentiles'] = tuple(map(int, settings['percentiles'][1:-1].split(',')))
        settings['normalize'] = settings['normalize'].lower() == 'true'
        settings['rows'] = int(settings['rows'])
        settings['columns'] = int(settings['columns'])
        if settings['measurement'].lower() == 'none':
            settings['measurement'] = None
        if settings['threshold'].lower() == 'none':
            settings['threshold'] = None
        
        # Clear previous content instead of destroying the root
        if hasattr(parent_frame, 'winfo_children'):
            for widget in parent_frame.winfo_children():
                widget.destroy()
        
        # Start the annotate application in the same root window
        annotate_app(parent_frame, settings)
        
    run_button = CustomButton(scrollable_frame.scrollable_frame, text="Run", command=run_app,
                              font=tkFont.Font(family="Arial", size=12, weight=tkFont.NORMAL))
    run_button.grid(row=row, column=0, columnspan=2, pady=10, padx=10)

    return parent_frame

def annotate_app(parent_frame, settings):
    global global_image_refs
    global_image_refs.clear()
    root = parent_frame.winfo_toplevel()
    annotate_with_image_refs(settings, root, lambda: load_next_app(root))

def annotate_with_image_refs(settings, root, shutdown_callback):
    settings = get_annotate_default_settings(settings)
    src = settings['src']

    db = os.path.join(src, 'measurements/measurements.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('PRAGMA table_info(png_list)')
    cols = c.fetchall()
    if settings['annotation_column'] not in [col[1] for col in cols]:
        c.execute(f"ALTER TABLE png_list ADD COLUMN {settings['annotation_column']} integer")
    conn.commit()
    conn.close()

    app = ImageApp(root, db, src, image_type=settings['image_type'], channels=settings['channels'], image_size=settings['img_size'], grid_rows=settings['rows'], grid_cols=settings['columns'], annotation_column=settings['annotation_column'], normalize=settings['normalize'], percentiles=settings['percentiles'], measurement=settings['measurement'], threshold=settings['threshold'])

    # Set the canvas background to black
    root.configure(bg='black')

    next_button = tk.Button(root, text="Next", command=app.next_page, background='black', foreground='white')
    next_button.grid(row=app.grid_rows, column=app.grid_cols - 1)
    back_button = tk.Button(root, text="Back", command=app.previous_page, background='black', foreground='white')
    back_button.grid(row=app.grid_rows, column=app.grid_cols - 2)
    exit_button = tk.Button(root, text="Exit", command=lambda: [app.shutdown(), shutdown_callback()], background='black', foreground='white')
    exit_button.grid(row=app.grid_rows, column=app.grid_cols - 3)

    app.load_images()

    # Store the shutdown function and next app details in the root
    root.current_app_exit_func = app.shutdown
    root.next_app_func = None
    root.next_app_args = ()

def load_next_app(root):
    # Get the next app function and arguments
    next_app_func = root.next_app_func
    next_app_args = root.next_app_args

    if next_app_func:
        next_app_func(*next_app_args)

def gui_annotate():
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")
    root.title("Annotate Application")
    
    # Clear previous content if any
    if hasattr(root, 'content_frame'):
        for widget in root.content_frame.winfo_children():
            widget.destroy()
        root.content_frame.grid_forget()
    else:
        root.content_frame = tk.Frame(root)
        root.content_frame.grid(row=1, column=0, sticky="nsew")
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
    
    initiate_annotation_app_root(root.content_frame)
    create_menu_bar(root)
    root.mainloop()

if __name__ == "__main__":
    gui_annotate()