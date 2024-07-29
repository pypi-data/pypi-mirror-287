import sys
import zipfile
import os
import subprocess
import platform
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QPixmap
import requests

# FastAPI endpoint

class ImageUploaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Image to Form")
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Upload an image and send it to a REST API along with other parameters", self)
        self.layout.addWidget(self.label)

        self.api_label = QLabel("API Endpoint URL:", self)
        self.layout.addWidget(self.api_label)
        self.api_entry = QLineEdit(self)
        self.layout.addWidget(self.api_entry)
        
        self.upload_btn = QPushButton("Upload Image", self)
        self.upload_btn.clicked.connect(self.upload_image)
        self.layout.addWidget(self.upload_btn)
        
        self.iris_label = QLabel("Iris workspace path:", self)
        self.layout.addWidget(self.iris_label)
        self.iris_entry = QLineEdit(self)
        self.layout.addWidget(self.iris_entry)
        
        self.volt_label = QLabel("Volt iris link file path:", self)
        self.layout.addWidget(self.volt_label)
        self.volt_entry = QLineEdit(self)
        self.layout.addWidget(self.volt_entry)
        
        self.channel_label = QLabel("Channel:", self)
        self.layout.addWidget(self.channel_label)
        self.channel_entry = QLineEdit(self)
        self.layout.addWidget(self.channel_entry)
        
        self.submit_btn = QPushButton("Submit", self)
        self.submit_btn.clicked.connect(self.submit_data)
        self.layout.addWidget(self.submit_btn)
        
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)
        
        self.setLayout(self.layout)
    
    def upload_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.filepath, _ = QFileDialog.getOpenFileName(self, "Choose an image...", "", "Image Files (*.jpg *.jpeg *.png);;All Files (*)", options=options)
        file_name_sp = os.path.basename(self.filepath)
        file_name_sp = os.path.splitext(file_name_sp)
        self.file_name = file_name_sp[0]
     
        if self.filepath:
            pixmap = QPixmap(self.filepath)
            pixmap = pixmap.scaled(200, 200)
            self.image_label.setPixmap(pixmap)
    
    def submit_data(self):
        if not hasattr(self, 'filepath'):
            QMessageBox.critical(self, "Error", "Please upload an image")
            return
        
        self.submit_btn.setEnabled(False)
        api_url = self.api_entry.text()

        
        data = {
            "iris_workspace_path": self.iris_entry.text(),
            "volt_iris_link_file_path": self.volt_entry.text(),
            "channel": self.channel_entry.text()
        }
        
        try:
            with open(self.filepath, "rb") as f:
                files = {"file": (os.path.basename(self.filepath), f, "image/jpeg")}
                
                response = requests.post(api_url, files=files, data=data)
                
                if response.status_code == 200:
                    zip_file_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{self.file_name}.zip")
                    with open(zip_file_path, "wb") as f:
                        f.write(response.content)
                    
                    self.extract_and_open(zip_file_path, data)
                else:
                    raise Exception(f"Failed to upload image and parameters: {response.status_code}\n{response.text}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            self.submit_btn.setEnabled(True)

    def extract_and_open(self, zip_file_path, data):
        extract_dir = data['iris_workspace_path']
        volt_iris_app = data['volt_iris_link_file_path']
        os.makedirs(extract_dir, exist_ok=True)
        
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        
        QMessageBox.information(self, "Success", f"Files extracted to {extract_dir}")
        self.open_extracted_files_app(extract_dir, volt_iris_app)

    def open_extracted_files_app(self, extract_dir, volt_iris_app):
        viewer_app = FileViewerApp(extract_dir, volt_iris_app)
        viewer_app.exec_()

class FileViewerApp(QWidget):
    def __init__(self, directory, volt_iris_app):
        super().__init__()
        self.directory = directory
        self.volt_iris_app = volt_iris_app
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Extracted Files")
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel(f"Contents of the extracted directory: {self.directory}", self)
        self.layout.addWidget(self.label)
        
        files = os.listdir(self.directory)
        for file in files:
            file_label = QLabel(file, self)
            self.layout.addWidget(file_label)
        
        self.setLayout(self.layout)
        self.launch_file_viewer()
    
    def launch_file_viewer(self):
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", self.volt_iris_app])
        elif platform.system() == "Windows":  # Windows
            os.startfile(self.volt_iris_app)
        else:
            QMessageBox.critical(self, "Error", "Unsupported operating system")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ImageUploaderApp()
    ex.show()
    sys.exit(app.exec_())
