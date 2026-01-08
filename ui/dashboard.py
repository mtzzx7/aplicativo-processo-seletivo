from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from ui.dashboard_repository import get_dashboard_cards, get_stage_averages

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        
        title = QLabel("Dashboard Geral")
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        self.layout.addWidget(title)

        self.cards_layout = QHBoxLayout()
        self.layout.addLayout(self.cards_layout)

        # Placeholder for other charts
        self.stages_layout = QVBoxLayout()
        self.layout.addLayout(self.stages_layout)

        refresh_button = QPushButton("Atualizar Dados")
        refresh_button.clicked.connect(self.update_data)
        self.layout.addWidget(refresh_button, 0, Qt.AlignRight)
        
        self.update_data()

    def update_data(self):
        # Clear old widgets before updating
        for i in reversed(range(self.cards_layout.count())): 
            self.cards_layout.itemAt(i).widget().setParent(None)
        
        for i in reversed(range(self.stages_layout.count())):
            self.stages_layout.itemAt(i).widget().setParent(None)

        # Fetch and display new data
        self.create_cards()
        self.create_stage_averages()

    def create_cards(self):
        cards_data = get_dashboard_cards()
        if not cards_data:
            self.cards_layout.addWidget(QLabel("Não foi possível carregar os cards."))
            return

        for title, value in cards_data.items():
            card = self.create_metric_card(title.capitalize(), str(value))
            self.cards_layout.addWidget(card)
    
    def create_stage_averages(self):
        stages_data = get_stage_averages()
        if not stages_data or not any(stages_data):
            self.stages_layout.addWidget(QLabel("Dados de estágio indisponíveis."))
            return

        imm, dev, pres = stages_data
        
        stages_title = QLabel("Médias das Etapas (Avaliações Ativas)")
        stages_title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.stages_layout.addWidget(stages_title)

        self.stages_layout.addWidget(QLabel(f"Imersão: {imm:.2f}" if imm else "Imersão: N/A"))
        self.stages_layout.addWidget(QLabel(f"Desenvolvimento: {dev:.2f}" if dev else "Desenvolvimento: N/A"))
        self.stages_layout.addWidget(QLabel(f"Apresentação: {pres:.2f}" if pres else "Apresentação: N/A"))


    def create_metric_card(self, title_text, value_text):
        card = QWidget()
        card.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                border-radius: 8px;
                border: 1px solid #2a2a2a;
            }
        """)
        layout = QVBoxLayout(card)
        
        title_label = QLabel(title_text)
        title_label.setFont(QFont("Segoe UI", 12))
        title_label.setAlignment(Qt.AlignCenter)

        value_label = QLabel(value_text)
        value_label.setFont(QFont("Segoe UI", 28, QFont.Bold))
        value_label.setAlignment(Qt.AlignCenter)
        value_label.setStyleSheet("color: #1e88e5;")

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        
        return card
